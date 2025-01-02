from pyecharts.charts import Bar
from pyecharts import options as opts

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]

bar = (
    Bar()
    .add_xaxis(attr)
    .add_yaxis("蒸发量", v1, markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]), markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), opts.MarkPointItem(type_="min")]))
    .add_yaxis("降水量", v2, markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]), markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max"), opts.MarkPointItem(type_="min")]))
    .set_global_opts(title_opts=opts.TitleOpts(title="蒸发量与降水量"))
)
bar.render("柱状图2.html")