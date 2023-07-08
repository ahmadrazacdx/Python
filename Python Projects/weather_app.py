import requests
import tkinter as tk
from tkinter import messagebox
def get_weather():
    API_KEY = '7cca0f8779be6597eb913fb93ad47468'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    city = city_entery.get()
    req_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
    response = requests.get(req_url)
    try:
        if response.status_code == 200:
            data = response.json()
            weather_desc = data['weather'][0]['description']
            global temp
            temp = float(data['main']['temp']) - 273.15
            temperature = round(temp, 2)

            weather_label.config(text='Weather: ' + weather_desc)
            temp_label.config(text=f"Temperature: {str(temperature)}°C")
        else:
            weather_label.config(text='No City Found', font=('Arial', 13))
            temp_label.config(text='')
    except requests.exceptions.RequestException as e:
        messagebox.showerror('Error',f'Error Occurred: {str(e)}')

def show_caution():
    if temp < 0:
        caution_label.config(text='⚠ Cautions: Extremely cold temperature!')
    elif temp >= 0 and temp <= 15:
        caution_label.config(text='⚠ Cautions:\n1. Cool weather!\n2. Watch for slippery surfaces.')
    elif temp > 15 and temp <= 30:
        caution_label.config(text='⚠ Cautions:\n1. Stay hydrated.\n2. Protect from sun.')
    elif temp > 30 and temp <= 40:
        caution_label.config(text='⚠ Cautions:\n1. Limit outdoor activities.\n2. Prevent heat exhaustion.')
    elif temp > 40 and temp <= 50:
        caution_label.config(text='⚠ Cautions:\n1. Avoid outdoor activities.\n2. Prevent heatstroke.')
    else:
        caution_label.config(text='⚠ Cautions:\n1. Extreme heat.\n2. Stay indoors!')


root = tk.Tk()
root.title('Weather App')
root.geometry('216x330')
root.resizable(False, False)

city_label = tk.Label(root, text='Enter City Name:', font=('Arial', 11))
city_label.grid(row=1, column=1, padx=10, pady=8)

city_entery = tk.Entry(root, width=22, font=('Arial', 11), bd=2, highlightthickness=1, highlightbackground='gray')
city_entery.grid(row=2, column=1, pady=5)

weather_button = tk.Button(root, text='Get Weather', command=get_weather, padx=8, pady=2)
weather_button.grid(row=3, column=1, pady=10)

weather_label = tk.Label(root, text='', font=('Arial', 12))
weather_label.grid(row=4, column=1)

temp_label = tk.Label(root, text='', font=('Arial', 11))
temp_label.grid(row=5, column=1)

show_caution_button = tk.Button(root, text='Show Cautions', command=show_caution, padx=8, pady=2)
show_caution_button.grid(row=6, column=1, pady=10)

caution_label = tk.Label(root, text='', font=('Arial', 11), fg='red', height=5, width=22, bd=2,
highlightthickness=2, highlightbackground='gray')
caution_label.grid(row=7, column=1, padx=5, pady=5)

root.mainloop()
