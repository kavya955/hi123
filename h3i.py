from matplotlib import pyplot as p
pro_na=["Intel","AMD","Snapdrangon","Tensor"]
use=[200,100,250,50]
p.bar(pro_na,use,color='black',width=0.2)
p.xlabel("processors"),p.ylabel("no of users")
p.title("processors user in a community")
p.show()
