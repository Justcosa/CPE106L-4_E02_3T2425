import requests
import tkinter as tk
from tkinter import ttk

base_url = "https://ghoapi.azureedge.net/api/Indicator?$filter=contains(IndicatorName,%20%27Mental%20Health%27)"

def fetch_data():
    response = requests.get(base_url)
    data = response.json()
    # Exclude 'Language' column
    items = data.get('value', [])
    for item in items:
        item.pop('Language', None)
    return items

def show_data():
    items = fetch_data()
    if not items:
        return
    # Exclude 'IndicatorCode' from columns
    columns = [key for key in items[0].keys() if key != 'IndicatorCode']
    tree = ttk.Treeview(root, columns=columns, show='headings')
    for col in columns:
        tree.heading(col, text=col)
    for item in items:
        # Only show values for columns excluding 'IndicatorCode'
        tree.insert('', tk.END, values=[item[col] for col in columns])
    tree.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
root.title("Mental Health Indicators")
root.geometry("800x600")

show_data()

root.mainloop()
