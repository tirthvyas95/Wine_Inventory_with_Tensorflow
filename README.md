# Wine Inventory with Object Detection using Tensorflow 2.X

## Introduction

I did this project as part of the curriculum in Fleming College. The idea is that we can detect the number of bottles and their positions using Object Detection which enables us to track the inventory of wine bottles. The user can enter details of bottles as they insert them into the slots one by one and whey they remove the multiple bottles at a time we can easily detect which bottles were removed. This makes for an effective inventory management system.

## Object Detection of Wine Bottles Guide

### Foreword

In this guide I will list the step on how to install TensorFlow and the necessary libraries to run the Computer Vision algorithm that I created in the project. The algorithm was designed as a proof of concept to demonstrate how the bottle in the rack can be located and counted. All the tests were done on a windows machine since it had a GPU.

This guide and project were made between September 2020 and April 2020 so the more time passes the more issues are going to appear with library dependencies since developers update the libraires frequently and something that is working right now might not work in future. I am going to mention versions of important libraires so if something is not working in the latest installations then you may need to look in the archive to fetch the version that I used. Always check on internet in the forums if you run into some trouble.

**List of Important Libraries and Tools used for the project:**

1.	Python Version 3.8.5
2.	TensorFlow GPU Version 2.3.1
3.	PIP Version 20.2.4
4.	CUDA Version 10.1.243
5.	cuDNN for CUDA 10.1 Version 8.0.4.30
6.	Cython Version 0.29.21
7.	avro-python Version 1.10.0
8.	Numpy Version 1.19.2
9.	OpenCV Version 4.3.0.38
10.	Protobuf Version 3.13.0
11.	Pandas Version 1.1.4
12.	Scipy Version 1.6.1
13.	Pillow Version 8.1.2

**Specs of the test PC:**

* Windows 10
* NVIDIA GeForce GTX 1060 Max-Q, 6 GDDR5 memory
* Intel Core i7-8750H
* 16 Gb DDR4 RAM
* PC type is DELL Notebook G7 15

### Steps:

**Setup TensorFlow GPU**

* First you need to download and install CUDA Toolkit with cudNN to use the NVIDIA graphics card. You can see the detailed tutorial at https://www.youtube.com/watch?v=hHWkvEcDBO0.
* Download TensorFlow models repository from https://github.com/tensorflow/models.
* Then you will need Anaconda for python you can download it from https://www.anaconda.com/products/individual.
* After installing anaconda, open anaconda command prompt in administrator mode and run this command to install PIP “conda install -c anaconda pip”. We are going to use pip to install all the libraries moving forward.
* Now make a new virtual environment in anaconda and install python. To do this use “conda create -n tensorflow pip python=3.8”. Virtual environments are very useful because you can isolate all the libraries and packages from other projects so that the versions of the installations do not clash. And, also if you want to start a project from scratch.
* Activate the environment by using “conda activate tensorflow”, we are going to use this environment for this project.
* Now, to install TensorFlow use “pip install tensorflow-gpu” for the GPU version. If you using only CPU to train or test the models use “pip install tensorflow” instead. I would recommend using GPU to train and test the models because neural networks benefit a lot from it since, GPUs have a large number of simultaneously processing cores. 
* Check if TensorFlow is properly installed by:
```Shell
python
>>> import tensorflow as tf
>>> print(tf. __version__)
```

**Setup other Libraries and Tools:**

* We need to install Protobuf for decompressing the protos by using this command “conda install -c anaconda protobuf”.
* No go to research folder by using “cd models\research”.
* Compile all the protos by “protoc object_detection\protos\*.proto --python_out=. ”.
* Install cython by using “pip install cython” command and close the terminal.
* You will need Visual C++ 2015 build to progress further. If you do not have them download and install from https://go.microsoft.com/fwlink/?LinkId=691126.
* There is a setup python script that can install the libraries for you automatically. To run it use:
```Shell
cd C:\TensorFlow\models\research
copy object_detection\packages\tf2\setup.py .
python -m pip install .
```
* To check if everything went correctly use “python object_detection\builders\model_builder_tf2_test.py”. The output should look like this:

![Capture2](https://user-images.githubusercontent.com/89932233/132107035-f17d7709-9817-4c52-a726-e6ea423b434f.PNG)

**If you done all the above steps correctly, you will be able to test and run the scripts!**

### Running the Scripts

I have made several scripts to test and develop the algorithm and I have also trained several models for recognizing the bottles. You can find everything in the folder.

**Final_Project_Test_1**

This python script uses a very slow but accurate model “faster_rcnn_resnet152_v1_640x640_coco17_tpu-8” and takes 124 areas of interests as a input, runs the neural network inference on each of them, displays an output as follows:

![Capture3](https://user-images.githubusercontent.com/89932233/132107218-0da44706-7639-4185-aa09-4af58a9b99fa.PNG)

The Xs represent the bottle slot that are occupied and Os represent empty bottle slots.

It also starts a JSON server and you can access the data from any device in the same network. This is how I sent the data to the iOS app.

This was a first attempt and this script is very slow making it practically unusable for practical purposes, this is just to test if I could send data over the network.

You can see the output in Preprocessing/test_output_5 directory. Here is an example:

![Capture12](https://user-images.githubusercontent.com/89932233/132107904-1f392e49-9667-4f43-bc62-6e7b8fa3b2d7.PNG)

**Final_Project_Test_3**

I made this script to test the speed of the fast recognition paired with the accuracy of neural network’s detection. This type of system is the fastest and the best I could create in the given time frame. This script is made to test the speed of the detection and it is a night and day difference compared to the earlier attempts. Basically, I you were only using the neural network to detect you would have to check each slot every time you make a change in the actual rack, this system eliminates the need for checking each slot, we are only using the neural network on areas of interests(slots) where a change could have been made. This makes this detection system exceptionally faster and efficient compared to our previous attempts.

This script takes 3 images of the rack and run them one by one essentially simulating changes made in the actual rack.

By pressing enter you can consecutively check 3 images of the rack. The outputs are below:

![Capture8](https://user-images.githubusercontent.com/89932233/132107365-81ccdd63-97a4-4601-8372-bbce1e808280.PNG)

![Capture9](https://user-images.githubusercontent.com/89932233/132107368-9f5b670e-29b6-4341-87bc-2a8f0f62111e.PNG)

![Capture10](https://user-images.githubusercontent.com/89932233/132107369-337bf072-976d-48e4-9042-4a5febee0c15.PNG)

![Capture11](https://user-images.githubusercontent.com/89932233/132107370-03408e3f-aca6-41bb-b66d-8e2361ffcc60.PNG)


## Xcode Views and its Description

This app has been developed by me and it is important to note and understand that I am no professional in iOS app development. I have written limited amount of code only to demonstrate the entire project as a proof of concept. There is a lot of work remaining to finish the entire app. This App only runs on a simulator since I have a very limited experience developing iOS app and it was my first attempt on developing the same. This App is developed on Xcode Version 12.4(12D4e).

The App fetches data from a local JSON server running on the windows machine where the object detection algorithm is also running. Here are some screen-shots of the app pages:

![1](https://user-images.githubusercontent.com/89932233/132107936-0b138694-79d9-4f43-abdf-ccc86b194085.png)

![2](https://user-images.githubusercontent.com/89932233/132107939-71ca1150-4d2f-416c-9774-7e00d942a295.png)

![Capture5](https://user-images.githubusercontent.com/89932233/132108018-ee6528b0-0e98-4940-b13b-37d8bd63e23a.PNG)

![Capture4](https://user-images.githubusercontent.com/89932233/132108020-0d4ab5bf-6d57-4b31-8a2b-ee921c55b961.PNG)


## Conclusion

I made this project as a proof of concept, I have had help from various sources on the internet. I will mention the prominent one in the reference. There is a lot of work to be done in this project and it can be scaled to even bigger systems. You can also run this on a Raspberry Pi if you train a lighter model. And also, for the scope of this project I trained and tested the model on open bottles where the cork is visible but the same rule should apply for new bottles. I would also like to thank Josephine Management Co. Ltd. for the test dataset.

## References

* Pariyadarshan, A. (n.d.). Armaanpriyadarshan's Github. Retrieved September 04, 2021, 
        from https://github.com/armaanpriyadarshan
* Persson, A. (n.d.). Aladdin Persson's Youtube Channel. Retrieved September 04, 2021, 
        from https://www.youtube.com/channel/UCkzW5JSFwvKRjXABI-UTAkQ
* @misc{tensorflowmodelgarden2020,
  author = {Hongkun Yu and Chen Chen and Xianzhi Du and Yeqing Li and
            Abdullah Rashwan and Le Hou and Pengchong Jin and Fan Yang and
            Frederick Liu and Jaeyoun Kim and Jing Li},
  title = {{TensorFlow Model Garden}},
  howpublished = {\url{https://github.com/tensorflow/models}},
  year = {2020}
}

