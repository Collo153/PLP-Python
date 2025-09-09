# File Read & Write with Error Handling

# Ask user for the filename
filename = input("Enter the filename to read: ")

try:
    # Try opening the file
    with open(filename, "r") as infile:
        content = infile.read()
        print("\nOriginal Content:")
        print(content)

    # Modify content (example: convert to uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"\nModified content has been written to '{new_filename}' ✅")

except FileNotFoundError:
    print("Error: The file does not exist. ❌")
except PermissionError:
    print("Error: You don’t have permission to read this file. 🚫")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
