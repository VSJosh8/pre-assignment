import requests
import json
from datetime import datetime
from .config import(
    LOG_FILENAME,
    JSON_FILENAME,
    URL_LIST,
    CONTENT_REQUIRED,
)


def check_url_status():
    with open(LOG_FILENAME,'a') as f:
        with open(JSON_FILENAME, 'w') as j:
            json_dict = []
            for url in URL_LIST:
                try:
                    log_time = datetime.now()
                    response = requests.get(url)
                    response_time = response.elapsed.total_seconds()
                    status = response.status_code
                    content = response.text
                                                        
                    if status == 200:
                        # Verify if webpage content contains approved keywords
                        if any(keyword in content for keyword in CONTENT_REQUIRED):
                            content_met = True
                            f.write(f"[{log_time}] URL: {url} --> Accessible | Response time: {response_time}s | Required content met: {content_met}\n")
                        else:
                            content_met = False      
                            f.write(f"[{log_time}] URL: {url} --> Accessible | Response time: {response_time}s | Required met: {content_met}\n")
                            
                    else:
                        content_met = None
                        f.write(f"[{log_time}] URL: {url} --> Not Accessible | Status code {status}\n")
                except requests.exceptions.RequestException as e:
                    content_met = None
                    f.write(f"[{log_time}] URL: {url} --> Not Accessible | An error occurred when trying to access {url}. Error details: {e}\n")
                
                response_dict = {
                        'url': url,
                        'status': status,
                        'response_time': response_time,
                        'content_met': content_met                   
                    }
                
                json_dict.append(response_dict)
                
            json.dump(json_dict,j,indent=len(response_dict)) 
