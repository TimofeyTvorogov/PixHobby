from PIL import Image

gscale1 = "@%#*+=-:. "


def main():
    path = input("enter path to image")
    try:
        image = Image.open(path)
    except Exception as e:
        print(f"cannot open image due to {e.__class__.__name__}")
        return
    try:
        new_width = int(input("enter width of ascii image"))
        if new_width <= 0:
            raise Exception
    except Exception as e:
        new_width = 200
        print("width must be an integer > 0")

    prepped_image = get_grayscale(resize_image(image, new_width))
    new_data = asciify(prepped_image)
    out = new_line(new_data, len(new_data), new_width)
    with open("output.txt", 'w') as file:
        file.write(out)


def resize_image(image, new_width):
    w, h = image.size
    ratio = h / w / 1.65
    return image.resize((new_width, int(new_width * ratio)))


def get_grayscale(image):
    return image.convert("L")


def asciify(image):
    pixels = list(image.getdata())
    return ''.join([gscale1[pixel // 30] for pixel in pixels])


def new_line(asciis: str, chars_num, new_width):
    return '\n'.join(
        [asciis[i:(i + new_width)] for i in range(0, chars_num, new_width)])


if __name__ == '__main__':
    main()
