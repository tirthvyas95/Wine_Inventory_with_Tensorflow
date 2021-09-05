#!/usr/bin/env python
# coding: utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
import pathlib
import tensorflow as tf
import cv2
import argparse
import os

tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

parser = argparse.ArgumentParser()
parser.add_argument('--model', help='Folder that the Saved Model is Located In',
                    default='exported-models/faster_rcnn_resnet152_v1_640x640_coco17_tpu-8')
parser.add_argument('--labels', help='Where the Labelmap is Located',
                    default='exported-models/faster_rcnn_resnet152_v1_640x640_coco17_tpu-8/saved_model/label_map.pbtxt')
parser.add_argument('--image', help='Name of the single image to perform detection on',
                    default='C:\Tensorflow\Preprocessing\test_output_4')
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                    default=0.20)
                    
args = parser.parse_args()
# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# PROVIDE PATH TO IMAGE DIRECTORY
IMAGE_PATHS = args.image


# PROVIDE PATH TO MODEL DIRECTORY
PATH_TO_MODEL_DIR = args.model

# PROVIDE PATH TO LABEL MAP
PATH_TO_LABELS = args.labels

# PROVIDE THE MINIMUM CONFIDENCE THRESHOLD
MIN_CONF_THRESH = float(args.threshold)

# LOAD THE MODEL

import time
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"

print('Loading model...', end='')
start_time = time.time()

# LOAD SAVED MODEL AND BUILD DETECTION FUNCTION
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

# LOAD LABEL MAP DATA FOR PLOTTING

category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS,
                                                                    use_display_name=True)

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
      path: the file path to the image

    Returns:
      uint8 numpy array with shape (img_height, img_width, 3)
    """
    return np.array(Image.open(path))



#print('Running inference for {}... '.format(IMAGE_PATHS), end='')

#list = os.listdir("C:/Tensorflow/Preprocessing/test_output_4")
x = 0
reg = []

while x<123:
    image = cv2.imread("C:/Tensorflow/Preprocessing/test_output_4/%i.jpg" %x)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    imH, imW, _ = image.shape
    image_expanded = np.expand_dims(image_rgb, axis=0)

    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis, ...]

    # input_tensor = np.expand_dims(image_np, 0)
    detections = detect_fn(input_tensor)

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                   for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)
    scores = detections['detection_scores']
    boxes = detections['detection_boxes']
    classes = detections['detection_classes']
    count = 0
    for i in range(len(scores)):
        if ((scores[i] > MIN_CONF_THRESH) and (scores[i] <= 1.0)):
            #increase count
            count += 1
            # Get bounding box coordinates and draw box
            # Interpreter can return coordinates that are outside of image dimensions, need to force them to be within image using max() and min()
            ymin = int(max(1,(boxes[i][0] * imH)))
            xmin = int(max(1,(boxes[i][1] * imW)))
            ymax = int(min(imH,(boxes[i][2] * imH)))
            xmax = int(min(imW,(boxes[i][3] * imW)))
        
            cv2.rectangle(image, (xmin,ymin), (xmax,ymax), (10, 255, 0), 2)
            # Draw label
            object_name = category_index[int(classes[i])]['name'] # Look up object name from "labels" array using class index
            label = '%s: %d%%' % (object_name, int(scores[i]*100)) # Example: 'person: 72%'
            labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
            label_ymin = max(ymin, labelSize[1] + 10) # Make sure not to draw label too close to top of window
            cv2.rectangle(image, (xmin, label_ymin-labelSize[1]-10), (xmin+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
            cv2.putText(image, label, (xmin, label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2) # Draw label text
        

    cv2.putText (image,'Total Detections : ' + str(count),(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(70,235,52),2,cv2.LINE_AA)
    if count>0:
        reg.append('X')
    else:
        reg.append('O')
    #print('Done')
    #filename = 'savedImage.jpg'
    #cv2.imwrite(filename, image)
    #print(count)
    # DISPLAYS OUTPUT IMAGE
    #cv2.imshow('Object Counter', image)


    #filename = 'savedImage.jpg'
    cv2.imwrite("C:/Tensorflow/Preprocessing/test_output_5/%i.jpg" %x, image)
    x = x + 1


print('Done')
print(' '+' '+' '+' '+' '+reg[0]+' '+reg[1]+' '+' '+' '+' ')
print(' '+' '+reg[3]+' '+reg[2]+' '+reg[4]+' '+reg[5]+' '+reg[6]+' '+' ')
print(' '+reg[7]+' '+reg[8]+' '+reg[9]+' '+reg[10]+' '+reg[11]+' '+reg[12])
print(reg[20]+' '+reg[19]+' '+reg[18]+' '+reg[17]+' '+reg[21]+' '+reg[14]+' '+reg[13])
print(' '+reg[27]+' '+reg[26]+' '+reg[25]+' '+reg[24]+' '+reg[22]+' '+reg[15])
print(reg[28]+' '+reg[29]+' '+reg[34]+' '+reg[36]+' '+reg[38]+' '+reg[23]+' '+reg[16])
print(' '+reg[30]+' '+reg[33]+' '+reg[35]+' '+reg[37]+' '+reg[39]+' '+reg[42])
print(reg[31]+' '+reg[32]+' '+reg[45]+' '+reg[47]+' '+reg[44]+' '+reg[40]+' '+reg[43])
print(' '+reg[48]+' '+reg[46]+' '+reg[51]+' '+reg[52]+' '+reg[53]+' '+reg[41])
print(reg[49]+' '+reg[50]+' '+reg[59]+' '+reg[58]+' '+reg[78]+' '+reg[54]+' '+reg[55])
print(' '+reg[63]+' '+reg[60]+' '+reg[62]+' '+reg[77]+' '+reg[79]+' '+reg[56])
print(reg[64]+' '+reg[65]+' '+reg[61]+' '+reg[72]+' '+reg[76]+' '+reg[83]+' '+reg[57])
print(' '+reg[66]+' '+reg[70]+' '+reg[71]+' '+reg[73]+' '+reg[75]+' '+reg[84])
print(reg[67]+' '+reg[69]+' '+reg[86]+' '+reg[90]+' '+reg[74]+' '+reg[80]+' '+reg[85])
print(' '+reg[68]+' '+reg[93]+' '+reg[87]+' '+reg[89]+' '+reg[118]+' '+reg[81])
print(reg[94]+' '+reg[92]+' '+reg[91]+' '+reg[88]+' '+reg[119]+' '+reg[117]+' '+reg[82])
print(' '+reg[95]+' '+reg[100]+' '+reg[105]+' '+reg[120]+' '+reg[115]+' '+reg[121])
print(reg[96]+' '+reg[99]+' '+reg[102]+' '+reg[107]+' '+reg[114]+' '+reg[116]+' '+reg[122])
print(' '+reg[98]+' '+reg[101]+' '+reg[104]+' '+reg[108]+' '+reg[110]+' '+reg[112])
print(reg[97]+' '+reg[100]+' '+reg[103]+' '+reg[106]+' '+reg[109]+' '+reg[111]+' '+reg[113])

