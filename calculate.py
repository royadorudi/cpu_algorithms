returnTimeList=list()
waitTimeList=list()

def calculation(n,df):
    for i in range(0,n):
        returnTime=df.iloc[i]['Completion']-df.iloc[i]['ArivalTime']
        waitTime=returnTime-df.iloc[i]['ExecuteTime']
        returnTimeList.append(returnTime)
        waitTimeList.append(waitTime)
    df['TurnAroundTime'] = returnTimeList
    df['WaitTime'] = waitTimeList
    avgReturnTime=round(((df['TurnAroundTime'].sum())/n),2)
    avgWaitTime=round(((df['WaitTime'].sum())/n),2)
    return df,avgReturnTime,avgWaitTime