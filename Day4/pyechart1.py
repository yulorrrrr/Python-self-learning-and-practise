from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts,ToolboxOpts, VisualMapOpts 
line = Line()
line.add_xaxis(["China", "USA", "UK"])
line.add_yaxis("GDP",[30,20,10])


line.set_global_opts(
    title_opts=TitleOpts(title="GDP", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
line.render()