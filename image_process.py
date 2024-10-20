from PIL import Image
import os

# Open the image
input_path = './static/cards.png'
img = Image.open(input_path)

# Create output directory if it doesn't exist
output_dir = 'split_cards'
os.makedirs(output_dir, exist_ok=True)

# Get the dimensions of the original image
width, height = img.size

# Calculate the dimensions of each card
card_width = width // 7
card_height = height // 2

# Split the image into 14 cards
for row in range(2):
    for col in range(7):
        left = col * card_width
        upper = row * card_height
        right = left + card_width
        lower = upper + card_height

        # Crop the card
        card = img.crop((left, upper, right, lower))

        # Save the card
        card_filename = f'card_{row+1}_{col+1}.png'
        card_path = os.path.join(output_dir, card_filename)
        card.save(card_path)

print(f"14 cards have been saved in the '{output_dir}' folder.")
