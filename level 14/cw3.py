# 3) ოთახის გათბობა აქტიურდება თუ ტემპერატურა ან ძალიან დაბალია ან ძალიან მაღალი
age = int(input("Enter your age: "))

license = input("Enter yes/no if you have driving license: ")

if age > 18 and license == "yes":
    print("You can enter country")
else:
    print("You cannot enter country")