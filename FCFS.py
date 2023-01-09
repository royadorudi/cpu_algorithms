def fcfs(df):
    indexArray=[]
    completionArray=[]
    sortedDf = df.sort_values('ArivalTime')
    completion = sortedDf.iloc[0]['ArivalTime']
    for index in sortedDf.index:
        executeTime = sortedDf.loc[index]['ExecuteTime']
        completion += executeTime
        completionArray.append(completion)
        df.loc[index, 'Completion'] = completion
        indexArray.append(index)
    return df,indexArray,completionArray
