#11.Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.


def calculate_total(*numbers):
    # *numbers acts like a list containing all the arguments sent
    total = 0
    
    for num in numbers:
        total = total + num
        
    print(f"Total is: {total}")

print("Case 1:")
calculate_total(10,30,20)

print("\nCase 2:")
calculate_total(5,10,15,20,25,50,21,75)

print("\nCase 3:")
calculate_total(100)
