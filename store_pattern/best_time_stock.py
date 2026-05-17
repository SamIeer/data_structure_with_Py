def best_time_stock(arr:list)->int:
    profit=0
    buy=arr[0]
    for i in arr:
        buy = min(buy, i)
        profit = max(profit, i-buy)
    return profit

print(best_time_stock([7,1,5,3,6,4,15]))
        