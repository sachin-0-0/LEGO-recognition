# **LEGO Piece Classifier**
## Purpose
write software that will look at the back page of a LEGO set's instructions and make a list of all the piece required for the set. the software will then be able to recognize the piece irl thought a camera and machine learning. when presented with a piece the software will determine whether that piece is needed for the LEGO set being built.
## Limitations
the software will not be able to differentialte between the same piece with different desings printed on it ie. all minifigure torsos will only be recognized as one piece.
## Progress

first, i found a databank with 3d files of every single LEGO piece out there. downside is that they were .dat files. 

i copied then converted all the .dat files to stl. files to eventually use to make images to train an object recognition algorithm. i then filtered out the .stl files and mooved them to a new folder. i also filtered out all duplacate pieces with different prining. then i converted a single .stl file into an 3D plot using matplotlib


