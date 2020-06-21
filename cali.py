from tkinter import *




class Press:


   

    
    
    def __init__(self,root):

        self.a = 0

        
        self.b0 = Button(root,text="0",padx=50,pady=20,fg="white",bg="black",command=self.b0)
        #self.b0.place(x=60,y=60)
        self.b0.grid(row=4,column=1)


        self.a += 1

        self.b1 = Button(root,text="1",padx=50,pady=20,fg="white",bg="black",command=self.b1)                 #width=30
        #self.b1.place(x=50,y=220)
        self.b1.grid(row=3,column=0)

        self.a += self.a

        self.b2 = Button(root,text="2",padx=50,pady=20,fg="white",bg="black",command=self.b2)
        #self.b2.place(x=280,y=220)
        self.b2.grid(row=3,column=1)

        self.a += self.a

        self.b3 = Button(root,text="3",padx=50,pady= 20,fg="white",bg="black",command=self.b3)
        #self.b3.place(x=510,y=220)
        self.b3.grid(row=3,column=2)

        self.a += self.a

        
        self.b4 = Button(root,text="4",padx=50,pady=20,fg="white",bg="black",command=self.b4)
        #self.b4.place(x=50,y=190)
        self.b4.grid(row=2,column=0)

        self.a += self.a

        self.b5 = Button(root,text="5",padx=50,pady=20,fg="white",bg="black",command=self.b5)
        #self.b5.place(x=280,y=190)
        self.b5.grid(row=2,column=1)
        self.a += self.a

        self.b6 = Button(root,text="6",padx=50,pady=20,fg="white",bg="black",command=self.b6)
        #self.b6.place(x=510,y=190)
        self.b6.grid(row=2,column=2)
        
        self.a += self.a

        self.b7 = Button(root,text="7",padx=50,pady=20,fg="white",bg="black",command=self.b7)
        #self.b7.place(x=50,y=160)
        self.b7.grid(row=1,column=0)

        self.a += self.a
            
        self.b8 = Button(root,text="8",padx=50,pady=20,fg="white",bg="black",command=self.b8)
        #self.b8.place(x=280,y=160)
        self.b8.grid(row=1,column=1)
        self.a += self.a
  
        self.b9 = Button(root,text="9",padx=50,pady=20,fg="white",bg="black",command=self.b9)
        #self.b9.place(x=510,y=160)        
        self.b9.grid(row=1,column=2)
        self.a += self.a

        self.b10 = Button(root,text="+",padx=48,pady=20,fg="white",bg="black",command=self.add)
        #self.b10.place(x=740,y=160)
        self.b10.grid(row=1,column=4)
        
        
        self.a += self.a

        self.b11 = Button(root,text="-",padx=50,pady=20,fg="white",bg="black",command=self.sub)
        #self.b11.place(x=740,y=190)
        self.b11.grid(row=2,column=4)

        self.a += self.a

        self.b12 = Button(root,text="*",padx=50,pady=20,fg="white",bg="black",command=self.mul)
        #self.b12.place(x=740,y=220)
        self.b12.grid(row=3,column=4)

        self.a += self.a

        self.b13 = Button(root,text="=",padx=50,pady=20,fg="white",bg="black",command=self.equal)
        #self.b13.place(x=740,y=250)
        self.b13.grid(row=4,column=2)
        self.a += self.a
 
        self.b14 = Button(root,text="/",padx=50,pady=20,fg="white",bg="black",command=self.div)
        #self.b14.place(x=510,y=250)
        self.b14.grid(row=4,column=4)
        
        self.a += self.a


        self.b14 = Button(root,text="clear",padx=40,pady=20,fg="white",bg="black",command=self.reset)
        #self.b14.place(x=50,y=250)
        self.b14.grid(row=4,column=0)
        self.a += self.a





    def b0(self):
          e1.insert(self.a,0)
    def b1(self):
          e1.insert(self.a,1)
    def b2(self):
          e1.insert(self.a,2) 
    def b3(self):
          e1.insert(self.a,3)
    def b4(self):
          e1.insert(self.a,4)
    def b5(self):
          e1.insert(self.a,5) 
    def b6(self):
          e1.insert(self.a,6)
    def b7(self):
          e1.insert(self.a,7)
    def b8(self):
          e1.insert(self.a,8)
    def b9(self):
          e1.insert(self.a,9) 

    def add(self):
        a = e1.get()
        e1.delete(0,END)
        e1.insert(0,"+")
        b = e1.get()
        e1.delete(0,END)
        l1.append(a)
        l2.append(b)
        print(l1)
        print(l2)

    def sub(self):
        a = e1.get()
        e1.delete(0,END)
        e1.insert(0,"-")
        b = e1.get()
        e1.delete(0,END)
        l1.append(a)
        l2.append(b)
        print(l1)
        print(l2)

    def mul(self):
        a = e1.get()
        e1.delete(0,END)
        e1.insert(0,"*")
        b = e1.get()
        e1.delete(0,END)
        l1.append(a)
        l2.append(b)
        print(l1)
        print(l2)

     
    def div(self):
        a = e1.get()
        e1.delete(0,END)
        e1.insert(0,"/")
        b = e1.get()
        e1.delete(0,END)
        l1.append(a)
        l2.append(b)
        print(l1)
        print(l2)
    
    def reset(self):
        e1.delete(0,END)
        print(l1,l2)
        l1.clear()
        l2.clear()
    

    def equal(self):
        c = e1.get()
        l1.append(c)
        e1.delete(0,END)
        print(l1)
        ans = 0
        d =0 
        for i in l2:
            if i == "+":
                for j in l1:


                   
                     ans += float(j)

                print(ans)
                 

            if i == "-":
                d = float(l1[0])
                e = float(l1[1])
                ans = d - e
                print(ans)



            if i == "*":
                d = float(l1[0])
                e = float(l1[1])
                ans = d * e
                print(ans)


            if i == "/":
                d = float(l1[0])
                e = float(l1[1])
                ans = round((d / e),2)
                print(ans)
                




            e1.insert(0,ans)
            l3.append(ans)
    

        l1.clear()
        l2.clear()
        print(l1,l2)
        print(l3)
            


root = Tk()
root.title("Calculator")
l1 = []
l2 = []
l3 = []
e1 = Entry(root,width=55,borderwidth = 5)
e1.grid(row=0,column=0,columnspan=3)
b = Press(root)



root.mainloop() 
