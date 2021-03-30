from main import Process, inputFunction
import copy

processes = inputFunction()

processes = Process.sort_processes(processes, 'arrivalTime')
timeDelta = float(input("Enter the time frame: "))
current_time = processes[0].arrivalTime
process_execution_order = []

ready_queue = []

while True:

    new_processes = [proc for proc in processes if proc.arrivalTime <= current_time and proc not in ready_queue]
    ready_queue = new_processes + ready_queue

    # end of all process ...
    if len(ready_queue) == 0 and len(processes) == 0:
        break

    # Dealing with cases where cpu is in rest condition ...
    if len(ready_queue) == 0:
        current_time = Process.sort_processes(processes, 'arrivalTime')[0].arrivalTime
        continue

    # Dealing with general case ...
    for process in ready_queue:
        if process.leftovers <= timeDelta:
            process.startTime = current_time
            current_time += process.leftovers
            if process.endTime is not None:
                process.waitingTime += (current_time - process.endTime)
            process.leftovers = 0
            process.endTime = current_time
            ready_queue.remove(process)
            processes.remove(process)
        else:
            process.startTime = current_time
            if process.endTime is not None:
                process.waitingTime += (current_time - process.endTime)
            else:
                process.waitingTime = current_time - process.arrivalTime
            current_time += timeDelta
            process.leftovers -= timeDelta
            process.endTime = current_time

        process_execution_order.append(copy.deepcopy(process))


Process.print_proc_with_leftover(process_execution_order)