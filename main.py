import sys


def main():
    url = getYoutubeURL()
    unparsed_result = makeAPICall(url)


def getYoutubeURL() -> str:
    printHeader()
    url = input("Please enter a URL to a youtube video: ")
    if checkURLValidity(url):
        return url
    else:
        sys.exit("Invalid URL!!!")


def checkURLValidity(url) -> bool:
    if url.isnumeric:
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


def makeAPICall(url) -> str:
    ...


if __name__ == "__main__":
    main()

# Black, mypy, pycheck?, pytest of course
