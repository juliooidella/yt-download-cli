import yt_dlp

def baixar_audio(urls):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s', # Nome do arquivo será o título do vídeo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

if __name__ == "__main__":
    # Insira os links dos seus vídeos aqui
    links = [ 'https://www.youtube.com/watch?v=AiVlM7J_6zw'
    ]
    
    baixar_audio(links)
