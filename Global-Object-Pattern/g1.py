import calendar
calendar.January = 13
print(calendar.January)

ZIP_FILECCOUNT_LIMIT = (1 << 16) - 1
print(ZIP_FILECCOUNT_LIMIT)

def _f(): pass
FunctionType = type(_f)
