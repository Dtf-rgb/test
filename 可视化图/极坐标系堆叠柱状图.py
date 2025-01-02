from pyecharts import options as opts
from pyecharts.charts import Polar

data = [
    ("A", [1, 2, 3, 4, 3, 5, 1]),
    ("B", [2, 4, 6, 1, 2, 3, 1]),
    ("C", [1, 2, 3, 4, 1, 2, 5],),
]
categories = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
values = [data[i][1] for i in range(len(data))]


# 创建 Polar 实例
polar = (
    Polar()
    .add_schema(angleaxis_opts=opts.AngleAxisOpts(data=categories))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Polar Stacked Bar Chart"),

    )
)

# 添加堆叠柱状图
for i in range(len(values)):
    polar.add(
        series_name=data[i][0],
        data=values[i],
        type_="bar",
        stack="stack",
        label_opts=opts.LabelOpts(is_show=False),
    )

polar.render("极坐标系堆叠柱状图图.html")