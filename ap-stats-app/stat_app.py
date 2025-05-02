from ti_system import *  # TI-specific system functions
from notes import NOTES  # Custom AP Stats notes

class StatApp:
    def __init__(self):
        self.notes_data = NOTES
        self.units = sorted(list(self.notes_data.keys()),
                            key=lambda x: int(x.split()[1].split(':')[0]) if len(x.split()) > 1 else 0)
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
        print("\nSelect Unit:")
        for idx, unit_name in enumerate(self.units, 1):
            print("{}. {}".format(idx, unit_name))
        print("0. Back")

        while True:
            user_input = input("> ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= self.num_units:
                    selected_unit_name = self.units[choice - 1]
                    self.display_notes(selected_unit_name)
                    return "stay"
                elif choice == 0:
                    return "back"
                else:
                    print("Invalid. Try a unit number.")
            except ValueError:
                print("Invalid input.")

    def display_notes(self, unit_name):
        while True:
            disp_clr()
            unit_data = self.notes_data.get(unit_name, {})
            if not unit_data:
                print("No notes found.")
                input("\nPress Enter to return...")
                return

            print("\n{} - Subtopics:".format(unit_name))
            subtopics = list(unit_data.get("Concepts", {}).keys())  # Ensure it accesses the "Concepts" dictionary
            for idx, topic in enumerate(subtopics, 1):
                print("{}. {}".format(idx, topic))
            print("0. Back")

            user_input = input("\nSubtopic > ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= len(subtopics):
                    selected_topic = subtopics[choice - 1]
                    self.display_subtopic(unit_data["Concepts"][selected_topic], selected_topic, unit_name)
                elif choice == 0:
                    return
                else:
                    print("Invalid. Try again.")
            except ValueError:
                print("Invalid input.")

    def display_subtopic(self, content, subtopic_title, unit_name):
        lines = content.split("\n")  # No need for complex tuple handling

        lines_per_page = 7
        current_line = 0
        total_lines = len(lines)

        while current_line < total_lines:
            disp_clr()
            print("{} > {}".format(unit_name, subtopic_title))
            print("-" * 40)
            for i in range(current_line, min(current_line + lines_per_page, total_lines)):
                print("{}".format(lines[i]))
            current_line += lines_per_page
            if current_line < total_lines:
                input("\nPress Enter...")

        input("\nPress Enter to return...")

    def run(self):
        while self.running:
            if self.current_menu == "main":
                choice = self.display_main_menu()
                if choice == 1:
                    self.current_menu = "units"
                elif choice == 2:
                    self.running = False
                    print("Goodbye!")
            elif self.current_menu == "units":
                action = self.display_units_menu()
                if action == "back":
                    self.current_menu = "main"

# Run the app
app = StatApp()
app.run()
