# *_*coding:utf-8 *_*
import plotly.graph_objs as go
import plotly.figure_factory as ff
import plotly.express as px

tips = px.data.tips()[:10]

# 添加表格
fig = ff.create_table(tips)

# 添加图形
fig.add_trace(
    go.Scatter(
        x=tips["tip"],
        y=tips["total_bill"],
        marker=dict(color='#9099ff'),  # 标记颜色
        name="total_bill <br>tip",
        xaxis='x2',
        yaxis='y2'))

fig.add_trace(
    go.Scatter(x=tips["size"],
               y=tips["total_bill"],
               marker=dict(color='#a099af'),
               name="total_bill <br>size",
               xaxis='x2',
               yaxis='y2'))

fig.update_layout(title_text="消费数据图表联合",
                  height=500,
                  margin={
                      "t": 75,
                      "b": 100
                  },
                  xaxis={'domain': [0, .45]},
                  xaxis2={'domain': [0.6, 1.]},
                  yaxis2={
                      'anchor': 'x2',
                      'title': 'tips'
                  })

fig.show()
