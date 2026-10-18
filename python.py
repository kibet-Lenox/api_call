import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
#print(response.json())

if response.status_code == 200:
    data = response.json()
    for user in data:
        if user['id'] in [1, 2]:
            name = user['name']
            username = user['username']
            email = user['email']
            phone = user['phone']
            city = user['address']['city']
            website = user['website']
            
            print (f"User's name: {name}.")
            print(f"     Username: {username}.")
            print(f"     Email: {email}")
            print(f"     City: {city}.")
            print(f"     Website: {website}")
            print()
         
            continue
            
      
        
else:
    print("Request failed.", response.status_code)         
