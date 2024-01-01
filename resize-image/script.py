from PIL import Image
import os

def resize_image(source_path, target_path):
    # Open the source image
    source_image = Image.open(source_path)

    # Get the size of the source image
    source_size = source_image.size

    # Open the target image
    target_image = Image.open(target_path)

    # Resize the target image to the size of the source image
    resized_target_image = target_image.resize(source_size)

    # Get the file name with extension
    file_name = os.path.basename(target_path)
    # Get the file extension
    file_extension = os.path.splitext(target_path)[1]
    
    # print("File Name:", file_name)
    # print("File Extension:", file_extension)

    #Set new file name
    new_file_path = target_path.replace(file_extension, "_updated" + file_extension)
    # print("File Name:", new_file_path)

    # Save the resized target image
    resized_target_image.save(new_file_path)

# Example usage
resize_image("images/linkedin-logo.png", "images/github-logo.png")