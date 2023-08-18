def two_length_run(l):
    '''(list)-> bool
          Returns True if there is a run of length at least 2
          in the list of numbers x and False otherwise.

          Precondition: x is a list of numbers
         '''

    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return True
    return False


#main ask for lists seperated by spaces


raw_input = input("Please input a list of numbers separated by space: ").strip().split()
l=[]
for i in raw_input:
     l.append(float(i))
print(two_length_run(l))

