from main import Process, inputFunction
import sys

processes = inputFunction()

print("The entered Information is provided below:")
Process.print_array(processes)

flag = input("Is input correct [Y/N]: ").lower()
if flag == 'n':
    sys.exit("Wrong Input!")

print("<--------------------------------------------->")

choice = input("Preemptive or Non-Preemptive[P/N]: ").lower()
processes = Process.sort_processes(processes, 'arrivalTime')
last_end_time = processes[0].arrivalTime
ordered_sjf = []

if choice == 'n':
    print("Performing Non - Preemptive SJF\n")
    print("The processes in the order of execution is provided below:")
    while True:
        if len(processes) == 0:
            break
        else:
            jobs_arrived_initially = [proc for proc in processes if proc.arrivalTime <= last_end_time]

            if len(jobs_arrived_initially) == 0:
                last_end_time = Process.sort_processes(processes, 'arrivalTime')[0].arrivalTime
                continue

            processing = Process.sort_processes(jobs_arrived_initially, 'burstTime')[0]
            processes.remove(processing)
            processing.waitingTime = last_end_time - processing.arrivalTime

            # Starts AT start Time:
            processing.startTime = last_end_time

            # Process Running ....
            last_end_time = last_end_time + processing.burstTime

            # Completion time or time when processing of process is completed ....
            processing.endTime = last_end_time
            processing.leftovers = 0
            ordered_sjf.append(processing)

    Process.print_proc_with_leftover(ordered_sjf)
    print(f"The waiting time: {sum([proc.waitingTime for proc in ordered_sjf])/len(ordered_sjf)}")
    print(f'The turn around time is {sum([proc.endTime - proc.startTime for proc in ordered_sjf])/len(ordered_sjf)}')
else:
    print("Performing Preemptive SJF\n\n")


