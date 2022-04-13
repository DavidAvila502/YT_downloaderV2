import os
import tkinter
from typing import TextIO
from tkinter import*
import pytube


#CARGA DE RUTA


#Obtenemos la direccion de este script
actualdirectory = __file__


actualdirectory= str(actualdirectory)

#Asiganamos el caracter especial a reemplazar
especial = """ \ """
#Guaradmos unicamente el caracter sin los espaciaos
especial = especial[1]

#Reemplaza las \ por / para que funcione el dierectorio
actualdirectory  =    actualdirectory.replace(especial,"""/""")

#Ahora reemplazamos la ubicacion de este escript por la de la data de rutas
actualdirectory = actualdirectory.replace("/YT_downloader_v2.py","/data.txt")
 
#Intentamos cargar la ruta del archivo tx, en caso de no encontrar nada cargar con "" la variable ruta_load
try:
    with open(actualdirectory) as rutatext:
        ruta_load = rutatext.read()
except FileNotFoundError:
    print("Archivo de direcciones no encontrado...")
    ruta_load=""

#Esta funcion creara el archivo txt con la ruta introducida mas recientemente en caso de que este
# archivo no exista, y si existe lo sobreescribe con la nueva ruta
def ruta_create():
     ruta_data = ruta.get()
     newfile = open(actualdirectory,"w")
     newfile.write(ruta_data)
     newfile.close
     #pass




#DESCARGA DE VIDEO Y AUDIO





#Descarga en HD calidad(720p)
def descarga_video_720():

    url_data = url.get()
    ruta_data = ruta.get()
    youtube = pytube.YouTube(url_data)
    video= youtube.streams.get_by_itag(22)
    #video.download()
    video.download(output_path=ruta_data)

    ruta_create()

    url_entry.delete(0,END)

#Descarga en calidad baja (360p)
def descarga_video_360p():

    url_data = url.get()
    ruta_data = ruta.get()
    youtube = pytube.YouTube(url_data)
    video= youtube.streams.get_by_itag(18)
    #video.download()
    video.download(output_path=ruta_data)

    ruta_create()
    url_entry.delete(0,END)

#Descargar solo el audio musica(128kbps) calidad baja
def descarga_audio_128kbps():

     url_data = url.get()
     ruta_data = ruta.get()
     youtube = pytube.YouTube(url_data)
     video = youtube.streams.get_by_itag(140)
     out_file = video.download(output_path=ruta_data)
     base, ext = os.path.splitext(out_file)
     new_file = base + '.mp3'
     os.rename(out_file, new_file)
     
     ruta_create()
     url_entry.delete(0,END)


#Descargar solo el audio musica(160kbps) Calidad Alta

def descarga_audio_160kbps():

    url_data = url.get()
    ruta_data = ruta.get()
    youtube = pytube.YouTube(url_data)
    video = youtube.streams.get_by_itag(251)
    out_file = video.download(output_path=ruta_data)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    ruta_create()

    url_entry.delete(0,END)









#CREACION DE LA VENTANA





window = Tk()
#Crea las dimensiones de la ventana de la interfaz
window.geometry("650x550")
#Agrega el titulo a la ventana
window.title("Downloader YT 2.0")
#Evita que el usuario pueda ridemencionar los tamaños de las ventanas
window.resizable(False,False)
#Coloca color al fondo
window.config(background="#D5413E")

#Crea el titulo y lo coloca arriba al centro
main_title = Label(text="YT Downloader",font=("Arial Black",13),bg="#AF2825",fg="white",width="550",height="2")
main_title.pack()






#Descarga de video Interfaz



#Variables de la aplicacion
url=StringVar()
ruta = StringVar()



#Crea un label URL
url_label= Label(text="Url",bg="#D5413E",foreground="#FFFFFF",width="3",height="2",font=("Copperplate Gothic Bold",11))
#Posiciona el label URL
url_label.place(x=82,y=80)



#Crear campo de texto para el Url
url_entry=Entry(textvariable=url,width="46",font=("Lucida Console",12))
#Posiciona el campo de texto
url_entry.place(x=130,y=90)



#Crear elementos de la ruta


#Crea un label Ruta
ruta_label= Label(text="Ruta (opcional)",bg="#D5413E",foreground="#FFFFFF",width="12",height="2",font=("Copperplate Gothic Bold",10))
#Posiciona el label URL
ruta_label.place(x=82,y=140)



#Crear campo de texto para la Ruta
ruta_entry=Entry(textvariable=ruta,width="38",font=("Lucida Console",12))
#Posiciona el campo de texto
ruta_entry.place(x=210,y=150)

ruta_entry.insert(0,ruta_load)#Muestra la ruta que cargo del archivo txt



#BOTONES


#Crea un boton
Download =Button(window,text="Download(720p)",command=descarga_video_720,width="30",height="2",bg="#AF2825",foreground="#FFFFFF",font=("Copperplate Gothic Bold",10))
#Posiciona el boton
Download.place(x=30,y=200)


#Crea boton de desarga en baja calidad 360p
Download2 =Button(window,text="Download(360p)",command=descarga_video_360p,width="30",height="2",bg="#AF2825",foreground="#FFFFFF",font=("Copperplate Gothic Bold",10))
#Posiciona el boton
Download2.place(x=320,y=200)


#PARA DESCARGAR AUDIO Interfaz

#Crea un label de separacion para el audio
label_audio= Label(text="Descarga de Audio",bg="#AF2825",foreground="#FFFFFF",width="72",height="3",font=("Copperplate Gothic Bold",10),anchor="center")
#Posiciona el label URL
label_audio.place(x=0,y=270)

#label_audio.pack()



#Boton de descarga en 128bps
Download3 =Button(window,text="Download(audio 128kps)",command=descarga_audio_128kbps,width="30",height="2",bg="#AF2825",foreground="#FFFFFF",font=("Copperplate Gothic Bold",10))
#Posiciona el boton
Download3.place(x=320,y=350)



#Boton de descarga en 160bps
Download4 =Button(window,text="Download(audio 160kps)",command=descarga_audio_160kbps,width="30",height="2",bg="#AF2825",foreground="#FFFFFF",font=("Copperplate Gothic Bold",10))
#Posiciona el boton
Download4.place(x=30,y=350)








#Lanza la ventana (Toda la aplicacion)
window.mainloop()
