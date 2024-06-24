import threading, time
from concurrent.futures import ThreadPoolExecutor


def func(secs):
    print(f"sleeping for {secs} seconds")
    time.sleep(secs)
    return secs

def main():
    time1 = time.perf_counter()
    # normal way
    # func(4)
    # func(3)
    # func(2)
    time2 = time.perf_counter()
    # print(time2-time1)
    # way using threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[3])
    t3 = threading.Thread(target=func, args=[2])
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    print(time2 - time1)


# main()
def pool():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func , 3)
        # future2 = executor.submit(func, 4)
        # future3 = executor.submit(func, 5)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        #     other way for large data sets
        l = [2, 3, 4, 5]
        results = executor.map(func, l)
        for result in results:
            print(result) # also return the values


pool()
