from PIL import Image

def is_orange(pixel, tolerance=60):
    r, g, b, a = pixel
    return (
        r > 150 and
        40 <= g <= 180 and
        b < 120 and
        r > g > b
    )

def change_orange_to_white(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        if is_orange(item):
            new_data.append((255, 255, 255, item[3]))  # keep transparency
        else:
            new_data.append(item)

    img.putdata(new_data)
    img.save(output_path)

change_orange_to_white("aa.png", "output.png")