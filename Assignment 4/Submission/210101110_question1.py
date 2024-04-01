# creating test list
arr = []
for i in range(1000):
    arr.append(0)

#creating reserved list for storing the most optimal solution
a = []
for i in range(1000):
    a.append(0)

# this function returns the minimum number of denominations using dynamic programming
def minCoins(coins,m,amt):
    table=[]
    table.append(0)
    i=1
    while i<=amt:
        table.append(1000000000)
        i+=1
    i=1
    while i<=amt:
        j=0
        while j<m:
            if coins[j]<=i:
                subres = table[i-coins[j]]
                if subres!=1000000000 and subres+1<table[i]:
                    table[i]=subres+1
            j+=1
        i+=1
    if table[amt]==1000000000:
        return -1
    return table[amt]

# this function is used to store the compositional list of least size into a reserved list
def compocopy(arr,size,min):
    if size==min:
        for i in range(size):
            a[i]=arr[i]

# this function uses recursion to test all possible combinations of coins to yield a specific value
def printCompositions(amt,i,min,coins,m):
    if amt==0:
        compocopy(arr,i,min)
    elif amt>0:
        for k in range(m):
            arr[i] = coins[k]
            printCompositions(amt-coins[k], i+1, min, coins, m)

#taking input from the user
amt = int(input("Enter the amount = "))
coins = [1,5,10,20,25,50] # the given denominations


# reducing complexity of the problem by reducing the original amount, using the fact that any amount greater than 50 requires 50 as a coin.
k = int(amt/50)
amt%=50

# storing the min coins needed to produce the required amount
min = minCoins(coins,len(coins),amt)
print("\nThe minimum number of denominations is = "+str(k+min))

# evaluating the list which stores the most optimal solution to the given problem
printCompositions(amt,0,min,coins,len(coins))

print("\nThe composition is :- \n")

# storing the number of coins into respective variables
fif = k
twen = twif = ten=five=one=0
for i in range(min):
    if a[i]==25:
        twif+=1
    elif a[i]==20:
        twen+=1
    elif a[i]==10:
        ten+=1
    elif a[i]==5:
        five+=1
    elif a[i]==1:
        one+=1

# printing the composition
if fif!=0:
    print("Number of 50 rupee coins = "+str(fif))
if twif!=0:
    print("Number of 25 rupee coins = "+str(twif))
if twen!=0:
    print("Number of 20 rupee coins = "+str(twen))
if ten!=0:
    print("Number of 10 rupee coins = "+str(ten))
if five!=0:
    print("Number of 5 rupee coins = "+str(five))
if one!=0:
    print("Number of 1 rupee coins = "+str(one))
print()
