#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

This program creates a Quit
button. When we press the button,
the application terminates. 

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from Tkinter import Tk, Text, TOP, BOTH, X, N, LEFT
from ttk import Frame, Label, Entry, Button
import csv


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
        
    def initUI(self):
      
        self.parent.title("Review")
        self.pack(fill=BOTH, expand=True)
        labelfont20 = ('Roboto', 20, 'bold')
        labelfont12 = ('Roboto', 12, 'bold')
        
        frame0 = Frame(self)
        frame0.pack()
        
        lbl0 = Label(frame0, text="Hi USER")
        lbl0.config(font=labelfont20)    
        lbl0.pack( padx=5, pady=5)
        lbl00 = Label(frame0, text="Fill the data here")
        lbl00.config(font=labelfont12)
        lbl00.pack( padx=5, pady=5)
        
        
        frame1 = Frame(self)
        frame1.pack()
        
        lbl1 = Label(frame1, text="Name", width=15)
        lbl1.pack(side=LEFT, padx=7, pady=5)           
       
        self.entry1 = Entry(frame1,width=20)
        self.entry1.pack(padx=5, expand=True)
        
        frame2 = Frame(self)
        frame2.pack()
        
        lbl2 = Label(frame2, text="Branch", width=15)
        lbl2.pack(side=LEFT, padx=7, pady=5)        

        self.entry2 = Entry(frame2)
        self.entry2.pack(fill=X, padx=5, expand=True)
        
        frame3 = Frame(self)
        frame3.pack()
        
        lbl3 = Label(frame3, text="Percent", width=15)
        lbl3.pack(side=LEFT, padx=7, pady=5)        

        self.entry3 = Entry(frame3)
        self.entry3.pack(fill=X, padx=5, expand=True) 
        
        frame4 = Frame(self)
        frame4.pack()
        
        lbl4 = Label(frame4, text="Placed(Yes/No)", width=15)
        lbl4.pack(side=LEFT, padx=7, pady=5)        

        self.entry4 = Entry(frame4)
        self.entry4.pack(fill=X, padx=5, expand=True) 
        
        frame5 = Frame(self)
        frame5.pack()
        
        lbl5 = Label(frame5, text="Resume_File", width=15)
        lbl5.pack(side=LEFT, padx=7, pady=5)        

        self.entry5 = Entry(frame5)
        self.entry5.pack(fill=X, padx=5, expand=True)
        
        frame6 = Frame(self)
        frame6.pack()
        closeButton = Button(frame6, text="SUBMIT",width=15,command=self.getDate)
        closeButton.pack(padx=5, pady=5)
        
        frame000 = Frame(self)
        frame000.pack()
        
        self.lbl000= Label(frame000, text="Enter the data and click SUBMIT")
        self.lbl000.config(font=labelfont12)    
        self.lbl000.pack( padx=5, pady=5)
        
        
        
        
    def getDate(self):
        x1 = self.entry1.get()
        x2 = self.entry2.get()
        x3 = self.entry3.get()
        x4 = self.entry4.get()
        x5 = self.entry5.get()
        
        list1=[x1,x2,x3,x4,"=HYPERLINK("+"\""+x5+"\""+")"]
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')
        self.entry4.delete(0, 'end')
        self.entry5.delete(0, 'end')
        self.lbl000.config(text="YO")

        
        with open("test.csv", "ab") as fp:
            wr = csv.writer(fp, dialect='excel')
            wr.writerow(list1)
        fp.close()
    
   
        


def main():
  
    root = Tk()
    root.geometry("500x500+350+100")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main() 