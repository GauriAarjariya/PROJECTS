import tkinter as tk
from tkinter import*
from tkinter import Widget, ttk
from tkinter import font,colorchooser, filedialog, messagebox


# this is used for retrieving the base name of the file
import os
from tkinter.constants import LEFT

main_application = tk.Tk() #Create a Object
main_application.geometry('1200x800')
main_application.title('T-TextEditor')


main_menu = tk.Menu() #Create a Object




#Now we want to use Fileicons  Icons in our Application
new_icon = tk.PhotoImage(file='icons2/new.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')


#Now we want to use Editicons  Icons in our Application
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')


#Now we want to use ViewIcons  Icons in our Application
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')



#Now we want to use ColorIcons  Icons in our Application
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
paste_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')




#Here I creating The Four Options For our Editor
File=tk.Menu(main_menu,tearoff=False)



Edit = tk.Menu(main_menu,tearoff=False)



View = tk.Menu(main_menu,tearoff=False)



Color_Theme = tk.Menu(main_menu,tearoff=False)




#------Color_Theme------#
theme_choice = tk.StringVar()
color_icons = (light_default_icon,dark_icon,night_blue_icon,red_icon,paste_plus_icon,monokai_icon)

color_dict ={
        'Light Default' :('#000000','#ffffff'),
        'Dark' :('#c4c4c4','2d2d2d'),
        'NightBlue' :('#ededed','#6b9dc2'),
        'Red' :('#2d2d2d','#ff3d3d'),
        'Paste Plus' :('#4747474','#e0e0e0'),
        'Monokai' :('#d3b774','#474747'),
        
}







#Adding the EditIcons in the File Section
# Color_Theme.add_command(label='Light', image=light_default_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Black',image=dark_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Blue', image=night_blue_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Light-red', image=red_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Light', image=paste_plus_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Monokai', image=monokai_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Dark-red', image=darkred_icon, compound=tk.LEFT)
# Color_Theme.add_command(label='Light-green', image=lightgreen_icon, compound=tk.LEFT)







# Now  I am Cascade Them Otherwise They will Not show
main_menu.add_cascade(label='File',menu=File)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=View)
main_menu.add_cascade(label='Color Theme',menu=Color_Theme)


#================================= MAIN MENU ===============================#

#Text Editor
text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)



## variable 
url = ''

## new functionality
def new_file(event=None):
    global url 
    url = ''
    text_editor.delete(1.0, tk.END)

## file commands 
File.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)


## open functionality

def open_file(event=None):
    global url 
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return 
    except:
        return 
    main_application.title(os.path.basename(url))

## file commands 
File.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)




## save file 

def save_file(event=None):
    global url 
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2 = text_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        return 
       

File.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


## Save as Functionallity 
def save_as(event=None):
    try:
        content = text_editor.get(1.0,tk.END)
        url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return    


File.add_command(label='Save_as', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S',command=save_as)



##Exit Functionallity
def exit_func(event=None):
    global  url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('warning','Do You Want to Save The File?')
            if mbox is True: #User seleted Yes
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0,tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:  #User seleted No
                main_application.destroy()      
        else:
            main_application.destroy()    
    except:
        return               



File.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q',command=exit_func)



## =========== Find Functionallity ==========


############ find functionality

def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break 
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')
    
    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ## frame 
    find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
    find_frame.pack(pady=20)

    ## labels
    text_find_label = ttk.Label(find_frame, text='Find : ')
    text_replace_label = ttk.Label(find_frame, text= 'Replace')

    ## entry 
    find_input = ttk.Entry(find_frame, width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ## button 
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

    ## label grid 
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    ## entry grid 
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    ## button grid 
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()

























#Adding the EditIcons in the File Section
Edit.add_command(label='Copy',image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
Edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
Edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
Edit.add_command(label='Clear', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
Edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F',command=find_func)
    
    






#Adding the FileIcons in the File Section
# File.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
# File.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')                 
# File.add_command(label='Save', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+S')
# File.add_command(label='Save_as', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
# File.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')




#Adding the FileIcons in the File Section

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM) 
        show_toolbar = True   

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True  




View.add_checkbutton(label='Toolbar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon, compound=tk.LEFT,command=hide_toolbar)
View.add_checkbutton(label='Statusbar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon, compound=tk.LEFT,command=hide_statusbar)


#Now i am adding the RadioButton in colortheme

def change_theme():
    global theme_choice
    choosen_theme = theme_choice.get()
    color_tuple = color_dict.get(choosen_theme)
    fg_color,bg_color = color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg = fg_color)


count=0
for i in color_dict:
    Color_Theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=LEFT,command=change_theme)
    count+=1


#--------------------------@@@@@ END MAIN MENU @@@@@--------------------#






#================================= TOOLBAR ===============================#


#Creating Font Box and Give font-families 
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X)

font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0, column=0, padx=5)


#Creating Size Box 
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar,textvariable=size_var,state='readonly') 
font_size['values'] = tuple(range(8,80,2))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)


## Bold Button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)


## Italic Button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)


## Underline Button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)



## FontColor Button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)


## AlignLeft Button
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_left_btn = ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)


## AlignCenter Button
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_center_btn = ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)


## AlinnRight Button
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')
align_right_btn = ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)



#--------------------------@@@@@ END TOOLBAR @@@@@--------------------#


#================================= TEXT EDITOR ===============================#


#ScrollBar
scroll_bar = tk.Scrollbar(main_application)  # call class Constructor in scroll_bar



#I Want- when i open my application our cursor should be a proper position
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)


#Font Family and Font Size Functionllity by default the font should be arial and size=12
current_font_family='Arial'
current_font_size=12
text_editor.configure(font=('Arial',12))


#---ffffff------Now making a function which will change the font family of the text------fffff

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

#======Now bind the function with the comboBox========#
font_box.bind("<<ComboboxSelected>>",change_font)



#---ffffff-------Now making a function which will change the font family of the text------fffff
def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

#======Now bind the function with the comboBox========#
font_size.bind("<<ComboboxSelected>>",change_fontsize)



# BBBBBBBBBBBB====Buttons Functionallity=====BBBBBBBBBBBB#

#-----Bold Button Functionality-----
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

#Configure Bold Button
bold_btn.configure(command=change_bold)




#-----Itallic Button Functionality-----
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

# Configure itallic Button
italic_btn.configure(command=change_italic)





#-----Itallic Button Functionality-----
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

# Configure itallic Button
underline_btn.configure(command=change_underline)





# -------Change Font Color Functionallity
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

# Configure font color Button
font_color_btn.configure(command=change_font_color)   



####### <<<<<<< Align Functionality >>>>>>>>> ########

##--- Align Left

def align_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

#Configure alignleft Button
align_left_btn.configure(command=align_left)



##--- Align Center
def align_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

#Configure aligncenter Button
align_center_btn.configure(command=align_center)



##--- Align Left
def align_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

# Configure alignright Button
align_right_btn.configure(command=align_right)



#--------------------------@@@@@ END TEXT EDITOR @@@@@--------------------#


#================================= MAIN STATUS BAR ===============================#


status_bar = ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed = False

#====Status bar Functionallity we will want to calculate spaces====#
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0,'end-1c').split())
        characters = len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters :{characters} words :{words}')
    
    text_editor.edit_modified(False)   

text_editor.bind('<<Modified>>',changed)
#--------------------------@@@@@ END STATUS BAR @@@@@--------------------#


#================================= MAIN MENU FUNCTIONALITY ===============================#

#--------------------------@@@@@ END MAIN MENU FUNCTIONALITY @@@@@--------------------#


## Bind Shortcut Key's
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)

main_application.config(menu=main_menu)
main_application.mainloop()