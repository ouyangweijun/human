import time
from greenlet import greenlet


# gr1 = greenlet(task_1)
# gr2 = greenlet(task_2)
#
# #切换到gr1中执行
# gr1.switch()

def main():
    def task_1():

        while True:
            print("----1----")
            gr2.switch()
            #time.sleep(0.1)

    def task_2():
        while True:
            print("----2----")
            gr1.switch()
            #time.sleep(0.1)

    gr1 = greenlet(task_1)
    gr2 = greenlet(task_2)
    gr1.switch()
if __name__ == '__main__':
    main()