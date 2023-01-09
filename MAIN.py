import tkinter 
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import make_df, calculate,FCFS,SJF,SRT,RR,MLFQ,GanttChart
import pandastable
from pandastable import Table

root = tkinter.Tk()
root.title('Algorithms')
root.geometry('550x200')
root['bg']='#173D4F'

def next_entry(event):
    event.widget.tk_focusNext().focus()
    return("break")

def start():
    global numOfProcesses,top0
    root.withdraw()
    top0=Toplevel(bg='#173D4F')
    top0.title('Algorithms')
    top0.geometry('250x100')
    numOfProcesses = StringVar()
    numOfProcesses_lb = Label(top0, text='Number Of Processes:', font=('calibri', 12),bg='#173D4F',fg='#6FD690')
    numOfProcesses_lb.grid(row=1,column=1,rowspan=2,padx=5,pady=5)
    numOfProcesses_en = Entry(top0, textvariable=numOfProcesses,bg='#888899')
    numOfProcesses_en.focus_set()
    numOfProcesses_en.grid(row=3,column=1,rowspan=2,padx=5,pady=5)
    numOfProcesses_btn = Button(top0, text='Next', command=arival_execute_time,bg='#888899',fg='#173D4F')
    numOfProcesses_btn.grid(row=5,column=2,padx=5,pady=5)
    top0.bind('<Return>', lambda event=None: numOfProcesses_btn.invoke())

def arival_execute_time():
    global number_of_processes, arivalTime_en, executeTime_en, arivalTimeList, executeTimeList, indexList, top1,canvas
    top0.withdraw()
    top1 = Toplevel(bg='#173D4F')
    top1.title('Algorithms')
    top1.geometry('500x500')
    first_frame=Frame(top1,bg='#173D4F')
    first_frame.pack(expand=1,fill=BOTH)
    canvas=Canvas(first_frame,bg='#173D4F')
    canvas.pack(side=LEFT,expand=1,fill=BOTH)
    scrollBar_y=Scrollbar(first_frame,orient=VERTICAL,command=canvas.yview)
    scrollBar_y.pack(side=RIGHT,fill=Y)
    canvas.configure(yscrollcommand=scrollBar_y.set)
    canvas.bind('<Configure>',lambda event:canvas.configure(scrollregion=canvas.bbox('all')))
    second_frame=Frame(canvas,bg='#173D4F',padx=160,pady=5)
    canvas.create_window((0,0),anchor='nw',window=second_frame)
    number_of_processes = int(numOfProcesses.get())
    arivalTimeList = list()
    executeTimeList = list()
    indexList = list()
    arivalTime_lb=Label(second_frame, text='Arival time:',font=('calibri', 12),bg='#173D4F',fg='#6FD690')
    arivalTime_lb.grid(row=0,column=1,padx=10,pady=5)
    executeTime_lb=Label(second_frame, text='Execute time:', font=('calibri', 12),bg='#173D4F',fg='#6FD690')
    executeTime_lb.grid(row=0,column=2,padx=10,pady=5)
    for i in range(1, number_of_processes+1):
        arivalTime_en = Entry(second_frame,width=7,bg='#888899')
        arivalTime_en.grid(row=i,column=1,padx=10,pady=5)
        arivalTimeList.append(arivalTime_en)
        executeTime_en = Entry(second_frame,width=7,bg='#888899')
        executeTime_en.grid(row=i,column=2,padx=10,pady=5)
        executeTimeList.append(executeTime_en)
        indexList.append((f'Process {i}'))
    back_btn=Button(second_frame,text='Back',command=lambda event=None:[top0.deiconify(),top1.withdraw()],bg='#888899',fg='#173D4F')
    back_btn.grid(row=i+1,column=1,padx=10,pady=10)
    next_btn = Button(second_frame, text='Next', command=kind_of_algorithms,bg='#888899',fg='#173D4F')
    next_btn.grid(row=i+1,column=2,padx=10,pady=10)
    top1.bind('<Down>', next_entry)
    top1.bind('<Return>', lambda event=None: next_btn.invoke())

def kind_of_algorithms():
    global top2
    top1.withdraw()
    top2 = Toplevel(bg='#173D4F')
    top2.title('Algorithms')
    top2.geometry('300x300')
    keys_lb=Label(top2, text='"Algorithms"',font=('calibri', 15, 'bold'),bg='#173D4F',fg='#6FD690')
    keys_lb.grid(row=1,column=2,rowspan=2,pady=5)
    fcfsButton = Button(top2, text='FCFS', command=fcfs,height=2,width=5,bg='#888899',fg='#173D4F',font=('calibri'))
    fcfsButton.grid(row=3,column=1,pady=5)
    sjfButton = Button(top2, text='SJF', command=sjf,height=2,width=5,bg='#888899',fg='#173D4F',font=('calibri'))
    sjfButton.grid(row=3,column=3,pady=5)
    srtButton = Button(top2, text='SRT', command=srt,height=2,width=5,bg='#888899',fg='#173D4F',font=('calibri'))
    srtButton.grid(row=4,column=2,pady=5)
    rrButton = Button(top2, text='RR', command=quantum_rr,height=2,width=5,bg='#888899',fg='#173D4F',font=('calibri'))
    rrButton.grid(row=5,column=1,padx=35,pady=5)
    mlfqButton = Button(top2, text='MLFQ', command=quantum_mlfq,height=2,width=5,bg='#888899',fg='#173D4F',font=('calibri'))
    mlfqButton.grid(row=5,column=3,pady=5)
    back_btn=Button(top2,text='Back',command=lambda event=None:[top1.deiconify(),top2.withdraw()],bg='#888899',fg='#173D4F')
    back_btn.grid(row=6,column=2,pady=10)
    top2.resizable(width=False, height=False)

def return_value1():
    return[int(arivalTime_en.get()) for arivalTime_en in arivalTimeList]

def return_value2():
    return[int(executeTime_en.get()) for executeTime_en in executeTimeList]

def return_quantum_mlfq():
    return[int(quantum_en.get()) for quantum_en in quantums]

def fcfs():
    top2.withdraw()
    top3 = Toplevel(bg='#173D4F')
    top3.title('Algorithms')
    top3.geometry('600x600')
    df=make_df.make_dataFrame(return_value1(),return_value2(),indexList)
    mainDf,indexArray,completionArray=FCFS.fcfs(df)
    dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes,mainDf)
    df_show=Table(top3, dataframe=dataFrame)
    options={'cellbackgr':'#173D4F','textcolor':'#6FD690','colheadercolor':'#888899','rowselectedcolor':'#888899'}
    pandastable.config.apply_options(options,df_show)
    df_show.show()
    arivalList=return_value1()
    Label(top3, text=f'Average Turn Around Time= {averageTurnAroundTime} and Average Wait Time= {averageWaitTime}', font=('calibri', 12, 'bold'),bg='#173D4F',fg='#6FD690').grid(row=22,column=1,rowspan=5)
    Button(top3,text='Close',command=close,bg='#888899',fg='#173D4F').grid(row=28,column=1)
    GanttChart.gantt_chart(indexList,indexArray,completionArray,min(arivalList))

def sjf():
    top2.withdraw()
    top3 = Toplevel(bg='#173D4F')
    top3.title('Algorithms')
    top3.geometry('600x600')
    df=make_df.make_dataFrame(return_value1(),return_value2(),indexList)
    mainDf,indexArray,completionArray=SJF.sjf(df)
    dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes,mainDf)
    df_show = ScrolledText(top3,bg='#173D4F',fg='#6FD690')
    df_show=Table(top3, dataframe=dataFrame)
    options={'cellbackgr':'#173D4F','textcolor':'#6FD690','colheadercolor':'#888899','rowselectedcolor':'#888899'}
    pandastable.config.apply_options(options,df_show)
    df_show.show()
    arivalList=return_value1()
    Label(top3, text=f'Average Turn Around Time= {averageTurnAroundTime} and Average Wait Time= {averageWaitTime}', font=('calibri', 12, 'bold'),bg='#173D4F',fg='#6FD690').grid(row=22,column=1,rowspan=5)
    Button(top3,text='Close',command=close,bg='#888899',fg='#173D4F').grid(row=28,column=1)
    GanttChart.gantt_chart(indexList,indexArray,completionArray,min(arivalList))

def srt():
    top2.withdraw()
    top3 = Toplevel(bg='#173D4F')
    top3.title('Algorithms')
    top3.geometry('600x600')
    df=make_df.make_dataFrame(return_value1(),return_value2(),indexList)
    mainDf,indexArray,completionArray=SRT.srt(df,indexList)
    dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes,mainDf)
    df_show=Table(top3, dataframe=dataFrame)
    options={'cellbackgr':'#173D4F','textcolor':'#6FD690','colheadercolor':'#888899','rowselectedcolor':'#888899'}
    pandastable.config.apply_options(options,df_show)
    df_show.show()
    arivalList=return_value1()
    Label(top3, text=f'Average Turn Around Time= {averageTurnAroundTime} and Average Wait Time= {averageWaitTime}', font=('calibri', 12, 'bold'),bg='#173D4F',fg='#6FD690').grid(row=22,column=1,rowspan=5)
    Button(top3,text='Close',command=close,bg='#888899',fg='#173D4F').grid(row=28,column=1)
    GanttChart.gantt_chart(indexList,indexArray,completionArray,min(arivalList))

def quantum_rr():
    global top3,quantums
    top2.withdraw()
    top3 = Toplevel(bg='#173D4F')
    top3.title('Algorithms')
    top3.geometry('250x150')
    quantums=StringVar()
    quantum_lb=Label(top3,text='Quantum: ',font=('calibri', 12),bg='#173D4F',fg='#6FD690')
    quantum_lb.grid(row=1,column=1,rowspan=2,padx=5,pady=5)
    quantum_en=Entry(top3,textvariable=quantums,bg='#888899')
    quantum_en.focus_set()
    quantum_en.grid(row=3,column=1,rowspan=2,padx=5,pady=5)
    q_btn=Button(top3,text='Next',command=rr,bg='#888899',fg='#173D4F')
    q_btn.grid(row=5,column=2,padx=5,pady=5)
    top3.bind('<Return>',lambda e:q_btn.invoke())

def rr():
    top3.withdraw()
    top4 = Toplevel(bg='#173D4F')
    top4.title('Algorithms')
    top4.geometry('600x600')
    q=int(quantums.get())
    df=make_df.make_dataFrame(return_value1(),return_value2(),indexList)
    mainDf,indexArray,completionArray=RR.rr(df,q)
    dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes,mainDf)
    df_show=Table(top4, dataframe=dataFrame)
    options={'cellbackgr':'#173D4F','textcolor':'#6FD690','colheadercolor':'#888899','rowselectedcolor':'#888899'}
    pandastable.config.apply_options(options,df_show)
    df_show.show()
    arivalList=return_value1()
    Label(top4, text=f'Average Turn Around Time= {averageTurnAroundTime} and Average Wait Time= {averageWaitTime}', font=('calibri', 12, 'bold'),bg='#173D4F',fg='#6FD690').grid(row=22,column=1,rowspan=5)
    Button(top4,text='Close',command=close,bg='#888899',fg='#173D4F').grid(row=28,column=1)
    GanttChart.gantt_chart(indexList,indexArray,completionArray,min(arivalList))

def quantum_mlfq():
    global top3,quantums,quantum_en
    top2.withdraw()
    top3 = Toplevel(bg='#173D4F')
    top3.title('Algorithms')
    top3.geometry('450x250')
    quantums=[]
    Label(top3,text='This MLFQ Scheduling Has 3 Queues.\n First 2 Queues Algorithms Are RR.\nAnd The Third One Is FCFS.',font=('calibri',12,'bold'),bg='#173D4F',fg='#6FD690').grid(row=1,column=1,rowspan=5,padx=5,pady=5)
    Label(top3, text='Quantum 1:',font=('calibri', 10),bg='#173D4F',fg='#6FD690').grid(row=9,column=1,rowspan=2,padx=2,pady=2)
    Label(top3, text='Quantum 2:',font=('calibri', 10),bg='#173D4F',fg='#6FD690').grid(row=9,column=2,rowspan=2,padx=2,pady=2)
    for i in range(1, 3):
        quantum_en = Entry(top3,bg='#888899')
        quantum_en.grid(row=11,column=i,rowspan=5,padx=2,pady=5)
        quantums.append(quantum_en)
    q_btn=Button(top3,text='Next',command=mlfq,bg='#888899',fg='#173D4F')
    q_btn.grid(row=17,column=3,padx=5,pady=5)
    top3.bind('<Down>', next_entry)
    top3.bind('<Return>', lambda event=None: q_btn.invoke())

def mlfq():
    top3.withdraw()
    top4 = Toplevel(bg='#173D4F')
    top4.title('Algorithms')
    top4.geometry('600x600')
    df1=make_df.make_dataFrame(return_value1(),return_value2(),indexList)
    df2,sortedDf1,completion1,indexArray,completionArray=MLFQ.mlfq(df1,return_value2(),return_quantum_mlfq())
    if len(sortedDf1) != 0:
        df3, sortedDf2, completion2,indexArray,completionArray = MLFQ.fcfs_part1(df2, sortedDf1, completion1,return_quantum_mlfq())
    else:
        dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes, df2)
    if len(sortedDf2) != 0:
        df4,indexArray,completionArray=MLFQ.fcfs_part2(df3, sortedDf2, completion2)
        dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes, df4)
    else:
        dataFrame,averageTurnAroundTime,averageWaitTime=calculate.calculation(number_of_processes, df3)
    df_show=Table(top4, dataframe=dataFrame)
    options={'cellbackgr':'#173D4F','textcolor':'#6FD690','colheadercolor':'#888899','rowselectedcolor':'#888899'}
    pandastable.config.apply_options(options,df_show)
    df_show.show()
    arivalList=return_value1()
    Label(top4, text=f'Average Turn Around Time= {averageTurnAroundTime} and Average Wait Time= {averageWaitTime}', font=('calibri', 12, 'bold'),bg='#173D4F',fg='#6FD690').grid(row=22,column=1,rowspan=5)
    Button(top4,text='Close',command=close,bg='#888899',fg='#173D4F').grid(row=28,column=1)
    GanttChart.gantt_chart(indexList,indexArray,completionArray,min(arivalList))

def close():
    root.destroy()
    GanttChart.close()

main_lb=Label(root,text='This Program Calculates OS Scheduling Algorithms.\nYou Give Arival Times And Execute Times Of The Processes To The Program\nAnd It Returns Averages Of Turn Around Time And Wait Time. ',font=('calibri',12,'bold'),bg='#173D4F',fg='#6FD690')
main_lb.grid(row=1,column=1,rowspan=10,padx=10,pady=5)
start_btn=Button(root,text='Start',command=start,bg='#888899',fg='#173D4F')
start_btn.grid(row=11,column=1,padx=5,pady=20)
root.bind('<Return>',lambda e:start_btn.invoke())
root.mainloop()
