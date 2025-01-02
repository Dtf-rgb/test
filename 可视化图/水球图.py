from pyecharts.charts import Liquid
from pyecharts import options as opts

# 创建水球图
liquid = (
    Liquid()
    .add('Liquid', [0.6, 0.5, 0.4, 0.3])  # 指定水球图填充比例
    .set_global_opts(title_opts=opts.TitleOpts(title='水球图'))  # 设置标题
)

liquid.render("水球图.html")
