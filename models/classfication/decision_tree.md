[决策树（上）](https://mp.weixin.qq.com/s?__biz=MzI5MjYwNTU5NQ==&mid=2247484478&idx=1&sn=da568b74c409382ec264b07fb5177450&chksm=ec7f9fcadb0816dcb33cd1646e774e42f577a718a71b2442efd4ad5e30a4ae59ea4ff69b6359&token=1213245104&lang=zh_CN#rd)
[决策树（下）](https://mp.weixin.qq.com/s?__biz=MzI5MjYwNTU5NQ==&mid=2247484530&idx=1&sn=42edc529f35abcb99271baf7b6bd3324&chksm=ec7f9f86db08169038d445eb786c446a78a80737c060640ecf351e32faf62ee242f333690611&token=1213245104&lang=zh_CN#rd)

#### 
```python
# 决策树模型
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='entropy')

"""分离训练集和测试集"""
train_data = df[df['Survived'].notnull()].drop(['PassengerId'], axis=1)
test_data = df[df['Survived'].isnull()].drop(['Survived'], axis=1)
# 分离训练集特征和标签
y = train_data['Survived']
X = train_data.drop(['Survived'], axis=1)

# 设置参数
parameters = {
    'criterion': ['gini', 'entropy'],
    'max_depth': range(2, 10),
    'min_impurity_decrease': np.linspace(0, 1, 10),
    'min_samples_split': range(2, 30, 2),
    'class_weight': ['balanced', None]
}

"""通过网格搜索寻找最优参数"""
gird_clf = GridSearchCV(DecisionTreeClassifier(), parameters, cv=5, return_train_score=True)
# 模型训练
gird_clf.fit(X, y)
# 结果预测
pred_labels = gird_clf.predict(test_data.drop(['PassengerId'], axis=1))


```






