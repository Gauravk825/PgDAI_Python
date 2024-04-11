while True:
    marks = int(input("Enter marks: "))

    if marks >= 80: # terminated condition
        print("A")
        break
    elif marks >= 60 and marks <= 80:
        print(f"Grade :{B}")
    elif marks >= 50 and marks < 60:
        print(f"C")
    elif marks >= 45 and marks < 50:
        print("D")
    elif marks >= 25 and marks < 45:
        print("E")
    else:
        print("F")
