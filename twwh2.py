import pandas as pd
import os
from tkinter import filedialog
from tkinter import messagebox

print('import main tsv...')
main_tsv = filedialog.askopenfilename(initialdir="/", title = "main")
main = pd.read_csv(main_tsv, sep='\t', header=1)

import tossi
def tossier(inputstring):
  str2 = '@'
  while str2 in inputstring:
    b = inputstring.find(str2)
    pre_tossied = inputstring[b-1:b+3]
    x = inputstring[b-1:b]
    y = inputstring[b+1:b+3]
    yB = False

    try:
      if y[0] == "'":
        y = y[1:]
        x = x + "'"
      if y[-1] == ' ':
        y = y.rstrip()
        yB = True
    except:
      pass

    try:
      tossied = tossi.postfix(x, y)
      if yB == True:
        tossied = tossied + ' '
      inputstring = inputstring.replace(pre_tossied, tossied)
    except:
      tossied = pre_tossied
      exceptionPass = pre_tossied.replace('@', '')
      inputstring = inputstring.replace(pre_tossied, exceptionPass)

  return inputstring

print('import dictionary tsv...')
dict_tsv = filedialog.askopenfilename(initialdir="/", title = "dictonary")
import csv
with open(dict_tsv, newline='', encoding='UTF-8') as f:
  reader = csv.DictReader(f, delimiter='\t')
  dicts = {rows['key']:rows['value']+'@' for rows in reader}

print('replacing values...')
n = 1
for keys, values in dicts.items():
  main['text'] = main['text'].str.replace(keys, values, regex=False)
  print('\r%d/%d'%(n,len(dicts.keys())), end='')
  n += 1
print('')
main_text = main[main['text'].str.contains('@', na=True)]
main_text = main_text.dropna()

print('correcting postpositions...')
# for i in main_text.index.values:
#   print(i)
#   try:
#     print = tossier(main['text'].iloc[i])
#   except:
#     pass
n2 = 1
for i in main_text.index.values:
#   prestring = main['text'].iloc[i]
#   poststring = tossier(prestring)
  main['text'].iloc[i] = tossier(main['text'].iloc[i])
  print('\r%d/%d'%(n2,len(main_text.index.values)), end='')
  n2 += 1
print('')

print('exporting tsv file...')
main.to_csv('exported.tsv', sep='\t', index=False)
print('export complete')

