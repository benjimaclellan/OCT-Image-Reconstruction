from scipy.interpolate import spline, interp1d
from scipy.signal import hilbert
from numpy.fft import fft, ifft
from math import pi
import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog




def normalize_image_(im, c1, c2):
    im_norm = im - c1
    im_norm *= 1/c2
    im_norm[np.where(im_norm>1)] = 1
    im_norm[np.where(im_norm<0)] = 0
    
    im = np.uint8(im_norm * 255)
    
    return im

def disp_comp_(self, smat, a):
    dc_col = np.exp( 1j * np.polyval( a, self.w - self.w0 ) )
        
    self.dc = np.tile( dc_col, (smat.shape[0],1) )
    self.dc_smat = np.multiply(smat, self.dc)
    
    return self

def create_smatcomp_(self):
    smat = np.zeros(self.mat.shape, dtype=np.complex128)
    for i_ascan in range(smat.shape[0]):
        f = interp1d( self.w, self.mat[i_ascan,:], kind='cubic' )
        R = hilbert( f( self.ow ) )
        
        smat[i_ascan,:] = R
    self.smat = smat
    return self
    
def create_imatcomp_(self):

    a = [self.dispcomp_a3.get(), \
         self.dispcomp_a2.get(), \
         self.dispcomp_a1.get(), \
         self.dispcomp_a0.get(), \
         0.0, \
         0.0 ]
        
    disp_comp_(self, self.smat, a)
    self.imatcomp = fft( self.dc_smat, axis = 1 )
    
    return self

def create_intensityimage_(self):

    iimage_raw = np.log10( np.abs( self.imatcomp[:,0:1024] ) ).T
    self.iimage = normalize_image_(iimage_raw, \
                                   self.intscale_c1.get(), \
                                   self.intscale_c2.get())

    return self


def create_phaseimage_(self):
    # add functionality
    print("At the moment, the analysis for phase images may not be fully functional. Please contact the developers with any questions.\n")
    
    pimage_raw = np.angle(self.imatcomp[:,0:1024]).T

    pimage_blue = np.array(pimage_raw)
    pimage_blue[np.where(pimage_blue > 0)] = 0
    
    pimage_red = np.array(pimage_raw)
    pimage_red[np.where(pimage_red < 0)] = 0
    
    pimage = np.zeros((pimage_raw.shape[0], pimage_raw.shape[1],3))
    pimage[:,:,0] = np.array(pimage_blue) * (-255/pi)
    pimage[:,:,2] = np.array(pimage_red) * (255/pi)
    
    self.pimage = np.uint8(pimage)
    return
