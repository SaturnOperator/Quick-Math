#!/bin/bash
/usr/bin/docker run -v /home/xunxun/Quick-Math/images/:/tf_files -v /home/xunxun/Desktop/plus.jpg:/img/guess.jpg xblaster/tensor-guess /bin/sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg"
