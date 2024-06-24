# demonstrates how to use the multiprocessing module in Python to create multiple processes that run a
# function. The function print_func prints the name of a continent. Let's
from multiprocessing import Process

def print_func(continent='Asia'):
    print('The name of continent is : ', continent)

if __name__ == "__main__":  # confirms that the code is under main function
    names = ['America', 'Europe', 'Africa']
    procs = []
    # Instantiate and start a process for the default continent 'Asia'
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # Instantiate and start processes for each continent in the names list
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()