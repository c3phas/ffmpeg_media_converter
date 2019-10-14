
<h3>wrapper for the ffmpeg library</h3>
<b><h4>Description:</h4>This program is basically used to convert your media files
from one format to another.</b>
<b>It wraps the functionality of the ffmpeg library which is used 
for converting media files to different formats</b>


<pre>usage:
	The program uses python3 and was tested on kali linux but 
	should pretty much work on any system supporting python3 and 
	has ffmpeg installed
	to install ffmpeg on debian systems : apt install ffmpeg
	Note that most debian systems run python2 by default so be
	carefull and make sure you run the programm using  python3


	To run the program on the terminal do the fillowing
	python3 convert_me.py -option

	NOTE: the option must be specified to instruct the program what to do

	options:
		-b -basic video format conversion(mp4 to webm,webm to mp4 etc)
		-c -cut video at specific time(eg to remove intro)
		-m - convert your video files to mp3
		-v -mute the video file provided
		--merge - merge an audio and video file together(The output will be an mp4 file)
		-h -help
</pre>
