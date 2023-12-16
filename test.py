import requests

url = 'http://localhost:8000/'
# Send a GET request to retrieve the CSRF token
response = requests.get(url)

# Set the CSRF token in the headers of the POST request
data = {'key': 'value'}
csrf_token = response.cookies.get('csrftoken')
headers = {
    'X-CSRFToken': csrf_token,
    'Cookie': f'csrftoken={csrf_token};'
}
response = requests.post(url, data=data, headers=headers)
