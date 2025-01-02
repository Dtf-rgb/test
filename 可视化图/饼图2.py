import random
from pyecharts.charts import Pie
from pyecharts import options as opts

attr = ['A', 'B', 'C', 'D', 'E', 'F']
data = [random.randint(0, 100) for _ in range(6)]

pie = Pie()
pie.add(
    series_name="",
    data_pair=list(zip(attr, data)),
    radius=[50, 55],
    center=[80, 100],
    label_opts=opts.LabelOpts(is_show=True),
)
pie.add(
    series_name="",
    data_pair=list(zip(attr, data)),
    radius=[0, 45],
    center=[80, 100],
    rosetype="area",
    label_opts=opts.LabelOpts(is_show=True),
)
pie.add(
    series_name="",
    data_pair=list(zip(attr, data)),
    radius=[50, 55],
    center=[400, 100],
    label_opts=opts.LabelOpts(is_show=True),
)
pie.add(
    series_name="",
    data_pair=list(zip(attr, data)),
    radius=[0, 45],
    center=[400, 100],
    rosetype="radius",
    label_opts=opts.LabelOpts(is_show=True),
)

pie.render("饼图2.html")