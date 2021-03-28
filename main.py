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

    @staticmethod
    def print_array(proc):
        for each in proc:
            print(each)
            if proc.index(each) == len(proc)-1:
                print("<---------- END OF PROCESSES ---------->")
            else:
                print("<----------- NEXT PROCESSES ----------->")

    @staticmethod
    def print_proc_with_leftover(obj_array):
        for each in obj_array:
            print(each)
            print(f"Leftovers: {each.leftovers}")
            if obj_array.index(each) == len(obj_array)-1:
                print("<---------- END OF PROCESSES ---------->")
            else:
                print("<----------- NEXT PROCESSES ----------->")


def inputFunction():
    processes = []
    while True:
        temporary = Process()
        processes.append(temporary)
        flag = str(input('Want to continue[Y/N]: ')).lower()
        if flag == 'n':
            return processes
