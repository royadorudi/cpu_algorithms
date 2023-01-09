def rr(df,q):
    sortedDf = df.sort_values('ArivalTime')
    completion = sortedDf.iloc[0]['ArivalTime']
    indexArray=[]
    completionArray=[]
    while True:
        for index in sortedDf.index:
            indexArray.append(index)
            service = sortedDf.loc[index]['ExecuteTime']
            if q < service:
                newservice = service-q
                sortedDf.loc[index, 'ExecuteTime'] = newservice
                completion += q
                df.loc[index, 'Completion'] = completion
            elif q >= service:
                completion += service
                df.loc[index, 'Completion'] = completion
                sortedDf.drop(index, inplace=True)
            completionArray.append(completion)
        length = len(sortedDf['ExecuteTime'])
        if length == 0:
            break
    return df,indexArray,completionArray
