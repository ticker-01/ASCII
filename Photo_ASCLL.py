import cv2

string = " `.,-':<>;+!*/?%&98#"
coef = 255 / (len(string) - 1)
image = cv2.imread('Img/img_1.jpg')



new_width = 480
new_height = 270

resized_image = cv2.resize(image, (new_width, new_height))

height, width, channels = resized_image.shape
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#gray_image = cv2.resize(gray_image, (30, 12))
for y in range(0, height - 1, 8):
    s = ""
    for x in range(0, width - 1, 4):
        s += string[len(string) - int(gray_image[y, x] / coef) - 1]
    if len(s) != 0:
        print(s)