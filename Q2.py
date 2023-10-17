# Name - Pashvi Prajapati
# COSC 3P95 
# Assign 1 : Q2 

# The following code will implement the sorting algorithm to sort the list of array in ascending order and generate random test cases.

import random #to generate random numbers from the python library

# This function will sort the array list with the sorting algorithm in ascending order
def sort_arr(list):
    l = len(list) #length of list is defined 
    for p in range(l):  #iterating through each element in the list of array
        indexM = p #index has the minimum value in the list of array
        for k in range(p + 1, l): #iterating the rest elements in the list that is remained
            if list[k] < list[indexM]: #to check if there is any other smaller element present 
                indexM = k #then change it to minimum element 
        list[p], list[indexM] = list[indexM], list[p] #elements will be swaped in order to sort the list of array
    return list #returns the list of array  

# This fucntion will generate random test cases for sorting algorithm to the elementts in the array list and returns the sorted array
def rand_arr(size, minI, maxI):
    arrI = [random.randint(minI, maxI) #random length of list between 5 to 50
            for j in range(size)] 
    sort = sorted(arrI) #this will generate a random array list
    return arrI, sort #it will return the input array list as well as the sorted array

#main function 
def main():
    #defining the size, min and max value to be generated from random function 
    size = 4  #the size is set to be 4
    minI = 5  #minimum value is set to 5 
    maxI = 50  #maximum value is set to 50
    arrI, expA = rand_arr(size, minI, maxI) #this will generate a random test case 
    print("Given is the input array list:", arrI) #it will print the input array
    sort = sort_arr(arrI.copy())  #sorts the array and a backup for original array
    print("Given is expected sorted array list:", expA)  #this will give the expected sorted array
    print("Given is sorted array list:", sort) #this will print the actual sorted array

if __name__ == "__main__":
    main()
#program end 
 