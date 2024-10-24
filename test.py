import requests

def send_separation_request(file_path, api_token):
    url = 'https://mvsep.com/api/separation/create'
    
    # Prepare the files and data
    files = {
        'audiofile': ('Fateful Encounter.mp3', open(file_path, 'rb'))
    }
    
    data = {
        'api_token': 'SEKrzrZQf4mA64lNYRkbewEYD1IvYC',
        'sep_type': '44',
        'add_opt1': '3',
        'add_opt2': '0',
        'output_format': '2',
        'is_demo': '0'
    }
    
    # Send the POST request
    response = requests.post(url, files=files, data=data)
    
    return response

# Example usage
file_path = 'Fateful Encounter.mp3'
api_token = 'SEKrzrZQf4mA64lNYRkbewEYD1IvYC'

try:
    response = send_separation_request(file_path, api_token)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"An error occurred: {str(e)}")