from tkinter import messagebox

def show_error(textvar1,textvar2,var):
    messagebox.showerror(textvar1,textvar2, parent = var)
    
def show_info(textvar1,textvar2,var):
    messagebox.showinfo(textvar1,textvar2,parent = var)

def ask_question(textvar1,textvar2):
    return messagebox.askquestion(textvar1,textvar2)
