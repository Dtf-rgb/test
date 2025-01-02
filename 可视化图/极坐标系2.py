
import math
from pyecharts.charts import Polar
from pyecharts import options as opts

data = []
for i in range(361):
    t =i /180*math.pi
    r =math.sin(2*t) *math.cos(2*t)
    data.append([r, i])
polar = Polar()
polar.add(series_name="Love", data=data, type_="line")
polar.set_series_opts(area_color="#CD853F", area_opacity=0.4)
polar.set_global_opts(title_opts=opts.TitleOpts(title="极坐标系示例"))
polar.render("极坐标系2.html")