def two_sum(arr:list,k:int)->list:
    seen = {}
    for i in range(len(arr)):
        n = k - arr[i]
        if n in seen:
            return [seen[n],i]
        seen[arr[i]] = i
    return 0

print(two_sum([2,7,11,15],9))

''''
So In this problem we have to find the index of two 
elements from the array which give us the trageted 
number 
it can be sovled with brute force that has O(n**2)
that would be not bad but not good too
so we have to look clearly about the problem and use basci maths 
of substractions and storing the each element we have visted in the 
dict 
so in end we will get time of O(n) and space O(1) to O(K) in worst it would be 
O(n)
'''