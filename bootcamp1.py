
#Q 1
#/This code calculates the total grade of a student.
HomeWork_Grade = float(input("Enter your home work grade: "))
Exam_Grade = float(input("Enter your exam grade: "))
Discussion_Grade = float(input("Enter your discussion grade: "))
Total = HomeWork_Grade + Exam_Grade + Discussion_Grade
print(f" my total grade is {Total}")

#Q 3
#This code calculates the total amount of an investment
Principal = 1000
n = 12
rate = 8
t= float(input("enter the number of years: "))
Amount = float(Principal*(1 + rate/n)**n*t)
print(f" The total amount is $ {Amount}")

# Q 5
# This code calculates the area of a circle with any radius entered
import math
r= float(input("enter thr radius of the circle: "))
Area = float(math.pi* r**2)
print(Area)


# This code determines what lengths of different sticks that can form a triangle
#Q 6 (a)

def triangle(base, height, hypotenus,):
    if base + height > hypotenus:
        print("True")
    elif base + height == hypotenus:
        print("degenerate triangle")
    else:
        print("false")
triangle(3, 5, 9)

#Q 6 (b)
# This code ask for user inputs to determine whether the lengths can form a triangle or not.
def triangle():
    stick1 = int(input("Enter the length of stick1: "))
    stick2 = int(input("Enter the length of stick2: "))
    stick3 = int(input("Enter the length of stick3: "))
    if int(stick1 + stick2) > int(stick3):
        print("They can form a triangle")
    elif int(stick1 + stick2) == int(stick3):
        print("degenerate triangle will be formed")
    else:
        print("They cannot form a triangle")
triangle()

#Q 2) A void function is a function that does not return a value after its execution while a fruitful function is a function that returns a value after execution.

# Q 4) This code calculates GPAs and their corresponding honors.
def calculateGPA():

    Course1 = int(input("enter the score: "))
    Course2 = int(input("enter the score: "))
    Course3 = int(input("enter the score: "))
    Course4 = int(input("enter the score: "))
    
    if (Course1 >= 80):
        Course1== 4.0
        print(4.0)
    elif ( 75<= Course1 <= 79):
        Course1==3.5
        print(3.5)
    elif(70 <= Course1 <= 74):
        Course1==3.0
        print(3.0)
    elif(65 <= Course1 <=69):
        Course1==2.5
        print(2.5)
    elif(60<= Course1 <=64):
        Course1==2.0
        print(2.0)
    elif(55<= Course1 <=59):
        Course1==1.5
        print(1.5)
    elif(50<= Course1 <=54):
        Course1==1.0
        print(1.0)
    else:
        Course1==0.0
        print(0.0)
    if (Course2 >= 80):
        Course2==4.0
        print(4.0)
    elif ( 75<= Course2 <= 79):
        Course2==3.5
        print(3.5)
    elif(70 <= Course2 <= 74):
        Course2==3.0
        print(3.0)
    elif(65 <= Course2 <=69):
        Course2==2.5
        print(2.5)
    elif(60<= Course2 <=64):
        Course2==2.0
        print(2.0)
    elif(55<= Course2 <=59):
        Course2==1.5
        print(1.5)
    elif(50<= Course2 <=54):
        Course2==1.0
        print(1.0)
    else:
        Course2==0
        print(0.0)
    if (Course3 >= 80):
        Course3==4.0
        print(4.0)
    elif ( 75<= Course3 <= 79):
        Course3==3.5
        print(3.5)
    elif(70 <= Course3 <= 74):
        Course3==3.0
        print(3.0)
    elif(65 <= Course3 <=69):
        Course3==2.5
        print(2.5)
    elif(60<= Course3 <=64):
        Course3==2.0
        print(2.0)
    elif(55<= Course3 <=59):
        Course3==1.5
        print(1.5)
    elif(50<= Course3 <=54):
        Course3==1.0
        print(1.0)
    else:
        Course3==0
        print(0.0)
    if (Course4 >= 80):
        Course4==4.0
        print(4.0)
    elif ( 75<= Course4 <= 79):
        Course4==3.5
        print(3.5)
    elif(70 <= Course4 <= 74):
        Course4==3.0
        print(3.0)
    elif(65 <= Course4 <=69):
        Course4==2.5
        print(2.5)
    elif(60<= Course4 <=64):
        Course4==2.0
        print(2.0)
    elif(55<= Course4 <=59):
        Course4==1.5
        print(1.5)
    elif(50<= Course4 <=54):
        Course4==1.0
        print(1.0)
    else:
        Course4==0.0
        print(0.0)
   
    
def calculateHonors():
    calculateGPA()
    GP1 = float(input("enter your GPA for course1: "))
    GP2 = float(input("enter your GPA for course2: "))
    GP3 = float(input("enter your GPA for course3: "))
    GP4 = float(input("enter your GPA for course4: "))
    
    CGPA =  float((GP1 + GP2 +GP3 + GP4)/4)
    if (3.5 <= CGPA <= 3.69):
        print("You got a cum laude")
    elif(3.70 <= CGPA <=3.84):
        print("You got a magna cum laude")
    elif(CGPA >= 3.85):
        print("You got a summa cumlaude")
    elif(2.0 <= CGPA <=3.49):
        print("Graduating with no honor")
    else:
        print("Sorry,you can't graduate")
    
calculateHonors()
                    
    
    