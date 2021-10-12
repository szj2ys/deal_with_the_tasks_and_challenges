# *_*coding:utf-8 *_*
import plotly.graph_objects as go
import pathlib
import pandas as pd

colors = [
    'rgb(239, 243, 255)',  # rgb值越接近255，越接近白色
    'rgb(189, 215, 231)',
    'rgb(107, 174, 214)',
    'rgb(59, 130, 189)',
    'rgb(9, 81, 156)'
]

student = pd.DataFrame({
    "性别": ["小明", "小红", "小周", "小孙", "小苏"] * 100,  # 将数据同时扩大100倍
    "年龄": [19, 29, 32, 20, 18] * 100,
    "性别": ["男", "女", "男", "女", "男"] * 100,
    "成绩": [590, 588, 601, 670, 555] * 100
})
print(student)

fig = go.Figure(data=[
    go.Table(
        header=dict(
            values=list(student.columns),  # 表头取值是data列属性
            fill_color='paleturquoise',  # 填充色和文本位置
            align='left'),
        cells=dict(
            values=[student.性别, student.年龄, student.成绩
                    ],  # 单元格的取值就是每个列属性的Series取值
            fill_color='lavender',
            align='left'))
])

fig.show()
