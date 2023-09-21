import threading
import time 

# define a funciton for the thread to run
# this is basically another program that does whatever you want
# all of this happens in a new thread, independent of the main thread
def thread_function(controller: dict):
    
    # a fake 'long running' job, this would be whatever you want
    for i in range(10):

        time.sleep(1)

        print("Thread is looping...")

        # we're gonna use this controller object to signal shutdown
        # so make sure to check if we should stop in the thread
        if controller.get('shutdown', False):
            print("Thread is stopping...")
            return

# make our controller object, this lets us signal shutdown to our thread
e = { "shutdown" : False }
thread = threading.Thread(target=thread_function, args=(e,))
thread.start()

while True:

    a = input("Type exit to quit\n")

    if a.lower() == "quit":

        # signal the shutdown
        e["shutdown"] = True 
        break 

# block the current thread until thread is done
thread.join()