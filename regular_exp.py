import pandas as pd
import numpy as np

ds = pd.DataFrame(np.random.choice([0.9,4.1,'t2t3','2tn',np.nan], size=(20,5)),columns=['fir','sec','thir','4th','5th'])

# list down two columns where string begins with 't'
print(ds.loc[:,['fir','5th']][ds.fir.str.contains('^t')])

# print all rows where fir column value doesn't start with 't'
print(ds.ix[ds.fir.str.match(r'[^t]')])

# recognise floats
print(ds.ix[ds.fir.str.match(r'^\d*\.*\d*$')])

# list down all rows in one 'fir' column where there is digit on any of the position
print(ds.ix[ds.fir.str.match(r'[0-9]')])

# print(ds)

#list all the rows where digit is the first char and rest is a-z
print(ds.ix[ds.fir.str.match(r'\d[a-z]')])

#prints the same as above except it also check 'sec' column
print(ds.ix[ds.fir.str.match(r'\d[a-z]') | ds.sec.str.match(r'\d[a-z]') ])

# list all columns where 1st col 1st char contains dig and 2nd contain only digits
print(ds.ix[ds.fir.str.match(r'\d[a-z]') | ds.sec.str.match(r'[a-z]') ])

# list down all columns where string match 1st is digit than two letters
print(ds.ix[ds.fir.str.match(r'\d[a-z]{2}')])

# print(ds)

# print(ds.loc[:,'4th':'5th'][ds['4th'] == 4])
# print(ds[pd.isnull(ds).any(axis=1)])
#print(ds[ds['stq'].str.contains('\?')])


####################################################
# \d - reprezents any number
# \D - anythig but a number
# \s - space
# \S - anything byt a space
# \w - any character (any letter)
# \W - anything but a character
# . anything but a new line
# \b - space followed by word
# ? - 0 or 1 repetition
# * - 0 to multi repetitions
# {3} - three occurrences in a row
# \d{1,5} - 1 to 5 digits in a row
# \s - space
# \w+ - one or more characters (w = any character)
# \. - dot is expected
# calend[ae]r - search for words calendar and calender
# [a-z][1-9][A-Za-z0-9] - characters from these ranges
#####################################################