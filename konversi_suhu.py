import tkinter as tk

jendela =tk.Tk()
jendela.title("conversi suhu")
jendela.geometry("300x400")

def hasil():
    suhu = float(imput_suhu.get())
    conver = (suhu*9/5)+32
    label_hasil.config(text=conver)

def hasil2():
    suhu = float(imput_suhu.get())
    conver = (suhu - 32)*5/9
    label_hasil.config(text=conver)


judul = tk.Label(jendela,text="PENGONVERSI SUHU")

imput_suhu = tk.Entry(jendela)

tombol = tk.Button(jendela,text="celcius", command=hasil)
tombol2 = tk.Button(jendela,text="ferenheat",command=hasil2)

label_hasil = tk.Label(jendela,text="hasil: ")
#struktuk semua
judul.pack()
imput_suhu.pack()
tombol.pack()
tombol2.pack()
label_hasil.pack()


jendela.mainloop()