import os
import re


def main():
    from wakepy import keep

    with keep.running():
        url = str(
            input("Enter url of the stream you want to download (live or archived), press enter to start download: \n")
        )

        print("\nThis window will close automatically when the download is complete\n")

        twitch = re.search("twitch.tv", url)

        command = str(
            'yt-dlp.exe -S "ext,res,proto" "'
            + url
            + '" --no-playlist --cookies-from-browser firefox:z7tc6j6k.default-nightly --wait-for-video 30 --downloader aria2c -N 10 -R 30 --live-from-start'
        )

        if twitch:
            command = f"npx twitch-dlp {url} --live-from-start"

        print(command + "\n")

        os.system(command)


if __name__ == "__main__":
    try:
        main()
    except ModuleNotFoundError:
        os.system("python -m pip install wakepy yt-dlp -U")
        main()
