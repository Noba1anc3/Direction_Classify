# 基于PaddleOCR的文档方向四分类说明文档

## Usage

```
pip install paddlepaddle-gpu==2.0.0b0
pip install -r requirments.txt
cd tools/infer
python predict_system.py
```

## 接口

- 接口类 : tools/infer/predict_system.py -> TextSystem
- 初始化类 : `text_sys = TextSystem(utility.parse_args(), DET_MODEL_DIR, CLS_MODEL_DIR, GPU)`
  - 默认`DET_MODEL_DIR`=`'../../inference/ch_ppocr_mobile_v1.1_det_infer/'`
  - 默认`CLS_MODEL_DIR`=`'../../inference/ch_ppocr_mobile_v1.1_cls_infer/'`
  - 默认GPU = `True`
- 推理图片 : `text_sys(image, cls_box_num)`
  - 输入 : 
    - image : numpy.ndarray ( w * h * 3)
    - cls_box_num : 用于分类的文字框数量 (default = 10)
  - 输出 : 文档方向
    - 0 : 上向 (文字阅读方向为自左向右)
    - 1 : 左向 (文字阅读方向为自下向上)
    - 2 : 下向 (文字阅读方向为自右向左)
    - 3 : 右向 (文字阅读方向为自上向下)

## 推荐配置

### GPU环境

#### model

在GPU环境上推荐使用`mobile_server + mobile_cls`的配置

完整流程的平均时间对比: 
- `mobile_server + mobile_cls` : 74.34ms
- `mobile_det + mobile_cls` : 65.54ms

测试集上的总准确率对比:
- `mobile_server + mobile_cls` : 99.67%
- `mobile_det + mobile_cls` : 99.53%

组合替换方法 : 
1. 下载(`mobile_server`)[https://paddleocr.bj.bcebos.com/20-09-22/server/det/ch_ppocr_server_v1.1_det_infer.tar]
2. 将模型放在项目目录`inference`文件夹之下
3. 修改类初始化参数`DET_MODEL_DIR`为`'../../inference/ch_ppocr_server_v1.1_det_infer/'`

#### cls_box_num

如果希望以最低时间成本达到99%以上的总准确率，推荐将`cls_box_num`修改为`5`，在该配置下分类任务的平均耗时不足10ms,最高耗时不足15ms.  
如果对耗时没有十分严格的要求，将分类任务的最高耗时控制在50ms以内即可，则推荐将`cls_box_num`修改为`20`，该配置的总准确率为99.53%.  
如果对时间消耗的要求介于两者之间，则推荐使用默认配置，该配置下的分类任务平均时间不足20ms,总任务平均时间不足100ms，且拥有99.42的总准确率.

### CPU环境

在CPU环境上推荐使用当前`mobile_det + mobile_cls`的配置，保持参数`cls_box_num`为默认值`10`.  
根据实验结果，在只损失分类任务准确率0.14%的前提之下，`cls_det_num=10`时可以将分类任务的平均耗时降低2/3至110ms，将总任务的平均耗时降低1/3至558ms，最终总准确率为99.39%.  
如若进一步将`cls_det_num`修改为`5`，则可以在分类任务平均耗时为55ms时达到98.67%准确率.



