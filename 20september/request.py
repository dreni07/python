import requests

the_url = 'http://127.0.0.1:8000/create_person'
context = {
    'name':'Dren',
    'age':17
}
response = requests.post(the_url,json=context)
the_full_response = response.json()

print(the_full_response)