s= "hii sulekkha"
print(s)


def simple_multiplication_table(n):
    # Print the header
    print("Multiplication Table:")
    for i in range(1, n + 1):
        row = [i * j for j in range(1, n + 1)]
        print(" ".join(f"{num:2}" for num in row))

# Example: 2x2 table
simple_multiplication_table(2)
