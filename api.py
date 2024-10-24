import requests
import time
from settings import config
from file import AudioFile

CREATE_URL = "https://mvsep.com/api/separation/create"
GET_URL = "https://mvsep.com/api/separation/get"

def createRequest(audio_file,sep_type,add_opt1=None,add_opt2=None):
    post_data = {
        "api_token": config.secert.token,
        "sep_type": sep_type,
        "output_format": config.common.output_format,
        "is_demo": config.common.is_demo
    }
    
    if add_opt1 is not None:
        post_data["add_opt1"] = add_opt1
    if add_opt2 is not None:
        post_data["add_opt2"] = add_opt2

    files = {'audiofile': (audio_file.path, audio_file.binary)}

    response = requests.post(CREATE_URL, files=files, data=post_data)
    
    response_json = response.json()

    if response_json["success"] == True:
        audio_file.hash = response_json["data"]["hash"]


    return response, response_json
        
def checkStatus(audio_file):
        result_url = GET_URL + "?hash=" + audio_file.hash
        while audio_file.status != "done":
            time.sleep(5)
            response = requests.get(result_url)
            print(response.text)
            response_json = response.json()
            audio_file.status = response_json["status"]
            print(f"Status: {audio_file.status}")
            
        return response, response_json

audio_file = AudioFile("./Fateful Encounter.mp3")
audio_file.hash = "20241024004516-ef4bdfa430-fateful-encounter.mp3"

try:
    #response_post, response_post_json = createRequest(audio_file,40,29)
    #print(f"Status Code: {response_post.status_code}")
    #print(f"Response: {response_post_json}")
    response_get, response_get_json = checkStatus(audio_file)
    print(f"Status Code: {response_get.status_code}")
    print(f"Response: {response_get_json}")
    
except Exception as e:
    print(f"An error occurred: {str(e)}")

