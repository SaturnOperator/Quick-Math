#!/bin/bash
#docker run -v $1:/tf_files -v $2:/img/guess.jpg  xblaster/tensor-guess sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg"
docker run -it -v /home/xunxun/tensorflow_image_classifier/images/:/tf_files -v /home/xunxun/Desktop/plus.jpg:/img/guess.jpg xblaster/tensor-guess sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg" | grep 'score'
