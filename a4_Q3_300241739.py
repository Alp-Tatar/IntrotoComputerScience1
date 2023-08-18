def longest_run(l):
    '''(list)-> int
     Returns the length of the longest run in the list of numbers x.
     Precondition: x is a list of numbers
    '''

    if len(l)==0:
        return 0
    else:



        while i < len(l) - 1:
            length = 1
            while i < len(l) - 1 and l[i] == l[i + 1]:
                length = length + 1
                i = i + 1
            if length > max_length:
                max_length = length
            i = i + 1
        return max_length


#Main list of numbers seperated by spaces

raw_input = input("Please input a list of numbers separated by space: ").strip().split()
l=[]
for s in raw_input:
     l.append(float(s))
print(longest_run(l))


