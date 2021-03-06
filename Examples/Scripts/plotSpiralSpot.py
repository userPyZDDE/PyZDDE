#-------------------------------------------------------------------------------
# Name:      plotSpiralSpot.py
# Purpose:   Example of using the "spiral spot" covenience function of pyZDDE.
#
# NOTE:      Please note that this code uses matplotlib plotting library from
#            http://matplotlib.org/ for 2D-plotting
#
# Copyright: (c) 2012- 2014
# Licence:   MIT License
#-------------------------------------------------------------------------------
from __future__ import print_function
import sys, os
import traceback
import matplotlib.pyplot as plt

# *********** Add PyZDDE to the python search path ***********************
cd = os.path.dirname(os.path.realpath(__file__))
ind = cd.find('Examples')
cd = cd[0:ind-1]
##
if cd not in sys.path:
    sys.path.append(cd)
# ************************************************************************
import pyzdde.zdde as pyzdde

# The ZEMAX file path
zmxfp = cd+'\\ZMXFILES\\'
zmxfile = 'Cooke 40 degree field.zmx'
filename = zmxfp+zmxfile

# Create a PyZDDE object
link0 = pyzdde.PyZDDE()

try:
    # Initiate the DDE link
    status = link0.zDDEInit()
    if ~status:
        # Load a lens file into the ZEMAX DDE server
        ret = link0.zLoadFile(filename)
        if ~ret:
            hx = 0.0
            hy = 0.4
            spirals = 10 #100
            rays = 600 #6000
            (xb,yb,zb,intensityb) = link0.zSpiralSpot(hx,hy,1,spirals,rays)
            (xg,yg,zg,intensityg) = link0.zSpiralSpot(hx,hy,2,spirals,rays)
            (xr,yr,zr,intensityr) = link0.zSpiralSpot(hx,hy,3,spirals,rays)
            fig = plt.figure(facecolor='w')
            ax = fig.add_subplot(111)
            ax.set_aspect('equal')
            ax.scatter(xr,yr,s=5,c='red',linewidth=0.35,zorder=20)
            ax.scatter(xg,yg,s=5,c='lime',linewidth=0.35,zorder=21)
            ax.scatter(xb,yb,s=5,c='blue',linewidth=0.35,zorder=22)
            ax.set_xlabel('x');ax.set_ylabel('y')
            fig.suptitle('Spiral Spot')
            ax.grid(color='lightgray', linestyle='-', linewidth=1)
            ax.ticklabel_format(scilimits=(-2,2))
            plt.show()
        else:
            print("Could not load lens file.")
    else:
        print("DDE link could not be established.")
except Exception, err:
    traceback.print_exc()
finally:
    # close the DDE channel
    link0.zDDEClose()