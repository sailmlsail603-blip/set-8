import statistics as st
data=[90,50,70,80,70,60,20,30,80,90,20]
print("Mean is:",st.mean(data))
print("Median is:",st.median(data))
print("Mode is:",st.mode(data))
data.sort()
print("2nd largest:",data[-3])
print("3rd lowest:",data[3])
print(data)