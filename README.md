# SUNify

Turn a cloudy picture into a SUNNY one!!!

This model uses the CycleGAN to perform unpaired image to image translation.

The pretrained model is stored in the "saved" folder in .pb format. 
You can load it using tf.saved_model.load(): https://www.tensorflow.org/api_docs/python/tf/saved_model/load

You can take the untrained model and use it to train on a different dataset to produce your own image translator. For the untrained model, checkout sun-syle.py

