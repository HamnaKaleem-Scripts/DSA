class Process:
 def __init__(self, processId, processName, processExecTime):
    self.processId = processId
    self.processName = processName
    self.processExecTime = processExecTime
    
 def displayState(self):
        print("Process ID:", self.processId)
        print("Process Name:", self.processName)
        print("Execution Time:", self.processExecTime)
        