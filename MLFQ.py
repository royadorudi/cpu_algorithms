def mlfq(df,serviceTime,quantums):
    global indexArray,completionArray
    indexArray=[]
    completionArray=[]
    sortedDf = df.sort_values('ArivalTime')
    sortedDf['Q1'] = serviceTime
    sortedDf['Q2'] = 0
    sortedDf['Q3'] = 0
    completion = sortedDf.iloc[0]['ArivalTime']
    for index in sortedDf.index:
        arival = sortedDf.loc[index]['ArivalTime']
        if arival <= completion:
            service = sortedDf.loc[index]['Q1']
            indexArray.append(index)
            if service > quantums[0]:
                newService = service-quantums[0]
                sortedDf.loc[index, 'Q2'] = newService
                completion += quantums[0]
                df.loc[index, 'Completion'] = completion
            else:
                completion += service
                df.loc[index, 'Completion'] = completion
                sortedDf.drop(index, inplace=True)
            completionArray.append(completion)
        elif arival > completion:
            services = sortedDf.loc[(sortedDf['ArivalTime'] < completion) & (sortedDf['Q3'] == 0), 'Q2']
            availableService = services.tolist()
            for service in availableService:
                otherIndex = sortedDf[(sortedDf['Q2'] == service) & (sortedDf['ArivalTime'] < completion)].index.item()
                indexArray.append(otherIndex)
                if service > quantums[1]:
                    newService = service-quantums[1]
                    sortedDf.loc[otherIndex, 'Q3'] = newService
                    completion += quantums[1]
                    df.loc[otherIndex, 'Completion'] = completion
                else:
                    completion += service
                    df.loc[otherIndex, 'Completion'] = completion
                    sortedDf.drop(otherIndex, inplace=True)
                completionArray.append(completion)
                if completion == arival:
                    break
            service = sortedDf.loc[index]['Q1']
            indexArray.append(index)
            if service > quantums[0]:
                newService = service-quantums[0]
                sortedDf.loc[index, 'Q2'] = newService
                completion += quantums[0]
                df.loc[index, 'Completion'] = completion
            else:
                completion += service
                df.loc[index, 'Completion'] = completion
                sortedDf.drop(index, inplace=True)
            completionArray.append(completion)
    return df, sortedDf, completion,indexArray,completionArray

def fcfs_part1(df, sortedDf, completion,quantums):
    for index in sortedDf.index:
        value = sortedDf.loc[index]['Q3']
        if value != 0:
            continue
        else:
            indexArray.append(index)
            service = sortedDf.loc[index]['Q2']
            if service > quantums[1]:
                newService = service-quantums[1]
                sortedDf.loc[index, 'Q3'] = newService
                completion += quantums[1]
                df.loc[index, 'Completion'] = completion
            else:
                completion += service
                df.loc[index, 'Completion'] = completion
                sortedDf.drop(index, inplace=True)
            completionArray.append(completion)
    return df, sortedDf, completion,indexArray,completionArray


def fcfs_part2(df, sortedDf, completion):
    for index in sortedDf.index:
        indexArray.append(index)
        service = sortedDf.loc[index]['Q3']
        completion += service
        completionArray.append(completion)
        sortedDf.drop(index, inplace=True)
        df.loc[index, 'Completion'] = completion
    return df,indexArray,completionArray
