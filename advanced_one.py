from tkinter import *
from tkinter.ttk import *
class Helloapp:
    
    def __init__ (self , parent):
        self.label = Label(parent,text="hello world")
        self.label.grid(row = 0,column = 0,columnspan = 2)
        
        self.button1 =Button(parent,text = "Texas",command = self.Texas_hello)#here parenthesis shouldn't be used in command
        self.button1.grid(row = 1,column = 0)
        self.button2 =Button(parent,text = "nepal",command = self.Nepal_hello)
        self.button2.grid(row = 1, column = 1)
        
    def Texas_hello(self):
        self.label.config(text = "howdy dude")
            
    def Nepal_hello(self):
        self.label.config(text ="Namaste dude")
            
            
def main():
    root = Tk()
    app = Helloapp(root)
    root.mainloop()
    
if __name__ == '__main__':
        main()
        
            

    