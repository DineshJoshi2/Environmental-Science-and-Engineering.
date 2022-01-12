import pandas as pd
def AverageDailyCarbonaceousOxygenDemand(T_1,T_2,SRT_i,SRT_f):
    bHT_T1 = 0.24*(1.029**(T_1-20))
    bHT_T2 = 0.24*(1.029**(T_2-20))
    fi_raw= 0.75
    fi_settled = 0.83
    list_FOc_Raw_14DegreeC=[]
    list_FOc_Raw_22DegreeC=[]
    list_FOc_Settled_14DegreeC=[]
    list_FOc_Settled_22DegreeC=[]
    Days=["Day "+str(i) for i in range(SRT_i,SRT_f+1)]
    for SRT in range(SRT_i,SRT_f+1):
        # for raw waste water at temperature 14 degree celsius
        FOc_Raw_14DegreeC = 8775*(0.334+0.533*((bHT_T1*SRT)/(1+bHT_T1*SRT)))
        list_FOc_Raw_14DegreeC.append(round(FOc_Raw_14DegreeC,4))
        # for raw waste water at temperature 22 degree celsius
        FOc_Raw_22DegreeC = 8775*(0.334+0.533*((bHT_T2*SRT)/(1+bHT_T2*SRT)))
        list_FOc_Raw_22DegreeC.append(round(FOc_Raw_22DegreeC,4))
        # for settled waste water at temperature 14 degree celsius
        FOc_Settled_14DegreeC = 5690*(0.334+0.533*((bHT_T1*SRT)/(1+bHT_T1*SRT)))
        list_FOc_Settled_14DegreeC.append(round(FOc_Settled_14DegreeC,4))
        # for settled waste water at temperature 22 degree celsius
        FOc_Settled_22DegreeC = 5690*(0.334+0.533*((bHT_T2*SRT)/(1+bHT_T2*SRT)))
        list_FOc_Settled_22DegreeC.append(round(FOc_Settled_22DegreeC,4))
    
    data = {'FOc_Raw_14':list_FOc_Raw_14DegreeC,
            'FOc_Raw_22':list_FOc_Raw_22DegreeC,
            'FOc_Settled_14':list_FOc_Settled_14DegreeC,
            'FOc_Settled_22':list_FOc_Settled_22DegreeC,
            'Day':Days}
    df=pd.DataFrame(data)
    df.set_index('Day',inplace=True)
    return df
def graph(T_1,T_2,SRT_i,SRT_f):
    #%matplotlib inline 
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.style.use(['ggplot'])
    AverageDailyCarbonaceousOxygenDemand(T_1,T_2,SRT_i,SRT_f).plot(kind='line',legend=None)
    plt.text(2, 5000, ' Avg daily carbonaceous oxygen demand (raw waste water) ')
    plt.text(1, 3000, 'Avg daily carbonaceous oxygen demand (settled waste water)')
    #plt.text(12,0.4 , '$F_{at}$')
    #plt.text(12, 0.2, '$F_{at}$')
    #plt.text(23, 35000, 'MXt')
    #plt.text(23, 20000, 'MXv')
    #plt.text(9,55000,'14 $^\circ$C')
    #plt.text(15,57000,'22 $^\circ$C')
    plt.ylabel('Average daily COD (FOc, kgO2/d),')
    plt.xlabel('Sludge age (d)')