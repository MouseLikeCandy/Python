import time
import threading

class MyThread(threading.Thread):
    def __init__(self, input, output, lock):
        super(MyThread, self).__init__()
        # super().__init__()
        self.input = input
        self.output = output
        self.lock = lock

    def run(self):
        self.lock.acquire()

        for line in self.input.readlines():
            time.sleep(1)
            self.output.write(line)

        self.lock.release()
        print('Thread Done')


def main():
    lock = threading.Lock()
    txt1 = open('1.txt', 'r')
    txt2 = open('2.txt', 'r')
    txt3 = open('3.txt', 'a')
    t1 = MyThread(txt1, txt3, lock)
    t2 = MyThread(txt2, txt3, lock)
    t1.start()
    t2.start()
    print('Done')


main()