# sales_report.py

import os
import csv
#import pdb

print("PROCESSING SOME CSV FILES HERE")

csv_filenames = os.listdir("data")

for filename in csv_filenames:
    filepath = f"data/{filename}"
    print("--------------------")
    print("Monthly Sales File: " + filepath)
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        all_sales = [float(row["sales price"]) for row in reader]
        monthly_sales = sum(all_sales)
        monthly_sales_usd = "${0:,.2f}".format(monthly_sales)
        print("... Total Sales: " + monthly_sales_usd)
