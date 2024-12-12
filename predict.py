import sys
import pickle
import numpy as np
import pandas as pd  # Import pandas

# Load the model
with open('model/FarmVisionModel.pkl', 'rb') as f:
    model = pickle.load(f)

# Get inputs from Node.js
nitrogen = float(sys.argv[1])
phosphorus = float(sys.argv[2])
potassium = float(sys.argv[3])
ph = float(sys.argv[4])
humidity = float(sys.argv[5])
temperature = float(sys.argv[6])
rainfall = float(sys.argv[7])

# Create input DataFrame for model prediction
input_features = pd.DataFrame({
    'N': [nitrogen],
    'P': [phosphorus],
    'K': [potassium],
    'temperature': [temperature],
    'humidity': [humidity],
    'ph': [ph],
    'rainfall': [rainfall]
})

# Predict crop
prediction = model.predict(input_features)

# Send the prediction back to Node.js
print(prediction[0])
