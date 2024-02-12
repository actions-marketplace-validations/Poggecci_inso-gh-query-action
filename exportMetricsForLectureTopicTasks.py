import csv
import json
from generateLectureTopicTaskMetrics import getLectureTopicTaskMetrics
from getTeamMembers import get_team_members

from utils.models import LectureTopicTaskData


def write_lecture_topic_task_data_to_csv(
    ltt_data: LectureTopicTaskData, csv_file_path: str, task_quota: int
):
    with open(csv_file_path, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Developer", "Lecture Topic Tasks Completed", "Met Quota"])
        writer.writerow(["Total", ltt_data.totalLectureTopicTasks, "N/A"])
        for developer, tasks_closed in ltt_data.lectureTopicTasksByDeveloper.items():
            writer.writerow([developer, tasks_closed, tasks_closed >= task_quota])
