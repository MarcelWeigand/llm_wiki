import os
import re
import sys
from datetime import date
from pathlib import Path

import requests
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

# Propagate proxy settings so all HTTP clients honour them
_http_proxy = os.getenv("HTTP_PROXY")
_https_proxy = os.getenv("HTTPS_PROXY")
if _http_proxy:
    os.environ["http_proxy"] = _http_proxy
if _https_proxy:
    os.environ["https_proxy"] = _https_proxy

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def extract_video_id(url: str) -> str | None:
    for pattern in (
        r"(?:v=)([0-9A-Za-z_-]{11})",
        r"youtu\.be/([0-9A-Za-z_-]{11})",
        r"embed/([0-9A-Za-z_-]{11})",
    ):
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    return None


def get_video_metadata(video_id: str) -> dict:
    proxies = {k: v for k, v in {"http": _http_proxy, "https": _https_proxy}.items() if v}
    resp = requests.get(
        "https://www.googleapis.com/youtube/v3/videos",
        params={"part": "snippet", "id": video_id, "key": YOUTUBE_API_KEY},
        proxies=proxies,
    ).json()
    if resp.get("items"):
        s = resp["items"][0]["snippet"]
        return {
            "title": s.get("title", "Unknown"),
            "channel": s.get("channelTitle", "Unknown"),
        }
    return {"title": "Unknown", "channel": "Unknown"}


def save_summary(summary: str, metadata: dict, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", metadata["title"])
    filename = f"{date.today()}_{safe_title}.txt"
    path = out_dir / filename
    path.write_text(summary, encoding="utf-8")
    return path


def summarize_with_gemini(url: str) -> str:
    client = genai.Client(api_key=GEMINI_API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part(file_data=types.FileData(file_uri=url)),
            types.Part(text="Provide a detailed summary covering all key points."),
        ],
    )
    return response.text


def main():
    url = sys.argv[1] if len(sys.argv) > 1 else input("YouTube URL: ").strip()

    video_id = extract_video_id(url)
    if not video_id:
        sys.exit("Error: Could not extract a video ID from the provided URL.")

    print(f"Video ID : {video_id}")

    print("Fetching metadata ...")
    metadata = get_video_metadata(video_id)
    print(f"Title    : {metadata['title']}")
    print(f"Channel  : {metadata['channel']}")

    print("Summarising with Gemini ...\n")
    summary = summarize_with_gemini(url)
    print(summary)

    out_dir = Path(__file__).parent.parent / "raw" / "youtube"
    saved_path = save_summary(summary, metadata, out_dir)
    print(f"\nSummary saved to: {saved_path}")


if __name__ == "__main__":
    main()
