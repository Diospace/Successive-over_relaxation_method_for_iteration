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
        print("initail values are \n"+str(x))

    M = 0
    j = 0
    while True:
        x_old= x.copy()
        j = j + 1  # The number of Iteration
        print("Iteration::" + str(j))
        for i in range(A.shape[0]):
            x[i] = (x[i]*(1-w))+((w/A[i,i])*(B[i]-np.dot(A[i,:i],x[:i])-np.dot(A[i,(i+1):],x_old[(i+1):])))
            M = np.allclose(x, x_old, t)
        print(x)


        if M:
            break

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