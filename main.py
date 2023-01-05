from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename      #for file operations
import subprocess                                                     #for showing the outpot in another tkinter



compiler = Tk()
compiler.title('My_Own_Idle')

file_path = ''


def set_file_path(path):                                  #to see if the file already exist or not
    global file_path
    file_path = path



def save_as():                                             #block for save and save as both
    if file_path == '':
           path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
            path = file_path
    with open(path, 'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)


def open_file():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)              #need to delete the existing content first then new file content will appear
        editor.insert('1.0', code)
        set_file_path(path)
 
def run():                                    #...............to run the program in our own output window
    if file_path == '':                       #............if file is not saved editor will hang, to avoid this here is this if block
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return         
    COMMAND = f'python {file_path}'                        
    process = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, stderr=subprocess.PIPE , shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)



menu_bar = Menu(compiler)                        #creating a menu bar

file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_as)
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_command(label='Exit',command=run)


menu_bar.add_cascade(label='File', menu=file_menu)



run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)
compiler.config(menu=menu_bar)

editor = Text()                                                     # editor window
editor.pack()


code_output = Text(height=10)                                                      # output window
code_output.pack()



compiler.mainloop()
