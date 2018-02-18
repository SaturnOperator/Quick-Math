# Tensorflow Image Classifier

This is the code for 'Image Classifier in TensorFlow which classifies the handwritten notes. At the moment , this classifier can classify numbers 0 to 9 , as well as recognize mathematical operators (ie multiplication or division signs ).  

## Requirements

* [docker](https://www.docker.com/products/docker-toolbox)

## Usage 
This web app can be used to streamline the process of recording class notes , writting equations ,  and making cheat sheets. It does by transferring the student writing into a printed values.  This also provides a fun way to determine quick values for simple math, through a "filter" which identifies the "=" sign and performs the mathmatical calculations for you.
## Train process
## Guess process

Just type for a single guess
```
 ./guess.sh [any_path]/my_own_classifier /yourfile.jpg
```

To guess an entire directory
```
./guessDir.sh [any_path]/classifier [any_path]/srcDir [any_path]/destDir
```

