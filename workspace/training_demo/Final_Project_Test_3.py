#!/usr/bin/env python
# coding: utf-8

import os
import shutil
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
import pathlib
import tensorflow as tf
import cv2
import argparse
import os
import numpy as np

reg = []

tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

parser = argparse.ArgumentParser()
parser.add_argument('--model', help='Folder that the Saved Model is Located In',
                    default='exported-models/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8')
parser.add_argument('--labels', help='Where the Labelmap is Located',
                    default='exported-models/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/saved_model/label_map.pbtxt')
parser.add_argument('--image', help='Name of the single image to perform detection on',
                    default='C:\Tensorflow\Preprocessing\final_test_output_3')
parser.add_argument('--threshold', help='Minimum confidence threshold for displaying detected objects',
                    default=0.80)
                    
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

def crop_fun(path,d1):
    img = cv2.imread(path)

    x = 0
    i = 1
    
    img_cropped = img[197:468,109:368]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[231:497, 720:989]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[271:539, 1279:1515]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[313:568, 1816:2084]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[673:911, 36:282]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[704:925, 518:729]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[715:952, 988:1211]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[741:975, 1493:1707]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[775:1027, 1932:2197]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1075:1268, 1:202]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1066:1245, 382:579]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1086:1293, 768:982]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1075:1282, 1188:1418]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1086:1293, 1604:1809]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1127:1352, 2004:2252]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1368:1550, 1:136]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1375:1566, 295:477]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1377:1536, 632:813]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1380:1543, 982:1186]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1377:1568, 1377:1566]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1418:1600, 1688:1911]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1327:1534, 2036:2252]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1593:1757, 220:400]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1586:1741, 545:711]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1584:1736, 850:1018]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1595:1757, 1170:1341]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1602:1768, 1477:1668]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1611:1773, 1820:2000]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1748:1923, 157:336]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1782:1943, 429:611]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1791:1939, 723:900]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1759:1920, 1007:1186]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1766:1925, 1294:1487]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1770:1916, 1595:1750]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1766:1909, 1877:2057]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1923:2057, 388:527]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1930:2061, 643:791]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1925:2055, 891:1041]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1923:2041, 1177:1297]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1936:2057, 1434:1568]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[1914:2036, 1704:1825]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2043:2159, 338:452]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2057:2166, 579:692]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2059:2170, 809:936]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2066:2180, 1038:1174]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2070:2186, 1275:1400]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2051:2161, 1525:1650]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2020:2136, 1774:1899]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2138:2246, 511:626]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2168:2265, 727:835]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2182:2276, 958:1051]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2172:2264, 1170:1272]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2158:2251, 1382:1485]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2116:2213, 1623:1736]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2243:2347, 430:536]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2236:2331, 653:759]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2249:2347, 858:965]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2276:2378, 1055:1162]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2258:2364, 1261:1362]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2250:2351, 1468:1581]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2208:2319, 1675:1803]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2320:2415, 584:682]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2323:2415, 785:883]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2328:2428, 969:1069]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2353:2445, 1154:1249]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2330:2432, 1357:1459]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2310:2415, 1549:1653]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2388:2478, 520:616]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2372:2477, 711:807]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2395:2491, 893:984]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2396:2488, 1066:1161]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2414:2499, 1254:1341]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2399:2481, 1436:1526]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2385:2473, 1616:1701]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2444:2528, 646:731]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2443:2539, 813:904]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2457:2536, 992:1081]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2459:2538, 1162:1253]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2451:2523, 1329:1402]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2448:2531, 1497:1577]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2482:2566, 581:670]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2507:2585, 764:838]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2503:2582, 920:997]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2508:2588, 1092:1174]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2507:2581, 1241:1316]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2503:2584, 1391:1477]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2491:2573, 1566:1651]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2552:2628, 700:769]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2551:2623, 855:924]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2564:2636, 1007:1081]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2544:2612, 1170:1246]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2547:2622, 1300:1369]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2553:2618, 1454:1527]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2582:2657, 635:711]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2586:2661, 782:861]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2593:2655, 941:1008]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2604:2670, 1081:1149]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2599:2668, 1232:1307]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2595:2665, 1361:1432]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2577:2651, 1506:1574]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2632:2697, 723:799]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2630:2692, 873:939]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2630:2695, 1016:1084]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1
    img_cropped = img[2634:2696, 1151:1216]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2627:2691, 1296:1365]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2627:2695, 1424:1493]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2664:2714, 680:746]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2659:2715, 809:872]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2662:2714, 949:1008]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2672:2731, 1078:1143]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2676:2736, 1214:1272]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2677:2732, 1353:1422]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2669:2731, 1480:1557]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2692:2747, 765:822]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2692:2742, 885:942]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2701:2759, 1014:1073]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2700:2751, 1142:1201]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2711:2761, 1272:1328]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2705:2750, 1405:1458]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2726:2773, 711:762]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2718:2772, 824:881]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2719:2769, 947:1004]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2726:2780, 1081:1138]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2732:2785, 1208:1261]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2718:2774, 1331:1389]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    img_cropped = img[2724:2791, 1454:1520]
    img_cropped = cv2.resize(img_cropped, (150,150))
    cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    x = x + 1

    # img_cropped = img[2731:2789, 1460:1508]
    # img_cropped = cv2.resize(img_cropped, (150,150))
    # cv2.imwrite("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % x, img_cropped)
    # x = x + 1


    print("Crop and Resize Success! at " + path)

def check_all():
    x = 0
    
    while x<126:
        print("Running instance on no. %i" %(x+1))
        image = cv2.imread("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" %x)
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
        cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_4/%i.jpg" %x, image)
        x = x + 1

    print('Done')
    print(' '+' '+' '+reg[0]+' '+reg[1]+' '+reg[2]+' '+reg[3]+' '+' '+' ')
    print(' '+' '+reg[4]+' '+reg[5]+' '+reg[6]+' '+reg[7]+' '+reg[8]+' '+' ')
    print(' '+reg[9]+' '+reg[10]+' '+reg[11]+' '+reg[12]+' '+reg[13]+' '+reg[14]+' ')
    print(reg[15]+' '+reg[16]+' '+reg[17]+' '+reg[18]+' '+reg[19]+' '+reg[20]+' '+reg[21])
    print(' '+reg[22]+' '+reg[23]+' '+reg[24]+' '+reg[25]+' '+reg[26]+' '+reg[27]+' ')
    print(reg[28]+' '+reg[29]+' '+reg[30]+' '+reg[31]+' '+reg[32]+' '+reg[33]+' '+reg[34])
    print(' '+reg[35]+' '+reg[36]+' '+reg[37]+' '+reg[38]+' '+reg[39]+' '+reg[40]+' ')
    print(reg[41]+' '+reg[42]+' '+reg[43]+' '+reg[44]+' '+reg[45]+' '+reg[46]+' '+reg[47])
    print(' '+reg[48]+' '+reg[49]+' '+reg[50]+' '+reg[51]+' '+reg[52]+' '+reg[53]+' ')
    print(reg[54]+' '+reg[55]+' '+reg[56]+' '+reg[57]+' '+reg[58]+' '+reg[59]+' '+reg[60])
    print(' '+reg[61]+' '+reg[62]+' '+reg[63]+' '+reg[64]+' '+reg[65]+' '+reg[66]+' ')
    print(reg[67]+' '+reg[68]+' '+reg[69]+' '+reg[70]+' '+reg[71]+' '+reg[72]+' '+reg[73])
    print(' '+reg[74]+' '+reg[75]+' '+reg[76]+' '+reg[77]+' '+reg[78]+' '+reg[79]+' ')
    print(reg[80]+' '+reg[81]+' '+reg[82]+' '+reg[83]+' '+reg[84]+' '+reg[85]+' '+reg[86])
    print(' '+reg[87]+' '+reg[88]+' '+reg[89]+' '+reg[90]+' '+reg[91]+' '+reg[92]+' ')
    print(reg[93]+' '+reg[94]+' '+reg[95]+' '+reg[96]+' '+reg[97]+' '+reg[98]+' '+reg[99])
    print(' '+reg[100]+' '+reg[101]+' '+reg[102]+' '+reg[103]+' '+reg[104]+' '+reg[105]+' ')
    print(reg[106]+' '+reg[107]+' '+reg[108]+' '+reg[109]+' '+reg[110]+' '+reg[111]+' '+reg[112])
    print(' '+reg[113]+' '+reg[114]+' '+reg[115]+' '+reg[116]+' '+reg[117]+' '+reg[118]+' ')
    print(reg[119]+' '+reg[120]+' '+reg[121]+' '+reg[122]+' '+reg[123]+' '+reg[124]+' '+reg[125])

def fast_check(d1,d2):
    z = 0
    while z<126:
        img = cv2.imread("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" % z)
        img2 = cv2.imread("C:/Tensorflow/Preprocessing/"+d2+"/%i.jpg" % z)
        
        diff = cv2.subtract(img, img2)
        imgray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(imgray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        count = 0
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 0:
                count = count + 1
                cv2.drawContours(diff, contours, -1, (0, 255, 0), 3)
        
        if count>0:
            #cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_1/%i.jpg" %z, diff)
            check_one(z,d1)
        #print(count)
        z = z + 1
    print('Done')
    print(' '+' '+' '+reg[0]+' '+reg[1]+' '+reg[2]+' '+reg[3]+' '+' '+' ')
    print(' '+' '+reg[4]+' '+reg[5]+' '+reg[6]+' '+reg[7]+' '+reg[8]+' '+' ')
    print(' '+reg[9]+' '+reg[10]+' '+reg[11]+' '+reg[12]+' '+reg[13]+' '+reg[14]+' ')
    print(reg[15]+' '+reg[16]+' '+reg[17]+' '+reg[18]+' '+reg[19]+' '+reg[20]+' '+reg[21])
    print(' '+reg[22]+' '+reg[23]+' '+reg[24]+' '+reg[25]+' '+reg[26]+' '+reg[27]+' ')
    print(reg[28]+' '+reg[29]+' '+reg[30]+' '+reg[31]+' '+reg[32]+' '+reg[33]+' '+reg[34])
    print(' '+reg[35]+' '+reg[36]+' '+reg[37]+' '+reg[38]+' '+reg[39]+' '+reg[40]+' ')
    print(reg[41]+' '+reg[42]+' '+reg[43]+' '+reg[44]+' '+reg[45]+' '+reg[46]+' '+reg[47])
    print(' '+reg[48]+' '+reg[49]+' '+reg[50]+' '+reg[51]+' '+reg[52]+' '+reg[53]+' ')
    print(reg[54]+' '+reg[55]+' '+reg[56]+' '+reg[57]+' '+reg[58]+' '+reg[59]+' '+reg[60])
    print(' '+reg[61]+' '+reg[62]+' '+reg[63]+' '+reg[64]+' '+reg[65]+' '+reg[66]+' ')
    print(reg[67]+' '+reg[68]+' '+reg[69]+' '+reg[70]+' '+reg[71]+' '+reg[72]+' '+reg[73])
    print(' '+reg[74]+' '+reg[75]+' '+reg[76]+' '+reg[77]+' '+reg[78]+' '+reg[79]+' ')
    print(reg[80]+' '+reg[81]+' '+reg[82]+' '+reg[83]+' '+reg[84]+' '+reg[85]+' '+reg[86])
    print(' '+reg[87]+' '+reg[88]+' '+reg[89]+' '+reg[90]+' '+reg[91]+' '+reg[92]+' ')
    print(reg[93]+' '+reg[94]+' '+reg[95]+' '+reg[96]+' '+reg[97]+' '+reg[98]+' '+reg[99])
    print(' '+reg[100]+' '+reg[101]+' '+reg[102]+' '+reg[103]+' '+reg[104]+' '+reg[105]+' ')
    print(reg[106]+' '+reg[107]+' '+reg[108]+' '+reg[109]+' '+reg[110]+' '+reg[111]+' '+reg[112])
    print(' '+reg[113]+' '+reg[114]+' '+reg[115]+' '+reg[116]+' '+reg[117]+' '+reg[118]+' ')
    print(reg[119]+' '+reg[120]+' '+reg[121]+' '+reg[122]+' '+reg[123]+' '+reg[124]+' '+reg[125])
    
def check_one(x,d1):
    print("Found change in slot no: %i" %(x+1))
    image = cv2.imread("C:/Tensorflow/Preprocessing/"+d1+"/%i.jpg" %x)
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
        reg.pop(x)
        reg.insert(x,"X")
    else:
        reg.pop(x)
        reg.insert(x,"O")
        
    #print('Done')
    #filename = 'savedImage.jpg'
    #cv2.imwrite(filename, image)
    #print(count)
    # DISPLAYS OUTPUT IMAGE
    #cv2.imshow('Object Counter', image)
    


    #filename = 'savedImage.jpg'
    cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_1/%i.jpg" %x, image)

print("Testing for the first Image!")
crop_fun("C:/Tensorflow/Preprocessing/test_new_2/first.jpg","final_test_output_3")

print("Checking all the slots with Neural Network assisted detection.....")

check_all()

print("This is the result of neural network checking each slot.")

input("Press enter key to initiate fast checking....")

while(1):
    crop_fun("C:/Tensorflow/Preprocessing/test_new_2/second.jpg","final_test_output_2")
    fast_check("final_test_output_2","final_test_output_3")

    input("Press enter key to initiate fast checking....")
    
    crop_fun("C:/Tensorflow/Preprocessing/test_new_2/third.jpg","final_test_output_3")
    fast_check("final_test_output_3","final_test_output_2")
    
    input("Press enter key to initiate fast checking....")
    
    crop_fun("C:/Tensorflow/Preprocessing/test_new_2/first.jpg","final_test_output_2")
    fast_check("final_test_output_2","final_test_output_3")
    
    input("Press enter key to initiate fast checking....")

