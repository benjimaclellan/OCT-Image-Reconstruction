from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class OCT_GUI:
    def __init__(self, master):
        master.title("OCT Image Reconstruction")

        gen_frame = LabelFrame(master)
        gen_frame.grid( row=0,column=0 )

        file_frame = LabelFrame(gen_frame, text="File")
        file_frame.grid()



        update_im = Button(file_frame, text="Update Image", command=self.update_im )
        update_im.grid(row=0, column=0, sticky=W+E) 
        
        choose_im = Button( file_frame, text="Choose Image", command=self.choose_im )
        choose_im.grid(row=1, column=0, sticky=W+E)  
        
        save_ims = Button( file_frame, text="Save Images", command=self.update_im )
        save_ims.grid(row=2, column=0, sticky=W+E) 

        self.saveall_ims = IntVar()
        saveall_ims = Checkbutton(file_frame, \
                                  text="Process All Files in Current Folder?",\
                                  onvalue = 1, offvalue = 0, \
                                  variable = self.saveall_ims)
        saveall_ims.grid(row=3, column=0, sticky=W+E) 




        image_settings = LabelFrame(gen_frame, text="Preview Settings")
        image_settings.grid(sticky = W+E)
        
        
        self.variable = StringVar()
        self.variable.set("Intensity") # default value
        
        disp_im = OptionMenu(image_settings, self.variable, "Intensity", "Phase", "Doppler")
        disp_im.grid()




        ## --- Image Display Frame
        image_frame = LabelFrame(master)
        image_frame.grid(  row=0, column=1)


#        self.my_image1 = PhotoImage(file = "index1.png")

        
        self.image_canvas = Canvas(image_frame)
        self.image_canvas.grid(row=0, column=0, sticky = E+W+N+S)        

        
        ## --- Dispersion Compensation
        dispcomp_frame = LabelFrame(gen_frame,text="Dispersion Control")
        dispcomp_frame.grid(sticky=W+E)
        
        self.dispcomp_a0 = DoubleVar()
        self.dispcomp_a1 = DoubleVar()
        self.dispcomp_a2 = DoubleVar()
        self.dispcomp_a3 = DoubleVar()
        
        dispcomp_a0 = Scale(dispcomp_frame, from_=-100, to=100, \
                                 variable = self.dispcomp_a0 )
        dispcomp_a1 = Scale(dispcomp_frame, from_=-100, to=100, \
                            variable = self.dispcomp_a1 )
        dispcomp_a2 = Scale(dispcomp_frame, from_=-100, to=100, \
                            variable = self.dispcomp_a2)
        dispcomp_a3 = Scale(dispcomp_frame, from_=-100, to=100, \
                            variable = self.dispcomp_a3)
        
        dispcomp_a0.grid(row=0, column=0)
        dispcomp_a1.grid(row=0, column=1)
        dispcomp_a2.grid(row=0, column=2)
        dispcomp_a3.grid(row=0, column=3)
        
        ## --- Save Image Types
        saveset_frame = LabelFrame(gen_frame,text="Save Images")
        saveset_frame.grid( sticky=W+E )
        
        self.saveim_intensity = IntVar()
        self.saveim_phase = IntVar()
        self.saveim_mask = IntVar()
        
        saveim_intensity = Checkbutton(saveset_frame, text="Intensity Image",\
                                            onvalue = 1, offvalue = 0, \
                                            variable = self.saveim_intensity)
        saveim_phase = Checkbutton(saveset_frame, text="Phase Image",\
                                            onvalue = 1, offvalue = 0, \
                                            variable = self.saveim_phase)
        saveim_mask = Checkbutton(saveset_frame, text="Mask Image",\
                                            onvalue = 1, offvalue = 0, \
                                            variable = self.saveim_mask)
        
        saveim_intensity.grid( row=0, column=0, sticky=W )
        saveim_phase.grid( row=1, column=0, sticky=W )
        saveim_mask.grid( row=2, column=0, sticky=W )
        
## _______________________________________________________________________ 
        
    def update_im(self):
        self.new_image = PhotoImage(file = "index2.png")
        self.canvas.itemconfig(self.image_on_canvas, image = self.new_image)
        
    def choose_im(self):
        self.filename =  filedialog.askopenfilename( initialdir = "/home/benjamin/Documents/Misc - Projects/OCT-Image-Reconstruction/", \
                                               title = "Select file" )
        
        self.raw_image = PhotoImage(file = self.filename)
        self.image_disp = self.image_canvas.create_image(0, 0, anchor = NW, image = self.raw_image)


## _______________________________________________________________________ 
# Run GUI
        
root = Tk()
oct_gui = OCT_GUI(root)
root.mainloop()
