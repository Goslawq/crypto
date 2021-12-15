from PIL import Image
import numpy as np
from random import random, randrange


def encode_message(image):
    share1 = np.zeros((200, 200)) + 255
    share2 = np.zeros((200, 200)) + 255
    for x in range(100):
        for y in range(100):
            if image.getpixel((x, y))[0] == 0:
                for i in range(4):
                    if i == 0:
                        temp_x = x * 2
                        temp_y = y * 2
                    elif i == 1:
                        temp_x = x * 2 + 1
                        temp_y = y * 2
                    elif i == 2:
                        temp_x = x * 2
                        temp_y = y * 2 + 1
                    else:
                        temp_x = x * 2 + 1
                        temp_y = y * 2 + 1
                    if random() < 0.5:
                        share1[temp_y][temp_x] = 0
                        # if random() < 0.25:
                        #     share2[temp_y][temp_x] = 0
                    else:
                        share2[temp_y][temp_x] = 0
                        # if random() < 0.25:
                        #     share1[temp_y][temp_x] = 0
            else:
                p1 = False
                p2 = False
                valid_quarter = False
                while not valid_quarter:
                    for i in range(4):
                        if i == 0:
                            temp_x = x * 2
                            temp_y = y * 2
                        elif i == 1:
                            temp_x = x * 2 + 1
                            temp_y = y * 2
                        elif i == 2:
                            temp_x = x * 2
                            temp_y = y * 2 + 1
                        else:
                            temp_x = x * 2 + 1
                            temp_y = y * 2 + 1
                        if random() < 0.5:
                            share1[temp_y][temp_x] = 0
                        else:
                            p1 = True
                        if random() < 0.5:
                            share2[temp_y][temp_x] = 0
                        else:
                            p2 = True

                        if p1 and p2:
                            valid_quarter = True
                        p1, p2 = False, False

    Image.fromarray(share1.astype('uint8')).save("./share1.png", "PNG")
    Image.fromarray(share2.astype('uint8')).save("./share2.png", "PNG")


def decode_image(share1, share2):
    result = np.zeros((200, 200))
    result = result + 255
    for x in range(200):
        for y in range(200):
            # print(f"x = {x}, y = {y}, {share1.getpixel((x, y)) == 255 and share2.getpixel((x, y)) == 255}")
            if share1.getpixel((x, y)) == 0 or share2.getpixel((x, y)) == 0:
                result[y][x] = 0
    Image.fromarray(result.astype('uint8')).save('./decrypted.png', "PNG")


if __name__ == "__main__":
    test_img = Image.open("./test_img.png", mode='r')
    encode_message(test_img)
    s1 = Image.open("./share1.png", mode='r')
    s2 = Image.open("./share2.png", mode='r')
    decode_image(s1, s2)


