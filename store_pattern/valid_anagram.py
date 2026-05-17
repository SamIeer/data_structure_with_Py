from collections import Counter
def valid_anagram(s:str, t:str)->bool:
    return (sorted(s) == sorted(t))

def valid_anagram(s:str, t:str)->bool:
    return (Counter(s) == Counter(t))

s = "anagram"
t = "nagara"

valid_anagram(s,t)