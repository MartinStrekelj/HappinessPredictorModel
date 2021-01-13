import pickle
import numpy

print(pickle.__doc__)

with open ("model\light_model_metadata.pickle", "rb") as  file:
    obj = pickle.load(file)
    print(obj)
