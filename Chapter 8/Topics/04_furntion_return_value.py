# Function Definition

def practice_of_return_value():
    marks = int(input("Enter the marks: "))

    if (marks >= 50 and marks<=59):
        print("You are Passed exams But Not Eligible 60% Marks required out of 100")

    elif(marks >= 60):
        print("Congratzzzz!!!! Your are Passed your exams and eligible for the job\nThank you!!!")

    else:
        print("OOOOPPPPSSSS!!!! You are Failed in your exam just next year after getting passsing marks")

        # function ek value le ja or jo b variable mangy usko de dna
        # Return value showing in a where it is calling
        # kch b return krwa skty hain hm like below or 5, 6

    return marks # This will return marks which user enter
    # return 5


a = practice_of_return_value() # calling Function
print("Your marks is",a) # Taking value from function with return keyword