import json
import requests
import os



#AUTH_ENDPOINT  = "http://127.0.0.1:8000/api/auth/jwt/"
AUTH_ENDPOINT  = "http://127.0.0.1:8000/api/auth/"
#REFRESH_ENDPOINT  = AUTH_ENDPOINT + "refresh/"
#print(REFRESH_ENDPOINT)


image_path = os.path.join(os.getcwd() , "d.jpg")

headers = {
	
 	'content-type' : 'application/json',


}

data = {
	  'username' : 'rahul',
	  'password' : '123',
}

print(AUTH_ENDPOINT)
r = requests.post(AUTH_ENDPOINT , data =json.dumps(data) , headers=headers)
token = r.json()['token']
print(token)

ENDPOINT = "http://127.0.0.1:8000/api/status/22/"
#ENDPOINT = "22/"

headers2 = {
 	"Authorization" : "JWT " + token,
}

data2 = {
	  'content' : 'this new content postt Rahul'
}

# with open(image_path, 'rb') as image:
# 	file_data = {
# 	    'image': image
# 	  }
file_data = {
	  'image' : image_path
}

#r = requests.put(ENDPOINT , data = data2 , headers=headers2 )
r = requests.get(ENDPOINT , data = data2 , headers=headers2 )
print(r.text)


#AUTH_ENDPOINT  = "http://127.0.0.1:8000/api/auth/jwt/"
# AUTH_ENDPOINT  = "http://127.0.0.1:8000/api/auth/apiregister/"
# REFRESH_ENDPOINT  = AUTH_ENDPOINT + "refresh/"
# #print(REFRESH_ENDPOINT)
# ENDPOINT = "http://127.0.0.1:8000/api/status/"


# image_path = os.path.join(os.getcwd() , "logo.jpg")

# headers = {
	
#  	'content-type' : 'application/json',
#   	'Authorization' : 'JWT ' + 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxOSwidXNlcm5hbWUiOiJyYWozMzMxIiwiZXhwIjoxNTUyODE4MDg2LCJlbWFpbCI6InJhakByci5jb20zMSIsIm9yaWdfaWF0IjoxNTUyODE3Nzg2fQ.VnYIH4B6JagYFWjoxIT6WToF_s0aBMOYX49YkA-eQNs',


# }

# data = {
# 	  'username' : 'raj3331',
# 	  'email' : 'raj@rr.com31',
# 	  'password' : 'raj',
# 	  'password2' : 'raj'
# }

# print(AUTH_ENDPOINT)
# r = requests.post(AUTH_ENDPOINT , data =json.dumps(data) , headers=headers)
# token = r.json()
# print(token)

# headers = {
# 	#"Content-Type" : "application/json",
# 	"Authorization" : "JWT " + token,
# }

# with open(image_path, 'rb') as image:
# 	file_data = {
# 	    'image': image
# 	  }
# data = {
# 	"content" : "new Content Type"
# }

# json_data = json.dumps(data)
# #post_data = json.dumps({"content" : "random content"})
# posted_response = requests.post(ENDPOINT, data=data , headers=headers)
# print(posted_response.text)


# refresh_data = {
#  	'token':token
#  }

# new_response = requests.post(REFRESH_ENDPOINT , data= json.dumps(refresh_data) , headers=headers)
# new_token = new_response.json()#['token']
# print(new_token)

# ENDPOINT = "http://127.0.0.1:8000/api/status/"

# image_path = os.path.join(os.getcwd() , "logo.jpg")

# get_endpoint = ENDPOINT + str(12)
# post_data  = json.dumps({"content" : "some random content"})

# r  =  requests.get(get_endpoint)
# print(r.text)

# r2  =  requests.get(get_endpoint)
# print(r2.status_code)

# post_headers = {
# 	'content-type' : 'application/json'
# }

# post_response = requests.post(ENDPOINT , data = post_data , headers=post_headers)
# print(post_response.text)


# def do_img(method='get' , data={} , is_json=True , img_path=None):
# 	headers = {}
# 	if is_json:
# 		headers['content-type']  = 'application/json'
# 		data = json.dumps(data)
# 	if img_path is not None:
# 		with open(img_path , 'rb') as image:
# 			file_data = { 'image' : image }
# 			r = requests.request(method , ENDPOINT , data = data , files=file_data , headers=headers)
# 	else:
# 		r = requests.request(method , ENDPOINT , data = data , headers=headers)
# 	print(r.text)
# 	print(r.status_code)
# 	return r

# do_img(method='put' , 
# 	data={'id':2,'user' : 1 , "content" : "ss" } ,
#     is_json=False ,
#      img_path=image_path)



# def do(method='get' , data={} , is_json=True):
# 	headers = {}
# 	if is_json:
# 		headers['content-type']  = 'application/json'
# 		data = json.dumps(data)
# 	r = requests.request(method , ENDPOINT , data = data , headers=headers)
# 	print(r.text)
# 	print(r.status_code)
# 	return r
	

