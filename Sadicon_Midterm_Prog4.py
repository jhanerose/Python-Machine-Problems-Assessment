import sys
import os

filename = input("Enter file name: ")

try:
    file = open(filename)
except FileNotFoundError:
    print("File not found:", filename)
    sys.exit(1)

total = 0
for line in file:
    if line.startswith("X-Value:"):
        # Extract the number from the line, starting from the 8th character onward
        try:
            number = int(line[8:].strip())  # Convert to int after trimming whitespace
            total += number
        except ValueError:
            print("Error: Could not convert to an integer on line:", line)

print("Total:", total)
file.close()
