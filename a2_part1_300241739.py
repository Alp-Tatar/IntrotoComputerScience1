import math
import random

#Elementry quiz function
def elementary_school_quiz(flag, n):
    '''
      (flag, n)-> number

      Preconditions:
      flag must either be a 1 or 0 number
      n must be 1 and 2 number

      Returns:
      the amount of correct answers a student has done for either logorithm or exponation questions as an int
    '''

    correctresult = 0

    if flag == 0 and 1<=n<=2:
        for i in range(n):
            print("Question" +" "+ str(i + 1)+":")
            Answer = (random.randint(1, 10))
            logvalue=int(math.pow(2,Answer))
            studentanswer=int(input("2 to what is " + str(logvalue)+" i.e. what is the result of log_2 ("+str(logvalue)+")?"))
            if Answer == studentanswer:
                correctresult +=1
            i+=1

    if flag == 1 and 1<=n<=2:
        for i in range(n):
            print("Question " + str(i +1))
            power = random.randint(1, 10)
            Answer = int(math.pow(2,power))
            studentanswer = int(input("What is the result of 2^" + str(power)+"?"))
            if Answer == studentanswer:
                correctresult +=1
            i+=1

    return correctresult


#highschool quiz function
def high_school_quiz(coefficentA,coefficentB,coefficentC):
    '''
          (coefficentA,coefficentB,coefficentC)-> number

          Preconditions: This function (coefficentA,coefficentB,coefficentC) = representing three real numbers

         Returns the string and prints the string of the equation and the roots of it.
    '''

    if coefficentC ==0 and coefficentA == 0 and coefficentB ==0 :
        equationofFunction = "0.0·x + 0.0 = 0"
        return print("the quadradic equation "+ str(equationofFunction)+ "\nis satisfied for all numbers x")
    elif coefficentA ==0 and coefficentC:
        equationofFunction = str(coefficentB) + "·x "+  " = 0"
        return print("the quadradic equation " + str(equationofFunction) + "\nis satisfied for all numbers x")

    elif coefficentA == 0:
        equationofFunction = str(coefficentB) + "·x + " + str(coefficentC) + " = 0"
        root = coefficentC/coefficentB
        return print("The quadradic expression " +  str(equationofFunction) + "\nhas the following root" + str(root))

    elif coefficentB ==0:
        equationofFunction= str(coefficentA)+"·x^2 + "+ str(coefficentC) + " = 0"
        root = math.sqrt(coefficentC)
        return print("The quadradic expression " + str(equationofFunction) + "\nhas the following root" + str(root))

    elif coefficentC ==0:
        equationofFunction = str(coefficentA)+"·x^2 + "+  str(coefficentB) + "·x "+  " = 0"
        discriminant = math.pow(float(coefficentB), 2)
        if discriminant == 0:
            quadradicformula = "has only one solution, a real root: " + "\n" + str((-1 * (coefficentB)) / (2 * coefficentA))
        elif discriminant > 0:
            quadradicformula = "has the following real roots:" + "\n" + str((-1 * coefficentB + math.sqrt((discriminant))) / (2 * coefficentA)) + " and " + str(((-1 * coefficentB - math.sqrt((discriminant))) / (2 * coefficentA)))
        return print("The quadratic equation \n " + equationofFunction + "\n" + quadradicformula)
    else:
        equationofFunction = str(coefficentA)+"·x^2 + " + str(coefficentB)+"·x + " +  str(coefficentC)+ " = 0"
        discriminant = math.pow(float(coefficentB), 2) - (4 * (float(coefficentA)) * (float(coefficentC)))

        if discriminant < 0:
            quadradicformula = "has the following two complex roots:" + "\n" + str(
                -1 * coefficentB / (2 * coefficentA)) + " +" + " i " + str(
                math.sqrt((-1 * discriminant)) / (2 * coefficentA)) + " and \n " + str(
                -1 * coefficentB / (2 * coefficentA)) + " - " + "i " + str(
                math.sqrt((-1 * discriminant)) / (2 * coefficentA))
        elif discriminant == 0:
            quadradicformula = "has only one solution, a real root: " + "\n" + str(
                (-1 * (coefficentB)) / (2 * coefficentA))
        elif discriminant > 0:
            quadradicformula = "has the following real roots:" + "\n" + str(
                (-1 * coefficentB + math.sqrt((discriminant))) / (2 * coefficentA)) + " and " + str(
                ((-1 * coefficentB - math.sqrt((discriminant))) / (2 * coefficentA)))

        return print("The quadratic equation \n " + equationofFunction + "\n" + quadradicformula)

def ascii_name_plaque(name):
    '''
    (str)->None
    Draws/Prints name plaque
    '''
    thePlaquetopandbot = "**" + ("*" * (len(name) + 4)) + "**"
    thePlaquespaceswith = "* " + ((" ") * (len(name) + 4)) + " *"
    thePlaquemiddle = "* " + ("__" + name + "__") + " *"
    print(thePlaquetopandbot + "\n" + thePlaquespaceswith + "\n" + thePlaquemiddle + "\n" + thePlaquespaceswith + "\n" + thePlaquetopandbot)

    # main

ascii_name_plaque("Welcome to my math quiz-generator")

name = input("\nWhat is your name? ")

status = input("Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status == '1':#Elementary school quiz

    ascii_name_plaque(str(name)+", welcome to my quiz-generator for elementary school students.")
    studentselection= input(name+" what would you like to practice? Enter \n"+"0 for inverse of exponentiation\n"+ "1 for exponentitation \n")
    howmanyquestions= int(input("How many practice questions would you like to do? Enter 0, 1, or 2: "))
    correctamount=0
    if int(howmanyquestions) == 0:
        print("Zero questions. OK. Good bye")
    elif int(studentselection) <0:
        print("Invalid chose. Only 0 or 1 is accepted.")
    else:
        print(name + " here is your "+ str(howmanyquestions) + " questions:")
        correctamount = elementary_school_quiz(int(studentselection), int(howmanyquestions))

    if correctamount == 0:#Based of correct amount the student does prints a message accordingly
        print("I think you need some more practice " + name)
    elif (correctamount == 1 and howmanyquestions == 1) or (correctamount == 2 and howmanyquestions == 2):
        print("Congratulations " + name + " You’ll probably get an A tomorrow.")
    elif (correctamount == 1 and howmanyquestions == 2):
        print("You did ok " + name + ", but I know you can do better.")

elif status == '2':#Highschool school quiz
    ascii_name_plaque("quadratic equation, a·x^2 + b·x + c= 0, solver for "+str(name))
    flag = True
    while flag:#continues until user types something else
        question = input(name + ", would you like a quadratic equation solved? ")
        question = question.lower() #by lowercasing the input it will help them

        if question != "yes":
            flag = False#ends loop
        else:
            print("Good choice!")#inputs for the function
            CoefficentA = int(input("Enter a number the coefficient a:"))
            CoefficentB = int(input("Enter a number the coefficient B:"))
            CoefficentC = int(input("Enter a number the coefficient C:"))
            high_school_quiz(CoefficentA, CoefficentB, CoefficentC)#prints the high_school_quiz
else:
    print(name + " you are not a target audience for this software.")

print("Good bye " + name + "!")
