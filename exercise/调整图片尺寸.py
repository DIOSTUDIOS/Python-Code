from PIL import Image
import os


def main():
    images = os.listdir(r'D:\Code\images')
    sn = 1

    for image in images:
        # print(image)
        old_picture = Image.open(r'D:\Code\images\{:s}'.format(image))
        # width, height = old_picture.size
        # print(width, height)
        new_picture = old_picture.resize((750, 1334), Image.ANTIALIAS)
        new_picture.save(r'D:\Code\pictures\picture_' + str(sn) + '.bmp')

        sn += 1


if __name__ == '__main__':
    main()
