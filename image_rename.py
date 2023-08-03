#. . . . . . . . . . . . . . . ╰──╮ NUMERICAL IMAGE RENAMER

# . . . . . ╰──╮ INSTRUCTIONS:
# . . . . . ╰──╮ to run this program, provide the path to your directory with the directory_path variable
# . . . . . ╰──╮ then, open a terminal and run the following command:
# . . . . . ╰──╮ python image_rename.py


# . . . . . ╰──╮ IMPORTS.
# . . . . . ╰──╮ os module lets us interact with our computer's file system.
import os

#. . . . . . . . . . . . . . . ╰──╮ PROGRAM.
# . . . . . ╰──╮ provide the directory path where your image files are located.
directory_path = "path/to/your/images"

# . . . . . ╰──╮ list the image files found (file extensions .jpg, .jpeg, .png, .gif).
# . . . . . ╰──╮ lowercase all file extensions first to catch '.JPG', etc on string matching
image_files = [f for f in os.listdir(directory_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# . . . . . ╰──╮ sort the list of image files for most cohesive renaming.
image_files.sort()

# . . . . . ╰──╮ iterate over, and numerically rename, the image files.
for index, old_filename in enumerate(image_files, start=1):
    file_extension = os.path.splitext(old_filename)[-1]
    new_filename = f"{index}{file_extension}"
    old_path = os.path.join(directory_path, old_filename)
    new_path = os.path.join(directory_path, new_filename)
    
    # . . . . . ╰──╮ rename the image file.
    os.rename(old_path, new_path)
    print(f"Renamed {old_filename} to {new_filename}")
    
# . . . . . ╰──╮ inform the user that the renaming is complete.    
print("Renaming complete.")

