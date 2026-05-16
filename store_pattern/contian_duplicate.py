def contain_dup(arr:list)->bool:
    seen = set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False