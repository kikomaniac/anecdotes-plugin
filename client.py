# client.py
import requests

from utils import log_info, log_error


class DummyJsonClient:
    def __init__(self, username, password):
        self.base_url = "https://dummyjson.com"
        self.token = None
        self.username = username
        self.password = password

    def authenticate(self):
        url = f"{self.base_url}/auth/login"
        payload = {
            "username": self.username,
            "password": self.password
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            data = response.json()
            self.token = data.get("accessToken")  # ← FIXED HERE
            if not self.token:
                print("[DEBUG] Full response:", data)
                raise Exception("Access token not found in response")
            log_info("Authenticated successfully.")
        else:
            raise Exception(f"Authentication failed: {response.status_code} {response.text}")

    def _get_headers(self):
        if not self.token:
            raise Exception("Client is not authenticated")
        return {
            "Authorization": f"Bearer {self.token}"
        }

    def get_user_info(self):
        url = f"{self.base_url}/auth/me"
        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_posts(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            posts = response.json().get("posts", [])
            log_info(f"Received {len(posts)} posts.")
            return posts
        else:
            log_error(f"Failed to get posts: {response.status_code} {response.text}")
            raise Exception(f"Failed to get posts: {response.status_code} {response.text}")

    def get_posts_with_comments(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            posts = response.json().get("posts", [])
            log_info(f"Received {len(posts)} posts.")

            for post in posts:
                log_info(f"Fetching comments for post {post['id']}...")
                post["comments"] = self.get_comments(post["id"])

            log_info(f"Collected {len(posts)} posts with comments.")
            return posts

    def get_comments(self, post_id):
        url = f"{self.base_url}/posts/{post_id}/comments"
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("comments", [])
