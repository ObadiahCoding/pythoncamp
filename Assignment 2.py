# Question 1

garlands = "aA"
flowers = "aAAbbbb"

def compareStrings():
    count = 0
    for char in flowers:
        if char in garlands:
            count +=1
    return count
        
result = compareStrings()
print(result)

# Question 3
number = int(input("Enter any number of your choice: "))
def calculateSum():
    count = 0 
    for i in range (1, number + 1):
        count += i
    return count   

total = calculateSum()
    
print(F"The sum of the numbers is: {total}")

# Question 4
string = input(" enter a string: ")
def customLen(string):
    count = 0
    for char in string:
        count += 1
    return count
length = customLen(string)
print(length)


# Question 5
number = int(input("enter a number: "))
def multiplicationTable():
    product = 0
    for i in range(1,13):
        product = i * number
        print(f"{i} * {number} = {product}")
result = multiplicationTable()


# Question 6
number = int(input("guess the magic number: "))
def secretNumber():
    count = 0
    for i in range(1,100):
        if 1 <= number < 60:
            return "number is too low"
        elif 60 <number<= 100:
            return "number is too high"
        elif number == 60:
            return "Hooray! you got it correct7"
        else:
            return "number is outside the range"
                        
print(secretNumber())

#Question 7
character = input(" Enter any letter of your choice: ")
def is_vowel():
    #char = ""
    vowels = ["a","e","i","o","u"]
    char = character.lower()
    if char in vowels:
       
        return True
    else:
        return False
        
print(is_vowel()) 



#Question 2

score = float(input("enter your score: "))
def numericalScore():
    if 80 <= score<= 100:
        grade = "A"
        grade_point = 4.0
    elif 75<= score<=79:
        grade = "B+"
        grade_point = 3.5
    elif 70<= score<75:
        grade = "B"
        grade_point = 3.5
    elif 65<= score<70:
        grade = "C+"
        grade_point = 3.0
    elif 65<= score<70:
        grade = "C"
        grade_point = 2.5
    elif 60<= score<65:
        grade = "D+"
        grade_point = 2.0
    elif 55<= score<60:
        grade = "D"
        grade_point = 1.5
    elif 50<= score<55:
        grade = "E"
        grade_point = 1.0
    elif 0<= score<50:
        grade = "F"
        grade_point = 0.0
    else:
        grade = "N/A"
        grade_point = 0.0
    return grade, grade_point
print(numericalScore())
GPA = float(input("enter your GPA: "))
def cummulativeGPA():
    if 3.85<=GPA<=4.0:
        honors = "Summa Cum Laude"
    elif 3.70<=GPA<3.85:
        honors = "Magnna Cum Laude"
    elif 3.50<=GPA<3.70:
        honors = "Cum Laude"
    elif 0.0<=GPA<3.5:
        honors = "None"
    else:
        honors = "N/A"
    return honors
print(cummulativeGPA())
    
    