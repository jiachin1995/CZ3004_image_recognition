# CZ3004_image_recognition
image recognition for MDP. It uses Keras/Tensorflow

Preparing the Dataset:
  1. Using the arduino camera on the robot we took pictures of the maze.
  2. We took images of both symbols & non-symbols inside the maze.
  3. Next, we crop the images to only include locations where the image is expected to appear. Which is 3 locations. 
      Therefore, we have 3 cropped images for every image we have taken. In total we had about 60 croppped images
  4. To improve the image recognition, we distorted the quality of these 60 images even further. We added blur effects, slightly tilted the image, reduced colors to black and white, etc.
  5. Finally, we trained the model on this dataset.
  
1st round of training:
  1. First, we taught the model to different between symbols & non-symbols images. 
  2. It outputs a yes if a symbol is detected and a no if not detected.
   
2nd round of training:
  1. Next, if a symbol is detected, we taught the model to differentiate the symbol between 15 possible symbols.
  2. The model tells us which of the symbol that the image is likely to be.
  
Implementation:
  1. On startup, the robot loads the model into memory. This is to remove the need to load from hard drive when the robot is exploring the maze.
  2. The robot takes an image whenever it detects a block in the maze. 
  3. The image is sent to our trained model (that is already loaded in memory). The model identifies the symbols if it is present.
  4. Finally, the robot designates the block as having a symbol and this is reflected in the android screen.
