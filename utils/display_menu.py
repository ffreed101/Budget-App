def display_menu(title, options):
    print(f"-- {title} --")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

