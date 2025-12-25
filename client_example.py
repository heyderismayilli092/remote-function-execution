import requests

url = "http://127.0.0.1:3419/func/oslist/list"

# function to be triggered within the library
arguments = {
  "databasefile": "os-list.db"
}

# headers
headers = {
    "Content-Type": "application/json"

}
response = requests.post(url, json=arguments, headers=headers)  # get request post
#response = requests.post(url, headers=headers)  # get request post (not arguments)
print(response.json())
