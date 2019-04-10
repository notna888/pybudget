from main_functions.file_handling import *
from pprint import pprint

if __name__ == "__main__":
  entryLog = input('File to open [spending_log.csv] :') or 'spending_log.csv'
  spendingDict = openSpendLog(entryLog)
  pprint(sum_up_by_category(spendingDict))

  