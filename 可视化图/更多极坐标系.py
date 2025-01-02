import math
from pyecharts.charts import Polar

data =[]
for i in range(101):
    theta =i /100*360
    r =5*(1+math.sin(theta /180*math.pi))
    data.append([r, theta])
    hour =[i for i in range(1, 25)]
polar =Polar()
polar.add("Love", data)
polar.render("更多图极坐标系.html")