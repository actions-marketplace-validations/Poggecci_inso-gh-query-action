import csv
from utils.models import MilestoneData


def write_milestone_data_to_csv(milestone_data: MilestoneData, csv_file_path: str):
    with open(csv_file_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(
            ["Developer", "Points Closed", "Percent Contribution", "Expected Grade"]
        )
        writer.writerow(["Total", milestone_data.totalPointsClosed, "/100%", "/100%"])
        for developer, metrics in milestone_data.devMetrics.items():
            writer.writerow(
                [
                    developer,
                    round(metrics.pointsClosed, 1),
                    round(metrics.percentContribution, 1),
                    round(metrics.expectedGrade, 1),
                ]
            )