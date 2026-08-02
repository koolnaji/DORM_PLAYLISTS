#!/usr/bin/env python3
"""
YouTube Music to MP3 Downloader
- Saves into DormPlaylist_MP3s
- Skips files that already exist there
- If you delete an MP3, it will re-download it later
"""

import sys
import subprocess
from pathlib import Path

def download_mp3s(url, output_folder="DormPlaylist_MP3s"):
    outdir = Path(output_folder)
    outdir.mkdir(exist_ok=True)

    cmd = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--embed-thumbnail",
        "--add-metadata",
        "--no-overwrites",  # Skip if file exists, but no permanent archive
        "-o", str(outdir / "%(title)s.%(ext)s"),
        url
    ]

    print(f"Saving to: {outdir.resolve()}")
    print("Skips files that already exist in this folder.")
    print("If you delete an MP3, it can be re-downloaded later.")
    subprocess.run(cmd, check=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python download_mp3.py <youtube_or_playlist_url>")
        raise SystemExit(1)

    download_mp3s(sys.argv[1])