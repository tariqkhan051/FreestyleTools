from PIL import Image
from os import listdir
from os.path import isfile, join, splitext
from pathlib import Path

base_path = "images"

files = [f for f in listdir(base_path) if isfile(join(base_path, f))]

if files != None and len(files) > 0:
    print("Files found :", len(files))
else:
    print("No files found.")
    exit()

for file in files:
    file_extension = splitext(file)[1]
    
    #Check if the image is PNG
    if file_extension.upper() == ".PNG":
        
        print("File extension is validated.")
        
        try:
            #Get the file name
            file_name = Path(file).stem

            img = Image.open(base_path + "/" + file)
        
            #specify sizes
            icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
        
            if (icon_sizes is not None and icon_sizes != []):
                img.save(base_path + "/" + file_name + '.ico', sizes=icon_sizes)
            else:
                img.save(base_path + "/" + file_name + '.ico')
        except:
            print("An exception occurred.")