# Video-DL CLI

Um utilitário simples em Python para baixar vídeos e músicas do YouTube (e outros sites suportados pelo yt-dlp) via linha de comando.

## Instalação

Você pode instalar diretamente via `uv`:

```bash
uv tool install video-dl-cli --from git+https://github.com/SEU_USUARIO/video-dl-cli.git
```

## Uso

### Baixar vídeos (Padrão)

```bash
video-dl-cli "URL_DO_VIDEO"
```

### Baixar como MP3 (Música)

```bash
video-dl-cli "URL_DO_VIDEO" --audio
```

### Diretório de Saída (Pasta Downloads)

Todos os downloads são salvos dentro de uma pasta `downloads/` no diretório atual.

- **Padrão**: Se você não informar nada, ele salva em `downloads/musicas`.
- **Personalizado**: Se você informar um nome, ele salva em `downloads/SEU_NOME`.

Exemplo:
```bash
video-dl-cli "URL_DO_VIDEO" --audio --output "RockNacional"
# O arquivo será salvo em: downloads/RockNacional/
```

### Baixar de um arquivo de texto

Crie um arquivo `links.txt` com uma URL por linha:

```bash
video-dl-cli -f links.txt -o "Downloads"
```
