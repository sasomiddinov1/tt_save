import requests

url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/index"
headers = {
    'x-rapidapi-host': "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
    'x-rapidapi-key': "a7b318cdb8msh1e5c642782a499fp1d9d27jsne2052ff95aae"
}


async def remove_background(tt_url):
    querystring = f"url={tt_url}"
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()['video'][0]