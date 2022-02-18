import pandas as pd
import csv
import os
import tossi
from tkinter import filedialog
from tkinter import messagebox
pd.set_option('mode.chained_assignment',  None)

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

print('[1] main.tsv 파일을 불러오는 중')
main_tsv = './main.tsv'
try:
  main = pd.read_csv(main_tsv, sep='\t', header=0)
except:
  print('폴더에서 main.tsv 파일을 찾지 못했습니다. 직접 파일을 선택해주세요.')
  main_tsv = filedialog.askopenfilename(initialdir="./", title = "main")
  main = pd.read_csv(main_tsv, sep='\t', header=0)
print('불러오기 완료')

print('[2] dict.tsv 파일을 불러오는 중')
dict_tsv = './dict.tsv'
try:
  with open(dict_tsv, newline='', encoding='UTF-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    dicts = {rows['key']:rows['value']+'@' for rows in reader}
except:
  print('폴더에서 dict.tsv 파일을 찾지 못했습니다. 직접 파일을 선택해주세요.')
  dict_tsv = filedialog.askopenfilename(initialdir="./", title = "dictonary")
  with open(dict_tsv, newline='', encoding='UTF-8') as f:
    reader = csv.DictReader(f, delimiter='\t')
    dicts = {rows['key']:rows['value']+'@' for rows in reader}
print('불러오기 완료')

print('[3] 찾아 바꾸기 처리중')
n = 1
for keys, values in dicts.items():
  main['text'] = main['text'].str.replace(keys, values, regex=False)
  print('\r%d/%d'%(n,len(dicts.keys())), end='')
  n += 1
print(' 완료')
main_text = main[main['text'].str.contains('@', na=True)].dropna()

print('[4] 조사 처리중')
# for i in main_text.index.values:
#   print(i)
#   try:
#     print = tossier(main['text'].iloc[i])
#   except:
#     pass
n2 = 1
for i in main_text.index.values:
  prestring = main['text'].iloc[i]
  poststring = tossier(prestring)
  main['text'].iloc[i] = tossier(main['text'].iloc[i])
  print('\r%d/%d'%(n2,len(main_text.index.values)), end='')
  n2 += 1
print(' 완료')

print('[5] exported.tsv 파일로 내보내는 중')
firstrow = {'Loc', 'PackedFile 1', ''}
main.to_csv('exported.tsv', sep='\t', index=False)
# with open('./exported.tsv', 'rb+') as fp:
#   file_text = fp.read()
#   fp.seek(0)
#   fp.write(b'Loc\tPackedFile 1\n' + file_text)
print('내보내기 완료')
