
import os
import re
from collections import defaultdict

def format_card_list(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    card_quantities = defaultdict(int)
    first_card_name = None

    for line in lines:
        # Match the quantity and card name in each line
        card_match = re.match(r'^(\d+)\s+(.+?)(?:\s*[\(\[0-9]|$)', line)
        if card_match:
            quantity = int(card_match.group(1))
            card_name = card_match.group(2).strip(" ,[]")
            card_quantities[card_name] += quantity
            if first_card_name is None:  # Set only if it hasn't been set yet
                first_card_name = card_name

    # Create a list of formatted cards with quantities
    formatted_cards = [f"{quantity} {card_name}" for card_name, quantity in card_quantities.items()]

    # Create the output file name based on the name of the first card
    output_file_name = f"{first_card_name.replace(' ', '_')}_formatted.txt"

    # Check if the file already exists, and add a suffix to make it unique
    suffix = 1
    while os.path.exists(output_file_name):
        output_file_name = f"{first_card_name.replace(' ', '_')}_{suffix}_formatted.txt"
        suffix += 1

    # Write the formatted cards to the output file
    with open(output_file_name, 'w') as f:
        f.write('\n'.join(formatted_cards))

    total_cards = len(card_quantities)

    # Create a message indicating the total number of unique cards
    message = f'\n\nTotal: {total_cards} unique cards in the overall list'

    # Append the message to the output file
    with open(output_file_name, 'a') as f:
        f.write(message)

# Example usage:
input_file_path = 'input.txt'
format_card_list(input_file_path)
