import requests
proxies = {
"https": 191.252.196.160:8080",
"http": 191.252.196.160:8080",
}
url = "https://httpbin.org/ip"
r = requests.get(url, proxies=proxies)
r.json()
{'origin': '191.252.196.160'}
r.json()
{'origin': '47.31.123.243}
