from src import *

n = int(input())
for i in range(n):
    print(i+1,"-", report[i]['name'], report[i]['market_cap'])