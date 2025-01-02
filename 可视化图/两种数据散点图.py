from pyecharts.charts import Scatter
from pyecharts import options as opts

# 定义 x 轴和 y 轴的数据
x_data =[10, 20, 30, 40, 50, 60]
y_data =[10, 20, 30, 40, 50, 60]

# 创建散点图实例
scatter = (
    Scatter()
    .add_xaxis(x_data[::-1])
    .add_yaxis(series_name="", y_axis=y_data)
    .add_xaxis(x_data)
    .add_yaxis(series_name="", y_axis=y_data)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="散点图"),
        xaxis_opts=opts.AxisOpts(type_="value"),
        yaxis_opts=opts.AxisOpts(type_="value"),
    )
)
scatter.render("散点图1.html")