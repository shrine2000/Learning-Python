import time
from multiprocessing import Process
import os


def print_numbers(process_name, n):
    for i in range(n):
        print(f"[{time.time()} | {process_name} | {os.getpid()}] {i}", flush=True)


if __name__ == "__main__":
    N = 10

    p1 = Process(target=print_numbers, args=("Process-1", N))
    p2 = Process(target=print_numbers, args=("Process-2", N))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both are done!")
