import pandas

pd=pandas.read_csv('News.csv',encoding='utf-8')
print(pd.head(10)['title'])
