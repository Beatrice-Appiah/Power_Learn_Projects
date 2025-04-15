``` A python program that reads content from a file, modifies it (in this example, by converting it to uppercase), 
and writes the modified content to a new file. ```

# Defines the input and output filenames
input_filename = 'input_data.txt'
output_filename = 'output_uppercase.txt'

try:
    # Open the input file for reading
    with open(input_filename, 'r') as infile:
        # Read the entire content of the input file
        original_content = infile.read()

    # Modify the content (convert to uppercase)
    modified_content = original_content.upper()

    # Open the new output file for writing ('w' mode creates or overwrites)
    with open(output_filename, 'w') as outfile:
        # Write the modified content to the new file
        outfile.write(modified_content)

    print(f"Successfully read '{input_filename}', converted to uppercase, and saved to '{output_filename}'.")


# Asks for a filename and tries to read it, handling common errors.
filename = input("Please enter the filename:  ")
try:
  with open('inspect.txt', 'r'):
    print("\n -- File Content--")
    print('inspect.txt'.read())
    print("--End of Content --")
except FileNotFoundError: 
  print(f"\nError: File {filename} not found!")
except PermissionError:
  print(f"\nError: Permission denied to read {filename}!! ")
