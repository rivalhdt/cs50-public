import sys
from PIL import Image
try:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")
    elif ".jpg" in sys.argv[1:] or ".png" in sys.argv[1:] or ".jpeg" in sys.argv[1:]:
        sys.exit("Invalid input")
    else:
        shirt = Image.open("shirt.png")
        sec_shirt = Image.open(f"{sys.argv[1]}")

        size = shirt.size
        sec_shirt = sec_shirt.resize((600,800))

        text_img = Image.new('RGB', size)
        text_img.paste(sec_shirt, (0,-100))
        text_img.paste(shirt, (0,0), mask=shirt)
        text_img.save(f"{sys.argv[2]}", format="jpeg")

except FileNotFoundError:
    sys.exit("File does not exist")