def is_palindrome(string):
    return string == string[::-1]


if __name__ == '__main__':
    print("Enter the phrase:")
    print("It's a palindrome!" if is_palindrome(input(">>")) else "It's not a palindrome!")
    