# Check input
def get_menu_input(accepted: list[str]) -> str:
    choice = ""
    choice = input()
    while choice not in accepted:
        print("Invalid choice, try again: ")
        choice = input()
    return choice