def multiplication_function(numbers):
    list_of_numbers = numbers.split()
    # 1 is a neutral number for multiplication
    ret = 1
    for num in list_of_numbers:
        if num.isdigit():
            ret = int(num) * ret
        else:
            print(" make sure entries should contain only digits")
            exit(1)
    return ret


if __name__ == "__main__":
    numbers = input("please enter your numbers\n")
    mul = multiplication_function(numbers)
    # Output the result
    print(mul)
