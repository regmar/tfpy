


import tensorflow as tf 

# from keras.utils import CustomObjectScope
from model import relu6


# print(relu6(5.4));
# print("after relu6");


# with CustomObjectScope({'relu6': keras.applications.mobilenet.relu6,'DepthwiseConv2D': keras.applications.mobilenet.DepthwiseConv2D}):
# with CustomObjectScope({'relu6': relu6}):
   # new_model= tf.keras.models.load_model(filepath="ep-083-vl-0.1770.hdf5")
    # model = load_model('ep-083-vl-0.1770.hdf5')

tf.compat.v2.executing_eagerly

new_model= tf.keras.models.load_model(filepath="ep-083-vl-0.1770.hdf5",tf.keras.utils.custom_object_scope={'relu6':relu6})
# tflite_converter = tf.compat.v2.lite.TFLiteConverter.from_keras_model(new_model)
# tflite_model = tflite_converter.convert()

converter = tf.compat.v2.lite.TFLiteConverter.from_keras_model(new_model)
converter.experimental_new_converter = True
tflite_model = converter.convert()


open("tf_lite_model_1.tflite", "wb").write(tflite_model)



#converter = lite.TFLiteConverter.from_keras_model(model)
#tflite_model = converter.convert()

#converter = lite.TFLiteConverter.from_keras_model(model)
#tflite_model = converter.convert()


#converter = lite.TFLiteConverter.from_saved_model(saved_model_dir)
#tflite_model = converter.convert()
#open("converted_model.tflite", "wb").write(tflite_model)

