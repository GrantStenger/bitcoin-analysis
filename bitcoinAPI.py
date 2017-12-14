import pandas as pd
import os

# Read in DataFrame of prices
df = pd.read_csv("year_of_close_data.csv", encoding='latin1')

# Count how many days the stock was up, down, trending, and reversing
upCount = 0
downCount = 0
trendingCount = 0
reversalCount = 0

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