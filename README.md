# 2025年河源市第二次数学建模比赛作品（程序源码）

### 代码运行要求:

1. 运行环境:
   - python 3.11 或以上
   - (可选) [uv](<https://docs.astral.sh/uv/>)
2. [安装模块](<https://developer.aliyun.com/mirror> "推荐使用阿里云镜像站下载"):
  - scikit-learn
  - numpy
  - pandas
  - matplotlib
3. 其他问题请寻找谢瑜恩[^1]

[^1]: 小组编程，手机15986023733

### 拟合结果

#### 线性回归模型

此模型拟合时使用河源市的数据

| 统计量 | 年降雨量 | 年日照时间 | 截距 |
| :---: | :---: | :------: | :---: |
| 回归系数 | 0.07136624136029754 | -0.06432925027537864 | 136.49270835356322 |
| P值 | 4.76940025695427e-07 | 0.003510708368445359 | 0.008[^2] |

[^2]: 截距P值使用 `statsmodels` 计算, `summary()`结果只有三位小数, 而其余结果均使用 `scikit-learn` 计算, 精度更高

- 决定R²: 0.9571011837013047
- 调整R²: 0.9509727813729196

> 注：此模型未对数据标准化，模型文件 `.pkl` 已经上传到 [**releases**](<https://github.com/xieyuen/Modeling-Program/releases> "点击跳转到releases") 中

#### 神经网络模型

待完成

- [ ] 更多的数据
- [ ] 完善代码
- [ ] 计算统计量，判定拟合效果
- [ ] 确定是否过拟合

### 部分`matplotlib`绘制结果

![](<./photo/humidity.png>)
![](<./photo/rain.png>)
![](<./photo/temperature.png>)
![](<./photo/sunshining_time.png>)
![](<./photo/rain_and_time.png>)
