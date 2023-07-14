#class_abstract.py

#추상클래스; abc library가 필수(abstract class library)
# 만들어 놓고 꼭 사용해야되게 설정해둠

# 추상클래스 만드는법
from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        #이 자리에 기본기능 적을 수 있음
        pass

    @abstractmethod
    def go_to_school(self):
        print("학교에가다")
        pass

class Student(StudentBase):
    def study(self):
        print("공부하기")
    def go_to_school(self):
        super().go_to_school()
        print("출석")

james = Student()
james.study()
