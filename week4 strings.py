# Name: Victor Mabira
# Date: 20.03.2026
# Description: This program reverses a string using multiple methods and calculates character frequency.

#  1. String Reversal Methods 

def reverse_string_slicing(text):
    # Uses Python slicing
    return text[::-1]

def reverse_string_loop(text):
    # Uses a loop to reverse string manually
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def reverse_string_recursive(text):
    # Bonus3: Using recursion 
    if len(text) == 0:
        return text
    return reverse_string_recursive(text[1:]) + text[0]

#  2. Character Frequency

def character_frequency(text, ignore_case=False, ignore_spaces=False):

    # Convert to lowercase if needed
    if ignore_case:
        text = text.lower()

    # Remove spaces if needed
    if ignore_spaces:
        text = text.replace(" ", "")

    freq = {}

    # Count characters
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq
#Bonus2: Display frequency as barchart
def display_bar_chart(freq):
    print("\nBar Chart Representation:")
    for char, count in freq.items():
        print(f"{char} : {'*' * count}")

#Bonus4: Add file input/output capability
def read_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("File not found.")
        return ""

def write_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

# Main Program
#Bonus4: Add file input capability
print("Choose input method:")
print("1. Enter text manually")
print("2. Read from file")

choice = input("Enter choice (1 or 2): ")

if choice == "2":
    filename = input("Enter filename: ")
    text = read_from_file(filename)
else:
    text = input("Enter a string: ")


# String reversal
print("\nSTRING REVERSAL:")
rev1= print("Method 1 (Slicing):", reverse_string_slicing(text))
rev2 =print("Method 2 (Loop):", reverse_string_loop(text))
rev3=print("Method 3(recursive reversal):", reverse_string_recursive(text))

# Character frequency
# Bonus option 1
ignore_case = input("\nIgnore case? (yes/no): ").lower() == "yes"
ignore_spaces = input("Ignore spaces? (yes/no): ").lower() == "yes"

# Count frequency of each character
freq = character_frequency(text, ignore_case, ignore_spaces)
print("\nCharacter Frequency Table:")
print("-" * 30)
print(f"{'Character':<15}{'Frequency':>10}")
print("-" * 30)

for char in sorted(freq):
    display_char = "SPACE" if char == " " else char
    print(f"{display_char:<15}{freq[char]:>10}")

print("-" * 30)
#Display barchart output
display_bar_chart(freq)

# Save output to file
save = input("\nSave results to file? (yes/no): ").lower()

if save == "yes":
    output = "STRING REVERSAL RESULTS:\n"
    output += f"Slicing: {rev1}\n"
    output += f"Loop: {rev2}\n"
    output += f"Recursive: {rev3}\n\n"

    output += "CHARACTER FREQUENCY:\n"
    for char, count in freq.items():
        output += f"{char} : {count}\n"

    write_to_file("output.txt", output)
    print("Results saved to output.txt")
