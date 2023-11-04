import math
import matplotlib.pyplot as plt
import numpy as np
from array import *
from astropy.coordinates import *
import astropy.units as u
from random import *
from tkinter import *

def graph_from_clusters(clusters_xyz,name,test,t):
    col_map=[]
    title=name +'''
    ''' ' α=' + str(test[0])+ ' μα*=' + str(test[1])+ ' δ=' + str(test[2])+ ' μδ=' + str(test[3])+ ' π=' + str(test[4])+ ' vr=' + str(test[5])+ ' t=' + str(t)
    

    
    legend= Tk()
    Label(text='Legend',width=20,height=3,font='Helvetica 15 bold').pack()
    
    Label(text='Orbits',height=2,font='Helvetica 13 bold').pack()
    Label(text='• Main orbit',fg='red').pack()
    Label(text='• Minimum orbit',fg='green').pack()
    Label(text='• Maximum orbit',fg='blue').pack()
    Label(text='• Test orbit',fg='black').pack()
    
    Label(text='Clusters',height=2,font='Helvetica 13 bold').pack()
    for i in range(len(clusters_xyz)): 
        name=clusters_xyz[i][0]
        col_map.append('#%06X' % randint(0, 0xFFFFFF))
        Label(text=name,fg=col_map[i],bg='#000000').pack()
    Label(text='\n').pack()
    
    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    plt.title(title)
    ax.set_xlabel('X(pc)')
    ax.set_ylabel('Y(pc)')
    ax.set_zlabel('Z(pc)')

    sun=ax.scatter(0,0,0,s=20,label='Sun',color='0')
    # ax.scatter(8e3,0,0,s=50,label='Galaxy Center',color='0')
    # ax.quiver(0,0,0,0,0,5e3)
    # ax.quiver(0,0,0,0,5e3,0)
    # ax.quiver(0,0,0,5e3,0,0)
    
    for num in range(len(clusters_xyz)): #l,b,par,diameter
        name=clusters_xyz[num][0]
        x=clusters_xyz[num][1]
        y=clusters_xyz[num][2]
        z=clusters_xyz[num][3]
        
        radius=(clusters_xyz[num][4])
        
        w = np.linspace(0, 2 * np.pi, 10)
        v = np.linspace(0,np.pi, 10)
        xs = radius * np.outer(np.cos(w), np.sin(v)) +x
        ys = radius * np.outer(np.sin(w), np.sin(v)) +y
        zs = radius * np.outer(np.ones(np.size(w)), np.cos(v)) +z
        ax.plot_surface(xs, ys, zs,color=col_map[num],alpha=0.4,label=name)     
            
    ax.set_aspect('equal')
    # plt.show()
    return ax
    
def orbits(pos,pos_min,pos_max,pos_test,ax):
    grade=np.linspace (0,1,len(pos[0]))
    r_grade=[]
    g_grade=[]
    b_grade=[]
    black_grade=[]
    
    for i in range(len(grade)):
        r_grade.append([grade[i],0,0])
        g_grade.append([0,grade[i],0])
        b_grade.append([0,0,grade[i]])
        black_grade.append([str(grade[i])])

    
    ax.scatter(pos[0],pos[1],pos[2],s=1,color=(r_grade))  #red mean
    ax.scatter(pos_min[0],pos_min[1],pos_min[2],s=1,color=(g_grade)) #green min
    ax.scatter(pos_max[0],pos_max[1],pos_max[2],s=1,color=(b_grade)) #blue max
    ax.scatter(pos_test[0],pos_test[1],pos_test[2],s=1,color=black_grade[-i]) #black test
    
    ax.set_aspect('equal')
    plt.show()
    return ax


