from sklearn import tree
#[height, weight, show size]
x=[[181,80,44],[177,78,43],[160,50,38],[154,54,37],[166,63,40],[190,90,47], [175,64,39],[177,70,40]]

y=['m','f','f','f','m','m','m','f','m','f','m']
clf=tree.DecisionTreeClassifier()

clf=clf.fit(x,y)

prediction=clf.predict([[190,70,43]])

print prediction