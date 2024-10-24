
from .task_2_1 import task2_1
from .task_2_2 import task2_2
from .task_2_3 import task2_3

import sys
import os
sys.path.append(os.path.dirname(__file__))

def main(**kwargs):
    task21 = task2_1()
    task22 = task2_2()
    task23 = task2_3()
    #print(f"Init: {sys.path}")

if __name__ == '__main__':
    main()
