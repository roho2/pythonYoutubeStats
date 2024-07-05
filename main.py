import sys
import requests
import pprint

api_key = 'AIzaSyDEgOtAKuGUT   7IZpQKxDUTfyOsM_xp5bqk'


def main():
    url = getYoutubeURL()
    video_id = getVideoId(url)
    title_response, statistics_response = makeAPICall(video_id)
    info = getInfoFromResponses(title_response, statistics_response)
    printVideoInformation(info)


def getYoutubeURL() -> str:
    printHeader()
    url = input("Please enter a URL to a youtube video: ")
    if checkURLValidity(url):
        return url
    else:
        sys.exit("Invalid URL!!!")


def checkURLValidity(url: str) -> bool:
    if url.isnumeric():
        return False
    elif url.strip() == "":
        return False
    else:
        return True


def printHeader() -> None:
    print("----------------------------------------------------------------------")
    print("-            Welcome to Python Youtube Statistics Fetcher            -")
    print("-                            Version 1.0                             -")
    print("-                    Created by Robert Hollinger                     -")
    print("----------------------------------------------------------------------")


def getVideoId(url: str) -> str:
    youtube, videoId = url.split('?v=')
    return videoId


def getInfoFromResponses(title_response: dict, statistics_response: dict) -> dict:
    # We want to print Title, views, likes, dislikes (if possible), comment count, and favorite count.
    info = {'title': title_response['items'][0]['snippet']['title'],
            'views': statistics_response['items'][0]['statistics']['viewCount'],
            'likes': statistics_response['items'][0]['statistics']['likeCount'],
            'comments': statistics_response['items'][0]['statistics']['commentCount'],
            'favorites': statistics_response['items'][0]['statistics']['favoriteCount']}
    return info


def makeAPICall(video_id: str) -> tuple[dict, dict]:
    # 'title', 'publishedAt' (in format 2024-06-30T19:00:26Z)
    titleResponse = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}')
    # dict with key 'items[]'->'statistics{}'->'commentCount', 'favoriteCount', 'likeCount', 'viewCount'
    statisticsResponse = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={video_id}&key={api_key}')
    return titleResponse.json(), statisticsResponse.json()


def printVideoInformation(info):
    print("===========================================================================")
    print(f"Video Title: {info['title']}")
    print(f"Views: {info['views']}")
    print(f"Likes: {info['likes']}")
    print(f"Comments: {info['comments']}")
    print(f"Favorites: {info['favorites']}")


if __name__ == "__main__":
    main()

# Black, mypy, pycheck?, pytest of course
