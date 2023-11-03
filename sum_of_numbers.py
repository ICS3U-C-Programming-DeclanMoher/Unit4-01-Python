#!/usr/bin/env python3
# created Nov 3rd 2023 by Declan Moher
def main():
    user_number = int(input(("Enter a number:")))
    try:
        user_number = int(user_number)
        count = 0
        while count <= 10:
            product = user_number * count
            print("{0} x {1} = {2}".format(user_number, count, product))
            count = count + 1
    except ValueError:
        print(f"{user_number}is not a valid number")


if __name__ == "__main__":
    main()
