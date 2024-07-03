# Wrapping up for the night. Got the basic get call working
# Need to fix url checker, get it to take a full URL and filter out just the ID.
# Then need to clean the json response, fill variables. Probably use a dictionary for this.

import sys
import requests

api_key = 'AIzaSyDEgOtAKuGUT7IZpQKxDUTfyOsM_xp5bqk'


def main():
    url = getYoutubeURL()
    video_id = getVideoId(url)
    # unparsed_result = makeAPICall(video_id)


def getYoutubeURL() -> str:
    printHeader()
    url = input("Please enter a URL to a youtube video: ")
    if checkURLValidity(url):
        return url
    else:
        sys.exit("Invalid URL!!!")


def checkURLValidity(url) -> bool:
    if url.isnumeric():
        return False
    elif url.strip() == "":
        return False
    else:
        return True


def printHeader():
    print("----------------------------------------------------------------------")
    print("-            Welcome to Python Youtube Statistics Fetcher            -")
    print("-                            Version 0.1                             -")
    print("-                    Created by Robert Hollinger                     -")
    print("----------------------------------------------------------------------")


def getVideoId(url):
    # Need to take in the url and strip everything except the video ID. Probably using regex yeehaw!


def makeAPICall(url) -> str:
    # response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={url}&key={api_key}')
    response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={url}&key={api_key}')
    print(response.json())


if __name__ == "__main__":
    main()
    # makeAPICall('jfKfPfyJRdk')


# Black, mypy, pycheck?, pytest of course
# https://stackoverflow.com/questions/26199933/youtube-api-3-0-search-videos-and-get-video-statistics-at-single-request
