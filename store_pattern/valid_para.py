def valid_para(s:str)->bool:
    pairs={
        ')':'(',
        '}':'{',
        ']':'['
    }
    st = []
    for i in s:
        if i in "({[":
            st.append(i)
        elif not st or st[-1] != pairs:
            return False
        st.pop()
    return True
