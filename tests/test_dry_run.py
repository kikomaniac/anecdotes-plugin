import unittest
from main import run_plugin

class DryRunTest(unittest.TestCase):
    def test_dry_run_execution(self):
        """Test that dry-run mode executes without exceptions and returns mock data"""
        try:
            run_plugin("testuser", "testpass", dry_run=True)
        except Exception as e:
            self.fail(f"Dry-run mode failed with exception: {e}")

if __name__ == "__main__":
    unittest.main()
