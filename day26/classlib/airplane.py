# 1

# AirPlane 클래스

class AirPlane:
    '''
    def __init__(self):         # 기본생성자 - 생성자가 생략된 경우 / 인터프리터가 자동으로 생성함
        pass                    # 생략가능
    '''

    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")


if __name__ == "__main__":
    plane = AirPlane()
    plane.take_off()
    plane.fly()
    plane.land()
