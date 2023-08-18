def number_divisible(l, n):
    '''(list of ints, int)->int
     Returns the number of elements of the list x that are divisible by n
     '''
    counter = 0
    for num in l:
        if num % n == 0:
            counter = counter + 1
    return counter



#Main  - asks for a list seperated by spaces and and a integer

raw_input = input("Please input a list of numbers separated by spaces: ").strip().split()
numberinput = int(input("Please input an integer: "))
listinput=[]
for item in raw_input:
     listinput.append(int(item))

print("The number of elements divisible by", numberinput, "is", number_divisible(listinput, numberinput))
