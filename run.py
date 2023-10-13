import time

from app.web_checker import(
    check_url_status,
    REQUEST_TIMEOUT,
    REQUEST_INTERVAL
)

start_time = time.time()
while True:
    check_url_status()
    time.sleep(REQUEST_INTERVAL) # periodic method run
    if time.time() - start_time > REQUEST_TIMEOUT: # comment to prevent timeout
        break