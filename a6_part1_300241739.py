import string

def open_file():
    '''None->file object
    function will prompt the user for a file-name, and try to open that file. If the file exists, it will return the file
    object; otherwise it will re-prompt until it can successfully open the file.
    '''
    while True:
        try:
            name=input("Enter the name of file you want to open: ")
            file=open(name,"r")
            return file
        except FileNotFoundError:
            print("There is no file with that name. Try again.")

def read_file(fp):
    '''(file object)->dict
    This function will read the contents of that file line by line, process them and store them in a dictionary. The dictionary is
    returned.
    '''
    lines = textlist(fp)
    for i in range(0,len(lines)):
        lines[i]=remove_Punctuation(lines[i])
    d=make_dict(lines)
    return d



def find_coexistance(D, query):
    '''(dict,str)->list
    This query contains zero or more words separated by white space. You need to split them into a list of words, and
    find the line numbers for each word. Then convert the resulting set to a sorted list, and return the sorted list.
    '''
    savedsets=[]
    returncoxistance=[]


    if(query.isdigit()== True):
        return [None,query]


    query = remove_query(query)

    searchfor=query.split()



    if not searchfor:
        return [None,0]

    for i in range(0,len(searchfor)):
        try:
            savedsets.append(D[searchfor[i]])
        except KeyError:
            return [None, searchfor[i]]


    x=list(compare_sets(savedsets))
    x.sort()
    if len(x) == 1:
        return x
    elif len(x)==0:
        return [None,0]
    return x


def remove_Punctuation(words):#anywhere that isn't a number must remove
    '''(str)->str
    Returns a string that removes the punctation and numbers '''
    sentence = words
    sentence=str(' '.join([w for w in sentence.split() if len(w)>1]))
    punc="#$%&()*'-+,./:;<=>?@[\]^_`{|}~1234567890\""
    sentence = sentence.translate(str.maketrans('', '', punc))
    sentence.lower()
    return sentence

def remove_query(words):#anywhere that isn't a number must remove
    '''(str)->str
    Returns a string that removes the punctation '''
    sentence = words
    sentence=str(' '.join([w for w in sentence.split() if len(w)>1]))
    punc="#$%&()*'-+,./:;<=>?@[\]^_`{|}~\""
    sentence = sentence.translate(str.maketrans('', '', punc))
    sentence.lower()
    return sentence


def make_dict(lsw):
    '''(list)->dic
    returns a dictionary of the list of words
    '''
    d={}

    for i in range(0,len(lsw)):
        textline=i+1
        senteceholder = lsw[i]
        senteceholder=senteceholder.lower()
        diffwords = senteceholder.split()
        for j in range(0,len(diffwords)):
          if d.get(diffwords[j]) == None:
            d.setdefault(diffwords[j],{textline})
          else:
            x=d[diffwords[j]]
            x.add(textline)
            d.update({diffwords[j]:x})
    return d

def textlist(fp):
    '''(fileobject)->list
    Returns a list of the file objects for each line of the text file
    '''
    return [line.strip() for line in fp]

def compare_sets(lst):
    '''(sets)-> set
    returns the intersecting points of sets
    '''
    return set.intersection(*lst)





##############################
# main
##############################
file=open_file()
d=read_file(file)
flag=True
while flag==True:
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
        if query == "q":
            flag = False
        else:
            coexistance = find_coexistance(d,query)
            if coexistance[0] is None:
                if coexistance[1] == 0:
                    print("There wasn't an input in the search. Please try again.")
                else:
                    print("Word '" +coexistance[1]+"' not in the file.")
            else:
                print("The one or more words you entered coexisted in the following lines of the file:")
                print(*coexistance)



