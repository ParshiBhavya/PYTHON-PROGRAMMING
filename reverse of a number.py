def reverse_integer(num):
    # Convert the integer to a string and reverse it
    reversed_str = str(num)[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    return reversed_num

num = int(input('Enter the number:'))
reversed_num = reverse_integer(num)
print("Reversed integer:", reversed_num)
