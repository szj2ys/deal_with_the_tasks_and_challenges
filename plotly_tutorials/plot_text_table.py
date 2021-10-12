import plotly.graph_objects as go
import pathlib

values = [
    ["李白 唐代", "杜甫 唐代", "苏轼 宋代", "王安石 宋代"],  # 第一列数据
    [
        "床前明月,疑是地上霜;举头望明月,低头思故乡",
        "国破山河在，城春草木深。感时花溅泪，恨别鸟惊心。<br>烽火连三月，家书抵万金。白头骚更短，浑欲不胜簪。",
        "十年生死两茫茫，不思量，自难忘。千里孤坟，无处话凄凉。<br>纵使相逢应不识，尘满面，鬓如霜。<br>夜来幽梦忽还乡，小轩窗，正梳妆。相顾无言，惟有泪千行。<br>料得年年肠断处，明月夜，短松冈。",
        "念往昔、繁华竞逐。叹门外楼头，悲恨相续。<br>千古凭高，对此谩嗟荣辱。<br>六朝旧事随流水，但寒烟、芳草凝绿。<br>至今商女，时时犹唱后庭遗曲。"
    ]
]

fig = go.Figure(data=[
    go.Table(
        columnorder=[1, 2],  # 列属性的顺序
        columnwidth=[800, 4000],  # 列属性中元素所占单元格整体大小

        # 表头
        header=dict(
            values=[["唐宋作家"], ["代表作品"]],  # 两个表头
            line_color='darkslategray',  # 线条和填充色
            fill_color='royalblue',
            align=['center', 'center'],  # 位置
            font=dict(color='white', size=13),  # 表头文本的颜色和字体大小
            font_size=13,
            height=40  # 高度
        ),

        # 单元格设置
        cells=dict(
            values=values,  # 数据
            line_color='darkslategray',  # 线条颜色
            fill=dict(color=['paleturquoise', 'white']),
            align=['center', 'center'],  # 两个列属性文本显示位置
            font_size=12,  # 字体大小
            height=50))
])

# fig.update_layout(width=600,height=400)

fig.write_image(pathlib.Path(__file__).stem + '.png')
