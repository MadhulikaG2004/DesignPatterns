import threading
import time

class ThreadSafeSingleton:
    _instance = None

    def __init__(self):
        time.sleep(0.1)   # Artificial delay
        print("Instance created")

    @staticmethod
    def get_instance():
        if ThreadSafeSingleton._instance is None:
            ThreadSafeSingleton._instance = ThreadSafeSingleton()
        return ThreadSafeSingleton._instance


def access_singleton():
    instance = ThreadSafeSingleton.get_instance()
    print(f"Thread {threading.current_thread().name} got instance id: {id(instance)}")


if __name__ == "__main__":
    threads = []

    for i in range(5):
        t = threading.Thread(target=access_singleton)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()