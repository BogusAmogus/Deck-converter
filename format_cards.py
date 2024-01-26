
import os
import re
from collections import defaultdict

def format_card_list(input_file_path):
    # Open the input file and read all lines
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Initialize a dictionary to store the counts of each card
    counts_per_card = defaultdict(int)
    # Initialize a variable to store the name of the first card
    first_card_name = None

    # Loop through each line in the file
    for line in lines:
        # Use regex to match the quantity and card name in each line
        card_match = re.match(r'^(\d+)\s+(.+?)(?:\s*[\(\[0-9]|$)', line)
        # If a match is found
        if card_match:
            # Extract the quantity and card name from the match
            quantity = int(card_match.group(1))
            card_name = card_match.group(2).strip(" ,[]")
            # Add the quantity to the count for this card
            counts_per_card[card_name] += quantity
            # If this is the first card, store its name
            if first_card_name is None:
                first_card_name = card_name

    # Create a list of formatted strings, each containing the count and name of a card
    formatted_cards = [f"{count} {card_name}" for card_name, count in counts_per_card.items()]

    # Create the output file name based on the name of the first card
    output_file_name = f"{first_card_name.replace(' ', '_')}_formatted.txt"

    # If the output file already exists, add a suffix to make the file name unique
    suffix = 1
    while os.path.exists(output_file_name):
        output_file_name = f"{first_card_name.replace(' ', '_')}_{suffix}_formatted.txt"
        suffix += 1

    # Write the formatted card strings to the output file
    with open(output_file_name, 'w') as file:
        file.write('\n'.join(formatted_cards))

    # Count the total number of unique cards
    total_unique_cards = len(counts_per_card)

    # Create a message indicating the total number of unique cards
    message = f'\n\nTotal: {total_unique_cards} unique cards in the overall list'

    # Append the message to the output file
    with open(output_file_name, 'a') as file:
        file.write(message)

# Example usage:
input_file_path = 'input.txt'
format_card_list(input_file_path)
