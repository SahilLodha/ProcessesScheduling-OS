from main import Process
from sys import exit

processes = []

while True:
    temp = Process()
    processes.append(temp)
    choice = input("Do you want to Continue[Y/N]: ").lower()
    if choice == 'n':
        break

processes = Process.sort_processes(processes, 'arrivalTime')
timeDelta = int(input("Enter the time frame: "))
first_arrival = processes[0].arrivalTime
print(first_arrival)
i = 0
while True:
    execution_time = first_arrival
    arrival_list = [proc for proc in processes if proc.arrivalTime <= execution_time]

    if (len(arrival_list) == 0) & (len(processes) != 0):
        execution_time = min([proc.arrivalTime for proc in processes])
        arrival_list = [proc for proc in processes if proc.arrivalTime <= execution_time]

    for proc in arrival_list:
        if proc.leftovers <= timeDelta:
            execution_time += proc.leftovers
            proc.leftovers = 0
            processes.remove(proc)
        else:
            proc.leftovers -= timeDelta
            execution_time = execution_time + timeDelta

        proc.waitingTime += execution_time - proc.arrivalTime
        proc.arrivalTime = execution_time
        print(proc)
        print(proc.leftovers)