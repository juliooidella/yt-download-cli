# 🎥 Video-DL CLI: Seu Downloader de Mídia Ultra-Rápido

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Install with uv](https://img.shields.io/badge/install%20with-uv-purple)](https://github.com/astral-sh/uv)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **Cansado de comandos complexos para baixar apenas um vídeo ou uma playlist inteira de músicas?**

O **Video-DL CLI** é uma ferramenta poderosa e simplificada, construída sobre o `yt-dlp`, que permite baixar vídeos e áudios com organização automática e alta performance.

---

## 🧐 O Problema que Resolvemos

Baixar vídeos do YouTube ou de outras plataformas geralmente exige comandos longos, ou você acaba com arquivos espalhados em pastas bagunçadas. Se você quer baixar uma playlist de 50 músicas, esperar uma por uma é uma perda de tempo.

❌ **Processo manual, sequencial e desorganizado.**

---

## ✨ A Solução: `video-dl-cli`

O **Video-DL CLI** automatiza o trabalho sujo. Ele organiza seus downloads em uma estrutura limpa e permite que você use o poder do seu processador para baixar múltiplos arquivos simultaneamente.

✅ **Organização automática em subpastas.**
✅ **Downloads paralelos (Multi-threading).**
✅ **Conversão direta para MP3 de alta qualidade.**
✅ **Interface CLI amigável e intuitiva.**

---

## 🚀 Guia Rápido: Instalação e Uso

### Passo 1: Instale a Ferramenta

Recomendamos usar o `uv` (o instalador de Python mais rápido do mercado).

```bash
# Instale o video-dl-cli globalmente
uv tool install video-dl-cli --from git+https://github.com/juliooidella/yt-download-cli.git
```

### Passo 2: Baixe sua primeira Mídia

O uso é extremamente direto.

```bash
# Baixar um vídeo na pasta padrão (downloads/musicas)
video-dl-cli "https://www.youtube.com/watch?v=..."

# Baixar como MP3 em uma pasta específica
video-dl-cli "URL" --audio --output "MinhasFavoritas"

# Baixar uma PLAYLIST INTEIRA em paralelo (5 vídeos por vez)
video-dl-cli "URL_DA_PLAYLIST" --parallel 5
```

---

## ⚙️ Estrutura de Pastas

O CLI mantém seu computador organizado sem que você precise mover um dedo:

```text
seu-diretorio/
└── downloads/
    ├── musicas/          <-- (Pasta padrão)
    ├── RockNacional/     <-- (Pasta via --output RockNacional)
    └── ...
```

---

## 🖥️ Recursos Principais

| Recurso | Descrição | Comando |
| :--- | :--- | :--- |
| **🎵 Modo Áudio** | Extrai automaticamente o áudio e converte para MP3 192kbps. | `-a` ou `--audio` |
| **⚡ Paralelismo** | Baixa múltiplos vídeos de uma playlist simultaneamente. | `-p` ou `--parallel` |
| **📂 Organização** | Cria pastas automaticamente dentro do diretório `downloads/`. | `-o` ou `--output` |
| **📄 Lote (Batch)** | Lê uma lista de links de um arquivo `.txt`. | `-f` ou `--file` |
| **🛡️ Robustez** | Ignora vídeos deletados ou privados em playlists sem travar. | *(Automático)* |

---

## 📝 Nota Importante

**Este projeto tem fins educacionais. O usuário é responsável por respeitar os termos de serviço das plataformas acessadas.**

---

[Reportar Bug](https://github.com/juliooidella/yt-download-cli/issues) • [Contribuir](https://github.com/juliooidella/yt-download-cli/pulls)
