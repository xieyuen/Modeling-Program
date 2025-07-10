# 2025年河源市第二次数学建模比赛作品（程序源码）

### 代码运行要求:
1. 环境: python 3.11 及以上
2. 模块:
    - scikit-learn
    - numpy
    - pandas
    - matplotlib
3. uv
    - 程序运行请使用命令: `uv run main.py`
    - 如果不是cpython 3.11版本需要加上`-p <版本号>`, 即`uv run -p <版本号> main.py`
        - **Example**: `uv run -p 3.13 main.py`
4. 其他问题请寻找[谢瑜恩](<mailto:xieyuenol@outlook.com> "小组编程,代码由其一人完成")

### 部分代码展示
```py
def main():
    data = pd.read_excel("./data/data.xlsx")

    tools.remove_na(data)

    y = data[Title.WATER_RESOURSE]
    x = data[Title.X_]

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
| 结果 | 年降雨量 | 年日照时间 | 截距 |
| --- | --- | --- | --- |
| 回归系数 | 0.07136624136029754 | -0.06432925027537864 | 136.49270835356322 |
| P值 | 4.76940025695427e-07 | 0.003510708368445359 | NaN |

决定R²: 0.9571011837013047<br>
调整R²: 0.9509727813729196<br>

### 部分`matplotlib`绘制结果
![](<./photo/humidity.png>)
![](<./photo/rain.png>)
![](<./photo/temperature.png>)
![](<./photo/sunshining_time.png>)
![](<./photo/rain_and_time.png>)
