QUESTION 1 :-

1. WE USE THE CONCEPT OF DYNAMIC PROGRAMMING TO CALCULATE THE MINIMUM NUMBER OF DENOMINATIONS.
2. THEN WE USE THE CONCEPT OF RECURSION AND COMPARE IT WITH THE MINIMUM VALUE TO RETURN THE LIST HAVING THE MOST OPTIMAL SOLUTION.
3. THEN WE OPEN THE TERMINAL, GO TO THE FOLDER USING cd COMMAND, AND TYPE :-
		
		python3 210101110_question1.py
	
   and then enter the input the data.
   
4. REST OF THE DETAILS HAVE BEEN EXPLAINED IN THE CODE BELOW :-

---------------------------------------------------------------- CODE FOR QUESTION 1 --------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

QUESTION 2 :-

1. WE INSTALL AND INCLUDE RELEVANT PACKAGES AND WRITE THE CODE SYMBOL WISE.
2. REST OF THE DETAILS HAVE BEEN EXPLAINED IN THE CODE, VIA COMMENTS.
3. WE RUN THE CODE ON ONLINE IDE overleaf.com aur THE SOFTWARE texworks OR texmaker.

---------------------------------------------------------------------- CODE FOR QUESTION 2 PART i ----------------------------------------------------------------------------------
\documentclass[12pt]{article} % starting the document
\usepackage{amsmath} % installing all the relevant packages
\usepackage[arrowdel]{physics}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{mathtools}
\usepackage{ upgreek }
\usepackage[version=4]{mhchem}
\usepackage{xfrac}
\usepackage{xcolor}
\usepackage[spanish]{babel}
\usepackage{breqn}
\title{Hello World!} % including the title
\author{Vatsal Jain} % author name
\date{January 1, 1831}
\begin{document}
\maketitle % used to put the title into the pdf
\section{Getting Started}
\textbf{Hello World!} Today I am learning \LaTeX. \LaTeX is a great program for writing math. I can write in line math such as $a^2+b^2 = c^2$. I can also give equations their own space:\thispagestyle{empty} % used to remove page number
\begin{align}
\gamma^2 + \theta^2 &= \omega^2 % \ is used to write the relevant symbols.
\end{align} % aligning the formula to the center
``Maxwell's Equations'' are made for James Clark Maxwell and are as follow:
\begin{align}
\vec{\nabla}.\vec{E} &= \frac{\rho}{\varepsilon_0} & & \text{Gauss's Law} \\ % all the symbols have been written via relevant codes
\vec{\nabla}.\vec{B} &= 0 & & \text{Gauss's Law for Magnetism}\\
\vec{\nabla} \times \vec{E} &= -\frac{\partial \vec{B}}{\partial t} & & \text{Faraday's Law of Induction} \\
\vec{\nabla} \times \vec{B} &= \mu_0\left(\varepsilon_0\frac{\partial \vec{E}}{\partial t}+\vec{J} \right) & & \text{Ampere's Circuital Law} 
\end{align}
Equations \textcolor{blue}{2}, \textcolor{blue}{3}, \textcolor{blue}{4} and \textcolor{blue}{5} are some of the most important in physics
\section{What about Matrix Equations?}
$$\begin{pmatrix} % pmatrix stands for matrix via parenthesis
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{n1} & a_{n2} & \cdots & a_{nn} 
\end{pmatrix}\begin{bmatrix} % b matrix is used for matrix with bold brackets
v_1 \\
v_2 \\
\vdots \\
v_n
\end{bmatrix}=\begin{matrix}
w_1 \\
w_2 \\
\vdots \\
w_n
\end{matrix} $$
\pagebreak % used for changing the page
\end{document}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---------------------------------------------------------   CODE FOR QUESTION 2 PART ii    -----------------------------------------------------------------------

\documentclass[12pt]{article} % starting the document
\usepackage{amsfonts}% installing all the relevant packages
\usepackage{amssymb}
\usepackage{ upgreek }
\usepackage[version=4]{mhchem}
\usepackage{breqn}
\usepackage[margin=1in]{geometry}
\begin{document} % starting of the document
\thispagestyle{empty} % removing the page number
$$ \iiint \limits_{V}f(x,y,z)\;dV=F $$
$$\frac{dx}{dy} = x'= \lim_{h \to 0}\frac{f(x+h)-f(x)}{h} $$
\begin{equation*} % writing the mod function using begin function
\lvert x \lvert  = 
    \begin{cases}
        -x, & \text{if } x<0 \\
        x, & \text{if } x\geq 0
    \end{cases}
\end{equation*}
$$F(x) = A_0+\sum_{n=1}^{N}\left[A_ncos\left(\frac{2\pi nx}{P}\right)+B_nsin\left(\frac{2\pi nx}{P}\right)\right]$$
$$\sum_{n}\frac{1}{n^s}=\prod_{p}\frac{1}{1-\frac{1}{p^s}}$$
$$m\ddot x + c\dot x + kx = F_0sin\left(2\pi ft\right)$$
\begin{align*}
f(x) &= x^2+3x+5x^2+8+6x \\
&= 6x^2+9x+8 \\
&=x\left(6x+9\right)+8
\end{align*}
$$X_0 = \frac{F_0}{k}\frac{1}{\sqrt{\left(1-r^2\right)^2+\left(2\zeta r\right)^2}}$$\\
$$G_{\mu v} \equiv R_{\mu v} - \frac{1}{2}Rg_{\mu v} = \frac{8\pi G}{c^4}T_{\mu v}$$\
\begin{align*} % writing chemical equations via text mode
\text{6CO}_2 + \text{6H}_2\text{O} \rightarrow \text{C}_6\text{H}_{12}\text{O}_6+\text{6O}_2
\end{align*}
$$\text{SO}_4^{2-} + \text{Ba}^{2+} \rightarrow  \text{BaSO}_4$$
$$
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots  & \vdots  & \ddots & \vdots  \\
a_{n1} & a_{n2} & \cdots & a_{nn} 
\end{pmatrix}\begin{pmatrix}
v_1 \\
v_2 \\
\vdots \\
v_n
\end{pmatrix}=\begin{pmatrix}
w_1 \\
w_2 \\
\vdots \\
w_n
\end{pmatrix}$$
$$\frac{\partial \textbf{u}}{\partial t} + \left(\textbf{u}.\nabla\right)\textbf{u} -\nu\nabla^2\left(\textbf{u}\right) = -\nabla \textbf{h} $$
$$\alpha A \beta B\gamma \Upgamma \delta \Updelta \pi \Pi \omega \Omega$$ % writing relevant code for the symbols
\end{document}

---------------------------------------------------------------------------------- END OF QUESTION 2 -----------------------------------------------------------------------------
