from main import Process, inputFunction
import sys

processes = inputFunction()
print("The entered Information is provided below:")
Process.print_array(processes)

flag = input("Is it correct [Y/N]: ").lower()
if flag == 'n':
    sys.exit("Wrong Input!")

print("\n<--------------- Implementing FCFS --------------->\n")
processes = Process.sort_processes(processes, 'arrivalTime')
end_time_last = 0

for proc in processes:
    if proc.arrivalTime >= end_time_last:
        proc.waitingTime = 0
        proc.startTime = proc.arrivalTime
        proc.endTime = proc.arrivalTime + proc.burstTime
    else:
        proc.waitingTime = end_time_last - proc.arrivalTime
        proc.endTime = end_time_last + proc.burstTime
        proc.startTime = end_time_last

    end_time_last = proc.endTime
    proc.leftovers = 0

Process.print_proc_with_leftover(processes)
print(f'Hence the average waiting time is {Process.avg_waiting_time_FCFS(processes):.2f}')
print(f'The CPU Utilization is {sum([proc.burstTime for proc in processes])/processes[-1].endTime:.4f}')
print(f"The turn around time is {sum(proc.endTime - proc.startTime for proc in processes)/len(processes)}")