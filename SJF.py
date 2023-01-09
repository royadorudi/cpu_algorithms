def sjf(df):
    dfCopy = df.copy()
    completion = df['ArivalTime'].min()
    i = 0
    indexArray=[]
    completionArray=[]
    while (i < len(dfCopy['ArivalTime'])):
        availableExecuteTimes = dfCopy.loc[dfCopy['ArivalTime']<= completion, 'ExecuteTime']
        execute = min(availableExecuteTimes)
        availableArivalTimes = dfCopy.loc[dfCopy['ExecuteTime']== execute, 'ArivalTime']
        arival = min(availableArivalTimes)
        index = dfCopy[(dfCopy['ArivalTime'] == arival) &(dfCopy['ExecuteTime'] == execute)].index.item()
        indexArray.append(index)
        completion += execute
        completionArray.append(completion)
        df.loc[index, 'Completion'] = completion
        dfCopy.drop(index, inplace=True)
    return df,indexArray,completionArray