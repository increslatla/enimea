# number of rows
rows = 5

# outer loop for each row
for i in range(0, rows):
    # inner loop for each column
    for j in range(0, i + 1):
        # print asterisk
        print("*", end=' ')
    # move to the next line after printing each row
    print("\r")
