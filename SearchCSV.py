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
import os


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
        lbl00 = Label(frame0, text="Search here")
        lbl00.config(font=labelfont12)
        lbl00.pack( padx=5, pady=5)
        
        
        frame1 = Frame(self)
        frame1.pack()
        
        lbl1 = Label(frame1, text="min %", width=9)
        lbl1.pack(side=LEFT, padx=7, pady=5)           
       
        self.entry1 = Entry(frame1,width=20)
        self.entry1.pack(padx=5, expand=True)
        
        
        
        
        
        frame6 = Frame(self)
        frame6.pack()
        closeButton = Button(frame6, text="Get Names",width=12,command=self.getDate)
        closeButton.pack(padx=5, pady=5)
        
        frame7 = Frame(self)
        frame7.pack()
        closeButton1 = Button(frame7, text="Open in excel",width=15,command=self.openDate)
        closeButton1.pack(padx=5, pady=5)
        
        
        
        frame000 = Frame(self)
        frame000.pack()
        self.lbl000= Label(frame000, text=" ")
        self.lbl000.config(font=labelfont12)    
        self.lbl000.pack( padx=5, pady=5)
        
        frame00a = Frame(self)
        frame00a.pack()
        self.lbl00a= Label(frame000, text=" ")
        self.lbl00a.pack( padx=5, pady=5)
        
        
        
        
    def getDate(self):
        x1 = self.entry1.get()
        nx = ""
        
        
        self.entry1.delete(0, 'end')
        
        self.lbl000.config(text="Names Are:")
        

        
        
        #read csv, and split on "," the line
        csv_file = csv.reader(open('test.csv', "rb"), delimiter=",")
        #loop through csv list
        for row in csv_file:
            if row[2] >= x1:
                nx+=str(row[0]+", ")
                with open("output5.csv", "ab") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow(row)
                fp.close()
        self.lbl00a.config(text=nx)
        
    def openDate(self):
        os.system("start "+'output5.csv')
        
    
   
        


def main():
  
    root = Tk()
    root.geometry("500x500+350+100")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main() 