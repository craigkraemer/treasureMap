# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
position = int(position)
treasure1 = ["💰", "⬜️", "⬜️"]
treasure2 = ["⬜️", "💰", "⬜️"]
treasure3 = ["⬜️", "⬜️", "💰"]

if position == 11:
    print(f"{treasure1}\n{row2}\n{row3}")

elif position == 12:
    print(f"{row1}\n{treasure1}\n{row3}")

elif position == 13:
    print(f"{row1}\n{row2}\n{treasure1}")

elif position == 21:
    print(f"{treasure2}\n{row2}\n{row3}")

elif position == 22:
    print(f"{row1}\n{treasure2}\n{row3}")

elif position == 23:
    print(f"{row1}\n{row2}\n{treasure2}")

elif position == 31:
    print(f"{treasure3}\n{row2}\n{row3}")

elif position == 32:
    print(f"{row1}\n{treasure3}\n{row3}")

elif position == 33:
    print(f"{row1}\n{row2}\n{treasure3}") 
else:
    print("Incorrect input.")  
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")