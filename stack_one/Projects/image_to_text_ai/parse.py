import re

def parse_text(text):
    # Initialize variables to store element information
    elements = {}
    current_element = None

    # Iterate through lines in text
    for line in text.split('\n'):
        # Check if line starts with "- " (indicating an attribute)
        if line.startswith('- '):
            # Extract attribute and value
            match = re.match(r'- (.*): (.*)', line)
            attribute = match.group(1)
            value = match.group(2)
            # Add attribute and value to current element
            elements[current_element][attribute] = value

        # Check if line ends with ":" (indicating a new element)
        elif line.endswith(':'):
            # Extract element name
            element_name = line[:-1]
            # Add new element to elements dictionary
            elements[element_name] = {}
            # Set current element to new element
            current_element = element_name

    return elements
