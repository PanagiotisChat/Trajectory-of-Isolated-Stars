import math
import numpy as np
from save_prints import *

from astropy.coordinates import *
import astropy.units as u

def kinematics(a,Va,d,Vd,par,Vr,t,step):
    step=int(t/step)
    dis=(1000/par)*u.pc #distance in parsec
    c = SkyCoord(distance=dis,ra=a*u.deg, dec=d*u.deg, pm_ra_cosdec=Va*u.mas/u.yr, pm_dec=Vd*u.mas/u.yr, radial_velocity=Vr*u.km/u.s,).galactic

    dis=dis.value
    x0=c.cartesian.x.value
    y0=c.cartesian.y.value
    z0=c.cartesian.z.value
    Vx=(c.velocity.d_x).to(u.pc/u.yr).value
    Vy=(c.velocity.d_y).to(u.pc/u.yr).value
    Vz=(c.velocity.d_z).to(u.pc/u.yr).value
    Vr=(Vr*u.km/u.s).to(u.pc/u.yr).value

    xt=[]
    yt=[]
    zt=[]
    distt=[]

    for ti in range(0,t,step):
        xt.append(x0-Vx*ti)
        yt.append(y0-Vy*ti)
        zt.append(z0-Vz*ti)
        distt.append(dis-Vr*ti)
        
        # if (dis-Vr*ti)<0:
        #     print("#################")
        #     print('Error for time: ',ti)
        #     print("#################")
        #     exit()
        #     # dist.pop()
        #     # dist.append(np.abs(dis-Vr*ti))
    results=[xt,yt,zt,distt]
    return results


def cartesian_cluster(catalogue,clusters,t,threshold,pos,pos_min,pos_max,pos_test): 

    if catalogue==False:
        j=0
    else:
        j=1
        clusters=from_catalogue()

    clusters_xyz=[]
    
    for num in range(len(clusters)): #l,b,par,diameter
        name=clusters[num][0+j]
        dis=1000/clusters[num][3+j]
        radius=(clusters[num][4+j])/2
        
        gal_cor=Galactic(l=clusters[num][1+j]*u.degree, b=clusters[num][2+j]*u.degree,distance=dis*u.pc).cartesian
        x=gal_cor.x.value
        y=gal_cor.y.value
        z=gal_cor.z.value
        
        vx=clusters[num][5+j]
        vx=((vx*(u.km/u.s)).to(u.pc/u.yr)).value
        vy=clusters[num][6+j]
        vy=((vy*(u.km/u.s)).to(u.pc/u.yr)).value
        vz=clusters[num][7+j]
        vz=((vz*(u.km/u.s)).to(u.pc/u.yr)).value
        
        x=x+vx*t
        y=y+vy*t
        z=z+vz*t
        
        clusters_xyz.append([name,x,y,z,radius])
        
    distance_table=[] 
    for i in range (len(clusters_xyz)):
        clust=clusters_xyz[i][0]
        radius=clusters_xyz[i][4]
        
        dx=clusters_xyz[i][1]-pos[0][-1]
        dx_min=clusters_xyz[i][1]-pos_min[0][-1]
        dx_max=clusters_xyz[i][1]-pos_max[0][-1]
        dx_test=clusters_xyz[i][1]-pos_test[0][-1]
        
        dy=clusters_xyz[i][2]-pos[1][-1]
        dy_min=clusters_xyz[i][2]-pos_min[1][-1]
        dy_max=clusters_xyz[i][2]-pos_max[1][-1]
        dy_test=clusters_xyz[i][2]-pos_test[1][-1]
        
        dz=clusters_xyz[i][3]-pos[2][-1]
        dz_min=clusters_xyz[i][3]-pos_min[2][-1]
        dz_max=clusters_xyz[i][3]-pos_max[2][-1]
        dz_test=clusters_xyz[i][3]-pos_test[2][-1]
        
        dist=np.sqrt(dx**2+dy**2+dz**2)
        dist_min=np.sqrt(dx_min**2+dy_min**2+dz_min**2)
        dist_max=np.sqrt(dx_max**2+dy_max**2+dz_max**2)
        dist_test=np.sqrt(dx_test**2+dy_test**2+dz_test**2)
        
        if threshold==None:
            distance_table.append([clust,clusters_xyz[i][1],clusters_xyz[i][2],clusters_xyz[i][3],radius,dist,dist_min,dist_max,dist_test])
        else:
            if dist<=threshold or dist_min<=threshold or dist_max<=threshold or dist_test<=threshold :
                distance_table.append([clust,clusters_xyz[i][1],clusters_xyz[i][2],clusters_xyz[i][3],radius,dist,dist_min,dist_max,dist_test]) 
                
    clusters_xyz=distance_table
    return clusters_xyz

