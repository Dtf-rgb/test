from pyecharts.charts import Radar
from pyecharts import options as opts

# 定义指标轴标签和数据
schema = [
    {"name": "销售", "max": 6500},
    {"name": "管理", "max": 16000},
    {"name": "信息技术", "max": 30000},
    {"name": "客服", "max": 38000},
    {"name": "研发", "max": 52000},
    {"name": "市场", "max": 25000},
]
values1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
values2 = [[5000, 14000, 28000, 31000, 42000, 21000]]

# 创建雷达图实例
radar = Radar()
radar.set_global_opts(title_opts=opts.TitleOpts(title="雷达图"))

# 添加数据并设置配置项
radar.add_schema(schema=schema)
radar.add("预算分配", values1, areastyle_opts=opts.AreaStyleOpts(opacity=0.5),color="blue")
radar.add("实际开销", values2, areastyle_opts=opts.AreaStyleOpts(opacity=0.5),color="yellow")

radar.render("雷达图.html")
