#argparse_car_class.py
import argparse

class Car:
    def __init__(self, door, brand, color):
        self.door = door
        self.brand = brand
        self.color = color

    def __str__(self):
        return f'Cat(name={self.door}, brand ={self.brand}, color ={self.color})'
    
    def rapid(self):
        print(f'차에는 문이 {self.door}개, 차의 브랜드는 {self.brand} 그리고 색상은 {self.color}입니다.')

# car = Car("4", "Mybach", "150")

# car.rapid()


def parsing_argument():
    parser = argparse.ArgumentParser(description="Sample for using argparse",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

   
    parser.add_argument(
        '-c',
        '--car',
        metavar="car option",
        type=str,
        nargs='*',
        help="assignment variables",
        default=["4", "mybach", "yellow"]
    )

    args = parser.parse_args()
    print(args)     #return하기전에 print로 확인해볼 것.
    return args



def main():
    args=parsing_argument()
    car = Car(args.car[0], args.car[1],args.car[2])

    car.rapid()


main()
