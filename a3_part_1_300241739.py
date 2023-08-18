import string
def split_tester(N, d):
    '''
    (string,string) -> Boolean
    Splits the string N into the amount of d and checks if the value was increasing
    precondition: lenth of string should be evenly divided the the value of D, Also N and d needs to be a positive integer
    '''
    isincreasing = False
    d = int(d)
    comparision1 = ""
    comparision2 = ""

    if len(N) % d == 0:
        isincreasing = True
        for i in range(int(len(N) / d) - 1):
            comparision1 = N[i*d:i*d + d]
            comparision2 = N[i*d + d:i*d + 2 * d]
            if int(comparision1) > int(comparision2):
                isincreasing = False
            print(comparision1 + ", ", end='')
    if len(N)==d:
        print(N)
        isincreasing = True
    else:
        print(comparision2)
    return isincreasing


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
# Your code for the welcome message goes here, instead of name="Vida"
ascii_name_plaque("Welcome to my increasing-splits tester")
name=input("What is your name?")
name=name.strip()
ascii_name_plaque(name+", welcome to my increasing-splits tester.")
flag=True
while flag:
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
    elif question =="yes":
        print("Good choice!")
        num= input("Enter a positive integer:")
        num = num.strip()
        if num.rfind(".") != -1:#checks if its a float
            print("The input can only contain digits. Try again.")
        elif any(c.isalpha() for c in num): # check if its a word string
            print("The input can only contain digits. Try again.")
        elif num.rfind("-") != -1 or int(num) <= 0:#checks if its a negative
            print("The input has to be a positive integer.Try again.")
        else:
            split=(input("Input the split. The split has to divide the length of " + str(num) +" i.e "+str(len(num))+" "))
            split=split.strip()
            if split.rfind(".") != -1:  # checks if its a float
                print("The input can only contain digits. Try again.")
            elif split.rfind("-") != -1:  # checks if its a negative
                print("The input can only contain digits. Try again.")
            elif any(c.isalpha() for c in split):  # check if its a word string
                print("The input can only contain digits. Try again.")
            elif len(num)%int(split) != 0:
                print(split + " does not divide "+ str(len(num))+". Try again.")
            elif int(num)>1 and isinstance(num,str):
                isincreasing=split_tester(str(num),str(split))
                if isincreasing == True:
                    print("The sequence is increasing")
                elif isincreasing == False:
                    print("The sequence is not increasing")
    else:
        print("Please enter yes or no. Try again.")


ascii_name_plaque("Good bye " + name+"!")
