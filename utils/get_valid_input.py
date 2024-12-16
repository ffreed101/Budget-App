def get_valid_input(prompt, is_number=False, is_float=False, min_number=None, max_number=None, length=None):
    while True:
        user_input = input(f"{prompt}: ")
        isValid = False

        if is_number:
            if user_input.isdigit():
                isValid = True
                user_input = int(user_input)

            elif is_float:
                try:
                    user_input = float(user_input)
                    isValid = True

                except:
                    print("Invalid input. Enter a decimal number.")

            else:
                print("Invalid input. Enter a number.")
                
            if min_number != None and max_number != None:
                if user_input in range(min_number, max_number+1):
                    isValid = True
                        
                else:
                    if isValid == True:
                        print(f"Invalid input. Enter a number from {min_number} to {max_number}.")
                    isValid = False

        else:
            if length != None:
                if len(user_input) == length:
                    isValid = True
                else:
                    print(f"Invalid input. Input must be {length} characters long.")
        if isValid == True:
            break
        else:
            print("Please Try again.")

    return user_input