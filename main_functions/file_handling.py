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

def openCatFile(filename):
  allCats = set()
  with open(filename, newline='') as catfile:
    for cat in catfile:
      allCats.add(cat.strip())
  return allCats

def append_entry(filename, dictOfEntry):
  with open(filename, newline='') as csvfile:
    spendreader = csv.reader(csvfile, delimiter=',')
    for row in spendreader:
      pass

def edit_most_recent_entry(filename):
  pass

def order_all_items_by_date(filename):
  pass

