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

if __name__ == '__main__':
    main()