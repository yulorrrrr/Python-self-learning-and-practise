'''
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map = Map()

data = [("北京市", 99),
        ("上海市", 8199),
        ("广东省", 999999)
        ]
map.add("map_test", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"mine":1, "max":9, "label":"1-9persons", "color":"#CCFFFF"},
            {"mine":10, "max":99, "label":"10-99persons", "color":"#FFFF99"},
            {"mine":100, "max":499, "label":"100-499persons", "color":"#FF9966"},
            {"mine":500, "max":999, "label":"500-999persons", "color":"#FF6666"},
            {"mine":1000, "max":9999, "label":"1000-9999persons", "color":"#CC3333"},
            {"mine":10000, "label":"more than 10000 persons", "color":"#990033"}
        ]
    )
)

map.render()
'''

import json
from pyecharts.charts import Map
from pyecharts.options import *

f = open("疫情.txt", "r", encoding="UTF-8")
data = f.read
f.close

data_dict = json.loads(data)

province_data_list = data_dict["areaTree"][0]["children"]
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["comfirm"]
    data_list.append(province_name,province_confirm)

map = Map()
map.add("各省份确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"mine":1, "max":9, "label":"1-9persons", "color":"#CCFFFF"},
            {"mine":10, "max":99, "label":"10-99persons", "color":"#FFFF99"},
            {"mine":100, "max":499, "label":"100-499persons", "color":"#FF9966"},
            {"mine":500, "max":999, "label":"500-999persons", "color":"#FF6666"},
            {"mine":1000, "max":9999, "label":"1000-9999persons", "color":"#CC3333"},
            {"mine":10000, "label":"more than 10000 persons", "color":"#990033"}
        ]
    )
)

map.render()