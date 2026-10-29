def strassen(A, B):
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    e, f, g, h = B[0][0], B[0][1], B[1][0], B[1][1]

    p = (a+d)*(e+h)
    q = (c+d)*e
    r = a*(f-h)
    s = d*(g-e)
    t = (a+b)*h
    u = (c-a)*(e+f)
    v = (b-d)*(g+h)

    return [[p+s-t+v, r+t],
            [q+s, p+r-q+u]]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Product Matrix:")
for row in strassen(A, B):
    print(row)
