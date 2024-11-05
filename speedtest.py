from tkinter import *
from speedtest import Speedtest

def test():
    text = Label(my_app, text='Проводим тестирования, пожалуйста, подождите..', font=35)
    text.pack()
    test_handler = Speedtest()
    download = test_handler.download()
    upload = test_handler.upload()
    result = {"download":round(download / (10**6), 2), 'upload':round(upload / (10**6), 2)}
    download_label.config(text=f'Скорость загрузки:\n{result["download"]} MbPs')
    upload_label.config(text=f'Скорость отдачи:\n{result["upload"]} MbPs')
    text.destroy()

my_app = Tk()

my_app.title('Florest App')

my_app.geometry('300x400')

button = Button(my_app, text='Нажать, чтобы начать', font=40, command=test)

button.pack(side=BOTTOM, pady=40)

download_label = Label(my_app, text=f'Скорость загрузки:\n-', font=35)
download_label.pack(pady=(50, 0))
upload_label = Label(my_app, text='Скорость отдачи:\n-', font=35)
upload_label.pack(pady=(10, 0))

my_app.mainloop()