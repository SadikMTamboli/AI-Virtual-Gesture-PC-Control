import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import cv2
import os


class Shadow(tk.Tk):
    '''
    Add shadow to a widget
    
    This class adds a squared shadow to a widget. The size, the position, and
    the color of the shadow can be customized at wills. Different shadow
    behaviors can also be specified when hovering or clicking on the widget,
    with binding autonomously performed when initializing the shadow. If the
    widget has a 'command' function, it will be preserved when updating the
    shadow appearance.
    Note that enough space around the widget is required for the shadow to
    correctly appear. Moreover, other widgets nearer than shadow's size will be
    covered by the shadow.
    '''
    def __init__(self, widget, color='#212121', size=5, offset_x=0, offset_y=0,
                 onhover={}, onclick={}):
        '''
        Bind shadow to a widget.

        Parameters
        ----------
        widget : tkinter widget
            Widgets to which shadow should be binded.
        color : str, optional
            Shadow color in hex notation. The default is '#212121'.
        size : int or float, optional
            Size of the shadow. If int type, it is the size of the shadow out
            from the widget bounding box. If float type, it is a multiplier of
            the widget bounding box (e.g. if size=2. then shadow is double in
            size with respect to widget). The default is 5.
        offset_x : int, optional
            Offset by which shadow will be moved in the horizontal axis. If
            positive, shadow moves toward right direction. The default is 0.
        offset_y : int, optional
            Offset by which shadow will be moved in the vertical axis. If
            positive, shadow moves toward down direction. The default is 0.
        onhover : dict, optional
            Specify the behavior of the shadow when widget is hovered. Keys may
            be: 'size', 'color', 'offset_x', 'offset_y'. If a key-value pair is
            not provided, normal behavior is maintained for that key. The
            default is {}.
        onclick : dict, optional
            Specify the behavior of the shadow when widget is clicked. Keys may
            be: 'size', 'color', 'offset_x', 'offset_y'. If a key-value pair is
            not provided, normal behavior is maintained for that key. The
            default is {}.

        Returns
        -------
        None.

        '''
        # Save parameters
        self.widget = widget
        self.normal_size = size
        self.normal_color = color
        self.normal_x = int(offset_x)
        self.normal_y = int(offset_y)
        self.onhover_size = onhover.get('size', size)
        self.onhover_color = onhover.get('color', color)
        self.onhover_x = onhover.get('offset_x', offset_x)
        self.onhover_y = onhover.get('offset_y', offset_y)
        self.onclick_size = onclick.get('size', size)
        self.onclick_color = onclick.get('color', color)
        self.onclick_x = onclick.get('offset_x', offset_x)
        self.onclick_y = onclick.get('offset_y', offset_y)
        
        # Get master and master's background
        self.master = widget.master
        self.to_rgb = tuple([el//257 for el in self.master.winfo_rgb(self.master.cget('bg'))])
        
        # Start with normal view
        self.__lines = []
        self.__normal()
        
        # Bind events to widget
        self.widget.bind("<Enter>", self.__onhover, add='+')
        self.widget.bind("<Leave>", self.__normal, add='+')
        self.widget.bind("<ButtonPress-1>", self.__onclick, add='+')
        self.widget.bind("<ButtonRelease-1>", self.__normal, add='+')
    
    def __normal(self, event=None):
        ''' Update shadow to normal state '''
        self.shadow_size = self.normal_size
        self.shadow_color = self.normal_color
        self.shadow_x = self.normal_x
        self.shadow_y = self.normal_y
        self.display()
    
    def __onhover(self, event=None):
        ''' Update shadow to hovering state '''
        self.shadow_size = self.onhover_size
        self.shadow_color = self.onhover_color
        self.shadow_x = self.onhover_x
        self.shadow_y = self.onhover_y
        self.display()
    
    def __onclick(self, event=None):
        ''' Update shadow to clicked state '''
        self.shadow_size = self.onclick_size
        self.shadow_color = self.onclick_color
        self.shadow_x = self.onclick_x
        self.shadow_y = self.onclick_y
        self.display()
    
    def __destroy_lines(self):
        ''' Destroy previous shadow lines '''
        for ll in self.__lines:
            ll.destroy()
        self.__lines = []
    
    def display(self):
        ''' Destroy shadow according to selected configuration '''
        def _rgb2hex(rgb):
            """
            Translates an rgb tuple of int to hex color
            """
            return "#%02x%02x%02x" % rgb
    
        def _hex2rgb(h):
                """
                Translates an hex color to rgb tuple of int
                """
                h = h.strip('#')
                return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        # Destroy old lines
        self.__destroy_lines()
        
        # Get widget position and size
        self.master.update_idletasks()
        x0, y0, w, h = self.widget.winfo_x(), self.widget.winfo_y(), self.widget.winfo_width(), self.widget.winfo_height()
        x1 = x0 + w - 1
        y1 = y0 + h - 1
        
        # Get shadow size from borders
        if type(self.shadow_size) is int:
            wh_shadow_size = self.shadow_size
        else:
            wh_shadow_size = min([int(dim * (self.shadow_size - 1)) for dim in (w,h)])
        uldr_shadow_size = wh_shadow_size - self.shadow_y, wh_shadow_size - self.shadow_x, \
                           wh_shadow_size + self.shadow_y, wh_shadow_size + self.shadow_x
        uldr_shadow_size = {k:v for k,v in zip('uldr', uldr_shadow_size)}
        self.uldr_shadow_size = uldr_shadow_size
        
        # Prepare shadow color
        shadow_color = self.shadow_color
        if not shadow_color.startswith('#'):
            shadow_color = _rgb2hex(tuple([min(max(self.to_rgb) + 30, 255)] * 3))
        self.from_rgb = _hex2rgb(shadow_color)
        
        # Draw shadow lines
        max_size = max(uldr_shadow_size.values())
        diff_size = {k: max_size-ss for k,ss in uldr_shadow_size.items()}
        rs = np.linspace(self.from_rgb[0], self.to_rgb[0], max_size, dtype=int)
        gs = np.linspace(self.from_rgb[2], self.to_rgb[2], max_size, dtype=int)
        bs = np.linspace(self.from_rgb[1], self.to_rgb[1], max_size, dtype=int)
        rgbs = [_rgb2hex((r,g,b)) for r,g,b in zip(rs,gs,bs)]
        for direction, size in uldr_shadow_size.items():
            for ii, rgb in enumerate(rgbs):
                ff = tk.Frame(self.master, bg=rgb)
                self.__lines.append(ff)
                if direction=='u' or direction=='d':
                    diff_1 = diff_size['l']
                    diff_2 = diff_size['r']
                    yy = y0-ii+1+diff_size[direction] if direction == 'u' else y1+ii-diff_size[direction]
                    if diff_1 <= ii < diff_size[direction]:
                        ff1 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff1)
                        ff1.configure(width=ii+1-diff_1, height=1)
                        ff1.place(x=x0-ii+1+diff_size['l'], y=yy)
                    if diff_2 <= ii < diff_size[direction]:
                        ff2 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff2)
                        ff2.configure(width=ii+1-diff_2, height=1)
                        ff2.place(x=x1, y=yy)
                    if ii >= diff_size[direction]:
                        ff.configure(width=x1-x0+ii*2-diff_size['l']-diff_size['r'], height=1)
                        ff.place(x=x0-ii+1+diff_size['l'], y=yy)
                elif direction=='l' or direction=='r':
                    diff_1 = diff_size['u']
                    diff_2 = diff_size['d']
                    xx = x0-ii+1+diff_size[direction] if direction == 'l' else x1+ii-diff_size[direction]
                    if diff_1 <= ii < diff_size[direction]:
                        ff1 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff1)
                        ff1.configure(width=1, height=ii+1-diff_1)
                        ff1.place(x=xx, y=y0-ii+1+diff_size['u'])
                    if diff_2 <= ii < diff_size[direction]:
                        ff2 = tk.Frame(self.master, bg=rgb)
                        self.__lines.append(ff2)
                        ff2.configure(width=1, height=ii+1-diff_2)
                        ff2.place(x=xx, y=y1)
                    if ii >= diff_size[direction]:
                        ff.configure(width=1, height=y1-y0+ii*2-diff_size['u']-diff_size['d'])
                        ff.place(x=xx, y=y0-ii+1+diff_size['u'])


top = tk.Tk()
top.title("AI Virtual Gesture PC Control")
top.geometry("500x400")
top.config(bg='#99FCD6')
name_var=tk.StringVar()

class access:
    def __init__(self,count=0,c=0) -> None:
        self.count=count
        self.c=c
    
    def submit(count=0):
        # count=0
        no=name_var.get()
        
        
        
        if count == 0 :
            def show():
                
                os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VolumeControl.py')
                
                    
            show()
            count=1
        elif count==1:
            
                
            count=0
               
        
    c=0

    def mouse(c=0):
        
        # no=name_var.get()
     

        
        if c == 0:
            def show():
                
                os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualMouse.py')
                
                    
            show()
            c=1
            
        else:
            return 
    def keyboard():       
        os.system('py C:/Users/Tamboli/OneDrive/Desktop/python/VirtualKeyboard.py')
       
    def onClick():
        tk.messagebox.showinfo("Info","Please consider this info while working with software.\n1.Do not press buttons multiple times system might hamper.\n2.Maintain clear background with no disturbance of people.")
  
    def Exit():
        exit()

        
    def onEnter(event):
        global img

        img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/vol.png')
        resize_image = img.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)

        i.config(image=img)
        i.place(x=900,y=250)


    def onLeave(event):
        global img
        img=None
        # img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/win.png')
        # resize_image = img.resize((200, 200))
        # img = ImageTk.PhotoImage(resize_image)

        i.config(image=img)
        i.place(x=900,y=250)

    def onEnterM(event):
        global img

        img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/mouse.png')
        resize_image = img.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)

        i.config(image=img)
        i.place(x=900,y=380)


    def onLeaveM(event):
        global img
        img=None
        # img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/win.png')
        # resize_image = img.resize((200, 200))
        # img = ImageTk.PhotoImage(resize_image)

        i.config(image=img)
        i.place(x=900,y=380)
    def onEnterK(event):
        global img

        img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/keyboard.jpeg')
        resize_image = img.resize((50, 50))
        img = ImageTk.PhotoImage(resize_image)

        i.config(image=img)
        i.place(x=900,y=380+130)


    def onLeaveK(event):
        global img
        img=None
        # img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/win.png')
        # resize_image = img.resize((200, 200))
        # img = ImageTk.PhotoImage(resize_image)

        i.config(image=img)
        i.place(x=900,y=380+130)

    # def onEnterT(event):
    #     global img

    #     img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/mouse.png')
    #     resize_image = img.resize((50, 50))
    #     img = ImageTk.PhotoImage(resize_image)

    #     i.config(image=img)
    #     i.place(x=900,y=380+130+130)


    # def onLeaveT(event):
    #     global img
    #     img=None
    #     # img=Image.open('C:/Users/Tamboli/OneDrive/Desktop/python/win.png')
    #     # resize_image = img.resize((200, 200))
    #     # img = ImageTk.PhotoImage(resize_image)

    #     i.config(image=img)
    #     i.place(x=900,y=380+130+130)
        


   

popup = Button(top, text="i",font=('italic',13, 'bold'),bd=4,borderwidth=0,command=access.onClick,width=5,height=2,justify='center')

popup.pack()
popup.place(x=1000,y=150)
Shadow(popup, size=10, offset_x=10, offset_y=10, onhover={'size':5, 'offset_x':5, 'offset_y':5})

l = tk.Label(top, text = "Welcome to AI Virtual Gesture PC Control\n",font=('calibre',40, 'bold'),bg='#309DFF',foreground='white',justify='center')

l.pack()

Shadow(l, size=10, offset_x=-2, offset_y=4)
# l.place(x=10,y=2)



l1=tk.Label(top,text="Choose your option\n",font=('calibre',20, 'bold'),bg="#99FCD6",justify='center')

l1.pack()
l1.place(x=600,y=150)


l2=tk.Button(top,text="Volume Access\n",font=('calibre',20, 'bold'),justify='center',width=14,bd=0,command=access.submit)

l2.pack(side='top',pady=0,padx=10)
l2.place(x=600,y=230)
img=None
i=tk.Label(top,image=img,bg='#99FCD6')
i.pack()
i.place(x=930,y=250)

l2.bind('<Enter>',  access.onEnter)
l2.bind('<Leave>',  access.onLeave)
# l2.bind("<Enter>",access.change)

l3=tk.Button(top,text="Mouse Access\n",font=('calibre',20, 'bold'),justify='center',width=14,bd=0,fg = "black",command=access.mouse)

l3.pack()
l3.place(x=600,y=360)
m=tk.Label(top,image=img,bg='#99FCD6')
m.pack()
m.place(x=990,y=350)

l3.bind('<Enter>',  access.onEnterM)
l3.bind('<Leave>',  access.onLeaveM)

l4=tk.Button(top,text="Keyboard Access\n",font=('calibre',20, 'bold'),justify='center',width=14,bd=0,command=access.keyboard)
# l4.config(font=("Courier",20),height=1)
l4.pack()
l4.place(x=600,y=480)

k=tk.Label(top,image=img,bg='#99FCD6')
k.pack()
k.place(x=990,y=450)

l4.bind('<Enter>',  access.onEnterK)
l4.bind('<Leave>',  access.onLeaveK)

l5=tk.Button(top,text="Terminate\n",font=('calibre',20, 'bold'),justify='center',width=14,bd=0,command=access.Exit)
# l4.config(font=("Courier",20),height=1)
l5.pack()
l5.place(x=600,y=600)

Shadow(l2, size=10, offset_x=10, offset_y=10, onhover={'size':5, 'offset_x':5, 'offset_y':5})
Shadow(l3, size=10, offset_x=10, offset_y=10, onhover={'size':5, 'offset_x':5, 'offset_y':5})
Shadow(l4, size=10, offset_x=10, offset_y=10, onhover={'size':5, 'offset_x':5, 'offset_y':5})
Shadow(l5, size=10, offset_x=10, offset_y=10, onhover={'size':5, 'offset_x':5, 'offset_y':5})



top.mainloop()
