import os
from PIL import Image, ImageEnhance

def resize_sign(sign, image):
    # sign.convert('RGBA')

    # sign = 1/100 of image
    lato_indice = image.height if sign.height > sign.width else image.width
    wanted_dim_bckg = lato_indice / 20  # wanted_dim_bckg = bg.width if main_side == img.width else bg.height

    wpercent = (wanted_dim_bckg / float(sign.size[0]))
    hsize = int((float(sign.size[1]) * float(wpercent)))
    sign = sign.resize((int(wanted_dim_bckg), hsize), Image.ANTIALIAS)
    return sign


def set_opacity(im, opacity):
    """
    NOT MINE
    Returns an image with reduced opacity.
    Taken from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/362879
    """
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def add_sign(images, signPath="sign.png", destinationFolder="signed/"):
    # folder = 'to sign'

    # folder = input("Path: ")

    default_sign = Image.open(signPath)
    #
    # image_paths = [os.path.join(folder, f)
    #             for f in os.listdir(folder) if f.endswith('.jpeg') or f.endswith('.jpg')]

    # images = list(map(Image.open, image_paths))
    for image in images:
        print(f"signing {image} ...")
        if image is not None:
            width, height = image.size
            sign = resize_sign(default_sign, image)
            sign = set_opacity(sign, 0.5)

            sign_w, sign_h = sign.size
            margin = 100
            #position of sign = width of image - (width of sign + margin), height of image - (height of sign + margin)
            image.paste(sign, (width - (sign_w + margin), height - (sign_h + margin)), sign)
            print("signed.")

            print("counting...")
            if not os.path.exists(destinationFolder): os.mkdir(destinationFolder)
            # count num of pics to make unique name for each new pic
            list_pics = next(os.walk(destinationFolder))[2]
            count = len(list_pics)
            # print("counted:", count)
            print(f"dest {destinationFolder}")
            # image.save(f'{destinationFolder}/signed_{str(count)}.png', 'PNG')
            image.save(f'{destinationFolder}/compressed_{str(count)}.jpg', 'JPEG', optimize=True, quality=70)

            print("saved!")
    print("DONE.")

        # save final image
