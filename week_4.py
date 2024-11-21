# Program to read a file, modify its content, and write to a new file

# Ask user for the filename to read
fileName = input("Please enter the filename to read: ")

try:
    # Open the file to read
    with open(fileName, 'r') as file:
        content = file.read()  
    
    # Modify the content by converting it to uppercase
    modified_content = content.upper()
    
    # Write the modified content to a new file
    modified_filename = 'modified_' + fileName
    with open(modified_filename, 'w') as new_file:
        new_file.write(modified_content)
    
    print(f"Modified content written to {modified_filename}")
    
except FileNotFoundError:
    print(f"Error: The file '{fileName}' does not exist.")
except IOError:
    print(f"Error: Unable to read the file '{fileName}'.")
