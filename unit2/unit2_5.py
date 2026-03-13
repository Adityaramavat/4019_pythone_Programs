def read_and_count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
        # Display file contents
        print("File contents:")
        print("-" * 40)
        print(content)
        print("-" * 40)
        
        # Count words (split by whitespace)
        words = content.split()
        word_count = len(words)
        
        print(f"Number of words in file: {word_count}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage example
filename = "os_assignment.txt"  
read_and_count_words(filename)
