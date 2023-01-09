import pandas as pd

def make_dataFrame(entranceTime,serviceTime,indexList):
    d = {'ArivalTime': entranceTime, 'ExecuteTime': serviceTime}
    df = pd.DataFrame(d, columns=['ArivalTime', 'ExecuteTime'], index=indexList)
    return df
