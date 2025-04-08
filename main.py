# main.py
import argparse
from client import DummyJsonClient
from evidence_collector import EvidenceCollector
from utils import log_error, log_info, pretty_print

# Default credentials from dummyjson docs (used responsibly)
USERNAME = "emilys"
PASSWORD = "emilyspass"

def run_plugin(username, password, dry_run=False):
    try:
        log_info("Starting plugin...")

        if dry_run:
            log_info("Dry-run mode activated. Simulating evidence collection.")
            evidence = {
                "E1_user_info": {"id": 1, "name": "Test User"},
                "E2_posts": [{"id": i, "title": f"Post #{i}"} for i in range(1, 6)],
                "E3_posts_with_comments": [{"id": i, "title": f"Post #{i}", "comments":
                    [{"id": 1, "body": "Test comment"}]} for i in range(1, 6)],
            }
        else:
            client = DummyJsonClient(username, password)
            log_info("Authenticating...")
            client.authenticate()
            log_info("Authenticated successfully.")

            collector = EvidenceCollector(client)
            evidence = collector.collect_all()

        log_info("Evidence collected:")
        for key, value in evidence.items():
            pretty_print(key, value)

    except Exception as e:
        log_error(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Anecdotes Plugin - DummyJSON Evidence Collector")
    parser.add_argument("--username", default=USERNAME, help="Username for DummyJSON login")
    parser.add_argument("--password", default=PASSWORD, help="Password for DummyJSON login")
    parser.add_argument("--dry-run", action="store_true", help="Run in dry-run mode without hitting the API")
    args = parser.parse_args()

    run_plugin(args.username, args.password, args.dry_run)
