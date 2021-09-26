import time
from fork import Fork
from philosopher import Philosopher


def DiningPhilosophers():
    # create array of 5 names: Plato, Kant, Confucius, Marx, and Nietzsche
    philosopher_names = ['Plato', 'Kant', 'Confucius', 'Marx', 'Nietzsche']
    # use a list comprehension to create 5 Fork’s
    forks = [Fork(), Fork(), Fork(), Fork(), Fork()]
    # use a list comprehension to create 5 Philosopher’s and correctly
    # assign each pair of forks to each philosopher
    # philosophers = [Philosopher(philosopher_names[i], forks[i], forks[i + 1]) for i in range(5)]
    philosophers = [Philosopher(philosopher_names[0], forks[0], forks[1]), Philosopher(philosopher_names[1], forks[1], forks[2]),
                    Philosopher(philosopher_names[2], forks[2], forks[3]), Philosopher(philosopher_names[3], forks[3], forks[4]),
                    Philosopher(philosopher_names[4], forks[4], forks[0])]
    # start all 5 Philosopher threads (should be non-blocking)
    philosophers[0].start()
    philosophers[1].start()
    philosophers[2].start()
    philosophers[3].start()
    philosophers[4].start()

    # sleep for 10 seconds
    time.sleep(10)
    # set ‘running’ to False
    for philosopher in philosophers:
        philosopher.running = False
    # exit all threads


if __name__ == '__main__':
    DiningPhilosophers()
