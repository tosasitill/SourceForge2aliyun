import requests

url = 'https://sourceforge.net/projects/<PROJECT_NAME>/files/latest/download'
response = requests.head(url, allow_redirects=True)
download_url = response.headers['location']
