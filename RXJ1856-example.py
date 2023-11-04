import os #to work in any folder
import sys
sys.path.insert(0,"function_files")

from calculations import *
from graph import *
from save_prints import *

##############################################################################################
##############################################################################################

star=['RXJ1856',284.15,326.7,0.8,-37.91,-59.1,0.7,5.41,0.6,193,3.1e5]
#name,ra,μra*[mas/yr],μra* error,dec,μdec[mas/yr],μdec error,parallax,parallax error,Vr,t
test=[284.15,326.7,-37.91,-59.1,5.41,210]
#ra,μra*[mas/yr],dec,μdec[mas/yr],parallax,Vr

save_results=True

step=50
#associated clusters
threshold=100 #THRESHOLD None to show all
catalogue=True  #If True Use catalogue and bypasses the table
clusters=[['US',351.07,19.43,6.65,30,-6.7,-16.0,-8.0], #[name,l,b,par,diameter,U,V,W in km/s],[...]
          ['B Bip Cap',330.95,-55.54,54.97,113,-10.8,-15.9,-9.8],
          ['Ext. R CrA',359.41,-17.19,9.85,62,-0.1,-14.8,-10.1],
          ['AB Dor',146.31,-59.00,71.43,85,-7.4,-27.4,-12.69],
          ['Sco OB4',352.40,3.44,0.91,65,3.9,-8.5,-8.5]]

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



