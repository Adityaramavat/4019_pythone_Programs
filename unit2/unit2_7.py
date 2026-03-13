# Program to copy contents of one text file to another


source_file = "source.txt"
destination_file = "destination.txt"

try:
    # Open source file in read mode
    with open(source_file, "r") as src:
        content = src.read()

    # Open destination file in write mode
    with open(destination_file, "w") as dest:
        dest.write(content)

    print("File copied successfully.")

except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print("An error occurred:", e)