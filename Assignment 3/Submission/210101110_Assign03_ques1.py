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
