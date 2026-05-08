import csv
import json
from config.settings import EXPORTS_DIR, EXPORT_CSV, EXPORT_JSON


class Exporter:
    def __init__(self, logger):
        self.logger = logger
        EXPORTS_DIR.mkdir(parents=True, exist_ok=True)

    def export_json(self, items: list[dict]):
        with open(EXPORT_JSON, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)
        self.logger.info("Exported JSON: %s", EXPORT_JSON)

    def export_csv(self, items: list[dict]):
        if not items:
            self.logger.warning("No items to export to CSV")
            return

        with open(EXPORT_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=items[0].keys())
            writer.writeheader()
            writer.writerows(items)

        self.logger.info("Exported CSV: %s", EXPORT_CSV)