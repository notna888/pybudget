

def split_full_dict(fullDict, start=None, period=14):
  # check for starting date, otherwise first day available
  #timedelta, need to consider month...
  if(start==None):
    pass
  if(period == 'month'):
    pass
  return None

def sum_up_by_category(alldayDict):
  totals = {}
  for daykey in alldayDict.keys():
    dayDict = alldayDict[daykey]
    for key, val in dayDict.items():
      totals[key] = round(totals.get(key, 0.0) + val,2)

  return totals
