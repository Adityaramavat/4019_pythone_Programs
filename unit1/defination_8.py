#8. Write a Python program to perform following operation on given string input:

def count_vowels(text):
    """Counts the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def get_length(text):
    """Counts length without using len()."""
    count = 0
    for _ in text:
        count += 1
    return count

def reverse_string(text):
    """Reverses the string using slicing."""
    return text[::-1]

def check_palindrome(text):
    """Checks if the string is the same forward and backward."""
    # We compare the lowercased version to make it case-insensitive
    clean_text = text.lower()
    reversed_text = clean_text[::-1]
    return clean_text == reversed_text

def main():
    while True:
        print("\n--- String Operations Menu ---")
        string_input = input("Enter a string to work with: ")
        
        print(f"Current String: '{string_input}'")
        print("a) Count Number of Vowels")
        print("b) Count Length of string (without len())")
        print("c) Reverse string")
        print("d) Find and replace operation")
        print("e) Check if palindrome")
        print("x) Exit")
        
        choice = input("Enter your choice (a-e): ").lower()

        if choice == 'a':
            print(f"Number of Vowels: {count_vowels(string_input)}")
            
        elif choice == 'b':
            print(f"Length of string: {get_length(string_input)}")
            
        elif choice == 'c':
            print(f"Reversed string: {reverse_string(string_input)}")
            
        elif choice == 'd':
            find_str = input("Enter substring to find: ")
            replace_str = input("Enter substring to replace with: ")
            # .replace() returns a new string, it does not modify the original in place
            new_string = string_input.replace(find_str, replace_str)
            print(f"Modified string: {new_string}")
            
        elif choice == 'e':
            if check_palindrome(string_input):
                print("Result: The string IS a palindrome.")
            else:
                print("Result: The string is NOT a palindrome.")
                
        elif choice == 'x':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        print("-" * 30)

if __name__ == "__main__":
    main()
