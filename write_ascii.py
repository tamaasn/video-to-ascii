from PIL import Image
import os

ascii_chars = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
ascii_chars = [" " , "#" , "$" , "%" , "'" , "." , "*" , ";" , ":" , "," , "," , "+" , "0"]

def resize(image):
    return image.resize((120 , 40))

def grayscale(image):
    return image.convert("L")

def generate_ascii(image):
    pixels = image.getdata()
    ascii_data=""
    for pixel in pixels:
        ascii_data += ascii_chars[pixel//20]
    return ascii_data

def write(frame_dir , ascii_dir):
    frame_list = os.listdir(frame_dir)
    count=0
    for i in range(0 , len(frame_list)):
        frame_file = frame_dir+"/frame{}.jpg".format(i)
        target_path = ascii_dir+"/frame{}.txt".format(i)
        image = Image.open(frame_file)
        image = resize(image)
        gray_image = grayscale(image)
        ascii_data = generate_ascii(gray_image)
        width , height = gray_image.size
        img = ""
        for j in range(0 , len(ascii_data) , width):
            img += ascii_data[j:j+width]+"\n"


        with open(target_path , "w") as f:
            f.write(img)
            f.close()
        count += 1
        print("Generating ascii {}/ ".format(frame_file) +target_path)




