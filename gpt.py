import requests

prompt = {
    "modelUri": "gpt://ajekjom0m5ghuv5e7uml/yandexgpt-lite",
        "complitionOptions":{
        "stream":False,
        "temperature": 0.6,
        "maxTokens":"2000"

    },
    "message":[
        {"role": "system",
         "text": "Ты ассистент, который помогает другим людям красиво написать историю жизни их предков"},
        {"role": "user",
        "text":"Привет, я бы хотел чтоб ты красиво написал историю моего предка по той информации, которую я тебе дам"},
        {"role": "assistant",
         "text": "Привет, как звали твоего предка, о котором ты хочешь рассказать?"},
        {"role": "user",
         "text": "Хорошо, его звали Иван Иванов Иванович"}
    ]
    }
url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN1J4sCxYR98rj-tVppyp6gXQthbdmYvmgtO7a"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)
