#!/usr/bin/python3

"""Module: print text with 2 new lines when characters are recognized"""


def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty result string
    result = ""

    # Initialize a flag to track whether we are in a new line
    new_line = True

    # Iterate through each character in the input text
    for char in text:
        # Check if the character is one of the specified punctuation marks
        if char in ".?:":
            # Add the punctuation mark to the result string with 2 new lines
            result += char + "\n\n"
            # Set the flag to indicate a new line
            new_line = True
        elif char == " ":
            # If the character is a space, skip it at the beginning of a line
            if new_line:
                continue
            else:
                # If not at the beginning of a line, add the space to the result
                result += char
        else:
            # Add the character to the result string
            result += char
            # Clear the new line flag
            new_line = False

    # Print the formatted text
    print(result)

