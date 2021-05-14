pending=["html"]
completed=[]
def addPending(cmd):
    if(cmd not in pending):
        pending.append(cmd)
def addCompleted(cmd):
    if(cmd not in completed):
        pending.remove(cmd)
        completed.append(cmd)
def getPending():
    return pending
def getCompleted():
    return completed