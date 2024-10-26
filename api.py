import os
import requests
import time
from settings import config
from file import InputFile, SeparatedFile


CREATE_URL = "https://mvsep.com/api/separation/create"
GET_URL = "https://mvsep.com/api/separation/get"

def createRequest(audio_file,sep_type,add_opt1=None,add_opt2=None,add_opt3=None):
    audio_file = InputFile(audio_file)
    
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
    if add_opt3 is not None:
        post_data["add_opt3"] = add_opt3
        
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
    
    # Create output directory if it doesn't exist
    output_dir = "./output"
    os.makedirs(output_dir, exist_ok=True)
    
    if not result_files.files:
        print("No files found to download!")
        return
    
    for file_info in result_files.files:
        try:
            response = requests.get(file_info["url"], stream=True)
            
            response.raise_for_status()
            
            # Get file size for progress bar
            total_size = int(response.headers.get('content-length', 0))
            
            with open(file_info["path"], 'wb') as file:
                if total_size == 0:  # If size is unknown
                    file.write(response.content)
                else:
                    for data in response.iter_content(chunk_size=8192):
                        file.write(data)
            
            # Verify file was created
            if os.path.exists(file_info["path"]):
                file_size = os.path.getsize(file_info["path"])
            else:
                print(f"File {file_info['name']} was not created!")
            
        except requests.exceptions.RequestException as e:
            print(f"Network error downloading {file_info['name']}: {str(e)}")
            continue
        except IOError as e:
            print(f"File system error for {file_info['name']}: {str(e)}")
            continue
        except Exception as e:
            print(f"Unexpected error while processing {file_info['name']}: {str(e)}")
            continue




# response_post, response_post_json = createRequest(audio_file,44,3,1)

# response_get, response_get_json = checkStatus(audio_file)
    
# downloadFiles(audio_file, response_get_json)