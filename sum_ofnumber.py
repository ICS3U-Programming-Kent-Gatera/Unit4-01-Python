#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Oct 30
# This program gets a number and adds up all the numbers leading up to it.


def main():
    print("This program gets a number and adds up all the numbers leading up to it.")
    # Input
    final_num = input("What is the number you wish to calculate? ")
    stop_catch_num = 0
    sum_num = 0
    # Process
    try:
        # Troubleshooting
        final_num_int = int(final_num)
        if final_num_int <= 0:
            print(f"Your input {final_num_int} is not valid (e.g 5)")
        # This while loop increments on itself until the maximum number, (the user input) is equal to the added number.
        # I could have also used "n(n + 1)/2 = Sum of Integers" but I am dumb and did not realize it was a thing.
        while stop_catch_num < final_num_int:
            stop_catch_num = stop_catch_num + 1
            sum_num = sum_num + stop_catch_num
            display_num = sum_num
            # The loop stops but the output is messy and repetitive so I added an "if" statement.
            if stop_catch_num == final_num_int:
                print(
                    f"All the numbers leading up to {final_num_int} equate to {display_num}"
                )
    except:
        # This try catch is there in case the user inputs a decimal number.
        try:
            float(final_num)
            print(f"{final_num} is not a whole number. (e.g 5)")
        except:
            print(f"Your input '{final_num}' is not a valid integer (e.g 5)")


# Run program
if __name__ == "__main__":
    main()
