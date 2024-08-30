# Problem 02

# Write a program to find out whether a student has passed or failed if it requires a total of 40% and
# atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

python_marks = int(input("Enter Marks of Python: "))
machine_learning_marks = int(input("Enter Marks of Machine Learning: "))
data_science_marks = int(input("Enter Marks of Data Dcience: "))

total_percentage = (100*(python_marks + machine_learning_marks + data_science_marks))/300

if(total_percentage>=40 and python_marks>=33 and machine_learning_marks>=33 and data_science_marks>=33):
    print("Congratulation!!! You Passed Your Exam", total_percentage)

else:
    print("OOPPPSSS!!!! You are Failed in you Exam, Try Next year",total_percentage)


