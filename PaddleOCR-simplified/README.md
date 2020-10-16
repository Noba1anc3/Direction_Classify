## Usage

pip install paddlepaddle-gpu==2.0.0b0  
pip install -r requirments.txt
cd tools/infer
python predict_system.py --det_model_dir="../../inference/ch_ppocr_server_v1.1_det_infer/" --cls_model_dir="../../inference/ch_ppocr_mobile_v1.1_cls_infer/" --use_gpu=True
