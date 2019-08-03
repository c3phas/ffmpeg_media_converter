import subprocess
import os
import sys
#we are going to create a wrappper for ffmpeg
#we are using subprocess module to execute the system commands
def spawn_child(cmds=[]):
	subprocess.run(cmds)

def convert_video(video_input,output_format,video_output):
	#pass
	cmds = [ 'ffmpeg','-i',video_input,'-q:a','0','-q:v','0', '-f',output_format, video_output,'-hide_banner']
	#ffmpeg -i $video -q:a 0 -q:v 0 -f webm "$videoName".webm
	spawn_child(cmds)

def extract_video_stream(video_input,video_output):

	cmds = ['ffmpeg','-i',video_input,'-an','-vc', 'copy',video_output,'-hide_banner']
	spawn_child(cmds)
	#print ("Thankyou for using this program")
def extract_audio_stream(video_input,audio_output):
	cmds = ['ffmpeg','-i',video_input ,'-vn' ,audio_output,'-hide_banner']
	spawn_child(cmds)

def cut_video(video_input,start_cut,end_cut,video_output):
	cmds = ['ffmpeg','-i',video_input,'-ss',start_cut,'-to',end_cut,'-c', 'copy',video_output, '-hide_banner']
	spawn_child(cmds)

def add_watermark(video_input,image_overlay,video_output):
	cmds = [ 'ffmpeg','-i',video_input,'-i',image_overlay,'-filter_complex','overlay=10:10',video_output]
	spawn_child(cmds)
def combine_video_mp3(video_input,audio_input,video_output):
	cmds = [ 'ffmpeg','-i',video_input,'-i',audio_input,'-q:a','0','-q:v','0','-shortest',video_output,'-hide_banner' ]
	spawn_child(cmds)


#now lets write the rest of the program

print("------------------------------------\n")
print("--Thankyou for trying this program--\n")
print("-------------------------------------\n")
print ("-"*30)
print("--This might take some time--  ")
print("-"*30)
if ( len(sys.argv) < 2):
	print("usage: script <option> ")
	exit()

if ( sys.argv[1] == "-w"):
	print("we are going to add a watermark on the video")
	video_input = input("Enter the name/path of the video:")
	image_overlay = input("Enter the image to use:")
	video_output  = input("How would you like to save the file:")

	add_watermark(video_input,image_overlay,video_output)
elif (sys.argv[1] == " -c"):
	#print ( "we are going to cut the video")	
	video_input = input("Enter the name/path of the video:")
	start_cut = input("Where the cut should start in seconds:")
	end_cut = input("How long the video should be in seconds:")

	video_output  = input("How would you like to save the file:")
	cut_video(video_input,start_cut,end_cut,video_output)

elif (sys.argv[1] == "-b"):
	video_input = input("Enter the name of the video:")
	output_format= input("Enter the format you want:")
	video_output = input("How would you like to save the file:")
	video_output = video_output + "." +output_format
	convert_video(video_input,output_format,video_output)	
elif (sys.argv[1] == "-m"):
	video_input = input ("Enter the name/path of the video file:")
	audio = video_input.split(".")


	audio_output = audio[0] + ".mp3"

	extract_audio_stream(video_input,audio_output)	


elif (sys.argv[1] == "--merge"):
	print("--This will merge a video file and audio file--")
	video_input = input("Enter the name of the video file: ")
	#we will use mp4 as the output
	audio_input = input("Enter the name of the audio file: ")
	video_output = input ("How would you like to save it: ")
	vidFormat = ".mp4"
	video_output = video_output+vidFormat
	combine_video_mp3(video_input,audio_input,video_output)

elif (sys.argv[1] == "-v"):
	print("--This will mute the video and save the muted copy--")
	video_input = input("Enter the name of the video: ")
	video_out = video_input.split(".")
	vidFormat = video_out[1]
	video_output = input ("How would you like to save the file : ")
	video_output = video_output + "."+vidFormat
	extract_video_stream(video_input,video_output)
elif (sys.argv[1] == "--help"):
	pass
else:
	print( "check the usage then try again")
	#sys.exit()
