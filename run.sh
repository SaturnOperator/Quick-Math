#!/bin/bash
#!/usr/bin/env python
#docker run -it -v /home/alain/Desktop/Hackathon/Quick-Maths/images/:/tf_files -v /home/alain/Desktop/Hackathon/plus.jpg:/img/guess.jpg xblaster/tensor-guess sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg"

python3 imageManip.py

for file in Units/finalImage[0-9]*.jpg;do
    echo "I do something with the file $file"
	docker run -it -v /home/alain/Desktop/Hackathon/Quick-Maths/images/:/tf_files -v /home/alain/Desktop/Hackathon/Quick-Maths/$file:/img/guess.jpg xblaster/tensor-guess sh -c "/usr/bin/python /tf_files/label_image.py /img/guess.jpg"
	rm $file
done