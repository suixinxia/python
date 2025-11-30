from moviepy import editor
video = editor.VideoFileClip('一拳超人.mp4')
audio = editor.AudioFileClip('一拳超人.mp3')
v= video.set_audio(audio)
v.write_videofile('合成后.mp4')












