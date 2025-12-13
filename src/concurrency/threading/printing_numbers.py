import threading
import time
import random


def print_number(thread_name, N):
    for i in range(N):
        print(f"[{thread_name} {i}]")
        time.sleep(random.uniform(0, 0.01))


if __name__ == "__main__":
    N = 10

    thread1 = threading.Thread(target=print_number, args=("Thread-1", N))
    thread2 = threading.Thread(target=print_number, args=("Thread-2", N))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Both are done!")
