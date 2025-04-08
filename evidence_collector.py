# evidence_collector.py
from utils import log_info


class EvidenceCollector:
    def __init__(self, client):
        self.client = client

    def collect_all(self):
        evidence = {}

        # E1 - Collect user info
        log_info("Collecting user info...")
        evidence["E1_user_info"] = self.collect_user_info()

        # E2 - Collect posts
        log_info("Collecting posts...")
        evidence["E2_posts"] = self.collect_posts()

        # E3 - Collect posts with comments
        log_info("Collecting posts with comments...")
        evidence["E3_posts_with_comments"] = self.collect_posts_with_comments()

        return evidence

    def collect_user_info(self):
        log_info("Fetching user info...")
        return self.client.get_user_info()

    def collect_posts(self):
        log_info("Fetching posts...")
        return self.client.get_posts()

    def collect_posts_with_comments(self):
        log_info("Fetching posts with comments...")
        return self.client.get_posts_with_comments()

