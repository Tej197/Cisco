# pip install requests 

import requests 
baseUrl = 'https://jsonplaceholder.typicode.com'

# read all posts : GET /posts 
print('Consuming : Read All Posts...')
response = requests.get(f'{baseUrl}/posts')
posts = response.json()
print(posts)

# read by id : GET /posts/1
print('Consuming : Read Post By Id == 1...')
response = requests.get(f'{baseUrl}/posts/1')
post = response.json()
print(post)

# create post : POST /posts {"userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : create post...')
post = {"userId":1, "title":"Some Title", "body" : "Some Body"}
response = requests.post(f'{baseUrl}/posts', data = post)
createdPost = response.json()
print(createdPost)

# update post : PUT /posts/1 {"id":1, "userId":1, "title":"Some Title", "body" : "Some Body"}
print('Consuming : update post id == 1...')
post = {"id":1, "userId":1, "title":"Different Title", "body" : "Some Body"}
response = requests.put(f'{baseUrl}/posts/1', data = post)
updatedPost = response.json()
print(updatedPost)

# delete post : DELETE /posts/1
print('Consuming : delete post id == 1...')
response = requests.delete(f'{baseUrl}/posts/1')
print('Deleted. Status : ', response.status_code)
