import multiprocessing
import time


def worker(task_id, n):
    print(f"[Process-{task_id}] Starting computation")
    result = sum(i * i for i in range(n))
    print(f"[Process-{task_id}] Finished computation")
    return result


def main():
    start = time.time()
    num_cores = multiprocessing.cpu_count()
    print(f"Number of cores: {num_cores}")
    with multiprocessing.Pool(processes=num_cores) as pool:
        results = pool.starmap(worker, [(i, 5_000_000) for i in range(num_cores)])

    end = time.time()

    print("All processes completed!")
    print(f"Results: {results}")
    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    main()
