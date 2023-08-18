import math
def sum_odd_divisors(n):
    '''
    (int) -> (int),if input is 0 (None)
    s returns the sum of all the postive odd divisors of n
    Preconditions:Must be an int
    '''
    odddivisor = 0
    if (n==0):
        return None
    else:
        for x in range(1, int(math.fabs(n) )+ 1):
            if (n % x == 0) and (x%2 != 0):
                odddivisor += x
    return odddivisor



def series_sum():
    '''
    (n/a) -> (int)
    Asks user for a non negative integer. If negative is given return a zero. Else find the sum of the series 100 + !q/n^2.
    Preconditions:Non negative int
    '''
    userinput = int(input("Please enter a non-negative integer:"))
    if userinput < 0:
        return None
    else:
        series=0
        for x in range(userinput):
            series += (1/((x+1)**2))
        return 1000+series

def pell(n):
    '''
    (int) -> (int)
    that If n is negative, pell returns None. Else,pell returns the nth Pell number
    Preconditions: n has to be a positive int
    '''
    if n <0:
        return None
    else:
        recrusivevaluefinal = 2
        recursivevalueinital = 1
        value= 0
        if n > 2:
            for i in range(3,n+1):
                value = recursivevalueinital + 2 * recrusivevaluefinal
                recursivevalueinital = recrusivevaluefinal
                recrusivevaluefinal = value
        elif n<=1:
            return n
        return recrusivevaluefinal

def countMembers(s):
    '''
    (string) -> (int)
    then returns the number of characters in s, that are extraordinary. It is extrairdinary if it is between e and j and between numbers 2 and 6 or if it is !, ',' ,  \\
    Preconditions: Must be a string input
    '''
    total=0
    for x in s:
        if (x>='e' and x<="j") or (x>='e' and x<="j") or (x>='2' and x<="6") or x=='!'or x==',' or x=='\\':
            total +=1
    return total


def casual_number(s):
    '''
    (string) -> (int)
    Checks if there is any alpha numeric characters and if there is a , between numbers remove them
    Preconditions: No letters or numbers with multiple ,,, back on back should be put in
    '''
    newnum=""
    if (any(c.isalpha() for c in s) == False) :
        anynegs= 0
        for x in range(len(s)):
            value=s[x]
            if value == "-":
                anynegs+=1
            elif anynegs>1:
                return None

        value = 0
        for x in range(len(s)):
            value=s[x]
            if value=='-' or value=='1' or value=='2' or value=='3' or value=='4' or value=='5' or value=='6' or value=='7'  or value=='9'  or value=='0':
                newnum+=value

        if newnum != "-":
            return int(newnum)
    else:
        return None

def alienNumbers(s):
    '''
    (string) -> (int)
    sorts through an alien language writing systgem where T = 1024, y=598, ! = 121, a=42, N=6, U =1 and find it in binary numbers
    Preconditions: must be a string using the alien number system
    '''
    return int((s.count('T')*1024)+(s.count('y')*598)+(s.count('!')*121)+(s.count('a')*42)+(s.count('N')*6)+(s.count('U')*1))

def alienNumbersAgain(s):
    '''
    (string) -> (int)
    sorts through an alien language writing systgem where T = 1024, y=598, ! = 121, a=42, N=6, U =1 and find it in binary numbers
    Preconditions: must be a string using the alien number system
    '''
    alienbinarynumber = 0
    for x in range(len(s)):
        value = s[x]
        if value == 'T':
            alienbinarynumber += 1024
        elif value == 'y':
            alienbinarynumber += 598
        elif value == '!':
            alienbinarynumber += 121
        elif value =='a':
            alienbinarynumber += 42
        elif value =='N':
            alienbinarynumber += 6
        elif value =='U':
            alienbinarynumber += 1
    return  alienbinarynumber

def encrypt(s):
    '''
    (input type) -> (output type)
    Function description
    Preconditions: (does the input have to be positive or something)
    '''
    reversstring = s[::-1]
    cipher=""
    for x in range(math.ceil(len(s)/2)):
        cipher+= reversstring[x]
        if math.floor(len(s)/2) == x:
          return cipher
        cipher+=s[x]

    return cipher

def oPify(s):
    '''
    (string) -> (string)
    adds an op based off of whether the inputer alphanumerica value is Uppercase or Lowercase.
    Preconditions: Must be a string
    '''
    final=""
    for x in range(len(s)-1):
      final += s[x]
      a=s[x]
      b=s[x+1]
      if a.isalpha() == True:
          if a.isupper() or b.islower():
            if a.isupper() and b.isupper():
                final+= "OP"
            elif a.isupper()and b.islower():
                final+= "Op"
            elif a.islower() and b.isupper():
                final+="oP"
            elif a.islower() and b.islower():
                final+="op"
    return final+s[len(s)-1]


def nonrepetitive(s):
    '''
    (str) -> (Boolean)
    Checks if a string is repetitive or if it isn't
    Preconditions: (must be a string input)
    '''
    for x in range(1,(int(len(s)/2)+1)):
        for y in range(len(s)):
            if(y+2*x <= len(s)) and (s[y:y+x] == s[y+x:y+(2*x)]):
                return False
    return True

