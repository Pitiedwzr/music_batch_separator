import re
import requests
import time
from settings import config
from file import InputFile, SeparatedFile


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
        response_json = response.json()
        audio_file.status = response_json["status"]
        print(f"Status: {audio_file.status}")    
        
    return response, response_json

def downloadFiles(audio_file, response_get_json):
    '''
    Download the files from the response
    '''
    result_files = SeparatedFile(response_get_json, audio_file)
        
    for file_info in result_files.files:
        response = requests.get(file_info["url"], stream=True)
        
        if response.status_code == 200:
            with open(file_info["path"], 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        print(f"File {file_info['name']} downloaded successfully!")
        
audio_file = InputFile("./miscs/Fateful Encounter.mp3")
audio_file.hash = "20241024004516-ef4bdfa430-fateful-encounter.mp3"

# try:
    #response_post, response_post_json = createRequest(audio_file,40,29)

response_get, response_get_json = checkStatus(audio_file)
    
downloadFiles(audio_file, response_get_json)


    
# except Exception as e:
    # print(f"An error occurred: {str(e)}")

