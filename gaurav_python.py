def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number: "))
        check_even_odd(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")
