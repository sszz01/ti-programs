from ti_system import * # TI-specific system functions
from notes import NOTES

class StatApp:
    def __init__(self):
        self.notes_data = NOTES
        self.topics = sorted(list(self.notes_data.keys()))
        self.num_topics = len(self.topics)
        self.running = True
        self.current_menu = "topics"

    def display_topics_menu(self):
        disp_clr()
        print("\nSelect Topic:")
        for i, topic_name in enumerate(self.topics, 1):
            print("{}. {}".format(i, topic_name))
            if i == 8:
                input("\nPress enter to continue...")
        print("0. Quit")

        while True:
            user_input = input("/ > ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= self.num_topics:
                    selected_topic_name = self.topics[choice - 1]
                    self.current_menu = "subtopics"
                    self.display_notes(selected_topic_name)
                    self.current_menu = "topics"
                    return "stay"
                elif choice == 0 and self.current_menu == "topics":
                    return "quit"
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
            for i, subtopic in enumerate(subtopics, 1):
                print("{}. {}".format(i, subtopic))
            print("0. Back")

            user_input = input("\n/Subtopic > ").strip()
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
        self.current_menu = "subtopics"
        lines = content.split('\n')

        lines_per_page = 8
        current_line = 0
        total_lines = len(lines)

        while current_line < total_lines:
            disp_clr()
            header = "{} > {}".format(topic_name[:10], subtopic_title[:10])
            print(header)
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

            if current_line < total_lines:
                input("Press Enter...")
            else:
                input("\nEnd. Press Enter...")


    def run(self):
        while self.running:
            if self.current_menu == "topics":
                action = self.display_topics_menu()
                if action == "quit":
                    self.running = False
                    disp_clr()

app = StatApp()
app.run()