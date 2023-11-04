import math
import numpy as np
import pandas as pd

def results_print(star,test,clusters_xyz):
    df=pd.DataFrame(clusters_xyz,columns=["Associated Cluster","X (pc)","Y (pc)","Z (pc)","Radius (pc)","Initial Distance(pc)","Initial mValues Distance(pc)","Initial MValues Distance(pc)","Initial Distance from Test Values (pc)"])
    df = df.drop(columns=["X (pc)","Y (pc)","Z (pc)","Initial Distance(pc)","Initial mValues Distance(pc)","Initial MValues Distance(pc)",])
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")
    
    print('Initial Distance from Test Obit:')
    print(df)
    print("--------------------------------------------------------------------")
    print("--------------------------------------------------------------------")

def xl_save(name,pos,pos_min,pos_max,pos_test,clusters_xyz,t,test,step):
    
    name=name+"_a_"+str(test[0])+"_va_"+str(test[1])+"_d_"+str(test[2])+"_vd_"+str(test[3])+"_p_"+str(test[4])+"_vr_"+str(test[5])+"_t_"+str(t)
    
    step=int(t/step)
    t_minus=range(0,t,step)
    t_minus=tuple(elem/1000 for elem in t_minus)
    
    clusters=pd.DataFrame(clusters_xyz,columns=["Associated Cluster","X (pc)","Y (pc)","Z (pc)","Radius (pc)","Initial Distance(pc)","Initial mValues Distance(pc)","Initial MValues Distance(pc)","Initial Test Values Distance(pc)"])
    orbits_main={'t-minus (kyr)':t_minus,'X (pc)':pos[0],'Y (pc)':pos[1],'Z (pc)':pos[2],
                     'Distance (pc)':pos[3]}
    orbits_main=pd.DataFrame(orbits_main)
    orbits_min={'t-minus (kyr)':t_minus,'X (pc)':pos_min[0],'Y (pc)':pos_min[1],'Z (pc)':pos_min[2],
                     'Distance (pc)':pos_min[3]}
    orbits_min=pd.DataFrame(orbits_min)
    orbits_max={'t-minus (kyr)':t_minus,'X (pc)':pos_max[0],'Y (pc)':pos_max[1],'Z (pc)':pos_max[2],
                     'Distance (pc)':pos_max[3]}
    orbits_max=pd.DataFrame(orbits_max)
    
    with pd.ExcelWriter("results/"+name+".xlsx") as writer:
        clusters.to_excel(writer, sheet_name="Asociated Cluster", index=False)
        orbits_main.to_excel(writer, sheet_name="Main Orbit", index=False)
        orbits_min.to_excel(writer, sheet_name="Minimum Values Orbit", index=False)
        orbits_max.to_excel(writer, sheet_name="Maximum Values Orbit", index=False)
    print('Saved as : '+ name)
               
def from_catalogue():
    clusters = pd.read_excel('clusters catalogue.xlsx')
    clusters=clusters.values.tolist()  
    return clusters


