# sky-image-downloader
Goal is to download images from different telescopes, given the position (ra, dec) of the desired stellar object.
#How to use it
This repository uses Python . Needed Python libs will be added soon.

To use this, go to data/Coord.csv
Input the list of coordinates. Format is ra,dec in degrees.
Save the file.

Run 'main.py' to start the magic.

Your images will be downloaded in folders:
* images\pan-starrs1
* images\poss1_red

The combined image of both catalogues will be stored in
* images\combined

The naming convention of the files is ra_dec.jpg