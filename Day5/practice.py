from practice_file_define import *
from practice_data_define import *
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType


text_file_reder = TextFileReader("/Users/huangchuning/Desktop/python/Day05/data01.txt")
json_file_reader = JsonFileReader("/Users/huangchuning/Desktop/python/Day05/data02.txt")

jan_data : list[Record] = text_file_reder.read_data()
feb_data : list[Record] = json_file_reader.read_data()

all_data : list[Record] = jan_data+feb_data

#calculation
data_dict = {}
for record  in all_data:
    if record.date in all_data:
        data_dict[record.date]  += record.money
    else:
        data_dict[record.date] = record.money

bar = Bar()
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("sale",list(data_dict.values()))
bar.set_global_opts(
    title_opts=TitleOpts(title="Daily sale")
)
bar.render("daily sale bar.html")