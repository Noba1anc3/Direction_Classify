# Document Direction Rectifization Algorithm

## RotDocs Testing Set Making

- [Testing Set](https://github.com/Noba1anc3/Direction_Classify/blob/master/Tesing%20Set.md)
- [Download Testing Set 1.0 @ 18*50](https://bhpan.buaa.edu.cn:443/link/787CCE6F804CBC0F52251D87A79DCD91)
- [Download Testing Set 2.0 @ 18*200](https://bhpan.buaa.edu.cn:443/link/7EFF874581A29BAE85822C1D11A9E0A2)

## Zhenyang's Model

[Performance on Testing Set](https://github.com/Noba1anc3/Direction_Classify/blob/master/zhenyang_version/README.md)

## Text Detection based Direction Classification

- [**Content Description**](https://github.com/Noba1anc3/Direction_Classify/blob/master/Text%20Detection%20Based/README.md)
- [Appendix](https://github.com/Noba1anc3/Direction_Classify/blob/master/Text%20Detection%20Based/Appendix.md)

## Differentiable Binarization Text Detection Based Ultra-lightweight Document Direction Rectifization Algorithm

![](https://i.postimg.cc/vT3nwzn9/1.png)

Differentiable Binarization based Text Detection

![](https://i.postimg.cc/13LqS48W/2.png)

Backbone

![](https://i.postimg.cc/zXGWSsmk/3.png)

FPGM Pruning

![](https://i.postimg.cc/MpcQg1pM/4.png)

```
chepiao_147.jpg
Image Rotation
   Elapsed : 9.19ms
Text Detection
   Boxes Num : 18
   Elapsed : 192.46ms
UD - LR
   UD Score : 1.44 
   LR Score : 97.05
Intermidiate Filter
   Filter Reversed WH-Ratio Boxes
   Filter Low WH-Ratio Boxes
   Filter Low WH-Ratio Boxes
   Filter Low WH-Ratio Boxes
   Remained Boxes Num : 14
   Elapsed : 5.23ms
Direction Classification
   Positive Score : 0.00 
   Negative Score : 9.99 
   Positive Percentage : 0.00% 
   Negative Percentage : 100.00%
   Used Boxes Num : 10
   Elapsed : 73.66ms
Final Direction : Left
```
### ChineseOCR_Lite

- [Performance on Testing Set](https://github.com/Noba1anc3/Direction_Classify/blob/master/chineseocr_lite/README.md)
- [Performance on Testing Set 2.0](https://github.com/Noba1anc3/Direction_Classify/blob/master/chineseocr_lite/Test%20Set%202.0.md)

### Differentiable Binarization

- [Performance on Testing Set](https://github.com/Noba1anc3/Direction_Classify/blob/master/PaddleOCR/README.md)
- [Performance on Testing Set 2.0](https://github.com/Noba1anc3/Direction_Classify/blob/master/PaddleOCR/Test%20Set%202.0.md)

### Comparison & Analysis

- [Comparison on Testing Set](https://github.com/Noba1anc3/Direction_Classify/blob/master/Comparison.md)
- [Comparison on Testing Set 2.0](https://github.com/Noba1anc3/Direction_Classify/blob/master/Comparison%202.0.md)
- [Result Analysis on Testing Set](https://github.com/Noba1anc3/Direction_Classify/blob/master/Result_Analysis.md)
- [Result Analysis on Testing Set 2.0](https://github.com/Noba1anc3/Direction_Classify/blob/master/Result_Analysis%202.0.md)

### Iterative Optimization

- [Optimization Plan](https://github.com/Noba1anc3/Direction_Classify/blob/master/PaddleOCR/Optimize.md)
- [**Accuracy Iterative Optimization Result Document**](https://github.com/Noba1anc3/Direction_Classify/blob/master/PaddleOCR/%E5%87%86%E7%A1%AE%E7%8E%87%E8%BF%AD%E4%BB%A3%E4%BC%98%E5%8C%96%E7%BB%93%E6%9E%9C%E6%96%87%E6%A1%A3.md) 
- [**Time Elapse Iterative Optimization Result Document**](https://github.com/Noba1anc3/Direction_Classify/blob/master/PaddleOCR/%E6%97%B6%E9%97%B4%E6%B6%88%E8%80%97%E8%BF%AD%E4%BB%A3%E4%BC%98%E5%8C%96%E7%BB%93%E6%9E%9C%E6%96%87%E6%A1%A3.md) 

### Released Project

- [**README Documentation of Project**](https://github.com/Noba1anc3/Direction_Classify/blob/master/PaddleOCR-simplified/README.md)
- [Project Link](https://github.com/Noba1anc3/Direction_Classify/tree/master/PaddleOCR-simplified)
