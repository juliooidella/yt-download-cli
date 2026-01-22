import argparse
import os
import yt_dlp
from pathlib import Path

def processar_videos(links, output_dir, audio_only=False):
    """
    Realiza o download dos vídeos usando yt-dlp.
    """
    # Garante que o diretório de saída existe (sempre dentro de downloads/)
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    out_path = os.path.join(output_dir, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
        'outtmpl': out_path, # Salva com o título do vídeo no diretório especificado
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in links:
            try:
                print(f"\nIniciando download: {link}")
                ydl.download([link])
            except Exception as e:
                print(f"Erro ao processar {link}: {e}")

def carregar_do_arquivo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    with open(caminho_arquivo, 'r') as f:
        # Remove espaços, linhas vazias e comentários simples
        return [linha.strip() for linha in f if linha.strip() and not linha.startswith('#')]

def main():
    parser = argparse.ArgumentParser(description="Downloader de vídeos e músicas via CLI")
    
    # Argumentos posicionais (links diretos)
    parser.add_argument('links', nargs='*', help='URLs dos vídeos separadas por espaço')
    
    # Argumento opcional para arquivo
    parser.add_argument('-f', '--file', help='Caminho para arquivo .txt com lista de links')
    
    # Argumento opcional para diretório de saída
    parser.add_argument('-o', '--output', help='Diretório onde os arquivos serão salvos')

    # Flag para apenas áudio
    parser.add_argument('-a', '--audio', action='store_true', help='Baixar apenas o áudio em formato MP3')

    args = parser.parse_args()
    lista_final = []

    if args.links:
        lista_final.extend(args.links)

    if args.file:
        lista_final.extend(carregar_do_arquivo(args.file))

    if not lista_final:
        print("Erro: Nenhum link ou arquivo fornecido. Use: video-dl-cli <url> ou -f <arquivo.txt>")
        return

    # Define o diretório de saída base
    base_download_dir = "downloads"
    if args.output:
        final_output = os.path.join(base_download_dir, args.output)
    else:
        final_output = os.path.join(base_download_dir, "musicas")

    # Remove duplicatas
    lista_final = list(dict.fromkeys(lista_final))
    
    print(f"Total de links únicos encontrados: {len(lista_final)}")
    print(f"Arquivos serão salvos em: {final_output}")
    processar_videos(lista_final, output_dir=final_output, audio_only=args.audio)

if __name__ == "__main__":
    main()
