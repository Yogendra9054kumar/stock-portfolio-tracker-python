# Stock Portfolio Tracker

#Stock prices
stock_prices = {
    'AAPL': 180,
    'TSLA': 250,
    'GOOGLE': 140,
    'MSFT': 320
}

portfolio = {}
total_investment = 0

# User input
n = int(input("Enter number of stocks : "))

for i in range(n):
    stock_name = input("Enter stock name (AAPL/TSLA/GOOGLE/MSFT): ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        portfolio[stock_name] = quantity
        total_investment += stock_prices[stock_name] * quantity
    else:
        print("Stock not found!")

# Output

print("\n--- Stock Portfolio ---")
for stock, qty in portfolio.items():
    print(stock, ":", qty, "shares")

print("Total Investment Value:", total_investment)

# Save file
choice = input("Save result to file?\n(yes/no): ").lower()

if choice == "yes":
    file_choice = input("Enter file type (txt/csv): ").lower()

    if file_choice == "txt":
        file = open("portfolio.txt", "w")
        file.write("Stock Portfolio\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock} {qty} {stock_prices[stock]}\n")
        file.write(f"Total Investment: {total_investment}")
        file.close()
        print("Saved to portfolio.txt")

    elif file_choice == "csv":
        file = open("portfolio.csv", "w")
        file.write("Stock,Quantity,Price\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock},{qty},{stock_prices[stock]}\n")
        file.write(f"Total,,{total_investment}")
        file.close()
        print("Saved to portfolio.csv")

    else:
        print("Invalid file type")

print("Program Finished")
