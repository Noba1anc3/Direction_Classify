# 测试集实验结果

## 1. 分类标准
- 根据长宽比确定文档是上下型还是左右型
- 对分类分数进行加权投票确认文字阅读方向是自左向右还是自右向左

## 2. 总体实验结果

| 实验            | 准确率 |
|:---------------:|:------:|
| PaddleOCR       | 97.14% |
| ChineseOCR_Lite | 94.00% |

| 检测时间         | 最大值  | 最小值 | 平均值 |
|:---------------:|:-------:|:-----:|:------:|
| PaddleOCR       | 2578.67 |  12.89 | 310.61 |
| ChineseOCR_Lite | 6304.24 | 262.37 | 578.66 |

| 分类时间        | 最大值   | 最小值 | 平均值 |
|:---------------:|:-------:|:-----:|:------:|
| PaddleOCR       | 7499.34 |   0.0 | 438.40 |
| ChineseOCR_Lite | 2718.34 |  0.73 |  51.93 |

| 总时间          | 最大值   | 最小值 | 平均值 |
|:---------------:|:-------:|:------:|:------:|
| PaddleOCR       | 7942.99 |  19.86 | 749.01 |
| ChineseOCR_Lite | 7253.86 |  268.8 | 630.59 |

## 3. 大类测试结果

### 3.1 种类

| 证件            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:---------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| PaddleOCR       | 100.0% |  100.0% |    87.16% |    92.96% |  94.75% |
| ChineseOCR_Lite | 100.0% |  100.0% |    80.73% |    91.96% |  92.75% |

| 其他            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:---------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| PaddleOCR       | 100.0% |  100.0% |    97.03% |    98.06% |  98.75% |
| ChineseOCR_Lite | 96.94% |  100.0% |    91.09% |    90.29% |  94.50% |

| 文档            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:---------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| PaddleOCR       | 100.0% |  99.64% |    92.76% |    94.61% |  96.75% |
| ChineseOCR_Lite | 98.75% |  99.29% |    85205% |    85.86% |  92.25% |

| 票据            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:---------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| PaddleOCR       | 99.66% |  99.36% |    97.41% |    97.86% |  98.58% |
| ChineseOCR_Lite | 99.66% |  99.36% |    95.47% |    90.71% |  96.42% |

### 3.2 方向

| 方向准确率       | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:---------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| PaddleOCR       | 99.89% |  99.66%  |  93.45%  |   95.68%  |  97.14% |
| ChineseOCR_Lite | 99.11% |  99.55%  |  88.20%  |   89.31%  |  94.00% |
