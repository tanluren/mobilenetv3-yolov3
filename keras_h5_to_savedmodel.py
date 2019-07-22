
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Input
from yolo3.mobilenet_base import relu6, hard_swish
from yolo3.model import yolo_body, tiny_yolo_body


def get_classes(classes_path):
    '''loads the classes'''
    with open(classes_path) as f:
        class_names = f.readlines()
    class_names = [c.strip() for c in class_names]
    return class_names

def get_anchors(anchors_path):
    '''loads the anchors from a file'''
    with open(anchors_path) as f:
        anchors = f.readline()
    anchors = [float(x) for x in anchors.split(',')]
    return np.array(anchors).reshape(-1, 2)



classes_path = 'model_data/voc_classes.txt'
anchors_path = 'model_data/yolo_anchors.txt'
weights_path = 'logs/000/backup.h5'
model_path = 'tmp/keras_savedmodel'
input_shape = (416,416) # multiple of 32, hw

class_names = get_classes(classes_path)
num_classes = len(class_names)
anchors = get_anchors(anchors_path)
num_anchors = len(anchors)

image_input = Input(shape=(input_shape[0], input_shape[0], 3),name='input0')
if num_anchors == 9:
	model_body = yolo_body(image_input, num_anchors//3, num_classes)
elif num_anchors == 6:
	model_body = tiny_yolo_body(image_input, num_anchors//3, num_classes)


model_body.load_weights(weights_path, by_name=True)
print('Load weights {}.'.format(weights_path))
print('model output names',model_body.output_names)
print('model input names',model_body.input_names)

tf.keras.experimental.export_saved_model(model_body, model_path, custom_objects={'hard_swish':hard_swish,'relu6':relu6})
print('export savedmodel to ', model_path)