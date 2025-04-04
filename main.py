import time
import os
from fairness_checker.config import Config
from fairness_checker.storage import S3Storage
from fairness_checker.database import Database
from fairness_checker.analyzer import FairnessAnalyzer

class FairnessCheckerApp:
    def __init__(self):
        self.config = Config()
        self.storage = S3Storage(self.config)
        self.db = Database(self.config)
        self.analyzer = FairnessAnalyzer(protected_attrs=['gender', 'age', 'race'])

    def run(self):
        print("[INFO] Starting fairness check run")
        files = self.storage.list_csv_files()

        for key in files:
            print(f"[INFO] Processing file: {key}")
            parts = os.path.basename(key).replace('.csv', '').split('_')
            customer = parts[0]

            try:
                raw_df = self.storage.read_csv(key)
                ref_df = self.db.load_customer_data(customer)
                report = self.analyzer.analyze(raw_df, ref_df)
                self.storage.write_report(report, key)
            except Exception as e:
                print(f"[ERROR] Failed to process {key}: {e}")

    def loop(self):
        while True:
            self.run()
            print(f"[INFO] Sleeping for {self.config.CHECK_INTERVAL_SECONDS} seconds")
            time.sleep(self.config.CHECK_INTERVAL_SECONDS)

if __name__ == '__main__':
    app = FairnessCheckerApp()
    app.loop()

