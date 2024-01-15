import tkinter as tk

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.geometry('600x600')
    window.resizable(False,False)
    
    window.rowconfigure(0, minsize = 0)
    window.columnconfigure(1, minsize = 125)
    
    text_edit = tk.Text(window, font="Helveltica 18 bold")
    text_edit.grid(row = 0, column = 1)
    
    frame = tk.Frame(window, relief = tk.RAISED, bd = 4)
    save_button = tk.Button(frame, text = "Save")
    open_button = tk.Button(frame, text = "Open")
    
    save_button.grid(row = 0, column = 0, padx = 5, pady = 5, stick = "ew")
    open_button.grid(row = 1, column = 0, padx = 5, pady = 5, stick = "ew")
    frame.grid(row = 0, column = 0, sticky = "n")
    
    window.mainloop()

    
main()
