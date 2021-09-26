import threading


class Fork:
    def __init__(self):
        # add a lock as an instance variable
        self.lock = threading.Lock()

    def acquire_fork(self):
        # return True if you can acquire self.lock, False otherwise
        return self.lock.locked()

    def release_fork(self):
        # release lock
        self.lock.release()

    def acquire(self):
        self.lock.acquire()


if __name__ == '__main__':
    pass
