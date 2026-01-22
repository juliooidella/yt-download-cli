import argparse
import os
import yt_dlp
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def baixar_link_unico(link, ydl_opts):
    """
    Função auxiliar para baixar um único link.
    """
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        print(f"Erro ao processar {link}: {e}")

def extrair_links_individuais(links, ydl_opts):
    """
    Extrai links individuais de listas/playlists para processamento paralelo.
    """
    links_individuais = []
    # Opções simplificadas apenas para extração
    opts_extrair = {
        'extract_flat': True,
        'quiet': True,
        'ignoreerrors': True,
    }
    
    print("Analisando links e playlists...")
    with yt_dlp.YoutubeDL(opts_extrair) as ydl:
        for link in links:
            try:
                info = ydl.extract_info(link, download=False)
                if info and 'entries' in info:
                    # É uma playlist
                    for entry in info['entries']:
                        if entry:
                            # Tenta pegar a URL do vídeo
                            url = entry.get('url') or entry.get('webpage_url')
                            if url:
                                links_individuais.append(url)
                else:
                    # É um vídeo único
                    links_individuais.append(link)
            except Exception as e:
                print(f"Erro ao extrair info de {link}: {e}")
                links_individuais.append(link)
    
    return list(dict.fromkeys(links_individuais))

def processar_videos(links, output_dir, audio_only=False, parallel=1):
    """
    Realiza o download dos vídeos usando yt-dlp, com suporte a paralelismo.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    out_path = os.path.join(output_dir, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best' if audio_only else 'bestvideo+bestaudio/best',
        'outtmpl': out_path,
        'ignoreerrors': True,
    }

    if audio_only:
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    if parallel > 1:
        # Quando em paralelo, o progresso padrão do yt-dlp bagunça o terminal
        ydl_opts['quiet'] = True
        ydl_opts['no_warnings'] = True
        
        links_para_baixar = extrair_links_individuais(links, ydl_opts)
        total = len(links_para_baixar)
        print(f"Iniciando download paralelo de {total} itens com {parallel} workers...")
        
        with ThreadPoolExecutor(max_workers=parallel) as executor:
            # Submete todos os links para a pool
            executor.map(lambda l: baixar_link_unico(l, ydl_opts), links_para_baixar)
    else:
        # Modo sequencial padrão
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for link in links:
                print(f"\nIniciando download: {link}")
                ydl.download([link])

def carregar_do_arquivo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    with open(caminho_arquivo, 'r') as f:
        return [linha.strip() for linha in f if linha.strip() and not linha.startswith('#')]

def main():
    parser = argparse.ArgumentParser(description="Downloader de vídeos e músicas via CLI")
    parser.add_argument('links', nargs='*', help='URLs dos vídeos separadas por espaço')
    parser.add_argument('-f', '--file', help='Caminho para arquivo .txt com lista de links')
    parser.add_argument('-o', '--output', help='Diretório onde os arquivos serão salvos')
    parser.add_argument('-a', '--audio', action='store_true', help='Baixar apenas o áudio em formato MP3')
    parser.add_argument('-p', '--parallel', type=int, default=1, help='Número de downloads simultâneos (padrão: 1)')

    args = parser.parse_args()
    lista_final = []

    if args.links:
        lista_final.extend(args.links)

    if args.file:
        lista_final.extend(carregar_do_arquivo(args.file))

    if not lista_final:
        print("Erro: Nenhum link ou arquivo fornecido. Use: video-dl-cli <url> ou -f <arquivo.txt>")
        return

    base_download_dir = "downloads"
    if args.output:
        final_output = os.path.join(base_download_dir, args.output)
    else:
        final_output = os.path.join(base_download_dir, "musicas")

    lista_final = list(dict.fromkeys(lista_final))
    
    print(f"Total de links únicos encontrados: {len(lista_final)}")
    print(f"Arquivos serão salvos em: {final_output}")
    
    processar_videos(lista_final, output_dir=final_output, audio_only=args.audio, parallel=args.parallel)

if __name__ == "__main__":
    main()
