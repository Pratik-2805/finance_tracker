import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV:
    CSV_file = "finance_data.csv"
    COLUMNS = ["date","amount","category","description"]

    @classmethod # initialize the new csv file
    def ini_csv(cls):
        try:
            pd.read_csv(cls.CSV_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMNS)
            df.to_csv(cls.CSV_file, index=False)

    @classmethod # adding the entry into the csv file
    def add_entry(cls, date, amount, category, description): #its a dictionary that will add the data into the csv file
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }
        with open(cls.CSV_file, "a",newline = "") as csvfile: #With with open and close the file and a will append new items into the csv file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added Successfully")

def add():
    CSV.ini_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or just click enter for today's date: ",allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

add()
