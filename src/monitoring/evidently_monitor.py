import pandas as pd

from evidently import Report
from evidently.presets import DataDriftPreset


def generate_report():

    reference_data = pd.read_csv(
        "artifacts/train.csv"
    )

    current_data = pd.read_csv(
        "artifacts/test.csv"
    )

    report = Report(
        metrics=[
            DataDriftPreset()
        ]
    )

    result = report.run(
        reference_data=reference_data,
        current_data=current_data
    )

    result.save_html(
        "evidently_report.html"
    )

    print("Evidently report generated successfully")


if __name__ == "__main__":
    generate_report()