'''
In this code, I will not provide our deep learning model and data shapes.
Because that it's our result of research.
So we can't provide our project core to you.
'''
import tensorflow as tf

# load from the trained model using keras.
m = tf.keras.models.load_model('keras_tiny_tf_v1.h5')
m.summary()

# predict
shapes = None # please setup your self.
x = np.array([shapes])
res = m.predict(x)
print(res)


#convert and save to lite tf model.
Converter = tf.lite.TFLiteConverter.from_keras_model(m)
tflite_model = Converter.convert()
open('converted_tfmodel_lite.tflite', 'wb').write(tflite_model)
