from Queues import Queue

class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum

    def assignProcessor(self):
        time = 0
        q = Queue()
        for process in self.processArray:
            q.enQueue(process)

        while not q.isEmpty():
            current_process = q.deQueue()
            current_process.displayState()
            while current_process.processExecTime > 0:
                time += 1
                current_process.processExecTime -= 1
                if time % 10 == 0:
                    print(f"Time: {time} - Process {current_process.processName} is paused")
                    q.enQueue(current_process)
                    break
                if current_process.processExecTime == 0:
                    print(f"Time: {time} - Process {current_process.processName} has finished execution")
            if current_process.processExecTime > 0:
                q.enQueue(current_process)
