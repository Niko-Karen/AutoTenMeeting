# 必需安装库： pykeyboard, pymouse, schedule
from pykeyboard import *
from pymouse import *
import time
import schedule as sch
import csv

m = PyMouse()  # 建立鼠标对象
k = PyKeyboard()  # 建立键盘对象


class TecentMeeting:
    def __init__(self, roomid, passwd):
        self.roomid = roomid
        self.passwd = passwd

    def survey(self):
        # 分别确定坐标
        print("五秒后开始确定位置……")
        time.sleep(5)

        print("请对准第1个位置: 加入")
        time.sleep(4)
        self.location1 = list(m.position())
        time.sleep(4)

        print("请对准第2个位置：会议号")
        time.sleep(6)
        self.location2 = list(m.position())

        print("请对准第3个位置：关闭摄像头")
        time.sleep(5)
        self.location3 = list(m.position())

        print("请对准第4个位置：加入")
        time.sleep(5)
        self.location4 = list(m.position())

        print("请对准第5个位置：密码")
        time.sleep(4)
        self.location5 = list(m.position())

        print("请对准第6个位置：加入")
        time.sleep(4)
        self.location6 = list(m.position())

        print("位置确定完成！\n")

    def run(self):
        m.click(self.location1[0], self.location1[1])
        time.sleep(2)
        m.click(self.location2[0], self.location2[1])
        time.sleep(2)
        k.tap_key(k.backspace_key)
        k.type_string(self.roomid)
        time.sleep(2)
        m.click(self.location3[0], self.location3[1])
        time.sleep(2)
        m.click(self.location4[0], self.location4[1])
        time.sleep(2)
        m.click(self.location5[0], self.location5[1])
        time.sleep(2)
        if self.passwd != '':  # 判空
            k.type_string(self.passwd)
        time.sleep(2)
        m.click(self.location6[0], self.location6[1])


if __name__ == "__main__":
    roomid = input("请输入会议号：")
    passwd = input("请输入房间密码（无请留空）：")

    teme = TecentMeeting(roomid, passwd)
    teme.survey()  # 先确定坐标

    print("请关闭子层窗口，10秒后开始试运行……（运行时请勿移动App）")
    time.sleep(10)

    teme.run()
    print("试运行完成")

    runcom = input("坐标点是否需要重新获取？(y or n): ")
    while runcom == "y":
        teme.survey()
        runcom = input("坐标点是否需要重新获取？(y or n): ")

    runtime = input("输入运行时间(小时:分钟): ")
    sch.every().day.at(runtime).do(teme.run)

    print("开始等待……（执行后请Ctrl-C终止程序）")  # 执行后请终止程序，否则每天这个时间点都会执行程序
    try:
        while True:
            sch.run_pending()
            time.sleep(60)
    except:
        pass
