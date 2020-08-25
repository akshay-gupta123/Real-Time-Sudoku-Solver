# Real-Time-Sudoku-Solver


## Usage

After cloning this repository, create a virtual environment and install all the packages required to run Sudoku-Solver.

```console
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirement.txt
$ python3 model.py
$ python3 solver.py
```

# About

## sudoku.py

This file contain the famous sudoku solving algorithm [<strong>Solving Every Sudoku Puzzle</strong>](https://norvig.com/sudoku.html)<br>
This [<strong>Link</strong>](https://medium.com/activating-robotic-minds/peter-norvigs-sudoku-solver-25779bb349ce) helps me to understand the algorithm.

## model.py

This file contain the model I trained using Keras framework for Digit-Recogonition on MNIST Data.

<strong>Model Summary</strong>
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 24, 24, 30)        780       
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 12, 12, 30)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 10, 10, 15)        4065      
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 5, 5, 15)          0         
_________________________________________________________________
dropout (Dropout)            (None, 5, 5, 15)          0         
_________________________________________________________________
flatten (Flatten)            (None, 375)               0         
_________________________________________________________________
dense (Dense)                (None, 128)               48128     
_________________________________________________________________
dense_1 (Dense)              (None, 50)                6450      
_________________________________________________________________
dense_2 (Dense)              (None, 10)                510       
=================================================================
Total params: 59,933
Trainable params: 59,933
Non-trainable params: 0
_________________________________________________________________
None
```

## solver.py

This file contains opencv code doing extraction of Sudoku then imposing solved sudoku . 
