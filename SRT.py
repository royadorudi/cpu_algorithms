def srt(df,indexList):
    dfCopy = df.copy()
    completion = df['ArivalTime'].min()
    indexArray=[]
    completionArray=[]
    while True:
        availableExecuteTimes = dfCopy.loc[(dfCopy['ArivalTime'] <= completion), 'ExecuteTime']
        execute = min(availableExecuteTimes)
        index = dfCopy[(dfCopy['ExecuteTime'] == execute) & (dfCopy['ArivalTime'] <= completion)].index
        element=dfCopy[(dfCopy['ExecuteTime'] == execute) & (dfCopy['ArivalTime'] <= completion)].index.values.tolist()
        if indexList[-1] in index:
            mainIndex = indexList[-1]
            completion += execute
            completionArray.append(completion)
            indexArray.append(mainIndex)
            dfCopy.drop(mainIndex, inplace=True)
            df.loc[mainIndex, 'Completion'] = completion
            break
        otherIndex = min(index)
        indexArray.append(min(element))
        newExecute = execute-1
        completion += 1
        if newExecute == 0:
            df.loc[otherIndex, 'Completion'] = completion
            dfCopy.drop(otherIndex, inplace=True)
        else:
            dfCopy.loc[otherIndex, 'ExecuteTime'] = newExecute
            df.loc[otherIndex, 'Completion'] = completion
        completionArray.append(completion)
    for i in range(1, len(dfCopy['ExecuteTime'])+1):
        availableExecuteTimes2 = dfCopy.loc[dfCopy['ArivalTime']<= completion, 'ExecuteTime']
        execute = min(availableExecuteTimes2)
        availableArivalTimes = dfCopy.loc[dfCopy['ExecuteTime']== execute, 'ArivalTime']
        arival = min(availableArivalTimes)
        index = dfCopy[(dfCopy['ArivalTime'] == arival) &(dfCopy['ExecuteTime'] == execute)].index.item()
        indexArray.append(index)
        completion += execute
        df.loc[index, 'Completion'] = completion
        completionArray.append(completion)
        dfCopy.drop(index, inplace=True)
    return df,indexArray,completionArray