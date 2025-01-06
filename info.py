from tkinter import *

roots=Tk()
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