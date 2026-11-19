from concurrent.futures import ThreadPoolExecutor

def run_parallel(tasks, max_threads=5):
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(lambda f: f(), tasks)