# Iterate over each row (1 to 5)
for i in range(1, 6):
    # Iterate over each column (1 to 5)
    for j in range(1, 6):
        # Calculate the product
        product = i * j
        # Print the product with formatting
        print(f"{product:4}", end="")
    # Move to the next line after each row
    print()
