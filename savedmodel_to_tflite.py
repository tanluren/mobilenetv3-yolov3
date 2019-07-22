import tensorflow as tf


converter = tf.lite.TFLiteConverter.from_saved_model('tmp/keras_savedmodel')
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
tflite_quant_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_quant_model)