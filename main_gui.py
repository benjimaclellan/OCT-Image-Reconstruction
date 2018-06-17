from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class OCT_GUI:
    def __init__(self, master):
        master.title("OCT Image Reconstruction")

        gen_frame = LabelFrame(master, text="General")
        gen_frame.pack( side = TOP )

        update_im = Button(gen_frame, text="Update Image", command=self.update_im )
        update_im.pack() 
        
        choose_im = Button( gen_frame, text="Choose Image", command=self.choose_im )
        choose_im.pack() 
        
        save_ims = Button( gen_frame, text="Save Images", command=self.update_im )
        save_ims.pack() 

        self.saveall_ims = IntVar()
        saveall_ims = Checkbutton(gen_frame, \
                                  text="Process All Files in Current Folder?",\
                                  onvalue = 1, offvalue = 0, \
                                  variable = self.saveall_ims)
        saveall_ims.pack()

        ## --- Image Display Frame
        image_disp = LabelFrame(master, text="Image Display")
        image_disp.pack( side = BOTTOM )
        
        self.variable = StringVar()
        self.variable.set("Intensity") # default value
        
        disp_im = OptionMenu(image_disp, self.variable, "Intensity", "Phase", "Doppler")
        disp_im.pack()

        self.im_data = Image.open('/home/benjamin/Pictures/Wallpapers/index.png')
        self.im_ref = ImageTk.PhotoImage(self.im_data)
        
        self.im_current = Label(image_disp,image=self.im_ref)
        self.im_current.pack()
        
        
        
#        filein_frame = LabelFrame(master,text="File Input")
#        filein_frame.pack( side = RIGHT )
#        
#        self.file_path = Entry(filein_frame)
#        self.file_path.pack()


        '''
        Buttons to add:
            Image (phase,intensity,doppler,mask,etc)
            Preview file
            Run files
            Set dispersion compensation
            
        '''
        
        ## --- Dispersion Compensation
        dispcomp_frame = LabelFrame(master,text="Dispersion Control")
        dispcomp_frame.pack( side = RIGHT )
        
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
        
        dispcomp_a0.grid()
        dispcomp_a1.grid()
        dispcomp_a2.grid()
        dispcomp_a3.grid()
        
        ## --- Save Image Types
        saveset_frame = LabelFrame(master,text="Save Images")
        saveset_frame.pack( side = TOP )
        
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
        
        saveim_intensity.pack( side = TOP )
        saveim_phase.pack( side = TOP )
        saveim_mask.pack( side = TOP )
        
        ## --- 
        
    def update_im(self):
        return
        
    def choose_im(self):
        filename =  filedialog.askopenfilename( initialdir = "/home/benjamin/", \
                                               title = "Select file", \
                                               filetypes = (("jpeg files","*.jpg"), \
                                                            ("all files","*.*")) )
#        print (root.filename)

root = Tk()
oct_gui = OCT_GUI(root)
root.mainloop()
