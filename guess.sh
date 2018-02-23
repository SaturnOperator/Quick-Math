#!/bin/bash
/usr/bin/docker run -v ~/Desktop/Quick-Math-master/images/:/tf_files -v '/home/xunxun/Desktop/t.jpeg':/img/guess.jpg xblaster/tensor-guess /bin/sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg"
