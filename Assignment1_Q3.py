class_held = int(input('Number of classes held: ')) # input for nuber of clas held 
class_attended = int(input('Number of classes attended: ')) # input for number of attednded class 
Medical_Cause = input("Do you have a medical cause(Y/N): ") # input for midical cause
percentage = class_attended*100/class_held  # caculating percentage
print(f"Percentage = {percentage}")

if percentage >= 75 or Medical_Cause =='Y' or Medical_Cause =='y':
    print("ALLOWED")

else:
    print("NOT ALLOWED")
