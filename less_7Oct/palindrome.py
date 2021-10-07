def is_palindrome(string):
    for i in range(len(string)):
        print(f"{''if i>9 else '0'}{i}: {string[i]} AND {string[-1-i]}")
    return string == string[::-1]


def recursive_palindrome(string):
    if len(string) == 1: return True
    if string[0] != string[-1]:return False
    return recursive_palindrome(string[1:-1])
    
    
if __name__ == '__main__':
    print("Enter the phrase:")
    print("It's a palindrome!" if is_palindrome(input(">>")) else "It's not a palindrome!")
    