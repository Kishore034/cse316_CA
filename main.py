import threading

n = 0  # number of threads
m = 0  # number of resources
available = []  # available resources
maximum = []  # maximum demand of each thread
allocation = []  # resources allocated to each thread
need = []  # remaining needs of each thread
mutex = threading.Lock()  # lock for accessing shared data

def main():
    global n, m, available, maximum, allocation, need

    # Read input from user
    n = int(input("Enter the number of threads: "))
    m = int(input("Enter the number of resources: "))

    # Initialize available resources
    print("Enter the number of available resources for each type:")
    available = list(map(int, input().split()))

    # Initialize maximum demand of each thread
    print("Enter the maximum demand of each thread for each resource type:")
    maximum = [[int(x) for x in input().split()] for _ in range(n)]

    # Initialize allocation and need
    allocation = [[0] * m for _ in range(n)]
    need = [[maximum[i][j] for j in range(m)] for i in range(n)]

    # Print initial state of the system
    print("\nInitial state of the system:")
    print("Available resources:", available)
    print("Maximum demand of each thread:")
    for i in range(n):
        print("Thread {}: {}".format(i, maximum[i]))
    print("Resources allocated to each thread:")
    for i in range(n):
        print("Thread {}: {}".format(i, allocation[i]))
    print("Remaining needs of each thread:")
    for i in range(n):
        print("Thread {}: {}".format(i, need[i]))

if __name__ == '__main__':
    main()
