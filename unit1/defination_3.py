s1=float(input("Enter The First Subject Marks :"))
s2=float(input("Enter The Second Subject Marks :"))
s3=float(input("Enter The Third Subject Marks :"))
s4=float(input("Enter The Fourth Subject Marks :"))

totel = s1+s2+s3+s4
print("Total marks of all subject is :",totel)

per = (totel/400)*100
print("Pr % of all subject marks:",per ,"%")

if per >= 90 :
    print("Grade A:")
elif per >= 80 and per <= 90:
    print("Grade B:")
elif per >= 70 and per <= 80:
    print("Grade C:")
elif per >= 60 and per <= 70:
    print("Grade D:")
else:
    print("Better luck Next Time")