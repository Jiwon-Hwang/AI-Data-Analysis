
class Square:
    크기 = 0
    def __init__(self, size):
        self.크기 = size
        
    def 넓이구하기(self):
        area = self.크기 * self.크기
        print('정사각형의 넓이는', area)
