# 02 Problem

# Write a program to accept marks of 6 students and display them in a sorted manner.

mark_of_students = []

# VERY IMPORTANT NOTE BELOW
# Change the type of the marks enter in the list because 
# by default its return string and we need to convert them in
# int then it cab be arraged in sorted manners

mrk_stu1 = int(input("Enter the Marks of Student 1: ")) 
mark_of_students.append(mrk_stu1)
mrk_stu2 = int(input("Enter the Marks of Student 2: "))
mark_of_students.append(mrk_stu2)
mrk_stu3 = int(input("Enter the Marks of Student 3: "))
mark_of_students.append(mrk_stu3)
mrk_stu4 = int(input("Enter the Marks of Student 4: "))
mark_of_students.append(mrk_stu4)
mrk_stu5 = int(input("Enter the Marks of Student 5: "))
mark_of_students.append(mrk_stu5)
mrk_stu6 = int(input("Enter the Marks of Student 6: "))
mark_of_students.append(mrk_stu6)


print(mark_of_students)
mark_of_students.sort()
print(mark_of_students)
