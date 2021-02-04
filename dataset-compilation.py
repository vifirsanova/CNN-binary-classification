import pandas as pd

def opener(path):
  with open(path) as f:
    data = f.read()
  return data

test0, test1, train0, train1 = opener('test0.txt').split('\n'), opener('test1.txt').split('\n'), opener('train0.txt').split('\n'), opener('train1.txt').split('\n')

test = pd.DataFrame.from_dict({'0': test0, '1': test1}, orient='index').transpose()
train = pd.DataFrame.from_dict({'0': train0, '1': train1}, orient='index').transpose()
