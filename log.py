from tkinter import *
from tkinter import messagebox
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

class Cancer():
    def __init__(self, root):
        self.t1=StringVar()
        self.t2=StringVar()
        self.t3=StringVar()
        self.t4=StringVar()
        self.t5=StringVar()
        self.t6=StringVar()
        self.t7=StringVar()
        self.t8=StringVar()
        self.t9=StringVar()
        
        self.label = Label(root, text='CANCER CHECKUP', font=('arial', 30, 'bold'), bg='#ffffff',fg='black')
        self.label.pack()

        self.label_1 = Label(root, text='CLUMP THICKNESS :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_1.place(x=30, y=110)

        self.T1 = Entry(root, textvariable=self.t1, bd=2)
        self.T1.place(x=250, y=110)

        self.label_2 = Label(root, text='UNIFORM CELL SIZE :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_2.place(x=30, y=160)

        self.T2 = Entry(root, textvariable=self.t2, bd=2)
        self.T2.place(x=250, y=160)
        self.label_3 = Label(root, text='UNIFORM CELL SHAPE :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_3.place(x=30, y=210)

        self.T3 = Entry(root, textvariable=self.t3, bd=2)
        self.T3.place(x=250, y=210)

        self.label_4 = Label(root, text='MARGINAL ADHESION :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_4.place(x=30, y=260)

        self.T4 = Entry(root, textvariable=self.t4, bd=2)
        self.T4.place(x=250, y=260)

        self.label_5 = Label(root, text='SINGLE EPI CELL SIZE :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_5.place(x=30, y=310)

        self.T5 = Entry(root, textvariable=self.t5, bd=2)
        self.T5.place(x=250, y=310)

        self.label_6 = Label(root, text='BARE NUCLIE :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_6.place(x=30, y=360)

        self.T6 = Entry(root, textvariable=self.t6, bd=2)
        self.T6.place(x=250, y=360)

        self.label_7 = Label(root, text='BLAND CHROMATION :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_7.place(x=30, y=410)

        self.T7 = Entry(root, textvariable=self.t7, bd=2)
        self.T7.place(x=250, y=410)

        self.label_8 = Label(root, text='NORMAL NUCLEOLI :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_8.place(x=30, y=460)

        self.T8 = Entry(root, textvariable=self.t8, bd=2)
        self.T8.place(x=250, y=460)

        self.label_9 = Label(root, text='MITOSIS :',bg="#ffffff", font=('arial', 10, 'bold'), fg='black',width=20)
        self.label_9.place(x=30, y=510)

        self.T9 = Entry(root, textvariable=self.t9, bd=2)
        self.T9.place(x=250, y=510)
        
        
        self.button1 = Button(root, width=6, text='ENTER',bg="#ffffff", command=self.prediction, font=('arial', 12,'bold'), bd=3)
        self.button1.place(x=80,y=600)

        self.button2 = Button(root, width=6, text='QUIT',bg="#ffffff", command=self.window_close, font=('arial', 12,'bold'), bd=3)
        self.button2.place(x=280,y=600)

        self.button3 = Button(root, width=6, text='RESET',bg="#ffffff", command=self.RESET, font=('arial', 12,'bold'), bd=3)
        self.button3.place(x=180,y=600)

        ############################################################################################################################

        self.can=Canvas(root,bd=5,bg='blue',width=150,height=150)
        self.can.place(x=520,y=175)
        
        self.I1 = Label(root, text="Type Of Cancer : ", font=('arial', 10, 'bold'), width=17, height=1)
        self.I1.place(x=470, y=380)
        ############################################################################################################################

        
        root.geometry('800x700+0+0')
        root.mainloop()
        
    
    def window_close(self):
        if messagebox.askokcancel("Quit", "Close Window? "):
            root.destroy()

    def RESET(self):
        self.t1.set("")
        self.t2.set("")
        self.t3.set("")
        self.t4.set("")
        self.t5.set("")
        self.t6.set("")
        self.t7.set("")
        self.t8.set("")
        self.t9.set("")
        

    def prediction(self):

        if ( self.T1.get() == '' or self.T2.get() == '' or self.T3.get() == '' or self.T4.get() == '' or self.T5.get() == '' \
             or self.T6.get() == '' or self.T7.get() == '' or self.T8.get() == '' or self.T9.get() == ''):
            messagebox.showwarning("Incorrect", "Enter All Columns Values")

        else:
            example_measures = np.array(
                [self.T1.get(), self.T2.get(), self.T3.get(), self.T4.get(), self.T5.get(), self.T6.get(),
                 self.T7.get(), self.T8.get(), self.T9.get()])
            
            example_measures = example_measures.reshape(1, -1)
            pred = clf.predict(example_measures)

            if (pred == 2):
                self.img1=PhotoImage(file='b.png')
                self.can.create_image(7,8,image=self.img1,anchor=NW)
                self.I2 = Label(root, text="BENIGN TUMOR", font=('arial', 10, 'bold'), width=17, height=1)
                self.I2.place(x=640, y=380)


            elif (pred == 4):
                self.img1=PhotoImage(file='m.png')
                self.can.create_image(7,8,image=self.img1,anchor=NW)
                self.I2 = Label(root, text="MALIGNANT TUMOR", font=('arial', 10, 'bold'), width=17, height=1)
                self.I2.place(x=640, y=380)




df = pd.read_csv('cancer.csv')
df.replace('?',-99999, inplace=True)
df.dropna(inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'], 1))
Y = np.array(df['class'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=0.2) 
 
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)

root = Tk()
root.title("CANCER")
root.config(bg="#46e9fb")
Can = Cancer(root)
root.mainloop()
