# *_*coding:utf-8 *_*
import plotly.express as px
import plotly.figure_factory as ff
import pathlib

data_matrix = [
    ['语言', '排名', '变化'],
    ['<a href="https://www.python.org">Python</a>', '1', '3'],
    ['<a href="https://www.java.com/zh-CN">Java</a>', '2', '-1'],
    ['<a href="https://www.plotly.com/">Plotly</a>', '3', '60'],
]

fig = ff.create_table(
    data_matrix,
    height_constant=20,
    colorscale=[[0, '#000000'], [.5, '#80beff'], [1, '#cce5ff']],
    # colorscale=[[0, '#4d004c'], [.5, '#f2e5ff'],
    #                                   [1, '#ffffff']],  # 表格中设置3种颜色
    # colorscale = [[0, '#4d004c'],[.25,'#0ac37d'],[.5, '#f2e5ff'],[.75,
    # '#afc271'],[1, '#1ff1ff']],  # 5种颜色
    font_colors=['#ffffff', '#304010', '#003090'])
fig.update_layout(title_text='Program language rank')
fig.update_layout({'margin': {'t': 50}})
fig.show()
# fig.write_image(pathlib.Path(__file__).stem + '.png')
