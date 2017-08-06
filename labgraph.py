from numpy import *
from matplotlib.pyplot import *
from scipy.optimize import curve_fit
import urllib2
import struct
import scipy.integrate as integ
from astropy.io import ascii
import scipy.fftpack as fft
import scipy.misc as misc


def ivg(filename,lab,url='none',point='none'):
    try:
        data=ascii.read(filename)
    except:
        if url=='none':
            print 'requires url'
        else:
            print('Downloading file')
            urlptr=urllib2.urlopen(url)
            rawdata=urlptr.read()
            urlptr.close()
            fp=open(filename,'w')
            fp.write(rawdata)
            fp.close()
            data=ascii.read(filename)

#standard graph    
    if point=='none':
        figure()
        plot(data['col1'],data['col2'])
        yscale('log')
        xlabel('Voltage')
        ylabel('Current')
        title(lab)
#formats graph to change color and type of plot                                 
    else:
        figure()
        plot(data['col1'],data['col2'],point)
        yscale('log')
        xlabel('Voltage')
        ylabel('Current')
        title(lab)


def f(x):
    return 1/(x**2)


def cvg(filename,lab,url='none',point='none'):
#trys to open the file if it doesn't exhist then it will download the file    
    try:
        data=ascii.read(filename)
    except:
        if url=='none':
            print 'requires url'
        else:
            print('Downloading file')
            urlptr=urllib2.urlopen(url)
            rawdata=urlptr.read()
            urlptr.close()
            fp=open(filename,'w')
            fp.write(rawdata)
            fp.close()
            data=ascii.read(filename)
#standard graph
    if point=='none':
        figure()
        plot(data['col1'],data['col2'])
        yscale('log')
        xlabel('Voltage')
        ylabel('Capacitance [pf]')
        title(lab)
        b=1/((data['col2'])**2)
#1/c^2 graph
        figure()
        plot(data['col1'],b)
        yscale('log')
        xlabel('Voltage')
        ylabel('1/$c^2$ [pf]')
        title(lab)
        v=array(data['col1'])
        c2=array(1/data['col2']**2)
#derivative
        r2d2=[]
        for n in range(50):
            z=(c2[n+1]-c2[n])/(v[n+1]-v[n])
            r2d2.append(z)
        q=array(r2d2)
        c=array(data['col2'])
#area divided by capacitance        
        x=(c/1.82)
        y=1/q*(2/1.6e-7*(1.82**2))
        figure()
        plot(x[:-1],y)
        yscale('log')
        xlabel('Depth')
        ylabel('Doping density')
        title(lab)
#formats graph to change color and type of plot
    else:
        figure()
        plot(data['col1'],data['col2'],point)
        yscale('log')
        xlabel('Voltage')
        ylabel('Capacitance [pf]')
        title(lab)
        b=1/((data['col2'])**2)
#1/c^2 graph                                                                      
        figure()
        plot(data['col1'],b,point)
        yscale('log')
        xlabel('Voltage')
        ylabel('1/$c^2$ [pf]')
        title(lab)
        v=array(data['col1'])
        c2=array(1/data['col2']**2)
#derivative                                                                       
        r2d2=[]
        for n in range(50):
            z=(c2[n+1]-c2[n])/(v[n+1]-v[n])
            r2d2.append(z)
        q=array(r2d2)
        c=array(data['col2'])
#Area divided by capacitance
        x=(c/1.82)
        y=1/q*(2/1.6e-7*(1.82**2))
#plot depletion depth     
        figure()
        plot(x[:-1],y,point)
        yscale('log')
        xlabel('Depth')
        ylabel('Doping density')
        title(lab)
