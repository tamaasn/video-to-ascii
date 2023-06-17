import cv2

def save(path , filename):
    vid = cv2.VideoCapture(filename)
    count=0
    success,image=vid.read()

    while success:
        cv2.imwrite(path+"frame{}.jpg".format(count) , image)
        success,image=vid.read()
        print("Saving frame {}".format(count))
        count += 1
