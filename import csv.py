import csv

# Input: Data without INSERT INTO command
data = """

"""

# Column headers
headers = ['product_code', 'customer_code', 'market_code', 'order_date', 'sales_qty', 'sales_amount', 'currency']

# Cleaning the data
data = data.strip().strip('(),')
rows = [row.strip().strip('()').replace("'", "") for row in data.split('),')]

# Splitting each row by comma and trimming extra spaces
rows = [row.split(',') for row in rows]

# Writing to CSV
output_file = 'output.csv'
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # Writing headers
    writer.writerows(rows)    # Writing data

print(f"Data has been successfully written to {output_file}")