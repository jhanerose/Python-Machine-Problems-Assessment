def char_frequency():
    # Prompt the user for input
    input_string = input("Enter a string: ")
    
    # Convert the input string to lowercase to ignore case
    input_string = input_string.lower()
    
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Iterate over each character in the string
    for char in input_string:
        # Update the frequency count in the dictionary
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    # Print the resulting frequency dictionary
    print("Character Frequency:", frequency_dict)

# Run the function
char_frequency()
