import requests as rq

link = "http://127.0.0.1:5000/nomes"  
requisicao = rq.get(link)

print(requisicao)
print(requisicao.json()[0])  

