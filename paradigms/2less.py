#функциональный
def multiplication_table(n):
    table = [(i, j, i*j) for i in range(1, n+1) for j in range(1, 10)]
    for i, j, result in table:
        print(f"{i} * {j} = {result}")

n = 5
multiplication_table(n)


#императивный
def multiplication_table(n):
    for i in range(1, n+1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i*j}")


k = 5
multiplication_table(k)
