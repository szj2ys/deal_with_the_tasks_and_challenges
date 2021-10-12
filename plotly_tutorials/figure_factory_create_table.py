# *_*coding:utf-8 *_*
import plotly.express as px
import plotly.figure_factory as ff
import pathlib

tips = px.data.tips()[:10]  # 取出前10条记录

print(tips)
fig = ff.create_table(tips)  # 将生成的tips数据放入

fig.write_image(pathlib.Path(__file__).stem + '.png')
