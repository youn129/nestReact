import requests

url = "https://deepl-translator2.p.rapidapi.com/translate"

payload = {
	"source_lang": "EN",
	"target_lang": "KO",
	"text": "I like kimchi!"
}
headers = {
	"x-rapidapi-key": "bdce1ac462msh00eeb56d3e83a0bp1401bfjsnfa1cdb083651",
	"x-rapidapi-host": "deepl-translator2.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json()['data'])