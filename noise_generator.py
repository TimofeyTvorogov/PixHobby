from PIL import Image
import random as rand
import time
import numpy as np


def main():
    def create_blanc_img(w, h):
        return Image.new('RGB', (w, h))

    def get_rand_color(noir=False):
        if noir:
            black_white = rand.randint(0, 1) * 255
            return black_white, black_white, black_white
        else:
            color = []
            for _ in range(3):
                color.append(rand.randint(0, 255))
            return tuple(color)

    def create_rand_name():
        return 'noise' + str(rand.randint(1000, 2000)) + '.jpg'

    start = time.time()
    img = create_blanc_img(100, 100)
    size = img.size
    #/ my solution
    # for x in range(size[0]):
    #     for y in range(size[1]):
    #         img.putpixel((x, y), get_rand_color(True))
    # if you pick this sol. you can switch to True to enable noir noise
    #/

    #/ optimized solution (definitely without the help of GPT)
    random_colors = np.random.randint(0, 256, (size[1],size[0],3), np.uint8)
    img = Image.fromarray(random_colors, 'RGB')
    # /

    img.save(f"./out/{create_rand_name()}")
    #for speed comparison
    print(f'{time.time() - start} seconds, image saved to \"./out\"')


main()
