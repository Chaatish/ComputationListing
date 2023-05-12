# Ask user to enter the name of the input text file
input_filename = input("Enter the name of the input text file: ")

# Ask user to enter the name of the output text file
output_filename = input("Enter the name of the output text file: ")

# Read items from the input text file and strip whitespace
with open(input_filename, "r") as f:
    items = [line.strip() for line in f]

# Generate list of comparisons
comparisons = [(items[i], items[j]) for i in range(len(items)) for j in range(i+1, len(items))]

# Save list of comparisons to output text file
with open(output_filename, "w") as f:
    for pair in comparisons:
        f.write(pair[0] + ", " + pair[1] + "\n")

print("Comparison list saved to", output_filename)
