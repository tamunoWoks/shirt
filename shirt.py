from PIL import Image, ImageOps
from sys import argv, exit
from os.path import splitext

def main():
    ...


def check_arg(argv):
    try:
        if len(argv) < 3:
            exit('Too few command-line arguments')
        elif len(argv) > 3:
            exit('Too many command-line arguments')

        support = ['.jpeg', '.jpg', '.png']
        input_file_root, input_file_ext = splitext(argv[1])
        output_file_root, output_file_ext = splitext(argv[2])

        if input_file_ext.lower() not in support:
            exit('Invalid input')
        if output_file_ext.lower() not in support:
            exit('Invalid output')
        if input_file_ext.lower() != output_file_ext.lower():
            exit('Input and output have different extensions')
        return True
    except FileNotFoundError:
        exit('File does not exist')


def overlay(input, output):
    try:
        shirt = Image.open('shirt.png')
        with Image.open(input) as input:
            cut = ImageOps.fit(input, shirt.size)
            cut.paste(shirt, mask=shirt)
            cut.save(output)
    except OSError:
        exit('Input does not exist')

        
if __name__ == '__main__':
    main()