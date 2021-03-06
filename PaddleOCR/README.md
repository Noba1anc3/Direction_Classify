# 测试集实验结果

## 1. 分类标准
- 根据长宽比确定文档是上下型还是左右型
- 对分类分数进行加权投票确认文字阅读方向是自左向右还是自右向左

## 2. 总体实验结果

| 实验           | 准确率 |
|:-------------:|:------:|
| PaddleOCR     | 93.44% |

| 检测时间  | 最大值   | 最小值 | 平均值 |
|:---------:|:-------:|:------:|:------:|
| PaddleOCR | 3959.18 |  29.05 | 368.63 |

| 分类时间  | 最大值   | 最小值 | 平均值 |
|:---------:|:-------:|:------:|:------:|
| PaddleOCR | 6381.17 |    0.0 | 389.06 |

| 总时间          | 最大值   | 最小值 | 平均值 |
|:---------------:|:-------:|:------:|:------:|
| PaddleOCR       | 7414.96 |  29.05 | 757.69 |

## 3. 大类测试结果

### 3.1 种类

| 种类            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| 证件            | 100.0% |  100.0% |    76.27% |    85.11% |  89.50% |
| 其他            | 100.0% |  88.46% |    90.32% |    86.36% |  91.00% |
| 文档            | 100.0% |  100.0% |    88.46% |    85.14% |  93.33% |
| 票据            | 98.48% |  97.80% |    94.29% |    97.26% |  97.0%  |

### 3.2 方向

| 方向准确率      | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:-------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| 平均           | 99.49% |  97.99%  |  87.39%  |   89.35%  |  93.44% |

## 4. 小类测试结果

### 证件

| 证件            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:---------:|:-------:|:---------:|:-------:|
| 名片 |  100.00 | 100.00 | 81.82 | 100.00 | 96.00 |
| 身份证 |  100.00 | 100.00 | 70.59 | 75.00 | 84.00 |
| 驾驶证 |  100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| 营业执照 |  100.00 | 100.00 | 58.82 | 69.23 | 78.00 |
| 平均   | 100.0% |  100.0% |    76.27% |    85.11% |  89.50% |

### 票据

| 票据           | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:-------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| 车票 |  100.00 | 100.00 | 90.91 | 100.00 | 98.00 |
| 机票 |  100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| 门票 |  92.86 | 100.00 | 90.00 | 93.33 | 94.00 |
| 收据 |  100.00 | 100.00 | 100.00 | 88.89 | 98.00 |
| 出租车发票 |  100.00 | 88.89 | 91.67 | 100.00 | 94.00 |
| 增值税发票 |  100.00 | 100.00 | 85.71 | 100.00 | 98.00 |
| 平均   | 98.48% |  97.80% |    94.29% |    97.26% |  97.0%  |

### 其他

| 其他            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:---------:|:-------:|:---------:|:-------:|
| 试卷 |  100.00 | 84.62 | 88.24 | 72.73 | 86.00 |
| 体检报告 |  100.00 | 92.31 | 92.86 | 100.00 | 96.00 |
| 平均    | 100.0% |  88.46% |    90.32% |    86.36% |  91.00% |

### 文档

| 文档            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:---------:|:-------:|:---------:|:-------:|
| 电子书 |  100.00 | 100.00 | 81.25 | 81.82 | 90.00 |
| 教材 |  100.00 | 100.00 | 100.00 | 70.59 | 90.00 |
| 募集 |  100.00 | 100.00 | 77.78 | 77.78 | 88.00 |
| 银行流水 |  100.00 | 100.00 | 100.00 | 100.00 | 100.00 |
| 评级报告 |  100.00 | 100.00 | 90.00 | 92.31 | 96.00 |
| 公司报表 | 100.00 | 100.00 | 90.91 | 91.67 | 96.00 |
| 平均  | 100.0% |  100.0% |    88.46% |    85.14% |  93.33% |


