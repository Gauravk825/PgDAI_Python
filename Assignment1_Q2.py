total_notes = 0 # intializtion for count  number of total notes
cnt = 0 # intitializaton for count indvidual number of notes
amount = int(input("Enter the amount: ")) #input for amount

if amount >= 2000:
    total_notes += amount // 2000
    cnt = amount // 2000 # count for 2000 rupees notes
    print(f"Notes of 2000 = {cnt}")
    amount %= 2000 # balenced amount after 2000 rupees notes
    
if amount >= 500:
    total_notes += amount // 500
    cnt = amount // 500 # count for 500 rupees notes
    print(f"Notes of 500 = {cnt}")
    amount %= 500 # blanced amount after 500 rupees notes

if amount >= 100:
    total_notes += amount // 100
    cnt = amount // 100 # count for 100 rupees notes
    print(f"Notes of 100 = {cnt}")
    amount %= 100 # balanced amount after 100 rupees notes

if amount >= 50:
    total_notes += amount // 50
    cnt = amount // 50 # count for 50 rupees notes
    print(f"Notes of 50 = {cnt}")
    amount %= 50 # balnced amount after 50 rupees

if amount >= 10:
    total_notes += amount // 10
    cnt = amount // 10 # count for 10 rupees notes 
    print(f"Notes of 10 = {cnt}")
    amount %= 10 # blanced amount after 10 rupees notes

if amount >= 5:
    total_notes += amount // 5
    cnt = amount // 5 # count for 5 rupees notes
    print(f"Notes of 5 = {cnt}")
    amount %= 5 3# blanced amount after 5 rupees notes

if amount >= 2:
    total_notes += amount // 2
    cnt = amount // 2 # count for 2 rupees notes
    print(f"Notes of 2 = {cnt}")
    amount %= 2 # amount after 2 rupees notes

if amount >= 1:
    total_notes += amount // 1
    cnt = amount //1 # count for 1 rupees notes
    print(f"Notes of 1 = {cnt}")


print(f"To number of notes : {total_notes}")
