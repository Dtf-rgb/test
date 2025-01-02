from pyecharts.charts import Line
from pyecharts import options as opts

attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line =Line()
line.add_xaxis(xaxis_data=attr)
line.add_yaxis("商家A",y_axis=v1,
               is_smooth=True,
               linestyle_opts=opts.LineStyleOpts(opacity=0.2),
               areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
               symbol=None)
line.add_yaxis("商家B",y_axis=v2,
               is_smooth=True, color='yellow',
               areastyle_opts=opts.AreaStyleOpts(opacity=0.8))
# 设置全局配置项
line.set_global_opts(
    title_opts=opts.TitleOpts(title="折线 - 面积图示例"),
    xaxis_opts=opts.AxisOpts(type_="category"),
    yaxis_opts=opts.AxisOpts(type_="value"),
)
line.render("折线——面积图.html")