from PIL import Image
import os

# save_dir cannot be a child of dir
def resize_images(img_dir, save_dir):
    width = 256
    height = 256
    ext = ".jpg"
    
    for folder, subfolders, files in os.walk(img_dir):
        i = 0
        for file in files:
            orig_path = img_dir + '/' + file
            try:
                orig_img = Image.open(orig_path)
            except FileNotFoundError:
                continue

            resized_img = orig_img.resize((width, height), Image.ANTIALIAS)
            resize_path = save_dir + '/' + str(i) + ext
            resized_img.save(resize_path)
            i+=1


# resize_images('pics/gloomy', 'resized/gloomy')
# resize_images('pics/sunny', 'resized/sunny')