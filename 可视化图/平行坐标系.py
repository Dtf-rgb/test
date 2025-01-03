from pyecharts.charts import Parallel
from pyecharts import options as opts
c_schema = [{"dim": 0, "name": "data"},
            {"dim": 1, "name": "AQI"},
            {"dim": 2, "name": "PM2.5"},
            {"dim": 3, "name": "PM10"},
            {"dim": 4, "name": "CO"},
            {"dim": 5, "name": "NO2"},
            {"dim": 6, "name": "CO2"},
            {"dim": 7, "name": "等级", "type": "category",
             "data": ['优', '良', '轻度污染', '中度污染', '重度污染', '严重污染']}]
data = [[1, 91, 45, 125, 0.82, 34, 23, "良"],
        [2, 65, 27, 78, 0.86, 45, 29, "良"],
        [3, 83, 60, 84, 1.09, 73, 27, "良"],
        [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
        [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
        [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
        [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
        [8, 89, 65, 78, 0.86, 51, 26, "良"],
        [9, 53, 33, 47, 0.64, 50, 17, "良"],
        [10, 80, 55, 80, 1.01, 75, 24, "良"],
        [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
        [12, 99, 71, 142, 1.1, 62, 42, "良"],
        [13, 95, 69, 130, 1.28, 74, 50, "良"],
        [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]]
parallel = Parallel()
parallel.add_schema(c_schema)
parallel.add("parallel", data)

parallel.set_global_opts(title_opts=opts.TitleOpts(title="平行坐标系-用户自定义指示器"))
parallel.render("平行坐标系-用户自定义指示器.html")

