# 3) მომხმარებელმა უნდა შეიყვანოს თავისი ასაკი და სახელი. პროგრამამ უნდა შეამოწმოს, რომ ასაკი 18-ზე მეტია და სახელი იწყება "A"-ზე.

name = input("Enter your name: ")

age = int(input("Enter number: "))


if age > 18:
    print("Age is high than 18")
elif name == "A":
    print("Your name starts with A")
else:
    print("Age is lower 18, name doesnt start with A")