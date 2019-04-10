import csv

def openSpendLog(filename):
  allDays = {}
  with open(filename, newline='') as csvfile:
    spendreader = csv.reader(csvfile, delimiter=',')
    for row in spendreader:
      thisRowDate = row[0] #This rows date.
      thisDay = allDays.get(thisRowDate, {}) #Gets the current day's dictionary
      
      thisRowCategory = row[2] #Get todays category
      thisRowSpend = float(row[1]) #How much was spent on this category

      # Get current spend in this category, and add this rows spend amount to it.
      thisDay[thisRowCategory] = thisDay.get(thisRowCategory,0.0) + thisRowSpend
      
      allDays[thisRowDate] = thisDay
  
  return allDays

def split_full_dict(fullDict, start=None, period=14):
  # check for starting date, otherwise first day available

  #timedelta, need to consider month...
  return None

def sum_up_by_category(alldayDict):
  totals = {}
  for daykey in alldayDict.keys():
    dayDict = alldayDict[daykey]
    for key, val in dayDict.items():
      totals[key] = totals.get(key, 0.0) + val

  return totals