def matrix_operations(matrix,row_sum,column_sum):
    total_sum=0
    for i in matrix:
        r_sum = 0
        r_sum += sum(i)
        total_sum += r_sum
        row_sum.append(r_sum)

    for j in range(len(matrix[0])):
        c_sum = 0
        for i in matrix:
            c_sum += i[j]
        column_sum.append(c_sum)

    return total_sum



