# khan_visualization

### Performance
The _Timing\_TSNEs_ file tests the performance of 3 different TSNE models. 

* Use the hidden state _txt_ file output from the _LSTM_ file from **khan_scripts** repo
* Uncomment bottom part of each section to save the TSNE output 

### Scrubber and Tooltips
The _Timestep\_Visualization_ file creates a visualization that allows for scrubbing between timesteps and hovering over specific points. 
* Use the dimension reduced _txt_ file output from the _Timing_\TSNEs_ file 
* Hovering currently displays Student and X,Y coordinates

### Images 
The _get\_image_ file creates a png files of a specific timestep.

* Use the dimension reduced _txt_ file output from the _Timing_\TSNEs_ file 
* Change the **tstep** variable to get a different timestep
* Change _output\_name_ to save file

*** Animation
The _animation_ file creates an animation using matplotlib.

* Use the dimension reduced _txt_ file output from the _Timing_\TSNEs_ file 
