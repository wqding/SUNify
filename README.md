# SUNify

Turn a cloudy picture into a SUNNY one!!!

This model uses the CycleGAN to perform unpaired image to image translation.

You can download the trained model at: https://drive.google.com/open?id=1YxaG1aUWy2EGobZ_V_FWJ1OOB2WbHE_-
You can load it using tf.saved_model.load(): https://www.tensorflow.org/api_docs/python/tf/saved_model/load

You can take the untrained model and use it to train on a different dataset to produce your own image translator. For the untrained model, checkout sun-syle.py

Results using images taken from my own camera:
Input vs Generated

![example 1](examples/ex1.png)

![example 2](./examples/ex2.png)

![example 3](./examples/ex3.png)
