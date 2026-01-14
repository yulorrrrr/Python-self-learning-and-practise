'''from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

bar1= Bar()
bar1.add_xaxis(["China","US","UK"])
bar1.add_yaxis("GDP",[30,60,90],label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2= Bar()
bar2.add_xaxis(["China","US","UK"])
bar2.add_yaxis("GDP",[40,40,80],label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3= Bar()
bar3.add_xaxis(["China","US","UK"])
bar3.add_yaxis("GDP",[20,60,100],label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar1, "t1")
timeline.add(bar2, "t2")
timeline.add(bar3, "t3")
#auto play
timeline.add_schema(
    play_interval=1000,
    is_auto_play=True,
    is_loop_play=True
)
timeline.render("timeline bar chart.html")
'''
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

f = open("gdp_1960_2020_simulated.txt", "r", encoding="UTF-8")
data_line = f.readlines()
f.close()

timeline = Timeline({"theme": ThemeType.LIGHT})
data_dict = {}
for line in data_line:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = int(line.split(",")[2])

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1])

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()

    bar.set_global_opts(
        title_opts=TitleOpts(title = f"{year} GDP data")
    )
    timeline.add(bar,str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("GDP.html")
