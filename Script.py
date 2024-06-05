import requests
from bs4 import BeautifulSoup
import time

def scrape_youtube_live_stream(url):
    try:
        # Send a GET request to the YouTube URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the element containing the live stream URL
        live_stream_url = soup.find('link', {'itemprop': 'url'}).get('href')
        
        return live_stream_url
    except Exception as e:
        print(f"Error: {e}")
        return None

def generate_m3u8_file(live_stream_url):
    if live_stream_url:
        # Generate the m3u8 playlist content
        m3u8_content = f"#EXTM3U\n#EXTINF:-1,{live_stream_url}"
        
        # Write the content to a file
        with open('live_stream.m3u8', 'w') as file:
            file.write(m3u8_content)

def main():
    https://www.youtube.com/live/qbI3WTofg1A?si=i4fesejVEnO-Jsbb = "https://www.youtube.com/channel/UCDgeNq9nfWI-ltAPhXm8bGw"  # Example YouTube channel URL
    while True:
        live_stream_url = scrape_youtube_live_stream(youtube_url)
        generate_m3u8_file(live_stream_url)
        print("m3u8 file updated.")
        time.sleep(216,000)  # Scrape the YouTube page every 60 seconds

if __name__ == "__main__":
    main()