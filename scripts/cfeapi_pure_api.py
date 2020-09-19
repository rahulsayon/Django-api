import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"

def get_list():
	r = requests.get(BASE_URL + ENDPOINT)
	print(r.status_code)
	status_code = r.status_code
	if status_code != 200:
		print('profility')
	data = r.json()
	for obj in data:
		if obj['id'] == 1:
			r2  = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
			print(r2.json())
		return data	

# def get_list():
# 	r = requests.get(BASE_URL + ENDPOINT)
# 	return r.json()

# print(get_list())


def create_update():
	new_data = {
	  'user'  : 1,
	  "content" : "Another new cool update"
	}
	r  = requests.delete(BASE_URL + ENDPOINT , data=new_data)
	# if r.status_code == requests.codes.ok:
	# 	print(r.json())
	# 	return r.json()  
	# return r.text
	print(r.headers)	
	print(r.status_code)
	if r.status_code == requests.codes.ok:
		#print(r.json())
		return r.json()
	return r.text


print(create_update())	