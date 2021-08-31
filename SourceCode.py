from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter
import webbrowser
import pefile
import sys
import os
import re

root = Tk()
# PyInstaller Configuration for icon
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root.iconbitmap(resource_path("radar.ico"))

# Create Class and Main Window

class HiddenImportDLL:


    def __init__(window,master):
        window.master=master
        master.geometry('500x500+500+150')
        master.title('Hidden Import DLL')

        encoding = "utf-8"
        url = "https://modware.tech/?page_id=5"


        # Define open URL function

        def OpenUrl(url):
            webbrowser.open_new(url)

        # Define Open File function
        def openFile():
            global filepath
            filetypes = (
                ("exe", "*.exe"),
                ("All Files", "*.*")
            )

            filepath = filedialog.askopenfilename(
                initialdir = "/",
                title = "Select A File",
                filetype = filetypes
            )

            import_detecter(filepath)


        # Define import library detection
        def import_detecter(filepath) :
            # Clear Tree View before every new submittion file
            for i in tree_view.get_children():
                tree_view.delete(i)
            mal_file = filepath
            pe = pefile.PE(mal_file)
            i=1
            o=1
            x=500
            y=1
            if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
                for entry in pe.DIRECTORY_ENTRY_IMPORT:
                    tree_view.insert(parent="",index='end',iid=i,value=(o,entry.dll.decode(encoding)))  #Insert Element inside Tree View
                    o+=1
                    filename_with_extension = os.path.basename(filepath)
                    filename = os.path.splitext(filename_with_extension)[0]
                    master.title("Hidden Import DLL" + " | " + filename_with_extension)
                    with open(filename+"_Output.txt", "a") as outputFile:
                        outputFile.write("%s" % (entry.dll.decode(encoding))+"\n")
                    for imp in entry.imports:
                        if imp.name != None:
                            tree_view.insert(parent=i,index='end',iid=x,value=(y,"         "+imp.name.decode(encoding)))
                            x+=1
                            y+=1
                            with open(filename+"_Output.txt" , "a") as outputFile:
                                outputFile.write("\t%s" % (imp.name.decode(encoding))+"\n")
                        else:
                            messagebox.showinfo(":(","Sorry Didn't Find any hidden Imports")

                    y=1
                    i+=1


        tree_view = ttk.Treeview(master,height = 19)        #Create Tree View

        # Define Our Columns
        tree_view['columns'] = ("No.","DLL's")

        # Formate Our Columns
        tree_view.column("#0",width=35)
        tree_view.column("No.", anchor=W,width=40)
        tree_view.column("DLL's", anchor=W,width=400)

        # Create headings
        tree_view.heading("#0", text="+/-", anchor=W)
        tree_view.heading("No.", text="No.", anchor=W)
        tree_view.heading("DLL's", text="DLL's", anchor=W)


        tree_view.pack(pady=20)             #TreeView Configuration

        # Button Options
        window.open_button = Button(master,bd=3,text = "Open A File",command=openFile).place(x=200,y=450)
        window.info_button = Button(master,bitmap="info",cursor="pirate",bd=5, command=lambda aurl=url:OpenUrl(aurl)).place(x=470,y=460)



Hidden_Import_DLL = HiddenImportDLL(root)


root.mainloop()
