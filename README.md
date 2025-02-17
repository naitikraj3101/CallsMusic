# SU Music Player || VCG MUSIC BOT

## Note

Repository ini milik [SU Music Player](https://github.com/suprojects) dan klik disini untuk [Original Repository.](https://github.com/suprojects/CallsMusic)

## Disclaimer

Saya disini hanya membantu menerjemahkan bot ini ke dalam bahasa Indoenesia.

## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Klik disini untuk deploy di Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/naitikraj3101/CallsMusicHeroku/)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/naitikraj3101/callsmusic-1Heroku/)


## Credits

- [Roj](https://github.com/rojserbest): main developer
- [Marvin](https://github.com/BlackStoneReborn): bug reporter
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls
