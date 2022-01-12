import pandas as pd
def MassOf_Volatile_and_TSS_InTheSystem(T_1,T_2,SRT_i,SRT_f):
    # for raw and temperature 14 degree celsius
    bHT_T1 = 0.24*(1.029**(T_1-20))
    bHT_T2 = 0.24*(1.029**(T_2-20))
    list_MXv_Raw_14DegreeC=[]
    list_MXt_Raw_14DegreeC=[]
    list_MXv_Raw_22DegreeC=[]
    list_MXt_Raw_22DegreeC=[]
    list_MXv_Settled_14DegreeC=[]
    list_MXt_Settled_14DegreeC=[]
    list_MXv_Settled_22DegreeC=[]
    list_MXt_Settled_22DegreeC=[]
    Days=["Day "+str(i) for i in range(SRT_i,SRT_f+1)]
    for SRT in range(SRT_i,SRT_f+1):
        # for raw waste water at temperature 14 degree celsius
        MXv_Raw_14DegreeC = 8755*((0.45*SRT)/(1+bHT_T1*SRT))*(1+(0.2*bHT_T1*SRT)) + (1140*SRT)
        MXt_Raw_14DegreeC = MXv_Raw_14DegreeC/0.75
        list_MXv_Raw_14DegreeC.append(round(MXv_Raw_14DegreeC,2))
        list_MXt_Raw_14DegreeC.append(round(MXt_Raw_14DegreeC,2))
        # for raw waste water at temperature 22 degree celsius
        MXv_Raw_22DegreeC = 8755*((0.45*SRT)/(1+bHT_T2*SRT))*(1+(0.2*bHT_T2*SRT)) + (1140*SRT)
        MXt_Raw_22DegreeC = MXv_Raw_22DegreeC/0.75
        list_MXv_Raw_22DegreeC.append(round(MXv_Raw_22DegreeC,2))
        list_MXt_Raw_22DegreeC.append(round(MXt_Raw_22DegreeC,2))
        # for settled waste water at temperature 14 degree celsius
        MXv_Settled_14DegreeC = 5690*((0.45*SRT)/(1+bHT_T1*SRT))*(1+(0.2*bHT_T1*SRT)) + (182.4*SRT)
        MXt_Settled_14DegreeC = MXv_Settled_14DegreeC/0.83
        list_MXv_Settled_14DegreeC.append(round(MXv_Settled_14DegreeC,2))
        list_MXt_Settled_14DegreeC.append(round(MXt_Settled_14DegreeC,2))
        # for settled waste water at temperature 22 degree celsius
        MXv_Settled_22DegreeC = 5690*((0.45*SRT)/(1+bHT_T2*SRT))*(1+(0.2*bHT_T2*SRT)) + (182.4*SRT)
        MXt_Settled_22DegreeC = MXv_Settled_22DegreeC/0.83
        list_MXv_Settled_22DegreeC.append(round(MXv_Settled_22DegreeC,2))
        list_MXt_Settled_22DegreeC.append(round(MXt_Settled_22DegreeC,2))
    
    data = {'MXv_Raw_14':list_MXv_Raw_14DegreeC,'MXt_Raw_14':list_MXt_Raw_14DegreeC,
            'MXv_Raw_22':list_MXv_Raw_22DegreeC,'MXt_Raw_22':list_MXt_Raw_22DegreeC,
            'MXv_Settled_14':list_MXv_Settled_14DegreeC,'MXt_Settled_14':list_MXt_Settled_14DegreeC,
            'MXv_Settled_22':list_MXv_Settled_22DegreeC,'MXt_Settled_22':list_MXt_Settled_22DegreeC,
            'Day':Days}
    df=pd.DataFrame(data)
    df.set_index('Day',inplace=True)
    return df
def graph(T_1,T_2,SRT_i,SRT_f):
    #%matplotlib inline 
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.style.use(['ggplot'])
    MassOf_Volatile_and_TSS_InTheSystem(T_1,T_2,SRT_i,SRT_f).plot(kind='line',legend=None)
    plt.text(15, 80000, 'Raw Sewage')
    plt.text(15, 10000, 'Settled Sewage')
    plt.text(23, 90000, 'MXt')
    plt.text(23, 55000, 'MXv')
    plt.text(23, 35000, 'MXt')
    plt.text(23, 20000, 'MXv')
    plt.text(9,55000,'14 $^\circ$C')
    plt.text(15,57000,'22 $^\circ$C')
    plt.ylabel('Sludge mass in the reactor (kg)')
    plt.xlabel('Sludge age (d)')
