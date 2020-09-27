# 测试集实验结果

## 1. 分类标准
- 根据长宽比确定文档是上下型还是左右型
- 对分类分数进行加权投票确认文字阅读方向是自左向右还是自右向左

## 2. 总体实验结果

| 实验            | 准确率 |
|:---------------:|:------:|
| ChineseOCR_Lite | 90.22% |

| 检测时间        | 最大值   | 最小值 | 平均值 |
|:---------------:|:-------:|:-----:|:------:|
| ChineseOCR_Lite | 5070.1 | 280.36 | 520.47 |

| 分类时间         | 最大值  | 最小值 | 平均值 |
|:---------------:|:-------:|:-----:|:------:|
| ChineseOCR_Lite | 2794.39 |  2.68 |  42.70 |

## 3. 大类测试结果

### 3.1 种类

| 种类            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:---------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| 证件            | 100.0% |  100.0% |    66.10% |    82.98% |  86.00% |
| 其他            | 95.24% |  96.15% |    80.65% |    77.27% |  87.00% |
| 文档            | 100.0% |  100.0% |    82.05% |    86.49% |  92.00% |
| 票据            | 100.0% |  98.90% |    90.00% |    79.45% |  92.33% |

### 3.2 方向

| 方向准确率     | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:-------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| 平均          | 99.49% |  99.20%  |  80.25%  |   82.41%  |  90.22% |

## 4. 小类测试结果

### 证件

| 证件            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:---------:|:-------:|:---------:|:-------:|
| 名片 |  100.00 | 100.00 | 63.64 | 86.67 | 88.00 |
| 身份证 |  100.00 | 100.00 | 64.71 | 83.33 | 84.00 |
| 驾驶证 |  100.00 | 100.00 | 92.86 | 85.71 | 96.00 |
| 营业执照 |  100.00 | 100.00 | 47.06 | 76.92 | 76.00 |
| 平均   | 100.0% |  100.0% |    66.10% |    82.98% |  86.00% |

### 票据

| 票据           | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:-------------:|:------:|:--------:|:--------:|:---------:|:-------:|
| 车票 |  100.00 | 100.00 | 100.00 | 92.86 | 98.00 |
| 出租车发票 |  100.00 | 94.44 | 91.67 | 83.33 | 92.00 |
| 机票 |  100.00 | 100.00 | 93.75 | 77.78 | 94.00 |
| 门票 |  100.00 | 100.00 | 60.00 | 80.00 | 86.00 |
| 收据 |  100.00 | 100.00 | 92.86 | 55.56 | 90.00 |
| 增值税发票 |  100.00 | 100.00 | 100.00 | 78.57 | 94.00 |
| 平均   | 100.0% |  98.90% |    90.00% |    79.45% |  92.33% |

### 其他

| 其他            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:---------:|:-------:|:---------:|:-------:|
| 试卷 |  88.89 | 92.31 | 76.47 | 72.73 | 82.00 |
| 体检报告 |  100.00 | 100.00 | 85.71 | 81.82 | 92.00 |
| 平均    | 95.24% |  96.15% |    80.65% |    77.27% |  87.00% |

### 文档

| 文档            | Up acc | Down acc | Left acc | Right acc | Avg acc |
|:--------------:|:------:|:---------:|:-------:|:---------:|:-------:|
| 电子书 |  100.00 | 100.00 | 93.75 | 81.82 | 94.00 |
| 教材 |  100.00 | 100.00 | 100.00 | 76.47 | 92.00 |
| 募集 |  100.00 | 100.00 | 66.67 | 88.89 | 86.00 |
| 银行流水 |  100.00 | 100.00 | 90.00 | 83.33 | 94.00 |
| 评级报告 |  100.00 | 100.00 | 80.00 | 92.31 | 94.00 |
| 公司报表 |  100.00 | 100.00 | 63.64 | 100.00 | 92.00 |
| 平均  | 95.24% |  96.15% |    80.65% |    77.27% |  87.00% |

