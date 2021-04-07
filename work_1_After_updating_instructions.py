import sys
###  חלק של אלכס
def crate_I_matrix(matrix):
    n=len(matrix)
    matrix_I = [[0 for i in range(n)] for y in range(n)]

    # מטריצת אפסים
    for i in range(n):
        for j in range(n):
          matrix_I[i][j]=0
    # הכנסת אלכסון 1
    for i in range(n):
        matrix_I[i][i]=1

    return matrix_I
###כפל מטריצות#
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A
def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print('Number of A columns must equal to the number of B rows.')
    C = zeros_matrix(rowsA, colsB)
    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C
###מציאת n U#
def get_U_matrix(matrix,matrix_i):
    U_matrix=matrix
    alahson=1
    flag=True
    n=len(matrix)
    matrix_i_temp=crate_I_matrix(matrix)
    temp=0
    pivot = matrix[temp][temp]
    for col in range(0,n-1):
        for row in range(col+1,n):
            if(matrix[row][col]!=0):
                matrix_i_temp[row][col]=-((U_matrix[row][col])/pivot)

                if(flag==True):
                  U_matrix=matrix_multiply(matrix_i_temp,matrix)
                  matrix_i_temp[row][col] = 0
                  flag=False
                else:
                    U_matrix = matrix_multiply(matrix_i_temp, U_matrix)
                    matrix_i_temp[row][col] = 0

        temp+=1
        pivot = U_matrix[temp][temp]
    return U_matrix
###מציאת מצטריצה U#
def get_L_matrix(matrix,matrix_i):
    U_matrix=matrix
    L_matrix=crate_I_matrix(matrix)
    alahson=1
    flag=True
    n=len(matrix)
    matrix_i_temp=crate_I_matrix(matrix)
    temp=0
    pivot = matrix[temp][temp]
    for col in range(0,n-1):
        for row in range(col+1,n):
            if(matrix[row][col]!=0):
                matrix_i_temp[row][col]=-((U_matrix[row][col])/pivot)
                L_matrix[row][col]=((U_matrix[row][col])/pivot)

                if(flag==True):
                  U_matrix=matrix_multiply(matrix_i_temp,matrix)
                  matrix_i_temp[row][col] = 0
                  flag=False
                else:
                    U_matrix = matrix_multiply(matrix_i_temp, U_matrix)
                    matrix_i_temp[row][col] = 0

        temp+=1
        pivot = U_matrix[temp][temp]
    return L_matrix
def multiply_matrix_by_vector(matrix, v):
    result = []
    for i in range(len(matrix[0])): #this loops through columns of the matrix
        total = 0
        for j in range(len(v)): #this loops through vector coordinates & rows of matrix
            total += v[j] * matrix[j][i]
        result.append(total)
    return result
###החלפת שורות במטריצה במידה ויש אפסים באלכסון#
def chnage_lanes_function(matrix):
    alahson=0
    while alahson<len(matrix):
        pivot = matrix[alahson][alahson]
        for i in range(alahson,len(matrix)):
            if(matrix[alahson][alahson]!=0):
                pass
            else:
                max= matrix[i][alahson]
                if(max > pivot):
                    pivot=max
                    max_value_new = matrix[i][alahson]
                    max_index=i
        if(matrix[alahson][alahson] ==0):
            matrix[max_index],matrix[alahson]=matrix[alahson],matrix[max_index]
        alahson += 1

    return matrix
###בדיקה האם יש מטריצה הופכית#
def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]
def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a
def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret
###  חלק א-פתרןן בדרך של גאוס #
def gaussy(A, b, n):
    l = [0 for x in range(n)]
    s = [0.0 for x in range(n)]
    for i in range(n):
        l[i] = i
        smax = 0.0
        for j in range(n):
            if abs(A[i][j]) > smax:
                smax = abs(A[i][j])
        s[i] = smax

    for i in range(n - 1):
        rmax = 0.0
        for j in range(i, n):
            ratio = abs(A[l[j]][i]) / s[l[j]]
            if ratio > rmax:
                rmax = ratio
                rindex = j
        temp = l[i]
        l[i] = l[rindex]
        l[rindex] = temp
        for j in range(i + 1, n):
            multiplier = A[l[j]][i] / A[l[i]][i]
            for k in range(i, n):
                A[l[j]][k] = A[l[j]][k] - multiplier * A[l[i]][k]
            b[l[j]] = b[l[j]] - multiplier * b[l[i]]

    x = [0.0 for y in range(n)]
    x[n - 1] = b[l[n - 1]] / A[l[n - 1]][n - 1]
    for j in range(n - 2, -1, -1):
        summ = 0.0
        for k in range(j + 1, n):
            summ = summ + A[l[j]][k] * x[k]
        x[j] = (b[l[j]] - summ) / A[l[j]][j]

    print ("The solution vector is [", end="")
    for i in range(n):
        if i != (n - 1):
            print(x[i], ",", end="")
        else:
            print(x[i], "].")
### סיום חלק א #


# main #
A=[[99,2,3],[4,5,6],[7,8,99]]
b=[12,30,40,3]
matrix_i = crate_I_matrix(A)


# לבדוק שאין אפסים על האלכסון!!!!
flag_zero=False
for i in range(0,len(A)):
    if(A[i][i]==0):
        flag_zero=True

## בדיקה האם יש אפסים על האלכסון
if(not(flag_zero)):  # אין אפסים על האלכסון
  pass
else: ## יש אפסים במטריצה על האלכסון
    # change Lanes
    print('There are zeros on the diagonal')
    print(A)
    A=chnage_lanes_function(A)
    print('After revised matrix:')
    print(A)


if(len(A)<4):
    try:
        inv_A = inverse(A)
        n = len(A)
        gaussy(A,b,n)
    except ValueError:
        print('no inverse matrix found')

else:
    lower_matrix=0
    upper_matrix=0
    try:
      upper_matrix = get_U_matrix(A, matrix_i)  # Upper_matrix
    except ZeroDivisionError:
        print('float division by zero')

    try:
      lower_matrix = get_L_matrix(A, matrix_i)  # Lower_matrix
    except ZeroDivisionError:
        print('float division by zero')
    if (upper_matrix):
        print('upper_matrix=', upper_matrix)
    if (lower_matrix):
        print('lower_matrix=', lower_matrix)
    if ( lower_matrix and upper_matrix):
        print('L*U matrix =', matrix_multiply(lower_matrix, upper_matrix))
    else:
        print('no solution')


