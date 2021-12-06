numbers = []
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    get_numbers()
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average number is {sum(numbers) / 5}")
    det_user_name(usernames)


def get_numbers():
    for i in range(5):
        number = float(input("Enter number: "))
        numbers.append(number)
    return numbers


def det_user_name(usernames):
    username = input("Enter username: ")
    if username in usernames:
        print("Access granted.")
    else:
        print("Access denied.")


main()
