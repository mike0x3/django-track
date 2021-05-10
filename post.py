import easypost 
import json

easypost.api_key = "EZTK9926332bdce64f5497b58fe743fcf653dIhj5YuJMXD3chpOP735qQ"

tracker = easypost.Tracker.create(
    tracking_code="EZ1000000001"
)
peso = tracker['weight']
stato = tracker['status']
dettagli = tracker['tracking_details']
data_consegna = tracker['est_delivery_date']

lista = list()
for el in dettagli:
	el = str(el)
	#el = json.loads(el)
	lista.append(el)

for j in range(len(lista)):
    lista[j]=lista[j]+str(j)
print(lista[1])

#print(
#	f'peso: {peso}\n',
#	f'stato: {stato}\n',
#	f'dettagli: {lista}\n',
#	f'data_consegna: {data_consegna}'
#	)

