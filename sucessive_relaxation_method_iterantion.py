import numpy as np
#Succesive relaxation method iteration
#this program is Write By Endurance ogun and is part of the Sfip program
#CopyRight:: can be use for any of your project but one should not delete this comment or claim ownship of the program.
#sign by the Sfip.inc

def SOR(A,B):
    w=float(input("the relaxation factor::"))
    t = float(input("the toll::"))
    input_x=str(input("Do you want to input for the initial_value of x (y or n)::"))
    if input_x=="y":
        x=get_matrixX(len(np.ones_like(B)),float)
    else:
        x = np.zeros_like(B)

    L = np.tril(A)
    U = A - L
    L_inv = np.linalg.inv(L)
    Dig=np.dot(w,L_inv)

    N = 1
    M = 0
    j = 0

    while True:
        for i in range(N):
            j=j+1 #The number of Iteration
            print("Iteration::" + str(j))
            Gx = np.dot((1-w), x)
            Ux = np.dot(U, x)
            B_UX=np.dot(Dig,(B-Ux))
            x_new = Gx + B_UX
            M = np.allclose(x, x_new, t)
            x = x_new
            print(x)
        if M:
            break
        N = N + 1

def get_matrixA(m_len,variable_type=float):
    A=[]
    for i in range(1,m_len+1):
        for j in range(1,m_len+1):
            m_col_row= float(input("enter value for \n a"+str(i)+str(j)+"::"))
            A.append(m_col_row)

    A=np.array(A).reshape(m_len,m_len)

    print(A)
    return A

def get_matrixB(m_len, variable_type=float):
    B = []
    for h in range(1, m_len + 1):
        m_col = float((input("enter value for  \n b" + str(h) + "::")))
        B.append(m_col)

    B = np.array(B).reshape(m_len, 1)
    print(B)
    return B
def get_matrixX(m_len, variable_type=float):
    B = []
    for h in range(1, m_len + 1):
        m_col = float((input("enter value for  \n X" + str(h) + "::")))
        B.append(m_col)

    B = np.array(B).reshape(m_len, 1)
    print(B)
    return B

def get_solution():
    N=int(input("NxN dimension of Matrix::"))
    A=get_matrixA(N)
    B=get_matrixB(N)
    SOR(A,B)


get_solution()