import tensorflow as tf
import matplotlib.pyplot as plt

import sun_style as SS


def generate_images(model, test_input):
    prediction = model(test_input)
        
    plt.figure(figsize=(12, 12))

    display_list = [test_input[0], prediction[0]]

    for i in range(2):
        plt.subplot(1, 2, i+1)
        # getting the pixel values between [0, 1] to plot it.
        plt.imshow(display_list[i] * 0.5 + 0.5)
        plt.axis('off')
    plt.show()
    
    
test_gloomy = SS.create_dataset('resized/test_gloomy')

test_gloomy = test_gloomy.map(
    SS.preprocess_image_test, num_parallel_calls=SS.AUTOTUNE).cache().shuffle(
    SS.BUFFER_SIZE).batch(1)

saved_model = tf.saved_model.load('./saved/generator_g')

# Run the trained model on the test dataset
for inp in test_gloomy:
    generate_images(saved_model, inp)
    