# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.Graph()

# xi  = "University"
# st  = "Student"
# cr  = "Course"
# lb  = "Library"

# G.add_edge(xi, st)
# G.add_edge(cr, st)
# G.add_edge(xi, cr)
# G.add_edge(xi, lb)


# nx.draw(G, with_labels=True)

# plt.show()

# import time
# import threading

# def tOne():
#     for i in range(5):
#         time.sleep(1)
#         print("loop one:",i)

# def tTwo():
#     for i in range(10):
#         time.sleep(1)
#         print("loop two:",i)
        
# threadOne = threading.Thread(target=tOne)
# threadTwo = threading.Thread(target=tTwo)

# threadOne.start()

# threadTwo.start()


# import threading
# import time

# def my_function():
#     for i in range(10):
#         print("Daemon thread is running",i)
#         time.sleep(1)

# my_thread = threading.Thread(target=my_function)
# my_thread.daemon = False
# my_thread.start()


import threading
import time
import signal
import sys

def my_function():
    for i in range(2):
        print("Daemon thread is running",i)
        time.sleep(1)

def sigint_handler(signum, frame):
    print("Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

my_thread = threading.Thread(target=my_function)
my_thread.daemon = True
my_thread.start()

my_thread.join()

print("Main program is done")
