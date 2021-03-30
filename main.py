def check_singular(A):
    """
    בודק שהמטריצה אינה יחידה
        :param A: המטריצה
        :return : מחזיר אמת או שקר
    """
    det = round(determinant(A))
    if det != 0:
        print("det=",det," go to X=A^-1*b")
        return True
    else:
        return False

def determinant(A):
    """
    מחשב את הדטרמיננתה של המטריצה המתקבלת
        :param A: המטריצה שאנחנו רוצים לחפש את הדטרמיננתה שלה
        :return: התוצאה של הדטרמיננתה שלנו
    """
    n = len(A)
    AM = copy_matrix(A)

    for fd in range(n):
        if AM[fd][fd] == 0:
            AM[fd][fd] = 1.0e-18  #למנוע חילוק ב0
        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][i]

    return product

def copy_matrix(M):
    """
    מעתיק מטריצה
        :param M: המטריצה שאנחנו רוצים להעתיק
        :return: מחזיר את המטריצה שהעתקנו
    """
    rows = len(M)
    cols = len(M[0])
    MC = zeros_matrix(rows, cols)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC

#הדפסת המטריצה שנשלחת
def print_matrix(Title, M):
    print(Title)
    for row in M:
        print([round(x, 3) + 0 for x in row])

#מטריצת האפסים
def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

# מכפלת מטריצות
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

# מטריצה A עם מספרים ומטריצה I (מטריצת היחידה)
A = [[5,7,3,-2,3],[-4,3,2,8,5],[3,2,-9,9,4],[6,9,5,4,-3],[1,3,-2,4,13]]
I = [[1,0,0,0,0],[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]
#הדפסה של המטריצות ההתחלתיות
print_matrix('A Matrix is:', A)
print()
print_matrix('I Matrix is:', I)

k = len(A)
temp = 0
fdScaler = 1. / A[temp][temp]

for j in range(k):
    A[temp][j] = fdScaler * A[temp][j]
    I[temp][j] = fdScaler * I[temp][j]

k = len(A)
indices = list(range(k))

for i in indices[0:temp] + indices[temp + 1:]:
    crScaler = A[i][temp]
    for j in range(k):
        A[i][j] = A[i][j] - crScaler * A[temp][j]
        I[i][j] = I[i][j] - crScaler * I[temp][j]


indices = list(range(k))
for temp in range(1, k):
    if A[temp][temp] == 0:
        A[temp][temp] = 1.0e-18 #למנוע חילוק ב0
    tempScaler = 1.0 / A[temp][temp]
    for j in range(k):
        A[temp][j] *= tempScaler
        I[temp][j] *= tempScaler

    print_matrix('A Matrix is:', A)
    print()
    print_matrix('I Matrix is:', I)
    print()

    # עובר על כל השורות חוץ משורת הtemp
    for i in indices[:temp] + indices[temp + 1:]:
        crScaler = A[i][temp]
        for j in range(k):
            A[i][j] = A[i][j] - crScaler * A[temp][j]
            I[i][j] = I[i][j] - crScaler * I[temp][j]

        print_matrix('A Matrix is:', A)
        print()
        print_matrix('I Matrix is:', I)
        print()

#הדפסת מכפלה של AI כשA לפני השינויים ו I הוא אחרי כל השינויים כדי לבדות שיוצא לנו מטריצת היחידה
A = [[5, 7, 3, -2, 3], [-4, 3, 2, 8, 5], [3, 2, -9, 9, 4], [6, 9, 5, 4, -3], [1, 3, -2, 4, 13]]
print_matrix('Proof of Inversion (A before any changes and I after all of the changes)', matrix_multiply(A, I))