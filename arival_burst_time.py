entranceTime = list()
serviceTime = list()
indexList = list()

def get_entrance_service_index(n):
    for i in range(1, n+1):
        entranceTime.append(
            int(input(f"enter the time of entrance of the process{i}: ")))
        serviceTime.append(
            int(input(f"enter the time of service of the process{i}: ")))
        indexList.append((f"Process{i}"))
    return entranceTime,serviceTime,indexList