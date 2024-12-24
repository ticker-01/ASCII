import yt_dlp

# URL YouTube
video_url = 'https://youtu.be/B0DSoc-QEzg?si=cu3VQYl3KKb6Er3V' #Bad Aplle URL(https://youtu.be/FtutLA63Cp8?si=grnZspZSk8jbT0ur) :)

ydl_opts = {
    'format': 'bestvideo[ext=mp4]/bestvideo', 
    'outtmpl': 'video_without_audio.mp4',
    'noplaylist': True,                      
    'quiet': False,                            
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])