#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sept 2021
# This program will perform addition with two numbers
#   given by the user


def main():
    # This program calculates the sum of the numbers give by the user

    # input
    first_number = int(input("Enter the first number (integer): "))
    second_number = int(input("Enter the second number (integer: "))

    # process
    total = first_number + second_number

    # output
    print("\n{0} + {1} = {2}".format(first_number, second_number, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
