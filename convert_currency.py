import requests
import json
import os
from datetime import datetime , timedelta


def convert_currency(amount , from_currency , to_currency ):
    fetch_last_api_call_time()
    base , rates = reading_file()
    if from_currency==base:
        rate=rates.get(to_currency)
        if rate is None:
            raise ValueError(f"The exchange rate for {to_currency} is not available.")
        return amount*rate
    if to_currency==base:
        rate = rates.get(from_currency)
        if rate is None:
            raise ValueError(f"The exchange rate for {from_currency} is not available.")
        return amount/rate
    rate_from = rates.get(from_currency)
    rate_to = rates.get(to_currency)
    if rate_from is None or rate_to is None:
        raise ValueError(f"The exchange rate for {from_currency} or {to_currency} is not available.")
    return amount * (rate_to / rate_from)



def get_rates_from_api():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(url)
    try:
        if response.status_code==200:
            data = response.json()
            with open("rates.json" , "w" , encoding="utf-8") as f :
                json.dump(data , f, ensure_ascii=False , indent=4 )
    except requests.exceptions.RequestException as e:
        print(f"Error fetching rates from API: {e}")
        if os.path.exists("rates.json"):
            print("Using existing rates file.")
        else:
            print("No rates file available. Currency conversion won't work properly.")
    
    
def fetch_last_api_call_time():   
    max_age = timedelta(hours=1)
    if os.path.exists("rates.json") :
        last_modified = datetime.fromtimestamp(os.path.getmtime("rates.json"))
        now = datetime.now()
        if now - last_modified >max_age:
            print("Rates file outdated. Fetching new rates from API...")
            get_rates_from_api()
        else:
            print("Rates file is up to date.")
    else:
        print("Rates file not found. Fetching from API...")
        get_rates_from_api()   
 
def reading_file():
    with open("rates.json" , "r" , encoding="utf-8") as file:
        data = json.load(file)
        base = data.get("base")
        rates = data.get("rates")
    return base , rates
    
 
    
 
    