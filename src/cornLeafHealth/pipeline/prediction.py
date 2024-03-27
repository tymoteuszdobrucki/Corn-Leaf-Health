import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

PREDICTION_DICT = {
    0: "Blight",
    1: "Common Rust",
    2: "Gray Leaf Spot",
    3: "Healthy"
    }

class PredictionPipeline:
    
    def __init__(self, filename):
        self.filename = filename
        
        
    def predict(self):
        model = load_model(os.path.join("model","model.h5"))
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = test_image/255 # rescale 1./255
        test_image = np.expand_dims(test_image, axis=0)
        result = model.predict(test_image)
        result_argmax = np.argmax(model.predict(test_image), axis=1)[0]
        confidence = round(result[0][result_argmax]*100)
        if result_argmax == 3:
            return [{ "Prediction" : f"{PREDICTION_DICT[result_argmax]} with {confidence}% confidence"}]   
        else:
            return [{ "Prediction" : f"Disease ({PREDICTION_DICT[result_argmax]}) with {confidence}% confidence"}]    