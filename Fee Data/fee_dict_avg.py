import statistics as st
from dict_class import fee

def avg_value():
    values=[value for value in fee.values() if isinstance(value,int)]
    avg=st.mean(values)
    avg=round(avg,2)
    return avg