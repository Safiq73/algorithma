
import pandas as pd
import threading
import random

def open_file(filename):
    filename= f"algorithma/{str(filename)}.txt"
    with open(filename, 'w') as f:
        f.write(str(random.random()))

if __name__ == "__main__":

    # Create thread for each filename.
    threads = [threading.Thread(target=open_file, args=(random.random(),)) for _ in range(5)]

    # Start execution of each thread.
    for thread in threads:
        thread.start()

