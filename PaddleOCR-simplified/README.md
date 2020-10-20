# 基于PaddleOCR的文档方向四分类说明文档

## Usage

```
pip install paddlepaddle-gpu==2.0.0b0
pip install -r requirments.txt
cd tools/infer
python predict_system.py
```

## Interface

- Interface Class : tools/infer/predict_system.py -> TextSystem
- `__init__` : `text_sys = TextSystem(utility.parse_args(), DET_MODEL_DIR, CLS_MODEL_DIR, GPU)`
  - `DET_MODEL_DIR: '../../inference/ch_ppocr_mobile_v1.1_det_infer/'` (default)
  - `CLS_MODEL_DIR: '../../inference/ch_ppocr_mobile_v1.1_cls_infer/'` (default)
  - `GPU: True` (default)
- `__call__` : `text_sys(image, cls_box_num)`
  - Input : 
    - `image` : numpy.ndarray ( w * h * 3)
    - `cls_box_num` : 用于分类的文字框数量 (default = 10)
  - Output : 文档方向
    - `0` : 上向 (文字阅读方向为自左向右)
    - `1` : 左向 (文字阅读方向为自下向上)
    - `2` : 下向 (文字阅读方向为自右向左)
    - `3` : 右向 (文字阅读方向为自上向下)

## Recommended

### GPU Environment

#### model

在GPU环境上推荐使用`mobile_server + mobile_cls`的配置

总任务平均耗时
- `mobile_server + mobile_cls` : 74.34ms
- `mobile_det + mobile_cls` : 65.54ms

总准确率
- `mobile_server + mobile_cls` : 99.67%
- `mobile_det + mobile_cls` : 99.53%

组合替换方法 : 
1. 下载[`mobile_server`](https://paddleocr.bj.bcebos.com/20-09-22/server/det/ch_ppocr_server_v1.1_det_infer.tar)
2. 将模型放在根目录下的`inference`文件夹内
3. 修改类初始化参数`DET_MODEL_DIR`为`'../../inference/ch_ppocr_server_v1.1_det_infer/'`

#### cls_box_num

以最低时间成本达到99%以上的总准确率: 推荐将`cls_box_num`配置为`5`
- 分类任务的平均耗时不足10ms
- 分类任务的最高耗时不足15ms

对耗时基本没有要求: 推荐将`cls_box_num`配置为`20`
- 分类任务的最高耗时不足50ms
- 总准确率为99.53%

对时间消耗的要求介于两者之间: 推荐使用默认配置
- 分类任务的平均耗时不足20ms
- 总任务的平均耗时不足100ms
- 总准确率为99.42%

### CPU Environment

#### model

在CPU环境上推荐使用当前`mobile_det + mobile_cls`的默认配置

#### cls_box_num

- cls_det_num = 10
  - 分类任务的平均耗时降低2/3至110ms
  - 总任务的平均耗时降低1/3至558ms
  - 总准确率: 99.39%

- cls_det_num = 5
  - 分类任务平均耗时: 55ms
  - 总准确率: 98.67%



