from PIL import Image, ImageFont, ImageDraw
import sys

text = "Pizza"
base_path = "images/"

if len(sys.argv) > 1:
    # The first command-line argument is at sys.argv[1]
    text = sys.argv[1]
    print(f"Text provided: {text}")
else:
    print("No text provided. Using default: " + text)

# Configurations
font_size = 36
font_filepath = "fonts/Mechanical-g5Y5.otf"

# Define font color in text format
font_color = "white"  # You can use color names like "red", "green", "blue", etc.
# or
# font_color = "#FF00FF"  # Hexadecimal format for RGB color
# or
# font_color = "#FF00FF80"  # Hexadecimal format for RGBA color (with alpha channel)
# or
# font_color = (67, 33, 116, 155)

# Set Background Color
outer_square_color = (0, 0, 0, 255)  # RGBA format with alpha channel set to 255 (fully opaque)
inner_circle_color = (255,102,125,255) # (0, 0, 0, 0)  # RGBA format with alpha channel set to 0 for transparent

# Set True if circle background is required
circle_background = True

margin = 10  # Adjust the margin as needed

diameter_factor = 2  # Adjust the factor as needed

try:
    # Use a TTF font
    font = ImageFont.FreeTypeFont(font_filepath, size=font_size)

    # Create a temporary image to get text size
    temp_img = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    draw_temp = ImageDraw.Draw(temp_img)
    text_bbox = draw_temp.textbbox((0, 0), text, font=font)

    # Calculate the required diameter to fit the text with a dynamic factor and margin
    diameter = int(max(text_bbox[2], text_bbox[3]) * diameter_factor) + 2 * margin

    # Create a circular background if enabled
    if circle_background:
        background_img = Image.new("RGBA", (diameter, diameter), (0, 0, 0, 0))
        draw = ImageDraw.Draw(background_img)

        # Adjust the coordinates to add margin
        circle_bbox = (margin, margin, diameter - margin, diameter - margin)
        draw.ellipse(circle_bbox, fill=inner_circle_color)

        # Calculate the centered position within the circle
        text_position = (
            (circle_bbox[2] - circle_bbox[0] - text_bbox[2]) // 2 + circle_bbox[0],
            (circle_bbox[3] - circle_bbox[1] - text_bbox[3]) // 2 + circle_bbox[1]
        )
    else:
        background_img = Image.new("RGBA", (text_bbox[2], text_bbox[3]), outer_square_color)

        # Calculate the centered position with margin
        text_position = (
            (background_img.width - text_bbox[2]) // 2 + margin,
            (background_img.height - text_bbox[3]) // 2 + margin
        )

    # Draw the text on a separate image without margin
    text_img = Image.new("RGBA", background_img.size, (0, 0, 0, 0))  # Transparent background
    draw = ImageDraw.Draw(text_img)
    draw.text(text_position, text, font=font, fill=font_color)

    # Combine the background and text images
    final_img = Image.alpha_composite(background_img.convert("RGBA"), text_img)

    final_img.save(base_path + "image.png")
    print("Image saved successfully.")
except Exception as e:
    print(f"An exception occurred: {e}")