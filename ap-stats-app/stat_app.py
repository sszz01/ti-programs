# from ti_system import * import ti-specific system functions
# import ti_plotlib as plt
from notes import NOTES

class StatApp:
    def __init__(self):
        self.notes_data = NOTES
        self.units = sorted(list(self.notes_data.keys()),
                            key=lambda x: int(x.split()[1].split(':')[0]) if len(x.split()) > 1 else 0)
        self.num_units = len(self.units)
        self.running = True
        self.current_menu = "main"

    def display_main_menu(self):
        print("\nUltimate AP Statistics Notes Guide")
        print("Select an option:")
        print("1. Study Guide (Select Unit)")
        print("2. Exit")

        while True:
            user_input = input("> ").strip()
            try:
                choice = int(user_input)
                if 1 <= choice <= 2:
                    return choice
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Enter number 1 or 2.")

    def display_units_menu(self):
        print("\nSelect a unit(1-9):")
        for _, unit_name in enumerate(self.units, 1):
            print("{unit_name}".format(unit_name=unit_name))
        print("0. Go Back")

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
                    print("Invalid choice. Please enter a number between 1 and {}.".format(self.num_units + 1))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and {}.".format(self.num_units + 1))

    def display_notes(self, unit_name):
        unit_data = self.notes_data.get(unit_name, "Notes not found for this unit.")
        if isinstance(unit_data, dict):
            print("\n{}".format(unit_name))
            print("-" * 40)
            for subtopic, content in unit_data.items():
                print("\n{}:".format(subtopic))
                if isinstance(content, tuple):
                    print("".join(content))
                else:
                    print(content)

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

app = StatApp()
app.run()