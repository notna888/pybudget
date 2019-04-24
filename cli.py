from main_functions.file_handling import *
from main_functions.analysis_functions import *

from pprint import pprint

def addEntry(file_name):
  pass



if __name__ == "__main__":
  entryLog = input('File to open [spending_log.csv] :') or 'spending_log.csv'
  spendingDict = openSpendLog(entryLog)
  catSet = openCatFile('categories.txt')
  pprint(catSet)
  pprint(sum_up_by_category(spendingDict))

  
