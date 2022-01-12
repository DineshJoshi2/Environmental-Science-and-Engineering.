import pandas as pd
def ActiveFractionOfSludge_WRT_VSS_TSS(T_1,T_2,SRT_i,SRT_f):
    bHT_T1 = 0.24*(1.029**(T_1-20))
    bHT_T2 = 0.24*(1.029**(T_2-20))
    list_Fav_Raw_14DegreeC=[]
    list_Fat_Raw_14DegreeC=[]
    list_Fav_Raw_22DegreeC=[]
    list_Fat_Raw_22DegreeC=[]
    list_Fav_Settled_14DegreeC=[]
    list_Fat_Settled_14DegreeC=[]
    list_Fav_Settled_22DegreeC=[]
    list_Fat_Settled_22DegreeC=[]
    Days=["Day "+str(i) for i in range(SRT_i,SRT_f+1)]
    for SRT in range(SRT_i,SRT_f+1):
        # for raw waste water at temperature 14 degree celsius
        Fav_Raw_14DegreeC = 1/(1+(0.2*bHT_T1*SRT)+(0.289*(1+(bHT_T1*SRT))))
        Fat_Raw_14DegreeC = Fav_Raw_14DegreeC*0.75
        list_Fav_Raw_14DegreeC.append(round(Fav_Raw_14DegreeC,4))
        list_Fat_Raw_14DegreeC.append(round(Fat_Raw_14DegreeC,4))
        # for raw waste water at temperature 22 degree celsius
        Fav_Raw_22DegreeC = 1/(1+(0.2*bHT_T2*SRT)+(0.289*(1+(bHT_T2*SRT))))
        Fat_Raw_22DegreeC = Fav_Raw_22DegreeC*0.75
        list_Fav_Raw_22DegreeC.append(round(Fav_Raw_22DegreeC,4))
        list_Fat_Raw_22DegreeC.append(round(Fat_Raw_22DegreeC,4))
        # for settled waste water at temperature 14 degree celsius
        Fav_Settled_14DegreeC = 1/(1+(0.2*bHT_T1*SRT)+(0.142*(1+(bHT_T1*SRT))))
        Fat_Settled_14DegreeC = Fav_Settled_14DegreeC*0.83
        list_Fav_Settled_14DegreeC.append(round(Fav_Settled_14DegreeC,4))
        list_Fat_Settled_14DegreeC.append(round(Fat_Settled_14DegreeC,4))
        # for settled waste water at temperature 22 degree celsius
        Fav_Settled_22DegreeC = 1/(1+(0.2*bHT_T2*SRT)+(0.142*(1+(bHT_T2*SRT))))
        Fat_Settled_22DegreeC = Fav_Settled_22DegreeC*0.83
        list_Fav_Settled_22DegreeC.append(round(Fav_Settled_22DegreeC,4))
        list_Fat_Settled_22DegreeC.append(round(Fat_Settled_22DegreeC,4))
    data = {'Fav_Raw_14':list_Fav_Raw_14DegreeC,'Fat_Raw_14':list_Fat_Raw_14DegreeC,
            'Fav_Raw_22':list_Fav_Raw_22DegreeC,'Fat_Raw_22':list_Fat_Raw_22DegreeC,
            'Fav_Settled_14':list_Fav_Settled_14DegreeC,'Fat_Settled_14':list_Fat_Settled_14DegreeC,
            'Fav_Settled_22':list_Fav_Settled_22DegreeC,'Fat_Settled_22':list_Fat_Settled_22DegreeC,
            'Day':Days}
    df= pd.DataFrame(data)
    df.set_index('Day',inplace=True)
    return df

def graph(T_1,T_2,SRT_i,SRT_f):
    #%matplotlib inline 
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    mpl.style.use(['ggplot'])
    ActiveFractionOfSludge_WRT_VSS_TSS(T_1,T_2,SRT_i,SRT_f).iloc[:,[1,3,5,7]].plot(kind='line',legend=None)
    plt.text(3, 0.2, 'Raw Sewage')
    plt.text(3, 0.6, 'Settled Sewage')
    plt.text(12,0.4 , '$F_{at}$')
    plt.text(12, 0.2, '$F_{at}$')
    #plt.text(23, 35000, 'MXt')
    #plt.text(23, 20000, 'MXv')
    #plt.text(9,55000,'14 $^\circ$C')
    #plt.text(15,57000,'22 $^\circ$C')
    plt.ylabel('Active fraction wrt VSS ($f_{av}$)')
    plt.xlabel('Sludge age (d)')
