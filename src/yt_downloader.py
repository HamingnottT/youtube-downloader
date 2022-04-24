from pytube import YouTube

class VideoExtractor:
    def get_vid_info():
        print(f"""\nTitle: {yt.title}
    Author: {yt.author}
    Number of views: {yt.views}
    Length of video: {yt.length} seconds
    Description: {yt.description}
    Ratings: {yt.rating}""")

    # Dash Stream - downloads the highest quality video and audio
    def download_dash():
        print(yt.streams)
        # print("-"*48)
        # print("audio only: ")
        # print(yt.streams.filter(only_audio=True))
        print("-"*48)
        print("video only: ")
        print(yt.streams.filter(resolution="1080p"))
        yd = yt.streams.get_by_itag(itag="137")
        yr = yt.streams.get_by_resolution(resolution="1080p")
        ya = yt.streams.get_audio_only()

        print("\nDownloading video. . .\n")
        
        yr.download(output_path=f"{default_path}", filename=f"~video-only-{yt.title}.mp4")
        ya.download(output_path=f"{default_path}",filename=f"~audio-only-{yt.title}.m4a")

        print(f"Downloaded video to {default_path}\n")
        print("Returning to main menu. . .")


    # Progressive - downloads progressive stream - already has audio and video binded
    def download_progressive():
        
        # print(yt.streams.filter(progressive=True))

        print("\nDownloading video. . .\n")

        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=f"{default_path}")

        print(f"Downloaded video to {default_path}\n")
        print("Returning to main menu. . .")


    def main():
        global yt
        global default_path
        link = input("Enter the link of YouTube video you want to download: ")
        yt = YouTube(link)
        default_path = "./downloads"