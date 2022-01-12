import pandas as pd
def MassOf_TSS_VSS_SludgeWasted(T_1,T_2,SRT_i,SRT_f):
    bHT_T1 = 0.24*(1.029**(T_1-20))
    bHT_T2 = 0.24*(1.029**(T_2-20))
    fi_raw= 0.75
    fi_settled = 0.83
    list_FXv_Raw_14DegreeC=[]
    list_FXt_Raw_14DegreeC=[]
    list_FXv_Raw_22DegreeC=[]
    list_FXt_Raw_22DegreeC=[]
    list_FXv_Settled_14DegreeC=[]
    list_FXt_Settled_14DegreeC=[]
    list_FXv_Settled_22DegreeC=[]
    list_FXt_Settled_22DegreeC=[]
    Days=["Day "+str(i) for i in range(SRT_i,SRT_f+1)]
    for SRT in range(SRT_i,SRT_f+1):
        # for raw waste water at temperature 14 degree celsius
        FXt_Raw_14DegreeC = (8775/0.75)*(0.45/(1+bHT_T1*SRT))*(1+(0.2*bHT_T1*SRT))+(1140/0.75)
        FXv_Raw_14DegreeC = FXt_Raw_14DegreeC*fi_raw
        list_FXv_Raw_14DegreeC.append(round(FXv_Raw_14DegreeC,4))
        list_FXt_Raw_14DegreeC.append(round(FXt_Raw_14DegreeC,4))
        # for raw waste water at temperature 22 degree celsius
        FXt_Raw_22DegreeC = (8775/0.75)*(0.45/(1+bHT_T2*SRT))*(1+(0.2*bHT_T2*SRT))+(1140/0.75)
        FXv_Raw_22DegreeC = FXt_Raw_22DegreeC*fi_raw
        list_FXv_Raw_22DegreeC.append(round(FXv_Raw_22DegreeC,4))
        list_FXt_Raw_22DegreeC.append(round(FXt_Raw_22DegreeC,4))
        # for settled waste water at temperature 14 degree celsius
        FXt_Settled_14DegreeC = (5690/0.83)*(0.45/(1+bHT_T1*SRT))*(1+(0.2*bHT_T1*SRT))+(142.8/0.83)
        FXv_Settled_14DegreeC = FXt_Settled_14DegreeC*fi_settled
        list_FXv_Settled_14DegreeC.append(round(FXv_Settled_14DegreeC,4))
        list_FXt_Settled_14DegreeC.append(round(FXt_Settled_14DegreeC,4))
        # for settled waste water at temperature 22 degree celsius
        FXt_Settled_22DegreeC = (5690/0.83)*(0.45/(1+bHT_T2*SRT))*(1+(0.2*bHT_T2*SRT))+(142.8/0.83)
        FXv_Settled_22DegreeC = FXt_Settled_22DegreeC*fi_settled
        list_FXv_Settled_22DegreeC.append(round(FXv_Settled_22DegreeC,4))
        list_FXt_Settled_22DegreeC.append(round(FXt_Settled_22DegreeC,4))
    
    data = {'FXv_Raw_14':list_FXv_Raw_14DegreeC,'FXt_Raw_14':list_FXt_Raw_14DegreeC,
            'FXv_Raw_22':list_FXv_Raw_22DegreeC,'FXt_Raw_22':list_FXt_Raw_22DegreeC,
            'FXv_Settled_14':list_FXv_Settled_14DegreeC,'FXt_Settled_14':list_FXt_Settled_14DegreeC,
            'FXv_Settled_22':list_FXv_Settled_22DegreeC,'FXt_Settled_22':list_FXt_Settled_22DegreeC,
            'Day':Days}
    df=pd.DataFrame(data)
    df.set_index('Day',inplace=True)
    return df

def graph(T_1,T_2,SRT_i,SRT_f):
    #%matplotlib inline 
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.style.use(['ggplot'])
    MassOf_TSS_VSS_SludgeWasted(T_1,T_2,SRT_i,SRT_f).iloc[:,[1,3,5,7]].plot(kind='line',legend=None)
    plt.text(3.5, 4500, 'mass of TSS sludge wasted per day for raw waste water ')
    plt.text(2.2, 2000, 'mass of TSS sludge wasted per day for settled waste water')
    #plt.text(12,0.4 , '$F_{at}$')
    #plt.text(12, 0.2, '$F_{at}$')
    #plt.text(23, 35000, 'MXt')
    #plt.text(23, 20000, 'MXv')
    #plt.text(9,55000,'14 $^\circ$C')
    #plt.text(15,57000,'22 $^\circ$C')
    plt.ylabel('Waste sludge (kgTSS/d)')
    plt.xlabel('Sludge age (d)')