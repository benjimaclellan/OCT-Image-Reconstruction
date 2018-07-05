from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import csv
import numpy as np
from math import pi
import imageio


from image_funcs import *


class OCT_GUI:
    ## Main layout definition of GUI and binding to callbacks, which give funcitonality
    def __init__(self, master):
        ## Title of the GUI, displayed in the top left corner
        master.title("OCT Image Reconstruction")

        ## Define Frame for all user interaction
        gen_frame = LabelFrame(master)
        gen_frame.grid( row=0,column=0 )

        ## Define Frame for choosing files
        file_frame = LabelFrame(gen_frame, text="File")
        file_frame.grid()

        ## Add Buttons for basic interactions - save, update and choose file
        update_im = Button(file_frame, text="Update Image", command=self._update_im )
        update_im.grid(row=0, column=0, sticky=W+E) 
        
        choose_im = Button( file_frame, text="Choose Image", command=self._choose_im )
        choose_im.grid(row=1, column=0, sticky=W+E)  
        
        save_ims = Button( file_frame, text="Save Images", command=self._save_images)
        save_ims.grid(row=2, column=0, sticky=W+E) 

        self.saveall_ims = IntVar()
        saveall_ims = Checkbutton(file_frame, \
                                  text="Process All Files in Current Folder?",\
                                  onvalue = 1, offvalue = 0, \
                                  variable = self.saveall_ims)
        saveall_ims.grid(row=3, column=0, sticky=W+E) 

        ## Define Frame for preview settings
        image_settings = LabelFrame(gen_frame, text="Preview Settings")
        image_settings.grid(row=3, column=0, sticky = W+E)
        
        
        self.imdisp_type = StringVar()
        self.imdisp_type.set("Intensity") # default value
        disp_im = OptionMenu(image_settings, self.imdisp_type, "Intensity", "Phase", command=self._change_disptype)
        disp_im.grid()


        ## --- Image Display Frame
        image_frame = LabelFrame(master)
        image_frame.grid( row=0, column=1 )

        
        self.image_canvas = Canvas(image_frame)
        self.image_canvas.pack(fill="both", expand=True)   

        
        ## --- Dispersion Compensation
        dispcomp_frame = LabelFrame(gen_frame,text="Dispersion Control")
        dispcomp_frame.grid(sticky=W+E)
        
        self.dispcomp_a0 = DoubleVar()
        self.dispcomp_a1 = DoubleVar()
        self.dispcomp_a2 = DoubleVar()
        self.dispcomp_a3 = DoubleVar()
                
        dispcomp_a0 = Scale(dispcomp_frame, from_=-1000, to=1000, \
                                 variable = self.dispcomp_a0 )
        dispcomp_a1 = Scale(dispcomp_frame, from_=-1000, to=1000, \
                            variable = self.dispcomp_a1 )
        dispcomp_a2 = Scale(dispcomp_frame, from_=-1000, to=1000, \
                            variable = self.dispcomp_a2)
        dispcomp_a3 = Scale(dispcomp_frame, from_=-1000, to=1000, \
                            variable = self.dispcomp_a3)
        
        dispcomp_a0.bind("<ButtonRelease-1>", self._change_settings)
        dispcomp_a1.bind("<ButtonRelease-1>", self._change_settings)
        dispcomp_a2.bind("<ButtonRelease-1>", self._change_settings)
        dispcomp_a3.bind("<ButtonRelease-1>", self._change_settings)
        
        dispcomp_a0.grid(row=0, column=0)
        dispcomp_a1.grid(row=0, column=1)
        dispcomp_a2.grid(row=0, column=2)
        dispcomp_a3.grid(row=0, column=3)
        
        ## --- Image Intensity Scale
        intscale_frame = LabelFrame(gen_frame,text="Intensity Scaling")
        intscale_frame.grid(sticky=W+E)
        
        self.intscale_c1 = DoubleVar()
        self.intscale_c2 = DoubleVar()
              
        self.intscale_c1.set(2.0)
        self.intscale_c2.set(4.0)
        
        intscale_c1 = Scale(intscale_frame, from_=0, to=10, resolution=0.1, \
                                 variable = self.intscale_c1 )
        intscale_c2 = Scale(intscale_frame, from_=0, to=10, resolution=0.1, \
                            variable = self.intscale_c2 )
        
        intscale_c1.bind("<ButtonRelease-1>", self._change_settings)
        intscale_c2.bind("<ButtonRelease-1>", self._change_settings)
        
        intscale_c1.grid(row=0, column=0)
        intscale_c2.grid(row=0, column=1)

        
        
        ## --- Save Image Types
        saveset_frame = LabelFrame(gen_frame,text="Save Images")
        saveset_frame.grid( sticky=W+E )
        
        self.saveim_intensity = IntVar()
        self.saveim_phase = IntVar()
        
        self.saveim_intensity.set(1)
        self.saveim_phase.set(1)
        
        saveim_intensity = Checkbutton(saveset_frame, text="Intensity Image",\
                                            onvalue = 1, offvalue = 0, \
                                            variable = self.saveim_intensity)
        saveim_phase = Checkbutton(saveset_frame, text="Phase Image",\
                                            onvalue = 1, offvalue = 0, \
                                            variable = self.saveim_phase)

        
        saveim_intensity.grid( row=0, column=0, sticky=W )
        saveim_phase.grid( row=1, column=0, sticky=W )
        
## _______________________________________________________________________ 

        self.c = 299792458
        self.laser = 800e-9
        self.pixel = 4600
        
        self.p = np.linspace(0,self.pixel,self.pixel) 
        
        self.c_l = [1.5414e-11, -8.52669e-7, 0.07614, 621.73286]
        self.L = np.polyval( self.c_l, self.p )*1e-9
        
        self.w0 = 2*pi*self.c/self.laser*1e-15       # central frequency
        self.ow = 2*pi*self.c*1e-15 / self.L    # convert wavelengths to angular frequencies 
        self.w = np.linspace(self.ow[0], self.ow[self.pixel-1], self.pixel)    #       % angular frequencies
        
## _______________________________________________________________________ 
        
        
    def _change_settings(self, *args):
        self._update_im()
        return
    
    def _change_disptype(self,value):
        self._update_im()
        return
    
    def _update_im(self):

        im_disptype = self.imdisp_type.get()
        print('Updating', im_disptype, 'image')

        create_imatcomp_(self)

        if im_disptype == 'Intensity':
            create_intensityimage_(self)            
            self._change_canvas(self.iimage)
            
        elif im_disptype == 'Phase':
            create_phaseimage_(self)
            self._change_canvas(self.pimage)

        return
    
    
    def _choose_im(self):
        initial_dir = "/home/benjamin/Documents/Misc - Projects/OCT-Image-Reconstruction/"
        self.filename =  filedialog.askopenfilename(initialdir = initial_dir, \
                                                    title = "Select file" )      
       
        self.mat = np.load(self.filename)
        create_smatcomp_(self)
        self._update_im()
        return


    def _save_images(self):
        initial_dir = "/home/benjamin/Documents/Misc - Projects/OCT-Image-Reconstruction/"
        filename_save = filedialog.asksaveasfilename(initialdir = initial_dir, \
                                                     title = "Save file" )
        if self.saveim_intensity.get() == 1:
            create_intensityimage_(self) 
            imageio.imwrite(filename_save+'_Intensity.png', self.iimage)
        if self.saveim_phase.get() == 1:
            create_phaseimage_(self)
            imageio.imwrite(filename_save+'_Phase.png', self.pimage)
        print('Saving images as', filename_save)
        return

    def _change_canvas(self, image_array):
        
        im = Image.fromarray(image_array)

        self.image = ImageTk.PhotoImage(image=im)
        self.image_disp = self.image_canvas.create_image(0,0, anchor = "nw", image = self.image)



## _______________________________________________________________________ 
# Run GUI
        
root = Tk()
g = OCT_GUI(root)
root.mainloop()
