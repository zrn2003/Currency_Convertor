import requests
import tkinter as tk
from tkinter import messagebox

def get_exchange_rate(api_key, base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "conversion_rates" in data:
            rates = data["conversion_rates"]
            if target_currency in rates:
                return rates[target_currency]
            else:
                return None
        else:
            return None
    else:
        return None

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def on_convert_button_click():
    try:
        base_currency = base_currency_entry.get().upper()
        target_currency = target_currency_entry.get().upper()
        amount = float(amount_entry.get())

        api_key = 'xxxxxxxxxxxxxxxxxxxxxxxx'

        exchange_rate = get_exchange_rate(api_key, base_currency, target_currency)

        if exchange_rate:
            converted_amount = convert_currency(amount, exchange_rate)
            result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            messagebox.showerror("Error", "Unable to fetch exchange rates.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the amount.")

root = tk.Tk()
root.title("Currency Converter")

root.geometry("400x300")
root.config(bg="#f2f2f2")

title_label = tk.Label(root, text="Currency Converter", font=("Arial", 18, "bold"), bg="#f2f2f2")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

base_currency_label = tk.Label(root, text="Base Currency:", font=("Arial", 12), bg="#f2f2f2")
base_currency_label.grid(row=1, column=0, padx=10, pady=5)
base_currency_entry = tk.Entry(root, font=("Arial", 12))
base_currency_entry.grid(row=1, column=1, padx=10, pady=5)
base_currency_entry.insert(0, "USD")

target_currency_label = tk.Label(root, text="Target Currency:", font=("Arial", 12), bg="#f2f2f2")
target_currency_label.grid(row=2, column=0, padx=10, pady=5)
target_currency_entry = tk.Entry(root, font=("Arial", 12))
target_currency_entry.grid(row=2, column=1, padx=10, pady=5)
target_currency_entry.insert(0, "EUR")

amount_label = tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f2f2f2")
amount_label.grid(row=3, column=0, padx=10, pady=5)
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.grid(row=3, column=1, padx=10, pady=5)
amount_entry.insert(0, "1.0")

convert_button = tk.Button(root, text="Convert", font=("Arial", 14), bg="#4CAF50", fg="white", command=on_convert_button_click)
convert_button.grid(row=4, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f2f2f2")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
