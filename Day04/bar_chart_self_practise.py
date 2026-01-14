from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import *

f = open("gdp_1960_2020_simulated.txt", "r", encoding="UTF-8")
dataline = f.readlines()
f.close()

timeline = Timeline()

data_dict = {}
for line in dataline:
    split_line = line.split(",")
    year = int(split_line[0]) 
    country = split_line[1]
    gdp = int(split_line[2])

    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country, gdp])

    
    
sorted_year_list = sorted(data_dict.keys())
#print (sorted_year_list)

def get_gpa(list):
    return list[1]

for year in sorted_year_list:

    bar = Bar()
    data_dict[year].sort(key=get_gpa, reverse=True)
    year_data = data_dict[year][0:8]

    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1])
    
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

timeline.render("GDP2.html")
   





        





