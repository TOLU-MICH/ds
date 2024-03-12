
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./exercise 1/djia.csv')

plt.figure(figsize=(10, 7))
plt.plot(df['Date'], df['Price'], marker='o', linestyle='-', color='b')
plt.title('DJIA Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.show()