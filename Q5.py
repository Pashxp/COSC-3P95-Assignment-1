# Name : Pashvi Prajapati
# COSC 3P95 
# Assign 1 : Q5 

# The following will implement the Delta Debugging algorithm in python to minimize the input string that reveals the bug.

#This fucntion divides the input string into equal parts.
def divide(in_S, num_S):
    len_Av = len(in_S) // num_S #it will calculate the average length for each element and to divide it equally
    return [in_S[e:e + len_Av] for e in range(0, len(in_S), len_Av)] #it will return the list of elements part

#The following function will iterate the input while corner the bug using delta debugging strategy
def inputR(in_S, pr):
    len_max, len_min = len(in_S) , 1 #it defines maximum length of the string and minimum length of the string which is set to 1, as it should not process empty string
    while len_min <= len_max: #while the maximum length is greater than or equal to minimum length
        m = (len_min + len_max) // 2 #it will give the mid length of the input string
        inpR = in_S[:m] #then it will minimize the input string to the midpoint that has been calculated in previous line 
        len_max = m - 1 if pr(inpR) else len_max  #then it will minimize the maximum length 
        len_min = m + 1 if not pr(inpR) else len_min  #otherwise it will increase the minimum length     
    return in_S[:len_min] #it will then return the minimized string upto minimum length as mentioned

#The following function will determine if the program has any bug in the code i.e. if the numeric value is duplicated in any case 
def bugIn(in_S):
    return "56" in str(in_S)  #checks the conditiona and returns the boolean value 

#The following function converts uppercase letters to lowercase and vice versa, exclusing the  numeric characters that is determined to be unchanged.
def str(in_S):
    strOut = "" #initializes empty string
    for c in in_S:
        if c.isupper(): #if the char is found to be uppercase 
            strOut += c.lower() #it will be changed to lowercase
        elif c.isnumeric(): #checks if the char is numeric 
            strOut += c  #appends as it as
        else:
            strOut += c.upper()
    return strOut #returns the output string 

#The following are the test cases that needs to be tested in order to check the functionality of the program 
inputS = ["abcdefG1", "CCDDEExy", "1234567b", "8665"] #list of strings given that needs to be processed 
#for loop iterates over the input string with the index plus 1
for e, in_S in enumerate(inputS, start=1):
    print(f"{e}: {in_S} : Unchanged output string") #prints actual output without modifying it 
    min = inputR(in_S, bugIn) #it will corner the bug from rest of the input string 
    print(str(min), "Final output string") #Prints the finalized output (changed string) 
   
   #end of program 
