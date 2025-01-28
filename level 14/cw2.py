# 2) მომხმარებელმა ფასდაკლება უნდა მიიღოს თუ 100 ლარზე მეტ რამეს ყიდულობს ან არის vip მომხმარებელი

checkout = int(input('Enter summary: '))

if checkout > 100:
    print("You have discount")
elif checkout == "VIP":
    print("You have discount, because you are VIP")
else:
    print("You have no discount")