from ti_system import * # TI-specific system functions
from notes import NOTES

class StatApp:
    def __init__(self):
        self.notes_data = NOTES
        self.units = sorted(list(self.notes_data.keys()))
        self.num_units = len(self.units)
        self.running = True
        self.current_menu = "main"

    def display_main_menu(self):
        disp_clr()
        print("\nAP Stats Notes")
        print("1. Study Guide")
        print("2. Exit")

        while True:
            user_input = input("> ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= 2:
                    return choice
                else:
                    print("Invalid. Enter 1 or 2.")
            except ValueError:
                print("Invalid. Enter 1 or 2.")

    def display_units_menu(self):
        disp_clr()
        print("\nSelect Topic:")
        for idx, topic_name in enumerate(self.units, 1):
            print("{}. {}".format(idx, topic_name))
        print("0. Back")

        while True:
            user_input = input("> ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= self.num_units:
                    selected_topic_name = self.units[choice - 1]
                    self.display_notes(selected_topic_name)
                    return "stay"
                elif choice == 0:
                    return "back"
                else:
                    print("Invalid. Try a topic number.")
            except ValueError:
                print("Invalid input.")

    def display_notes(self, topic_name): # Renamed parameter
        while True:
            disp_clr()
            topic_concepts = self.notes_data.get(topic_name, {}).get("Concepts", {})
            if not topic_concepts:
                print("No notes found.")
                input("\nPress Enter to return...")
                return

            print("\n{} - Subtopics:".format(topic_name))
            subtopics = list(topic_concepts.keys())
            for idx, subtopic in enumerate(subtopics, 1):
                print("{}. {}".format(idx, subtopic))
            print("0. Back")

            user_input = input("\nSubtopic > ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= len(subtopics):
                    selected_subtopic = subtopics[choice - 1]
                    self.display_subtopic(topic_concepts[selected_subtopic], selected_subtopic, topic_name)
                elif choice == 0:
                    return
                else:
                    print("Invalid. Try again.")
            except ValueError:
                print("Invalid input.")

    def display_subtopic(self, content, subtopic_title, topic_name):
        lines = content.split('\n')

        lines_per_page = 8
        current_line = 0
        total_lines = len(lines)

        page_num = 1
        total_pages = (total_lines + lines_per_page - 1) // lines_per_page

        while current_line < total_lines:
            disp_clr()
            header = "{} > {}".format(topic_name[:10], subtopic_title[:10])
            page_info = " (Pg {}/{})".format(page_num, total_pages)
            print(header + page_info)
            print("-" * 26)

            end_line = min(current_line + lines_per_page, total_lines)
            for i in range(current_line, end_line):
                line = lines[i]
                max_width = 26
                start = 0
                while start < len(line):
                    print(line[start:start+max_width])
                    start += max_width

            current_line = end_line
            page_num += 1

            if current_line < total_lines:
                input("Press Enter...")
            else:
                input("\nEnd. Press Enter...")


    def run(self):
        while self.running:
            if self.current_menu == "main":
                choice = self.display_main_menu()
                if choice == 1:
                    self.current_menu = "units"
                elif choice == 2:
                    self.running = False
                    disp_clr()
                    print("Goodbye!")
            elif self.current_menu == "units":
                action = self.display_units_menu()
                if action == "back":
                    self.current_menu = "main"

app = StatApp()
app.run()