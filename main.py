import tkinter as tk
import requests
import datetime

def get_covid_data():
    api_url = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api_url).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)

    label.config(text = "Total Cases: "+total_cases+
    "\n"+"Total Deaths: "+total_deaths+
    "\n"+"Today Cases: "+today_cases+
    "\n"+"Today Deaths: "+today_deaths+
    "\n"+"Today Recovered: "+today_recovered)

    label2.config(text = date)



window = tk.Tk()
window.title("COVID-19 Tracker")
window.geometry("300x200")

label = tk.Label(window)
label.pack(pady=20)
label2 = tk.Label(window, font=8)
label2.pack()

button = tk.Button(window, text="Get Data", command=get_covid_data)
button.pack()

window.mainloop()