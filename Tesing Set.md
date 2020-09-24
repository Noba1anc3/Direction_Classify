# 文字方向四分类测试集制作
## 测试集特点
- 保证种类的多样性
- 保证种类内数据的多样性
- 保证不同种类样本的个数平衡

## 数据类别
### 票据
- 车票
- 机票
- 门票
- 收据
- 增值税发票
- 出租车发票

### 证件
- 名片
- 身份证
- 营业执照
- 医保+护照+驾驶证

### 文档
- 电子书
- 教科书
- 银行流水
- 评级报告
- 公司报表
- 募集说明书

### 其他
- 试卷
- 体检表


## 数据来源
### PDF转图片
- 电子书
- 教科书

### 拍照
- 门票

### 数据集
- 身份证
- 银行流水
- 营业执照
- 评级报告
- 公司报表
- 募集说明书

### 网络图片 （扫描+拍照+电子版）
- 车票
- 机票
- 门票
- 名片
- 试卷
- 收据
- 体检表
- 增值税发票
- 出租车发票
- 医保+护照+驾驶证

## 数据分布
共有18个类，每个类50张图片，总计900张图片

- 车票
  - 火车票：35张
  - 其他：15张
- 机票
  - 拍照：37张
  - 电子版：13张
- 门票
  - 中文：34张
  - 外文：16张
- 名片
  - 拍照：3张
  - 电子版：47张
- 试卷
  - 大中小学中外文试卷均有
- 收据
  - 拍照：16张
  - 扫描：15张
  - 电子版：19张
- 体检表
  - 拍照：37张
  - 电子版：13张
- 身份证：
  - 人像面：31张
  - 国徽面：19张
- 电子书
  - 来源：三本电子书
- 教科书
  - 来源：人教版高中数学
- 银行流水
- 评级报告
- 公司报表
- 营业执照
  - 拍照：17张
  - 扫描：33张
- 募集说明书
- 增值税发票
  - 拍照：15张
  - 扫描：16张
  - 电子版：19张
- 出租车发票
  - 拍照：46张
  - 扫描：1张
  - 电子版：4张
- 医保+护照+驾驶证
  - 护照：19张
  - 医保卡：20张
  - 驾驶证：11张

## 数据处理
- 有效内容提取：编辑图片去掉无关内容

## 数据增强
- 因为是测试数据，不进行诸如亮度修改，噪声添加等主要用于训练数据的增强方式
- 在测试集中只使用四角度扩充
- 对数据集中的900张图片随机进行一个方向的调整并添加随机角度的旋转 90*random(0,4) + random(-15, 15)
  - 方案一 ： 只使用旋转
  - 方案二 ： 在90度整数倍调整的基础之上，进行小角度微调
  - 方案一与方案二交替使用
