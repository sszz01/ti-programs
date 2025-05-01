# from ti_system import * # import ti-specific system functions
# import ti_plotlib as plt
from notes import NOTES

class StatApp:
    def __init__(self):
        self.notes_data = NOTES
        self.units = list(self.notes_data.keys())
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
                    print(f"Invalid choice. Please enter a number between 1 and {self.num_units + 1}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between 1 and {self.num_units + 1}.")

    def display_notes(self, unit_name):
        print(self.notes_data.get(unit_name, "Notes not found for this unit."))
        input("> ").strip()

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

if __name__ == "__main__":
    app = StatApp()
    app.run()