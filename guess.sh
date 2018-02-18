#!/bin/bash
/usr/bin/docker run -v /home/xunxun/Quick-Math/images/:/tf_files -v /etc/uploads/image.jpg:/img/guess.jpg xblaster/tensor-guess /bin/sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg"
