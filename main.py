class Process:
    def __init__(self):
        self.processName = input("Enter the name of the process: ")
        self.arrivalTime = int(input("Enter the arrival time: "))
        self.burstTime = int(input("Enter the burst time associated: "))
        self.leftovers = self.burstTime
        self.startTime = None
        self.waitingTime = 0
        self.endTime = None

    def __str__(self):
        return f'Name: {self.processName}\nBurst Time: {self.burstTime}\nArrival Time: {self.arrivalTime}\nWaiting ' \
               f'Time: {self.waitingTime}\nEnd Time: {self.endTime} '

    @staticmethod
    def sort_processes(list_processes, sort_key):
        list_processes = sorted(list_processes, key=lambda x: x.__getattribute__(sort_key))
        return list_processes

    @staticmethod
    def avg_waiting_time_FCFS(processes):
        temp = []
        for proc in processes:
            temp.append(proc.waitingTime)

        return sum(temp)/len(temp)