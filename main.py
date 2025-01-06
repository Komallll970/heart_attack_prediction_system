from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from tkinter import PhotoImage
from tkinter.font import *  # type: ignore
from PIL import Image,ImageTk
from tkinter import messagebox
import matplotlib # type: ignore
from backend import *
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

background='#f0ddd5'
framebg='#62a7ff'
framefg='#fefbfb'

root=Tk()
root.title('Heat-Attack Prediction System')
root.geometry('1450x700')
#root.resize(False,False)
root.config(bg=background)


############analysis###############
def analysis():
    global prediction
    print('working!!!')
    name=Name.get()
    d1=Date.get()
    today=datetime.date.today()
    A=today.year-DOB.get()
    
    try:
        b=selection()
    except:
        messagebox.showerror('Missing','Please select the gender!')    
        return
   
    try:
        f=selection2()
    except:
        messagebox.showerror('Missing','Please select the fbs!')    
        return
    
    try:
        i=selection3()
    except:
        messagebox.showerror('Missing','Please select exang!')    
        return
    
     
    try:
        c=int(selection4())
    except:
        messagebox.showerror('Missing','Please select cp!!')    
        return
    
    try:
        g=int(restecg_combobox.get())
    except:
        messagebox.showerror('Missing','Please select slope!!')    
        return
    
    try:
        k=int(selection5())
    except:
        messagebox.showerror('Missing','Please select restecg!!')    
        return
    
    try:
        l=int(ca_combobox.get())
    except:
        messagebox.showerror('Missing','Please select ca!!')    
        return
    
    try:
        m=int(thal_combobox.get())
        
    except:
        messagebox.showerror('Missing','Please select thal!!')    
        return
    
    try:
        d=int(trestbps.get())
        e=int(chol.get())
        h=int(thalach.get())
        j=int(oldpeak.get())
    except:
        messagebox.showerror('Missing data','Please select, Few missing data entry!!')    
        return
    
    # lets cgcek all are working or not
    
    print('A is age:',A)
    print('B is gender:',b)
    print('C is cp:',c)
    print('D is trestbps',d)
    print('E is chol: ',E)
    print('F is fbs:',f)
    print('G is restecg',g)
    print('H is thalach:',h)
    print('I is exang',i)
    print('J is oldpeak:',j)
    print('K is slope:',k)
    print('L is ca:',l)
    print('M is thal',m)
    
   ############first graph
    F=Figure(figsize=(5,5),dpi=100)
    a1=F.add_subplot(111)
    a1.plot(['Sex','fbs','exang'],[b,f,i])
    canvas= FigureCanvasTkAgg(F)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=200,height=200,x=520,y=180)
    
   ############2nd graph
    F2=Figure(figsize=(5,5),dpi=100)
    a2=F2.add_subplot(111)
    a2.plot(['age','trestbps','chol','thalach'],[A,d,e,h])
    canvas2= FigureCanvasTkAgg(F2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=200,height=200,x=770,y=180)  
    
    ############3rd graph
    F3=Figure(figsize=(5,5),dpi=100)
    a3=F3.add_subplot(111)
    a3.plot(['oldpeak','restecg','cp',],[j,g,c])
    canvas3= FigureCanvasTkAgg(F3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=200,height=200,x=520,y=415)  
    
    ############4thgraph
    F4=Figure(figsize=(5,5),dpi=100)
    a4=F4.add_subplot(111)
    a4.plot(['slope','ca','thal'],[k,l,m])
    canvas4= FigureCanvasTkAgg(F4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=200,height=200,x=770,y=415)    
    
    ###############imput data
    input_data=(A,b,c,d,e,f,g,h,i,j,k,l,m)
    input_data_as_numpy_array=np.asanyarray(input_data)
    
    #reshape the numpy array as we are predicting for only one
    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)
    prediction=model.predict(input_data_reshape)
    print(prediction)
    if (prediction!=0):
        print('Person does not have a heart disease')
        report.config(text=f'Report:{0}',fg='#8dc63f')
        report1.config(text=f'{name},you do not have chances of heart attack')
    else:
        print('Person have chances of  heart attack')
        report.config(text=f'Report:{1}',fg='#8dc63f')
        report1.config(text=f'{name},you  have a heart disease')
           

############## info window(operated by info button)
def Info():
    roots=Toplevel(root)
    roots.title('Info')
    roots.geometry('600x500+50+50')

#icon
    icon_image=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/info.png')
    roots.iconphoto(False,icon_image)

## heading
    Label(roots,text='Information Related to Dataset',font='robot 14 bold').pack(padx=15,pady=15)

##info
    Label(roots,text='age - age in years',font='arial 9').place(x=16,y=80)
    Label(roots,text='sex - sex (1 = male; 0 = female)',font='arial 9').place(x=16,y=100)
    Label(roots,text='cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)',font='arial 9').place(x=16,y=120)
    Label(roots,text='trestbps - resting blood pressure (in mm Hg on admission to the hospital)',font='arial 9').place(x=16,y=140)
    Label(roots,text='chol - serum cholestoral in mg/dl',font='arial 9').place(x=16,y=160)
    Label(roots,text='fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)',font='arial 9').place(x=16,y=180)
    Label(roots,text='restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)',font='arial 9').place(x=16,y=200)
    Label(roots,text='thalach - maximum heart rate achieved',font='arial 9').place(x=16,y=220)
    Label(roots,text='exang - exercise induced angina (1 = yes; 0 = no)',font='arial 9').place(x=16,y=240)
    Label(roots,text='oldpeak - ST depression induced by exercise relative to rest',font='arial 9').place(x=16,y=260)
    Label(roots,text='slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)',font='arial 9').place(x=16,y=280)
    Label(roots,text='ca - number of major vessels (0-3) colored by flourosopy',font='arial 9').place(x=16,y=300)
    Label(roots,text='thal - 0 = normal; 1 = fixed defect; 2 = reversable defect',font='arial 9').place(x=16,y=320)

    roots.mainloop()

######to close the window3333333333
def logout():
    root.destroy()
    
    #############clear()-to clear entry fields
    
def Clear():
     Name.get('')
     DOB.get('')
     trestbps.get('')
     chol.get('')
     thalach.get('')
     oldpeak.get('')
 
 ###save
def Save():
    B2=Name.get()
    C2=Date.get()
    D2=DOB.get()
    
    today= datetime.date.today()
    E2=today.year-DOB.get()
    
    try:
        F2=selection()
    except:
        messagebox.showerror('Missing Data','Please Select the Gender!')  
        
    try:
        J2=selection2()
    except:
        messagebox.showerror('Missing Data','Please Select the fbs!')  
        
    try:
        M2=selection3()
    except:
        messagebox.showerror('Missing Data','Please Select the exang!')  
    
    try:
        G2=selection4()
    except:
        messagebox.showerror('Missing Data','Please Select the cp!')
        
    try:
        K2=restecg_combobox.get()
    except:
        messagebox.showerror('Missing Data','Please Select the restecg!')   
                            
    try:
        O2=selection5()
    except:
        messagebox.showerror('Missing Data','Please Select the slope!')  
        
    try:
        P2=ca_combobox.get()
    except:
        messagebox.showerror('Missing Data','Please Select the cal!')   
        
    try:
        Q2=thal_combobox.get()
    except:
        messagebox.showerror('Missing Data','Please Select the thal!')       
      
    H2=trestbps.get()
    I2=chol.get()
    L2=thalach.get()
    N2=float(oldpeak.get())                             
    
    print(B2)
    print(C2)
    print(D2)
    print(E2)
    print(F2)
    print(G2)
    print(H2)
    print(I2)
    print(J2)
    print(K2)
    print(L2)
    print(M2)
    print(N2)
    print(O2)
    print(P2)
    print(Q2)
    
    Save_Data_MySql(B2,C2,int(D2),int(E2),int(F2),int(G2),int(H2),int(I2),int(J2),int(K2),int(L2),int(M2),int(N2),int(O2),int(P2),int(Q2),int(prediction[0]))
    
    Clear()
    root.destroy('main.py')
    
                            
##########################################################
#icon1
image_icon=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/icon.png')
root.iconphoto(False,image_icon)


##header section2
img=Image.open('C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/hh.png')
img=img.resize((700,120)) # type: ignore
photoimg=ImageTk.PhotoImage(img)
l1=Label(root,image=photoimg)  # type: ignore
l1.place(x=0,y=0)
        
img1=Image.open('C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/hh2.png')
img1=img1.resize((400,120)) # type: ignore
photoimg1=ImageTk.PhotoImage(img1)
l2=Label(root,image=photoimg1)  # type: ignore
l2.place(x=690,y=0)
img2=Image.open('C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/hh2.png')
img2=img2.resize((320,120)) # type: ignore
photoimg2=ImageTk.PhotoImage(img2)
l2=Label(root,image=photoimg1)  # type: ignore
l2.place(x=1000,y=0)


### ADDING PHOTOS:
img11=Image.open('C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/headimg11.png')
#img11=img11.resize((800,10)) # type: ignore
photoimg11=ImageTk.PhotoImage(img11)
l11=Label(root,image=photoimg11)  # type: ignore
l11.place(x=770,y=2)

l111=Label(root,text='Get Info      ',bg='#df2d4b',fg='white',font='arial 13')  # type: ignore
l111.place(x=1060,y=14)

l1111=Label(root,text='Exit            ',bg='#df2d4b',fg='white',font='arial 13')  # type: ignore
l1111.place(x=1060,y=70)

l11111=Label(root,text='    HEART-ATTACK PREDICTION SYSTEM    ',bg='#df2d4b',fg='white',font='arial 17')  # type: ignore
l11111.place(x=200,y=40)



#logo=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/hh.png')
#myimage.place(x=0,y=7)



#### frame 3
heading_entry=Frame(root,width=450,height=170,bg='#df2d4b')
heading_entry.place(x=27,y=150)

Label(heading_entry,text='Regsitration No.',font='arial 12',bg='#df2d4b',fg=framefg).place(x=20,y=4)
Label(heading_entry,text='Date   ',font='arial 12',bg='#df2d4b',fg=framefg).place(x=220,y=4)
Label(heading_entry,text='Patient Name  ',font='arial 12',bg='#df2d4b',fg=framefg).place(x=20,y=80)
Label(heading_entry,text='Birth Year   ',font='arial 12',bg='#df2d4b',fg=framefg).place(x=220,y=80)

#Entry_image=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/Rounded Rectangle 1.png')
Entry_image2=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/Rounded Rectangle 2.png',width=170)
Label(heading_entry,image=Entry_image2,bg='white').place(x=12,y=25)
Label(heading_entry,image=Entry_image2,bg='white').place(x=220,y=25)

Label(heading_entry,image=Entry_image2,bg='white').place(x=12,y=110)
Label(heading_entry,image=Entry_image2,bg='white').place(x=220,y=110)


Registration=IntVar()
reg_entry=Entry(heading_entry,textvariable=Registration,font='arial 12',bg='#df2d4b',fg='white',bd=0,width=17)
reg_entry.place(x=23,y=35)

Date=StringVar()
today=date.today()
d1=today.strftime('%d/%m/%Y')
date_entry=Entry(heading_entry,textvariable=Date,font='arial 12',bg='#df2d4b',fg='white',bd=0,width=17)
date_entry.place(x=225,y=35)
Date.set(d1)

Name=StringVar()
name_entry=Entry(heading_entry,textvariable=Name,font='arial 12',bg='#df2d4b',fg='white',bd=0,width=17)
name_entry.place(x=23,y=120)

DOB=IntVar()
dob_entry=Entry(heading_entry,textvariable=DOB,font='arial 12',bg='#df2d4b',fg='white',bd=0,width=17)
dob_entry.place(x=225,y=120)

########################################Body$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Detail_entry=Frame(root,width=450,height=270,bg='#f3fefd')
Detail_entry.place(x=27,y=350)


Label(Detail_entry,text='sex:',font='arial 12',bg='#df2d4b',fg=framefg).place(x=8,y=8)
Label(Detail_entry,text='fbs:',font='arial 12',bg='#df2d4b',fg=framefg).place(x=160,y=8)
Label(Detail_entry,text='exang:',font='arial 12',bg='#df2d4b',fg=framefg).place(x=305,y=8)

def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return(Gender)
        print(Gender) 
    else:
        print(Gender)    
         
def selection2():
    if fbs.get()==1:
        Fbs=1
        print(Fbs)
        return(Fbs)
    elif fbs.get()==2:
        Fbs=0
        return(Fbs)
        print(Fbs) 
    else:
        print(Fbs)   
        
def selection3():
    if exang.get()==1:
        Exang=1
        print(Exang)
        return(Exang)
    elif exang.get()==2:
        Fbs=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen=IntVar()
R1=Radiobutton(Detail_entry,text='Male',variable=gen,value=1,background='white',command=selection)
R2=Radiobutton(Detail_entry,text='Female',variable=gen,value=2,background='white',command=selection)
R1.place(x=40,y=8)
R2.place(x=90,y=8)

fbs=IntVar()
R3=Radiobutton(Detail_entry,text='True',variable=fbs,value=1,background='white',command=selection2)
R4=Radiobutton(Detail_entry,text='False',variable=fbs,value=2,background='white',command=selection2)
R3.place(x=190,y=8)
R4.place(x=240,y=8)

exang=IntVar()
R5=Radiobutton(Detail_entry,text='Yes',variable=exang,value=1,background='white',command=selection3)
R6=Radiobutton(Detail_entry,text='No',variable=exang,value=2,background='white',command=selection3)
R5.place(x=355,y=8)
R6.place(x=398,y=8)


###############COMBOBOX#####################

def selection4():
    input=cp_combobox.get()
    if input=='0 = typical angina':
        return(0)
    elif input=='1 = atypical angina':
        return(1)
    elif input=='2 = non-anginal pain':
        return(2)
    elif input=='3 = asymptomatic':
        return(3)
    else:
        print(Exang)
        
def selection5():
    input=slope_combobox.get()
    if input=='0 = upsloping':
        return(0)
    elif input=='1 = flat':
        return(1)
    elif input=='2 = downsloping':
        return(2)
    else:
        print(Exang)        
    
    
    
    
    
Label(Detail_entry,text='cp:',bg='#df2d4b',fg=framefg,width=7).place(x=8,y=50)
Label(Detail_entry,text='restecg:',bg='#df2d4b',fg=framefg,width=7).place(x=8,y=90)
Label(Detail_entry,text='slope:',bg='#df2d4b',fg=framefg,width=7).place(x=8,y=130)
Label(Detail_entry,text='ca:',bg='#df2d4b',fg=framefg,width=7).place(x=8,y=170)
Label(Detail_entry,text='thal',bg='#df2d4b',fg=framefg,width=7).place(x=8,y=210)


cp_combobox=Combobox(Detail_entry,value=['0 = typical angina',' 1 = atypical angina', '2 = non-anginal pain','3 = asymptomatic'],font='arial 10',state='r',width=9)#,command=selection4)
restecg_combobox=Combobox(Detail_entry,value=['0','1','2'],font='arial 10',state='r',width=9)
slope_combobox=Combobox(Detail_entry,value=['0 = upsloping', '1 = flat', '2 = downsloping'],font='arial 10',state='r',width=9)#command=selection5)
ca_combobox=Combobox(Detail_entry,value=['0','1','2','3','4'],font='arial 10',state='r',width=9)
thal_combobox=Combobox(Detail_entry,value=['0','1','2','3'],font='arial 10',state='r',width=9)
cp_combobox.place(x=69,y=50)
restecg_combobox.place(x=69,y=90)
slope_combobox.place(x=69,y=130)
ca_combobox.place(x=69,y=170)
thal_combobox.place(x=69,y=210)

########################### data entry box#####################
Label(Detail_entry,text='Smoking:',bg='#df2d4b',fg=framefg,font='arial 10',width=7).place(x=230,y=50)
Label(Detail_entry,text='trestbps:',bg='#df2d4b',fg=framefg,font='arial 10',width=7).place(x=230,y=90)
Label(Detail_entry,text='chol:',bg='#df2d4b',fg=framefg,font='arial 10',width=7).place(x=230,y=130)
Label(Detail_entry,text='thalach:',bg='#df2d4b',fg=framefg,font='arial 10',width=7).place(x=230,y=170)
Label(Detail_entry,text='oldpeak:',bg='#df2d4b',fg=framefg,font='arial 10',width=7).place(x=230,y=210)

trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvariable=trestbps,width=13,font='arial 10',bg='#ededed',fg='black',bd=0)
chol_entry=Entry(Detail_entry,textvariable=chol,width=13,font='arial 10',bg='#ededed',fg='black',bd=0)
thalach_entry=Entry(Detail_entry,textvariable=thalach,width=13,font='arial 10',bg='#ededed',fg='black',bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=oldpeak,width=13,font='arial 10',bg='#ededed',fg='black',bd=0)
trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)

#####################################################################################################################################
#########################Report###################################################################

square_report_image=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/Report1.png')
report_background=Label(image=square_report_image,bg=background)
report_background.place(x=1000,y=250)

report=Label(root,font='arial 21 bold',bg='white',fg='#8dc63f')
report.place(x=1050,y=460)

report1=Label(root,font='arial 8 bold',bg='white',fg='#8dc63f')
report1.place(x=1010,y=520)


####################################################################################
################################Graph#######################
graph_image=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/graphh.png')
Label(image=graph_image).place(x=530,y=190)
Label(image=graph_image).place(x=770,y=190)
Label(image=graph_image).place(x=530,y=420)
Label(image=graph_image).place(x=770,y=420)

#######################333333333334button######################
Label(root,text='Visualization',background='#df2d4b',fg='white',font='arial 20').place(x=650,y=140)

analysis_button=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/Analysis2.png')
Button(root,image=analysis_button,bd=0,bg=background,cursor='hand2',command=analysis).place(x=1025,y=167)

info_button=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/info1.png')
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command=Info).place(x=1190,y=15)

#save_button=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/save1.png')
#Button(root,image=save_button,bd=0,bg=background,cursor='hand2',command=Save).place(x=1200,y=86)


###############smoking and non smokiing button

button_mode=True
choice='smoking'
def changemode():
    global button_mode
    global choice
    
    if button_mode:
        choice='non-smoking'
        mode.config(image=non_smoking_icon,activebackground='white')
        button_mode=False
    else:
        choice='smoking' 
        mode.config(image=smoking_icon,activebackground='white')
        button_mode=True 

    print(choice)

smoking_icon=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/smoker1.png')
non_smoking_icon=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/non-smoker1.png')

mode=Button(root,image=smoking_icon,bg='white',bd=0,cursor='hand2',command=changemode)
mode.place(x=330,y=400)    


##############################logout button######################
logout_icon=PhotoImage(file='C:/Users/KOMAL/Desktop/heart-attack-predcton-system/images/logout2.png')                                   
logout_button=Button(root,image=logout_icon,bg='#df2d4b',cursor='hand2',command=logout)
logout_button.place(x=1190,y=70)

root.mainloop()