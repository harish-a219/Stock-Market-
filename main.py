import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

stock_input = input('Enter a stock ticker symbol of your choice. Remember, it must be valid')
tsla = yf.Ticker(stock_input)

tsla.info

hist = tsla.history(period="1y")

prices =  []
for i in range (0,252):
     prices.append(hist["Close"][i]) #adds the prices of the stocks to the empty list defined above

#Array means list in numpy
days =[]
for i in range (0,252): #Data for 1 year of the stock
    days.append(i)      #We are now adding the data of the stock into the empty list, days.

x = np.array(days)     
y = np.array(prices)
# print(x,y)
plt.plot(x,y) #Plt = graphing function, plot = plotting the points function (x,y)

average14_list = []
#Calculating moving average 
for i in range (0, 252, 14): #This is the for loop calculating every 14 days
     total14  = 0
     for j in range (i,i+13): #This is the for loop for calculating every day in that 14 day for the average.
        total14 += (hist["Close"][j])

     average14 = total14/14 
     average14_list.append(average14)
print(average14_list)


average7_list = []
#Calculating moving average 
for i in range (0, 252, 7): #This is the for loop calculating every 7 days
     total7  = 0
     for j in range (i,i+6): #This is the for loop for calculating every day in that 7 day for the average.
        total7 += (hist["Close"][j])

     average7 = total7/7 
     average7_list.append(average7)

#This plots the 14 day moving avg.
a_list = []
for i in range (0,252,14):
    a_list.append(i)
plt.plot(a_list,average14_list)

#This plots the 7 day moving average
b_list = []   
for i in range (0,252,7):
     b_list.append(i)
plt.plot(b_list,average7_list)

if average7_list[-1] > average14_list[-1]: #-1 gives you the last value in the list. We need this because we need to compare the last value of the list to see if it is worthy to buy
    print("Buy!")


plt.title("7 and 14 day Moving Average Graph With Stock Price.") #creates title
plt.xlabel("Days") #Labels x axis
plt.ylabel("Prices") #Labels y axis
plt.legend(["stock price", "14 day moving average", "7 day moving average"]) #Creates legend
plt.show() #.show prints it onto your screeng

#This is to show if the stock is increasing or decreasing
counter = 0
for i in range (0,3):
    if (tsla.growth_estimates["stock"][i]) > 0: 
     counter +=1
if counter == 3:
  print("This stock is projected to increase in value.")
else:
    print("This stock is projected to decrease in value.")


#Analysts recommendations on what to do with the stock.
strongBuy = []
buy = []
hold = []
sell = []
strongSell = []

for i in range (0,4):
     strongBuy.append(tsla.recommendations["strongBuy"][i])
     buy.append(tsla.recommendations["buy"][i])
     hold.append(tsla.recommendations["hold"][i])
     sell.append(tsla.recommendations["sell"][i])
     strongSell.append(tsla.recommendations["strongSell"][i])

strongbuy = sum(strongBuy)
Buy = sum(buy)
Hold = sum(hold)
Sell = sum(sell)
strongsell = sum(strongSell)

if strongbuy > Buy and strongbuy > Hold and strongbuy > Sell and strongbuy > strongsell:
     print("Most analysts would recommend strongly buying this stock at this time.")
if Buy > strongbuy and Buy > Hold and Buy > Sell and Buy > strongsell:
    print("Most analysts would recommend buying this stock at this time.")
if Hold > strongbuy and Hold > Buy and Hold > Sell and Hold > strongsell:
    print("Most analysts would recommend holding this stock at this time.")
if Sell > strongbuy and Sell > Buy and Sell > Hold and Sell > strongsell:
    print("Most analysts would recommend selling this stock at this time.")
if strongsell > strongbuy and strongsell > Buy and strongsell > Hold and strongsell > Sell:
    print("Most analysts would strongly recommend selling this stock at this time.")


#tsla.eps_trend code

first_row = []
next_quarter = []
next_year = []

for i in ["current","30daysAgo", "90daysAgo"]:
    first_row.append(tsla.eps_trend[i][0])
    next_quarter.append(tsla.eps_trend[i][1])
    next_year.append(tsla.eps_trend[i][3])

if next_year[0] > next_quarter[0] and next_year[0] > first_row[0]:
    print("This stock's EPS values suggest it that you buy it sometime in the next year.")
elif next_quarter[0] > first_row[0] and next_quarter[0] < next_year[0]:
    print("This stock's EPS values suggest that you consider buying it for a slight profit in the next year.")
else:
    print("This stock's EPS values suggest that you don't buy this stock for the next year.")


#tsla.earnings_estimate code
if tsla.earnings_estimate.loc["0q", "growth"] > 0:
    print("This is shown by a"  + str((tsla.earnings_estimate["growth"][0]*100)) + "" + "percent increase in EPS values.")
else:
    print("This is shown by a" + str((tsla.earnings_estimate["growth"][0]*100)) + "" + "percent decrease in EPS values.")
