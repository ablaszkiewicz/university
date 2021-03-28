import numpy as np
import pandas as pd
import matplotlib.ticker as tick
from matplotlib import pyplot as plot

numbers_count = 1000
macd = np.zeros(numbers_count)
signal = np.zeros(numbers_count)
ema = np.zeros(numbers_count)
dema = np.zeros(numbers_count)
strength = np.zeros(numbers_count)
buy_ids = []
sell_ids = []

# file
file = pd.read_csv('wig20.csv').tail(numbers_count)
dates = file['Data'].to_numpy()
values = file['Zamkniecie'].to_numpy()

def past_average(N, index, array_of_values):
    sum = 0
    for i in range(N):
        sum += array_of_values[index-i]
    return sum/N

def exponential_moving_average(N, index, array_of_values):
    alpha = 2/(N+1)
    nominator = 0
    denominator = 0
    for i in range(N):
        nominator += (((1-alpha)**i)*array_of_values[index-N+i])
        denominator += (1-alpha)**i
    result = nominator/denominator
    return result


for i in range(26, numbers_count):
    macd[i] = exponential_moving_average(12, i, values) - exponential_moving_average(26, i, values)
    signal[i] = exponential_moving_average(9, i, macd)

    dema_n = 10
    ema[i] = exponential_moving_average(dema_n, i, values)
    dema[i] = 2*exponential_moving_average(dema_n, i, values) - exponential_moving_average(dema_n, i, ema)
    strength[i] = dema[i]
    if ((macd[i-1] - signal[i-1]) * (macd[i] - signal[i]) < 0):
        if (signal[i] > macd[i]):
            sell_ids.append(i)
        else:
            buy_ids.append(i)

strength /= np.max(strength)
dema[26:36] = dema[37]

start_capital = 1000
quantity = 0

for i in range(numbers_count):
    if (i in buy_ids):
        start_capital -= 0.1*values[i]
        quantity += 0.1
    if (i in sell_ids):
        start_capital += quantity*values[i]
        quantity = 0
start_capital += quantity*values[numbers_count - 1]
quantity = 0
print(start_capital)

# plot
loc = tick.MultipleLocator(base=40)
figure, axes = plot.subplots(1,1)
axes.xaxis.set_major_locator(loc)
plot.xticks(fontsize=8, rotation=45)
plot.xlabel('Date')
plot.ylabel("Value")
plot.subplots_adjust(bottom=0.2)
axes.plot(dates, macd, label="MACD")
axes.plot(dates, signal, label="SIGNAL")
axes.plot(dates, dema, label="DEMA")
#axes.plot(dates, strength, label="STRENGTH")
#axes.plot(dates, ema, label="EMA")
axes.plot(dates[buy_ids], values[buy_ids], 'go', label="BUY")
axes.plot(dates[sell_ids], values[sell_ids], 'ro', label="SELL")
axes.plot(dates, values, label="value")
axes.legend(loc='lower left', frameon=True)
plot.show()