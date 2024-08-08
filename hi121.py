import numpy as n
import pandas as p
d=p.DataFrame(
    {"date":p.date_range(start="2024-10-22",periods=5,freq="D"),"temp":n.random.randint(18,30,size=5)}
)
d["f"]=d["temp"].shift(1)
print("shift :\n",d)
dfw=d.resample("m",on="date").mean()
print("\n resamping:\n",dfw)