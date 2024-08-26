def print_full_multiplication_table(n):
    # Print the header row
    header = "     " + " ".join(f"{i:4}" for i in range(1, n + 1))
    print(header)
    print("    " + "-" * (n * 4 + 1))
    
    # Print each row of the table
    for i in range(1, n + 1):
        row = [f"{i * j:4}" for j in range(1, n + 1)]
        print(f"{i:2} | " + " ".join(row))

# Example: 10x10 table
print_full_multiplication_table(10)
