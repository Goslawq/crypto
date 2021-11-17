from PIL import Image
import numpy as np
from random import random, randrange


def encode_message(image):
    share1 = np.zeros((200, 200))
    share2 = np.zeros((200, 200))
    for x in range(100):
        for y in range(100):
            if image.getpixel((x, y))[0] == 0:
                for i in range(4):
                    temp_x = 2*x + (1 if i % 4 == 0 or i % 4 == 2 else 0)
                    temp_y = 2*y + (1 if i % 4 == 1 or i % 4 == 3 else 0)
                    if random() < 0.5:
                        share1[temp_y][temp_x] = 255
                    else:
                        share2[temp_y][temp_x] = 255
            else:
                protected = randrange(0, 4)
                for i in range(4):
                    if i != protected:
                        temp_x = 2 * x + (1 if i % 4 == 0 or i % 4 == 2 else 0)
                        temp_y = 2 * y + (1 if i % 4 == 1 or i % 4 == 3 else 0)
                        if random() < 0.5:
                            share1[temp_y][temp_x] = 255
                        else:
                            share2[temp_y][temp_x] = 255
                    else:
                        temp_x = 2 * x + (1 if i % 4 == 0 or i % 4 == 2 else 0)
                        temp_y = 2 * y + (1 if i % 4 == 1 or i % 4 == 3 else 0)
                        share1[temp_y][temp_x] = 255
                        share2[temp_y][temp_x] = 255

    Image.fromarray(share1.astype('uint8')).save("./share1.png", "PNG")
    Image.fromarray(share2.astype('uint8')).save("./share2.png", "PNG")


def decode_image(share1, share2):
    result = np.zeros((200, 200))
    for x in range(200):
        for y in range(200):
            if not (share1.getpixel((x, y)) == 0 or share2.getpixel((x, y)) == 0):
                result[y][x] = 255
    Image.fromarray(result.astype('uint8')).save('./decrypted.png', "PNG")


if __name__ == "__main__":
    test_img = Image.open("./test_img.png", mode='r')
    encode_message(test_img)
    s1 = Image.open("./share1.png", mode='r')
    s2 = Image.open("./share2.png", mode='r')
    decode_image(s1, s2)


