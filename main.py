# Wrapping up for the night. Got the basic get call working
# Need to fix url checker, get it to take a full URL and filter out just the ID.
# Then need to clean the json response, fill variables. Probably use a dictionary for this.

import sys
import requests
import pprint

api_key = 'AIzaSyDEgOtAKuGUT   7IZpQKxDUTfyOsM_xp5bqk'


# Video ID for lofi video: 'jfKfPfyJRdk'

def main():
    url = getYoutubeURL()
    video_id = getVideoId(url)
    unparsed_result = makeAPICall(video_id)
    pprint.pprint(unparsed_result)


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


def printHeader() -> None:
    print("----------------------------------------------------------------------")
    print("-            Welcome to Python Youtube Statistics Fetcher            -")
    print("-                            Version 0.1                             -")
    print("-                    Created by Robert Hollinger                     -")
    print("----------------------------------------------------------------------")


def getVideoId(url) -> str:
    youtube, videoId = url.split('?v=')
    return videoId


def makeAPICall(video_id) -> str:
    # Response1 has 'title', 'publishedAt' (in format 2024-06-30T19:00:26Z)
    response1 = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}')
    # Response2 has a dict with key 'items[]'->'statistics{}'->'commentCount', 'favoriteCount', 'likeCount', 'viewCount'
    response2 = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}')
    pprint.pprint(response2.json())
    test = response2.json()
    print(test['items'][0]['statistics']['likeCount'])
    return response2.json()


if __name__ == "__main__":
    makeAPICall('v44K0aRNFz8&t=983s')
    # main()
    # makeAPICall('jfKfPfyJRdk')

# Black, mypy, pycheck?, pytest of course
# https://stackoverflow.com/questions/26199933/youtube-api-3-0-search-videos-and-get-video-statistics-at-single-request
