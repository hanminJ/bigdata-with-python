import csv
f= open('seoul.csv','r',encoding='cp949')
data = csv.reader(f,delimiter=',')
next(data)
max=0
#가장 더웠던 날은 언제일까
for row in data:
    if row[-1]=='':

        row[-1]=-999
    row[-1]=float(row[-1])
    if row[-1]>max :
        max=row[-1]
        date=row[0]
print(max)
print(date)
#일교차가 가장 큰 시기는 1년중 언제쯤일까?



f.close







#겨울에는 몇월이 가장 추울까?
#대구보다 서울이 더 더운날이 1년중 얼마나 있을까