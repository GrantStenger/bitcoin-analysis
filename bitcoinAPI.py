import pandas as pd
import os

# Read in DataFrame of prices
df = pd.read_csv("year_of_close_data.csv", encoding='latin1')

# Count how many days the stock was up, down, trending, and reversing
upCount = 0
downCount = 0
trendingCount = 0
reversalCount = 0
percentageMoveAfterUp = []
percentageMoveAfterDown = []
testPercentSum = 0
testPercentProduct = 1
upProduct = 1

# As compared with Day 1's price, decide is Day 2 is up or down
if df.loc[1, 'Close Price'] > df.loc[0, 'Close Price']:
	previousDay = "Up"
else:
	previousDay = "Down"

# Iterating through every day in the year, count up, down, trending, and reverals
for i in range(df['Close Price'].count() - 1):
	# Decide if today is up or down
	if df.loc[i+1, 'Close Price'] > df.loc[i, 'Close Price']:
		today = "Up"
		upCount += 1
	else:
		today = "Down"
		downCount += 1

	# Fill arrays holding the percentage increase or decrease if yesterday was up or down
	if previousDay == "Up":
		percentChange = (df.loc[i+1, 'Close Price'] / df.loc[i, 'Close Price'])-1
		print("The price when up " + '{:.2%}'.format(percentChange) + " today.")
		print("You were long.")
		percentageMoveAfterUp.append(percentChange)
		upProduct = upProduct * (percentChange+1)
	else:
		percentChange = (df.loc[i+1, 'Close Price'] / df.loc[i, 'Close Price'])-1
		print("The price when up " + '{:.2%}'.format(percentChange) + " today.")
		print("You were short.")
		percentageMoveAfterDown.append(percentChange)
	testPercentSum = testPercentSum + (df.loc[i+1, 'Close Price'] / df.loc[i, 'Close Price'])-1
	testPercentProduct = testPercentProduct*(df.loc[i+1, 'Close Price'] / df.loc[i, 'Close Price'])

	# Compare today with yesterday, if both are up or both are down, the stock is trending
	if today == previousDay:
		print(df.loc[i+1])
		print("Yesterday: " + previousDay)
		print("Today: " + today)
		print("Trending")
		trendingCount += 1
		print()
	# Otherwise, the stock is reversing
	else:
		print(df.loc[i+1])
		print("Yesterday: " + previousDay)
		print("Today: " + today)
		print("Reversal")
		reversalCount += 1
		print()

	# Make previous day today and repeate for the next day
	previousDay = today

# Print insights
os.system('clear')
print("Insights")
print()

print("Up Count: " + str(upCount))
print("Down Count: " + str(downCount))
totalUpDown = upCount + downCount
print("Up percentage: " + str('{:.1%}'.format(upCount/totalUpDown)))
print("Down percentage: " + str('{:.1%}'.format(downCount/totalUpDown)))

print()

print("Trending Count: " + str(trendingCount))
print("Reversal Count: " + str(reversalCount))
total = trendingCount + reversalCount
print("Trending percentage: " + str('{:.1%}'.format(trendingCount/total)))
print("Reversal percentage: " + str('{:.1%}'.format(reversalCount/total)))
print()

upSum = 0
downSum = 0
print("You were long for these: ")
for item in percentageMoveAfterUp:
	print('{:.2%}'.format(item))
	upSum = upSum + item

print()
print()
print()

print("You were short for these: ")
for item in percentageMoveAfterDown:
	print('{:.2%}'.format(item))
	downSum = downSum + item

print()
print()

print("Average daily return when long: " + '{:.2%}'.format(upSum/upCount))
print("Average daily return when short: " + '{:.2%}'.format(downSum/downCount))
print("testPercentProduct: " + '{:.2%}'.format(testPercentProduct))
print("Actual return: " + '{:.2%}'.format(df.loc[df['Close Price'].count() - 1, 'Close Price']/df.loc[0, 'Close Price']))
print("Return from just investing when up: " + '{:.2%}'.format(upProduct))
print()
if testPercentProduct > upProduct:
	print("Not a great strategy, would have made more just holding all year.")
else:
	print("Good. This strategy is better than simply holding all year.")
