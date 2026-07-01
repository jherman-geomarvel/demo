def get_user_name():
    name = ""
    while len(name) < 2:
        name = input("What is your name? ")
    if len(name) < 2:
        print("Please type at least 2 characters.")

    name = name.capitalize()

    return name
