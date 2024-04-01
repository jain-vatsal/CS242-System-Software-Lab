TERMINAL:- 
1. Write "sudo apt install python3" to install the python package and compiler.
2. Write "python3 <file_name>.py" to run a particular file.

-----------------------------------------------------------------------------

QUESTION 1 EXPLANATION:- 
1. First we declare a list 'a' to store the alphabets
2. i =(i+k)%len(a) gives the index of the person going to be killed next, and we remove this person from the list using .remove function.
3. We use the current and former values of i to print the killer and the killed.
4. We repeat the process till len(a)>0. 
5. We get the required sequence.

------------------------- CODE FOR THE FIRST QUESTION --------------------------------
# this function is used to print the name of the killer
def printthekiller(a, k):
    print("\n"+str(a[k])+" kills ", end='')

# this function is used to given the index of the person being killed


def reqvalue(a, i, k):
    i += k
    i %= len(a)
    return i

# this function is used to print the name of the person being killed


def printthekilled(a, i):
    print(str(a[i]))

# this function is used to remove the element from the list


def removetheelement(a, i):
    a.remove(a[i])


# storing all the characters in the list initially
a = []
i = 1
while i <= 26:
    t = i+64
    i += 1
    a.append(chr(t))

# initializing the list to sequence of the people being killed
killed = []

# taking the input from the user
n = int(input("Enter the value of n = "))
k = int(input("Enter the value of k = "))

if k < 0:
    print("Invalid input")
else:
    i = 0
    while i < n:
        i += 1

    # getting the required list by removing unnecessary elements
    while len(a) > n:
        a.remove(a[i])

    i = 0

    # loop for order of killing of the people
    while len(a) > 1:
        if i == len(a):
            i = 0
        printthekiller(a, i)
        i = reqvalue(a, i, k)
        printthekilled(a, i)
        killed.append(a[i])
        removetheelement(a, i)
        if len(a) >= 1:
            print("Remaining = ", end='')
            for j in range(len(a)):
                print(str(a[j])+" ", end='')
        print()

    # printing the name of the lone survivor
    printthekiller(a, 0)
    printthekilled(a, 0)
    killed.append(a[0])
    removetheelement(a, 0)
    print(" ")

    # printing the order in which the people were killed
    print("Order of getting killed = ", end='')
    for i in range(len(killed)):
        print(str(killed[i])+" ", end='')

    print(" ")

------------------------------------------------------------------------------------

QUESTION 2 EXPLANATION :-
1. We link the goal matrix to a sorted list of alphabets for ease in inversion count theory.
2. We repeatedly find the number of misplaced characters, and try to minimize the for different possible values of indices for movement of the blank tile.
3. We repeat the process till the number of misplaced tiles is greater than zero.

----------------------------------- CODE FOR THE SECOND QUESTION --------------------------------

# initialing an increasing list for convenience in inversion theory concept
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

# declaring empty lists to store the initial and the user input matrices respectively
given = []
ideal = []

# declaring a check variable to handle the index of zero
zeroch = 'z'

# swapping two elements in an array
def swaparray(array, p, k):
    temp = array[p]
    array[p] = array[k]
    array[k] = temp
    return array

# this functions compares two lists and returns the list with the minimum number of misplaced positions from the actual list
def minimum(indexarray, index, ch, b):
    comp = 100000000
    reservearray = ch.copy()
    a = 0
    i = 0
    while i < len(indexarray): # for comparing with different possible indices
        k = indexarray[i]
        array = ch.copy()
        array = swaparray(array, index, k)
        t = misp(array, b)

        if t < comp: # storing the list with minimum number of misplaced tiles
            comp = t
            a = array[index]
            reservearray = array.copy()
        i += 1

    return a, reservearray, comp # returning the list with minimum number of misplaced tiles, and related values

# linking the goal matrix list with the sorted list
def getchar(k):
    i = 0
    while i < 9:
        if ideal[i] == k:
            return b[i]
        i += 1

# linking the sorted list with the goal matrix list
def getint(k):
    i = 0
    while i < 9:
        if b[i] == k:
            return ideal[i]
        i += 1

# applying the inversion count theory for checking the solvability of a 8-puzzle
def inversioncount(arr):
    inv = 0
    i = 0
    while i < 8:
        j = i+1
        while j < 9:
            if getint(arr[i]) and getint(arr[j]) and ord(arr[i]) > ord(arr[j]):
                inv += 1
            j += 1
        i += 1
    return inv


def solvable(arr):
    inversion = inversioncount(arr)
    return (inversion % 2 == 0)

# this function returns the number of misplaced tiles
def misp(set, b):
    i = 0
    m = 0
    while i < 9:
        if set[i] != b[i]:
            m += 1
        i += 1
    return m

# this function returns the indices of movement tiles, where the blank tile can go
def switch(pos):
    return {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4, 6],
        4: [1, 3, 5, 7],
        5: [2, 4, 8],
        6: [3, 7],
        7: [4, 6, 8],
        8: [5, 7]
    }

# this function prints the matrix in a proper format, the matrix is linked to a sorted list
def printmatrix(matrix):
    i = 0
    while i < 9:
        if i % 3 == 2:
            print(str(getint(matrix[i])))
        else:
            print(str(getint(matrix[i]))+" ", end='')
        i += 1

# prints the original matrix in proper format
def printoriginalmatrix(matrix):
    i = 0
    while i < 9:
        if i % 3 == 2:
            print(str(matrix[i]))
        else:
            print(str(matrix[i])+" ", end='')
        i += 1

alpha=0
# taking input in ROW MAJOR format from user and storing in a list for convenience
i = 0
print("Enter the GOAL MATRIX in ROW MAJOR FORMAT = ")
while i < 9:
    a = int(input(""))
    if a<0 or a>=9:
        alpha=1
    ideal.append(a)
    i += 1
i = 0
print("Enter the INITIAL MATRIX in ROW MAJOR FORMAT = ")
while i < 9:
    a = int(input(""))
    if a<0 or a>=9:
        alpha=1
    given.append(a)
    i += 1

if alpha==1:
    print("Invalid input. Program terminated")
else:
    # printing the original matrices
    print("")
    print("IDEAL MATRIX = ")
    printoriginalmatrix(ideal)
    print("")
    print("GIVEN matrix = ")
    printoriginalmatrix(given)
    print("")

    # linking the initial matrix to the corresponding characters, as in the GOAL MATRIX.
    ch = []
    i = 0
    while i < 9:
        ch.append(getchar(given[i]))
        i += 1

    # declaring variables required for re-use, multiple times
    zeroch = getchar(0)
    t=ch.copy()
    h = misp(ch, b) # checking misplaced positions

    # checking solvability.
    if solvable(ch):
        if h == 0:
            print("Already goal configuration. No need to solve")
        else: # executing the loop for the number of steps
            step = 0
            while h > 0:
                pos = int(ch.index(zeroch))
                step += 1
                arr = switch(pos)
                a,ch,h = minimum(arr[pos], pos, ch, b)
                if step>10:
                    break
        
            ch = t.copy()

            # re-using the same loop, but this time printing the matrices alongside
            if step<=10:
                print("")
                print("Solvable in less than 10 steps!")
                print("")
                h = misp(ch,b)
                step=0
                while h>0:
                    pos = int(ch.index(zeroch))
                    step += 1
                    arr = switch(pos)
                    print("Step "+str(step))
                    a,ch,h = minimum(arr[pos], pos, ch, b)
                    print("Move tile no. "+str(getint(str(a)))+" to blank position")
                    print("After Swapping, the matrix is :-")
                    printmatrix(ch)
                    print("")
                print("The puzzle is solved!")
            else:
                print("Solvable in >10 steps")

    else:
        print("Cannot be solved!")
    print("")

-----------------------------------------------------------------------------------------------------------

