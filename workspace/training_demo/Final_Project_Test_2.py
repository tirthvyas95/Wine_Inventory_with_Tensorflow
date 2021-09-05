#!/usr/bin/env python
# coding: utf-8

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
import pathlib
import tensorflow as tf
import cv2
import argparse
import os

path = "C:/Tensorflow/Preprocessing/test_new_2/first.jpg"

img = cv2.imread(path)

x = 0
i = 1
img_cropped = img[197:468,109:368]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[231:497, 720:989]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[271:539, 1279:1515]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[313:568, 1816:2084]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[673:911, 36:282]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[704:925, 518:729]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[715:952, 988:1211]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[741:975, 1493:1707]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[775:1027, 1932:2197]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1075:1268, 1:202]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1066:1245, 382:579]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1086:1293, 768:982]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1075:1282, 1188:1418]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1086:1293, 1604:1809]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1127:1352, 2004:2252]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1368:1550, 1:136]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1375:1566, 295:477]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1377:1536, 632:813]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1380:1543, 982:1186]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1377:1568, 1377:1566]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1418:1600, 1688:1911]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1327:1534, 2036:2252]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1593:1757, 220:400]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1586:1741, 545:711]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1584:1736, 850:1018]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1595:1757, 1170:1341]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1602:1768, 1477:1668]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1611:1773, 1820:2000]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1748:1923, 157:336]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1782:1943, 429:611]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1791:1939, 723:900]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1759:1920, 1007:1186]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1766:1925, 1294:1487]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1770:1916, 1595:1750]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1766:1909, 1877:2057]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1923:2057, 388:527]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1930:2061, 643:791]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1925:2055, 891:1041]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1923:2041, 1177:1297]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1936:2057, 1434:1568]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1914:2036, 1704:1825]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2043:2159, 338:452]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2057:2166, 579:692]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2059:2170, 809:936]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2066:2180, 1038:1174]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2070:2186, 1275:1400]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2051:2161, 1525:1650]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2020:2136, 1774:1899]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2138:2246, 511:626]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2168:2265, 727:835]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2182:2276, 958:1051]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2172:2264, 1170:1272]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2158:2251, 1382:1485]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2116:2213, 1623:1736]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2243:2347, 430:536]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2236:2331, 653:759]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2249:2347, 858:965]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2276:2378, 1055:1162]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2258:2364, 1261:1362]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2250:2351, 1468:1581]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2208:2319, 1675:1803]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2320:2415, 584:682]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2323:2415, 785:883]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2328:2428, 969:1069]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2353:2445, 1154:1249]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2330:2432, 1357:1459]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2310:2415, 1549:1653]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2388:2478, 520:616]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2372:2477, 711:807]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2395:2491, 893:984]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2396:2488, 1066:1161]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2414:2499, 1254:1341]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2399:2481, 1436:1526]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2385:2473, 1616:1701]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2444:2528, 646:731]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2443:2539, 813:904]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2457:2536, 992:1081]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2459:2538, 1162:1253]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2451:2523, 1329:1402]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2448:2531, 1497:1577]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2482:2566, 581:670]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2507:2585, 764:838]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2503:2582, 920:997]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2508:2588, 1092:1174]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2507:2581, 1241:1316]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2503:2584, 1391:1477]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2491:2573, 1566:1651]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2552:2628, 700:769]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2551:2623, 855:924]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2564:2636, 1007:1081]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2544:2612, 1170:1246]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2547:2622, 1300:1369]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2553:2618, 1454:1527]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2582:2657, 635:711]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2586:2661, 782:861]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2593:2655, 941:1008]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2604:2670, 1081:1149]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2599:2668, 1232:1307]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2595:2665, 1361:1432]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2577:2651, 1506:1574]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2632:2697, 723:799]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2630:2692, 873:939]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2630:2695, 1016:1084]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1
img_cropped = img[2634:2696, 1151:1216]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2627:2691, 1296:1365]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2627:2695, 1424:1493]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2664:2714, 680:746]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2659:2715, 809:872]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2662:2714, 949:1008]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2672:2731, 1078:1143]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2676:2736, 1214:1272]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2677:2732, 1353:1422]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2669:2731, 1480:1557]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2692:2747, 765:822]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2692:2742, 885:942]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2701:2759, 1014:1073]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2700:2751, 1142:1201]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2711:2761, 1272:1328]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2705:2750, 1405:1458]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2726:2773, 711:762]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2718:2772, 824:881]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2719:2769, 947:1004]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2726:2780, 1081:1138]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2732:2785, 1208:1261]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2718:2774, 1331:1389]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2724:2791, 1454:1520]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
x = x + 1

# img_cropped = img[2731:2789, 1460:1508]
# img_cropped = cv2.resize(img_cropped, (150,150))
# cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, img_cropped)
# x = x + 1


print("Crop and Resize Success!")



tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

parser = argparse.ArgumentParser()
parser.add_argument('--model', help='Folder that the Saved Model is Located In',
                    default='exported-models/faster_rcnn_resnet152_v1_640x640_coco17_tpu-8')
parser.add_argument('--labels', help='Where the Labelmap is Located',
                    default='exported-models/faster_rcnn_resnet152_v1_640x640_coco17_tpu-8/saved_model/label_map.pbtxt')
parser.add_argument('--image', help='Name of the single image to perform detection on',
                    default='C:\Tensorflow\Preprocessing\final_test_output_1')
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

import json

data = {}
data['posts'] = []
data['comments'] = []
data['profile'] = []

with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

print("Json data file created")
while x<126:
    print("Running instance on no. %i" %(x+1))
    image = cv2.imread("C:/Tensorflow/Preprocessing/final_test_output_1/%i.jpg" %x)
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
    
    data['posts'].append({
        's': '%s' %reg[x],
    })


    #filename = 'savedImage.jpg'
    cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_1/%i.jpg" %x, image)
    x = x + 1

x = 0
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

print("Json file written")

print('Done')
print(' '+' '+' '+' '+' '+reg[0]+' '+reg[1]+' '+' '+' '+' ')
print(' '+' '+reg[2]+' '+reg[3]+' '+reg[4]+' '+reg[5]+' '+reg[6]+' '+' ')
print(' '+reg[7]+' '+reg[8]+' '+reg[9]+' '+reg[10]+' '+reg[11]+' '+reg[12])
print(reg[13]+' '+reg[14]+' '+reg[15]+' '+reg[16]+' '+reg[17]+' '+reg[18]+' '+reg[19])
print(' '+reg[20]+' '+reg[21]+' '+reg[22]+' '+reg[23]+' '+reg[24]+' '+reg[25])
print(reg[26]+' '+reg[27]+' '+reg[28]+' '+reg[29]+' '+reg[30]+' '+reg[31]+' '+reg[32])
print(' '+reg[33]+' '+reg[34]+' '+reg[35]+' '+reg[36]+' '+reg[37]+' '+reg[38])
print(reg[39]+' '+reg[40]+' '+reg[41]+' '+reg[42]+' '+reg[43]+' '+reg[44]+' '+reg[45])
print(' '+reg[46]+' '+reg[47]+' '+reg[48]+' '+reg[49]+' '+reg[50]+' '+reg[51])
print(reg[52]+' '+reg[53]+' '+reg[54]+' '+reg[55]+' '+reg[56]+' '+reg[57]+' '+reg[58])
print(' '+reg[59]+' '+reg[60]+' '+reg[61]+' '+reg[62]+' '+reg[63]+' '+reg[64])
print(reg[65]+' '+reg[66]+' '+reg[67]+' '+reg[68]+' '+reg[69]+' '+reg[70]+' '+reg[71])
print(' '+reg[72]+' '+reg[73]+' '+reg[74]+' '+reg[75]+' '+reg[76]+' '+reg[77])
print(reg[78]+' '+reg[79]+' '+reg[80]+' '+reg[81]+' '+reg[82]+' '+reg[83]+' '+reg[84])
print(' '+reg[85]+' '+reg[86]+' '+reg[87]+' '+reg[88]+' '+reg[89]+' '+reg[90])
print(reg[91]+' '+reg[92]+' '+reg[93]+' '+reg[94]+' '+reg[95]+' '+reg[96]+' '+reg[97])
print(' '+reg[95]+' '+reg[100]+' '+reg[105]+' '+reg[120]+' '+reg[115]+' '+reg[121])
print(reg[96]+' '+reg[99]+' '+reg[102]+' '+reg[107]+' '+reg[114]+' '+reg[116]+' '+reg[122])
print(' '+reg[98]+' '+reg[101]+' '+reg[104]+' '+reg[108]+' '+reg[110]+' '+reg[112])
print(reg[97]+' '+reg[100]+' '+reg[103]+' '+reg[106]+' '+reg[109]+' '+reg[111]+' '+reg[113])

input("Press enter key to inject another image....")

path = "C:/Tensorflow/Preprocessing/test/second.jpg"

img = cv2.imread(path)

x = 0
i = 1
img_cropped = img[200:455,111:377]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[227:475, 722:970]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[270:525, 1279:1507]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[307:566, 1816:2082]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[682:918, 32:282]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[693:930, 529:747]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[716:959, 984:1200]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[734:975, 1472:1711]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1091:1264, 7:200]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1073:1257, 391:588]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1075:1273, 770:988]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1077:1275, 1204:1397]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1089:1300, 1611:1818]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1132:1336, 2020:2243]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1370:1536, 1:130]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1389:1545, 307:470]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1384:1534, 643:822]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1393:1523, 1011:1161]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1409:1561, 1375:1547]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1457:1600, 1727:1909]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1370:1511, 2086:2252]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1607:1743, 243:391]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1595:1725, 547:679]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1586:1732, 863:995]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1602:1752, 1172:1329]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1620:1764, 1502:1659]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1643:1764, 1847:1995]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1762:1885, 186:325]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1793:1939, 452:607]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1787:1919, 747:891]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1770:1900, 1030:1169]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1768:1914, 1318:1459]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1789:1909, 1616:1738]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1764:1905, 1897:2043]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1932:2057, 400:520]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1934:2064, 659:782]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1710:1829, 1028:1157]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1923:2057, 897:1038]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1932:2055, 1172:1311]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1948:2061, 1434:1579]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[1923:2034, 1691:1825]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2050:2161, 343:452]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2048:2150, 588:691]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2055:2159, 811:927]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2072:2177, 1052:1171]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2062:2175, 1288:1402]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2060:2158, 1539:1647]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2036:2134, 1769:1886]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2144:2241, 519:614]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2172:2270, 733:828]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2186:2280, 950:1052]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2172:2269, 1166:1272]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2153:2250, 1383:1484]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2127:2211, 1619:1711]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2253:2334, 439:533]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2252:2325, 659:758]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2264:2352, 866:962]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2266:2361, 1062:1148]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2273:2338, 1264:1352]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2257:2330, 1476:1571]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2219:2308, 1700:1781]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2328:2398, 594:675]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2328:2408, 791:877]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2345:2419, 978:1059]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2353:2430, 1162:1241]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2327:2411, 1361:1442]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2317:2386, 1561:1630]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2394:2466, 536:598]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2388:2455, 720:792]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2403:2472, 905:972]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2407:2490, 789:870]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2406:2475, 1075:1145]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2413:2488, 1258:1337]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2395:2469, 1436:1514]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2389:2463, 1614:1691]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2441:2516, 659:725]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2453:2530, 825:895]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2456:2533, 1006:1075]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2459:2533, 1169:1242]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2452:2516, 1330:1406]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2452:2519, 1502:1562]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2484:2559, 595:661]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2491:2577, 770:834]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2505:2581, 923:994]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2522:2589, 1105:1167]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2519:2581, 1253:1305]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2509:2580, 1394:1466]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2495:2572, 1567:1636]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2553:2625, 702:759]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2556:2616, 861:920]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2573:2634, 1020:1078]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2555:2613, 1175:1237]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2563:2617, 1306:1362]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2561:2616, 1455:1516]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2595:2652, 642:705]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2601:2654, 795:845]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2603:2654, 950:1011]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2609:2665, 1089:1145]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2609:2661, 1236:1298]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2600:2653, 1364:1423]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2591:2648, 1514:1572]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2638:2690, 734:782]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2634:2688, 877:934]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1
img_cropped = img[2644:2691, 1025:1077]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2640:2690, 1157:1203]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2627:2684, 1306:1350]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2636:2689, 1428:1482]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2661:2708, 692:741]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2666:2709, 817:863]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2668:2714, 957:1004]
img_cropped = img[2750:2819, 1176:1236]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2679:2726, 1087:1133]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2683:2734, 1218:1272]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2675:2731, 1358:1412]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2672:2725, 1480:1537]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2696:2746, 768:815]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2691:2738, 887:939]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2696:2750, 1015:1065]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2699:2743, 1146:1196]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2703:2753, 1275:1325]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2706:2752, 1410:1458]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2709:2768, 712:763]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2714:2772, 828:880]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2714:2770, 950:1000]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2720:2775, 1079:1138]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2724:2782, 1202:1263]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2725:2778, 1340:1388]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

img_cropped = img[2731:2789, 1460:1508]
img_cropped = cv2.resize(img_cropped, (150,150))
cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" % x, img_cropped)
x = x + 1

print("Crop and Resize Success for 2 image!")

while x < 126:
    image11 = cv2.imread("C:/Tensorflow/Preprocessing/final_test_output_1/%i.jpg" %x)
    image22 = cv2.imread("C:/Tensorflow/Preprocessing/final_test_output_2/%i.jpg" %x)

    diff = cv2.subtract(image11, image22)
    
    cv2.imwrite("C:/Tensorflow/Preprocessing/final_test_output_3/%i.jpg" % x, diff)

    imgray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #print(contours)
    for contour in contours:
        area = cv.contourArea(contour)
        if area > 0:
            if reg[x] == 'X':
                reg[x] = 'O'
            if reg[x] == 'O':
                reg[x] = 'X'
    
    
    data['posts'].append({
        's': '%s' %reg[x],
    })

    x = x + 1

print('Done')
print(' '+' '+' '+' '+' '+reg[0]+' '+reg[1]+' '+' '+' '+' ')
print(' '+' '+reg[2]+' '+reg[3]+' '+reg[4]+' '+reg[5]+' '+reg[6]+' '+' ')
print(' '+reg[7]+' '+reg[8]+' '+reg[9]+' '+reg[10]+' '+reg[11]+' '+reg[12])
print(reg[13]+' '+reg[14]+' '+reg[15]+' '+reg[16]+' '+reg[17]+' '+reg[18]+' '+reg[19])
print(' '+reg[20]+' '+reg[21]+' '+reg[22]+' '+reg[23]+' '+reg[24]+' '+reg[25])
print(reg[26]+' '+reg[27]+' '+reg[28]+' '+reg[29]+' '+reg[30]+' '+reg[31]+' '+reg[32])
print(' '+reg[33]+' '+reg[34]+' '+reg[35]+' '+reg[36]+' '+reg[37]+' '+reg[38])
print(reg[39]+' '+reg[40]+' '+reg[41]+' '+reg[42]+' '+reg[43]+' '+reg[44]+' '+reg[45])
print(' '+reg[46]+' '+reg[47]+' '+reg[48]+' '+reg[49]+' '+reg[50]+' '+reg[51])
print(reg[52]+' '+reg[53]+' '+reg[54]+' '+reg[55]+' '+reg[56]+' '+reg[57]+' '+reg[58])
print(' '+reg[59]+' '+reg[60]+' '+reg[61]+' '+reg[62]+' '+reg[63]+' '+reg[64])
print(reg[65]+' '+reg[66]+' '+reg[67]+' '+reg[68]+' '+reg[69]+' '+reg[70]+' '+reg[71])
print(' '+reg[72]+' '+reg[73]+' '+reg[74]+' '+reg[75]+' '+reg[76]+' '+reg[77])
print(reg[78]+' '+reg[79]+' '+reg[80]+' '+reg[81]+' '+reg[82]+' '+reg[83]+' '+reg[84])
print(' '+reg[85]+' '+reg[86]+' '+reg[87]+' '+reg[88]+' '+reg[89]+' '+reg[90])
print(reg[91]+' '+reg[92]+' '+reg[93]+' '+reg[94]+' '+reg[95]+' '+reg[96]+' '+reg[97])
print(' '+reg[95]+' '+reg[100]+' '+reg[105]+' '+reg[120]+' '+reg[115]+' '+reg[121])
print(reg[96]+' '+reg[99]+' '+reg[102]+' '+reg[107]+' '+reg[114]+' '+reg[116]+' '+reg[122])
print(' '+reg[98]+' '+reg[101]+' '+reg[104]+' '+reg[108]+' '+reg[110]+' '+reg[112])
print(reg[97]+' '+reg[100]+' '+reg[103]+' '+reg[106]+' '+reg[109]+' '+reg[111]+' '+reg[113])

input("Press enter key to start server....")

print("Starting the server.....")
print("Using IP: 192.168.69.180, Port: 3000, Keyword:'posts'")
os.system("json-server --host 192.168.69.180 data.json --port 3000")

