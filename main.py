A_ap = 5.0
B_ap = 4.0
C_ap = 3.0
D_ap = 2.0
F_ap = 1.0

A_honors = 4.5
B_honors = 3.5
C_honors = 2.5
D_honors = 1.5
F_honors = 0.5

A_cp = 4.0
B_cp = 3.0
C_cp = 2.0
D_cp = 1.0
F_cp = 0.0

total_gpa = 0.0
number_classes = 0

while True:
    grade_level = input("Enter Grade level (i.e A_ap) or type 'done': ")
    if grade_level == "done":
        break
    if grade_level in globals():  
        total_gpa += globals()[grade_level]
        number_classes += 1
    else:
        print("Grade level not found.")

another_class = input("Do you have another class? (yes or no): ")
while another_class.lower() == "yes":
    grade_level = input("Enter Grade level (i.e: A_ap) or if done type 'done': ")
    if grade_level == "done":
        break
    if grade_level in globals():
        total_gpa += globals()[grade_level]
        number_classes += 1
    else:
        print("Grade level not found.")
    another_class = input("Do you have another class? (yes or no): ")

if number_classes == 0:
    print("Not Valid: ")
else:
    average_gpa = total_gpa / number_classes
    print("Average GPA:", average_gpa)
