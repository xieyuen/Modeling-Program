# 2025年河源市第二次数学建模比赛作品（程序源码）

### 代码运行要求:
1. 运行环境:
   - python 3.11 或以上
2. [安装模块](<https://developer.aliyun.com/mirror> "推荐使用阿里云镜像站下载"):
  - scikit-learn
  - numpy
  - pandas
  - matplotlib
3. 其他问题请寻找[谢瑜恩](<mailto:xieyuenol@outlook.com> "小组编程,代码由其一人完成")

### 部分代码展示
```py
def main():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Index.WATER_RESOURSE]
    x = data[Index.X_]

    model = LinearRegression()

    model.fit(x, y)

    print("变量:",*x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {tools.adjusted_r_squared(model, x, y)}")
    print("P值:", *tools.p(model, x, y))

    drawer = Drawer(data)

    drawer.rain().show()



if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    main()

```
### 拟合结果

#### 线性回归模型
| 统计量 | 年降雨量 | 年日照时间 | 截距 |
| :---: | :---: | :------: | :---: |
| 回归系数 | 0.07136624136029754 | -0.06432925027537864 | 136.49270835356322 |
| P值 | 4.76940025695427e-07 | 0.003510708368445359 | 0.008[^Note] |

- 决定R²: 0.9571011837013047
- 调整R²: 0.9509727813729196

[^Note] 除截距P值使用`statsmodels`计算外, 其余结果均是使用`scikit-learn`计算, 所以截距的P值只保留了3位小数

#### 神经网络模型
暂未完成

### 部分`matplotlib`绘制结果
![](<./photo/humidity.png>)
![](<./photo/rain.png>)
![](<./photo/temperature.png>)
![](<./photo/sunshining_time.png>)
![](<./photo/rain_and_time.png>)
