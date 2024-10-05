import os
from PIL import Image
import extcolors

def get_colors(img_path):
    img = Image.open(img_path).convert("RGBA")
    return extcolors.extract_from_image(img, tolerance=33, limit=10)

def create_image_entry(colors, file_name):
    total_pixels = colors[1]
    image_dict = {'file_name': file_name}
    image_colors = [
        {'colorCode': str(index), 'percent': round(color / total_pixels * 100)}
        for index, color in colors[0]
        if round(color / total_pixels * 100) >= 1
    ]
    image_dict['img_colors'] = image_colors
    return image_dict

def process_images(directory):
    collection = []
    
    for dirpath, _, filenames in os.walk(directory):
        for f in filenames:
            img_path = os.path.abspath(os.path.join(dirpath, f))
            filename = os.path.basename(f)
            colors = get_colors(img_path)
            file_dict = create_image_entry(colors, filename)
            collection.append(file_dict)
    
    return collection

# Example usage
directory = "/Users/brandonkim/Desktop/Projects/Byul/images"
collection = process_images(directory)

print(collection)

