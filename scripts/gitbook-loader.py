import requests
from pprint import pprint
from time import sleep, time
import os

class GitBookAPI:
    def __init__(self, collection_id, bearer_token):
        self.collection_id = collection_id
        self.bearer_token = bearer_token
        self.base_url = 'https://api.gitbook.com/v1'
        self.headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json',
        }
        self.rate_limit = None
        self.rate_remaining = None
        self.rate_reset = None

    def pre_check_rate_limit(self):
        # Check if we have rate limit info and if we're close to hitting the limit
        if self.rate_remaining is not None and self.rate_remaining < 10:
            # Calculate how long to wait based on current time and rate reset time
            now = time()
            if self.rate_reset and self.rate_reset > now:
                wait_seconds = self.rate_reset - now
                print(f"Rate limit close to being reached. Waiting for {wait_seconds} seconds.")
                sleep(wait_seconds)
            else:
                print("Rate limit information outdated or reset time has passed. Proceeding with request.")


    def get_collection(self):
            url = f'{self.base_url}/collections/{self.collection_id}'
            response = self._make_request(url)
            if response:
                print("Collection:\n\n")
                pprint(response)

    def get_spaces(self):
        url = f'{self.base_url}/collections/{self.collection_id}/spaces'
        response = self._make_request(url)
        if response:
            print("Spaces:\n\n")
            pprint(response)
            return response['items'][0]['id']  # Returning the first space ID for further use

    def get_primary_content(self, space_id):
        url = f'{self.base_url}/spaces/{space_id}/content'
        response = self._make_request(url)
        if response:
            print("Primary Content:\n\n")
            pprint(response)

    def get_primary_content_files(self, space_id):
        url = f'{self.base_url}/spaces/{space_id}/content/files'
        response = self._make_request(url)
        if response:
            print("Primary Content Files:\n\n")
            pprint(response)

    def get_page(self, space_id, page_id):
        url = f'{self.base_url}/spaces/{space_id}/content/page/{page_id}'
        response = self._make_request(url)
        if response:
            print("Page:\n\n")
            pprint(response)

    def update_rate_limit_info(self, headers):
        self.rate_limit = headers.get('X-RateLimit-Limit')
        self.rate_remaining = int(headers.get('X-RateLimit-Remaining', 0))
        rate_reset = headers.get('X-RateLimit-Reset')
        if rate_reset:
            self.rate_reset = time() + int(rate_reset)

    def _make_request(self, url):
        self.pre_check_rate_limit()  # Check rate limit before making the request
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            self.update_rate_limit_info(response.headers)  # Update rate limit info from the response
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
        
    def _handle_rate_limiting(self, response):
        rate_limit = response.headers.get('X-RateLimit-Limit')
        rate_remaining = response.headers.get('X-RateLimit-Remaining')
        rate_reset = response.headers.get('X-RateLimit-Reset')

        if rate_remaining and int(rate_remaining) < 10:
            print(f"Rate limit reached. Limit: {rate_limit}, Remaining: {rate_remaining}, Reset: {rate_reset}")
            sleep_time = int(rate_reset) if rate_reset else 60  # Default to 60 seconds if reset time is not provided
            print(f"Sleeping for {sleep_time} seconds.")
            sleep(sleep_time)

def main():
    collection_id = '-MZW0ab4W4hbS01XfFjm'
    bearer_token = os.environ.get('GITBOOK_BEARER_TOKEN') # SETX GITBOOK_BEARER_TOKEN "<your token>" \M

    gitbook_api = GitBookAPI(collection_id, bearer_token)
    gitbook_api.get_collection()
    space_id = gitbook_api.get_spaces()
    if space_id:
        gitbook_api.get_primary_content(space_id)

if __name__ == "__main__":
    main()