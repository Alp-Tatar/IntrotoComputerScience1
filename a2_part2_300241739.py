import math

def min_enclosing_rectangle(radius, x, y):
    '''
     (radius, x, y)-> numbers
     Preconditions: radius must be positive float, x,y are also a positive int
     Returns x- and y-coordinates of the bottom-left corner of that rectangle
    '''
    xofrectangle= x-radius
    yofrectangle= y-radius
    if radius > 0:
       return (xofrectangle,yofrectangle)
    else:
        return None

def vote_percentage (results):
    '''
     (result)-> string
     Preconditions: must be a string of all lowercase results
     Returns the average of yes votes
    '''
    totYes = results.count("yes",0,len(results)+1)
    totNo = results.count("no", 0, len(results) + 1)
    totabstained = results.count("abstained", 0, len(results) + 1)
    return totYes/(totNo+totYes)


def vote():
    '''
     (result)-> string
     Preconditions: N/A
     Returns a string based off the percent of the percent of winning
    '''
    result =str(input("Enter the yes, no, abstained votes one by one and then press enter:\n"))
    percent=vote_percentage(result)
    if percent > 0.5:
        return "proposal passes with simple majority"
    elif percent> 2/3:
        return "proposal passes with super majority"
    else:
        return "proposal fails"


def l2lo(w):
    '''
     (w)-> number
     Preconditions: that takes a non-negative number w
     Returns a pair of numbers (l,o) such that w = l + o/16 and l is an integer and o is a non-negative number smaller than 16
    '''
    i=int(w//1)
    o= (w-i)*16
    return (i,o)
