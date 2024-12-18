def get_valid_float(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input.strip(): # if input is empty
                raise ValueError("Input cannot be empty")
            
            value = float(user_input) # ensure input is float
            
            if value < 0:
                raise ValueError("Please enter a positive number")
            
            return value
        except ValueError as e:
            print(f'Invalid input: {e}. Please try again.')


def get_valid_int(prompt):
    while True:
        try:
            user_input = input(prompt)
            if not user_input.strip(): # if input is empty
                raise ValueError("Input cannot be empty")
            
            value = int(user_input) # ensure input is int
            
            if value <= 0:
                raise ValueError("Must allow at least one loop")
            
            return value
        except ValueError as e:
            print(f'Invalid input: {e}. Please try again.')

            