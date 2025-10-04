from concurrent.futures import thread
import threading
import time


def worker(task_id, delay):
    print(f"[{task_id}] starting")
    time.sleep(delay)
    print(f"[{task_id}] finished")


def main():
    threads = []

    for i in range(3):
        thread = threading.Thread(target=worker, args=(i + 1, (i + 1) * 0.5))
        threads.append(thread)
        thread.start()

    for threads in threads:
        thread.join()

    print("all threads are done")


if __name__ == "__main__":
    main()
