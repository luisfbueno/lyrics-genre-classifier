import requests

#lyrics = {"Lyrics": "Vai tua vida\nTeu caminho é de paz e amor\nA tua vida\nÉ uma linda canção de amor\nAbre os teus braços e canta\nA última esperança\nA esperança divina\nDe amar em paz"}

response = requests.post("{}/predict".format("http://127.0.0.1:5000"), json = lyrics)

response.json()

print(response.json())
