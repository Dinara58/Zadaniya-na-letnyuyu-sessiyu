def is_palindrome(data):
    return data == data[::-1]

def main():
    user_input = input("Введите строку: ")
    
    if is_palindrome(user_input):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
