# Prompt the user for a file name
filename = input("Enter the file name: ")

try:
    # Open the file
    with open(filename, 'r') as file:
        count = 0
        # Read the file line by line
        for line in file:
            line = line.strip()  
            print(line)  
            # Check if the line starts with "From "
            if line.startswith("From "):
                count += 1
        # Print the total count of lines starting with "From "
        print("\nTotal count of lines starting with 'From':", count)

# Handle the case where the file does not exist
except FileNotFoundError:
    print("File not found:", filename)