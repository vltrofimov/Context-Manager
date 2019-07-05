import datetime
import time

class Myopen:
    def __init__(self):
        pass

    def __enter__(self):
        self.start=datetime.datetime.now()
        print(f"code start is: {self.start}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finish=datetime.datetime.now()
        print(f"code finish is:{self.finish}")
        print(f"time of code is: {self.finish-self.start}")


with Myopen() as cm:
    for i in range(5):
        print(i)
        time.sleep(1)

