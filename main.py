import os #to work in any folder
import sys
sys.path.insert(0,"function_files")

from calculations import *
from graph import *
from save_prints import *

##############################################################################################
##############################################################################################

star=[,,,,,,,,,,]
#name,ra,μra*[mas/yr],μra* error,dec,μdec[mas/yr],μdec error,parallax,parallax error,Vr,t
test=[,,,,,]
#ra,μra*[mas/yr],dec,μdec[mas/yr],parallax,Vr

save_results=

step=
#associated clusters
threshold= #THRESHOLD None to show all
catalogue=  #If True Use catalogue and bypasses the table
clusters=[[,,,,,,,], #[name,l,b,par,diameter,U,V,W in km/s],[...]
          [,,,,,,,],
          ]

##############################################################################################
##############################################################################################
name=star[0]
a=star[1] 
Va=star[2] 
erVa=star[3]
Vamin=Va-erVa
Vamax=Va+erVa
d=star[4]
Vd=star[5] 
erVd=star[6]
Vdmin=Vd-erVd
Vdmax=Vd+erVd
par=star[7] 
erpar=star[8]
parmin=par-erpar
parmax=par+erpar
Vr=star[9]
t=int(star[10]) 
# t_test=int(test[6])

#Orbits Calculations
pos=kinematics(a,Va,d,Vd,par,Vr,t,step)
pos_min=kinematics(a,Vamin,d,Vdmin,parmin,Vr,t,step)
pos_max=kinematics(a,Vamax,d,Vdmax,parmax,Vr,t,step)
pos_test=kinematics(test[0],test[1],test[2],test[3],test[4],test[5],t,step)

#Cluster Calculations
clusters_xyz=cartesian_cluster(catalogue,clusters,t,threshold,pos,pos_min,pos_max,pos_test)

results_print(star,test,clusters_xyz)

#saves\\\\\ Every save is an overight
if save_results==True:
    xl_save(name,pos,pos_min,pos_max,pos_test,clusters_xyz,t,test,step)

#graphs

ax=graph_from_clusters(clusters_xyz,name,test,t)
orbits(pos,pos_min,pos_max,pos_test,ax)



