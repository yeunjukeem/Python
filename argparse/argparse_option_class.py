#argparse_option_class.py

#str_cats.py

import argparse
import math


class Cat:
    def __init__(self, name, color, sound):
        self.name = name
        self.color = color
        self.sound = sound
    def __str__(self):
        return f'Cat(name={self.name}, color ={self.color}, sound={self.sound})'

    def lotto(self):
        print(f'이름은 {self.name}이고, 색깔은 {self.color}에 고양이가 {self.sound}하고 웁니다.')
    

def parsing_argument():
    parser = argparse.ArgumentParser(description="Sample for using argparse",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument(
        '-c',
        '--cat',
        metavar="string",
        type=str,
        nargs='*',
        help="cat",
        default=["nabi", "white", "meow"]
    )

    args = parser.parse_args()
    print(args)     #return하기전에 print로 확인해볼 것.
    return args 

# parsing_argument()

def main():
    args=parsing_argument()
    cat = Cat(args.cat[0], args.cat[1],args.cat[2])

    cat.lotto()


main()
