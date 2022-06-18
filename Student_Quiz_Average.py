def toFixed(value, digits):
    return "%.*f" % (digits, value)

average = 0.0 
total = 0.0

# INPUT OPERATIONS
print("Enter the name of Student #1")
stuName1 = input()
print("Enter quiz #1 for " + stuName1)
quiz1 = float(input())
print("Enter the name of Student #2")
stuName2 = input()
print("Enter the quiz #2 for " + stuName2)
quiz2 = float(input())
print("Enter the name of Student #3")
stuName3 = input()
print("Enter quiz #3 for " + stuName3)
quiz3 = float(input())
print("Enter the name of Student #4")
stuName4 = input()
print("Enter the quiz #4 for " + stuName4)
quiz4 = float(input())
print("Enter the name of Student #5")
stuName5 = input()
print("Enter the quiz #5 for " + stuName5)
quiz5 = float(input())

# CALCULATE TOTAL OF QUIZZES
total = quiz1 + quiz2 + quiz3 + quiz4 + quiz5
average = total / 5

# OUTPUT OPERATIONS
print("================================================")
print("STUDENT QUIZZES")
print("===============================================")
print("STUDENT NAME QUIZZES")
print("======================================")

# STUDENT NAMES AND QUIZ GRADES
print(stuName1 + "   " + toFixed(quiz1,2))
print(stuName2 + "  " + toFixed(quiz2,2))
print(stuName3 + "  " + toFixed(quiz3,2))
print(stuName4 + "  " + toFixed(quiz4,2))
print(stuName5 + "  " + toFixed(quiz5,2))
print("===================================================================")

# TOTAL/SUM OF QUIZZES
print("Total of the quizzes = " + toFixed(total,2))
print("===================================================================")

# QUIZ AVERAGE
print("QUIZ AVERAGE = " + toFixed(average,2) + "%")
print("===================================================================")

# END PROGRAM
