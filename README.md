# mobilenetv3-yolov3
An experiment of transferring backbone of yolov3 into mobilenetv3 which is implemented by TF/Keras and inspired by [qqwweee/keras-yolo3](https://github.com/qqwweee/keras-yolo3) and [xiaochus/MobileNetV3](https://github.com/xiaochus/MobileNetV3)



Training
--

Generate your own annotation file and class names file.<br>
    One row for one image;<br>
  Row format: `image_file_path box1 box2 ... boxN;`<br>
  Box format: `x_min,y_min,x_max,y_max,class_id` (no space).<br>
  For VOC dataset, try `python voc_annotation.py`<br>
  Here is an example:<br>

  &nbsp;   &nbsp;   &nbsp;   &nbsp; `path/to/img1.jpg 50,100,150,200,0 30,50,200,120,3`<br>
  &nbsp;   &nbsp;   &nbsp;   &nbsp; `path/to/img2.jpg 120,300,250,600,2`<br>
...


Modify train.py and start training.<br>
`python train.py`<br>

If you want to train from scratch ,set load_pretrained=False ;if training was interupted , you can set load_pretrained=True and load weights from weights_path ,then restart training.<br>


Usage
--
Use --help to see usage of yolo_video.py:<br>

`usage: yolo_video.py [-h] [--model MODEL] [--anchors ANCHORS]`<br>
  &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;  `[--classes CLASSES] [--gpu_num GPU_NUM] [--image]`<br>
  &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;  `[--input] [--output]`<br>

`positional arguments:`<br>
  &nbsp; `--input        Video input path`<br>
  &nbsp; `--output       Video output path`<br>

`optional arguments:`<br>
  &nbsp;  `-h, --help         show this help message and exit`<br>
  &nbsp;  `--model MODEL      path to model weight file, default model_data/yolo.h5`<br>
  &nbsp; `--anchors ANCHORS  path to anchor definitions, default`  
  &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;              `model_data/yolo_anchors.txt`<br>
  &nbsp; ` --classes CLASSES  path to class definitions, default`<br>
       &nbsp;   &nbsp;   &nbsp;   &nbsp;   &nbsp;     `model_data/coco_classes.txt`<br>
  &nbsp;  `--gpu_num GPU_NUM  Number of GPU to use, default 1`<br>
  &nbsp; `--image            Image detection mode, will ignore all positional arguments`<br>



