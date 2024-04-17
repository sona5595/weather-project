"""
from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import*
import requests 
import pytz
from PIL import Image,ImageTk

root = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg="#57adff")
root.resizable(False,False)


##icon
image_icon=PhotoImage(file=r"C:\Users\Sonali Mahato\OneDrive\Desktop\weather project\logo.png")
root.iconphoto(False,image_icon)

Round_box = PhotoImage(file=r"C:\Users\Sonali Mahato\OneDrive\Desktop\weather project\rectangle_img.png")
Label(root,image=Round_box,bg= "#57adff").place(x=30,y=110)

#label
label1=Label(root,text="Temperature",font=("Helvetica",11),fg="white",bg="#203243")
label1.place(x=0,y=120)

label2=Label(root,text="Humidity",font=("Helvetica",11),fg="white",bg="#203243")
label2.place(x=0,y=120)

label3=Label(root,text="pressure",font=("Helvetica",11),fg="white",bg="#203243")
label3.place(x=0,y=120)

label4=Label(root,text="Wind Speed",font=("Helvetica",11),fg="white",bg="#203243")
label4.place(x=0,y=120)

label5=Label(root,text="Description",font=("Helvetica",11),fg="white",bg="#203243")
label5.place(x=0,y=120)

"""


from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False,False)

def getWeather():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home = pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %P")
    clock.config(text=current_time)

##########Weather##########

api = "https://api.openweathermap.org/data/3.0/onecall/timemachine?lat"+str(location.latitude)+"&lon="+str(location.longitude)+"&dt=1643803200&appid=f2887cc020ea65601b3df89d21af4db2"
json_data = requests.get(api).json()

##########Current##########

temp = json_data['current']['temp']
humidity = json_data['current']['humidity']
pressure = json_data['current']['pressure']
wind = json_data['current']['wind speed']
description = json_data['current']['weather'][0]['description']
"""
print(temp)
print(humidity)
print(pressure)
print(wind)
print(description)
"""
t.config(text=(temp,"°C"))
h.config(text=(humidity,"%"))
p.config(text=(pressure,"hpa"))
w.config(text=(wind,"m/s"))
d.config(text=description)

##########icon##########

image_icon=PhotoImage(file="Weather Conditions - OpenWeatherMap_files/e75616098a16b28bbc620124c5f94aa2.jpg")   ###image
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="Weather Conditions - OpenWeatherMap_files/images.png")    ###image
Label(root,image=Round_box,bg="#57adff").place(x=30,y=110)

##########label-1###########

label1=Label(root,text="Temperature",font=('Helvetice',11),fg="white",bg="#203243")
label1.place(x=50,y=120)

label2=Label(root,text="Humidity",font=('Helvetice',11),fg="white",bg="#203243")
label2.place(x=50,y=140)

label3=Label(root,text="Pressure",font=('Helvetice',11),fg="white",bg="#203243")
label3.place(x=50,y=160)

label4=Label(root,text="Wind Speed",font=('Helvetice',11),fg="white",bg="#203243")
label4.place(x=50,y=180)

label5=Label(root,text="Description",font=('Helvetice',11),fg="white",bg="#203243")
label5.place(x=50,y=200)

##########Search Box##########

Search_image=PhotoImage(file="360_F_223046441_q3XSGr4pdWNbE4M55UKE1mL6l4kWCpxt.jpg")     ###image
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=270,y=120)

weat_image=PhotoImage(file="")     ###image
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=290,y=127)

textfield=tk.Entry(root,justify='center',width=15,font=('poppins',25,'bold'),bg="#203243",border=0,fg="white")
textfield.place(x=370,y=130)
textfield.focus()

Search_icon=PhotoImage(file="")     ###image
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=645,y=125)

##########Bottom Box##########

frame=Frame(root,width=900,height=180,bg="#212120")
frame.pack(side=BOTTOM)

##########Bottom Boxes##########

firstbox=PhotoImage(file="")
secondbox=PhotoImage("")

label1(frame,image=firstbox,bg="#212120").place(x=30,y=20)
label1(frame,image=secondbox,bg="#212120").place(x=300,y=30)
label1(frame,image=firstbox,bg="#212120").place(x=400,y=30)
label1(frame,image=firstbox,bg="#212120").place(x=500,y=30)
label1(frame,image=firstbox,bg="#212120").place(x=600,y=30)
label1(frame,image=firstbox,bg="#212120").place(x=700,y=30)
label1(frame,image=firstbox,bg="#212120").place(x=800,y=30)

##########Clock (here we will place time)##########

clock=Label(root,text="2 : 30 pm",font=("Helvetica",30,'bold'),fg="white",bg="#57adff")
clock.place(x=30,y=20)

##########Timezone##########
timezone=Label(root,font=("Helvetica",20),fg="white",bg="#57adff")
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg="white",bg="#57adff")
long_lat.place(x=700,y=50)

##########thpwd##########

t = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=150,y=120)

h = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=150,y=140)

p = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=150,y=160)

w = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=150,y=180)

d = Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=150,y=200)

##########first cell##########



#########second cell###########



##########third cell###########



##########fourth cell##########



##########fifth cell##########



##########sixth cell##########



##########seventh cell##########





root.mainloop()


"""

api = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=f2887cc020ea65601b3df89d21af4db2"
json_data = requests.get(api).json()

#current
temp = json_data['current']['temp']
print(temp)





## search box
Search_image=PhotoImage(file="")
root.mainloop()"""