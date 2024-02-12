from datetime import datetime
import json
import os
from exportMetricsForCourseMilestone import write_milestone_data_to_csv
from generateTeamMetrics import getTeamMetricsForMilestone

from getTeamMembers import get_team_members


def main():
    gh_api_token = os.getenv("GH_API_TOKEN")
    organization = os.getenv("ORGANIZATION_NAME")
    team = os.getenv("TEAM_NAME")
    managers = json.loads(os.getenv("MANAGERS"))
    milestone_name = os.getenv("MILESTONE_NAME")
    milestone_grade = os.getenv("MILESTONE_GRADE")
    milestone_starts_on = os.getenv("MILESTONE_STARTS_ON")
    milestone_ends_on = os.getenv("MILESTONE_ENDS_ON")

    if not gh_api_token:
        print("GitHub API token is required.")
        exit(1)
    if not organization:
        print("GitHub API token is required.")
        exit(1)
    if not milestone_name:
        print("GitHub API token is required.")
        exit(1)
    if milestone_starts_on is None or milestone_ends_on is None:
        startDate = datetime.now()
        endDate = datetime.now()
        useDecay = False
    else:
        startDate = datetime.fromisoformat(milestone_starts_on)
        endDate = datetime.fromisoformat(milestone_ends_on)
        useDecay = True

    print("Organization: ", organization)

    team_metrics = {}
    members = get_team_members(organization, team)
    team_metrics[team] = getTeamMetricsForMilestone(
        org=organization,
        team=team,
        milestone=milestone_name,
        milestoneGrade=milestone_grade,
        members=members,
        managers=managers,
        startDate=startDate,
        endDate=endDate,
        useDecay=useDecay,
    )
    csv_file_path = f"{milestone_name}-{team}-{organization}.csv"
    write_milestone_data_to_csv(team_metrics[team], csv_file_path)


if __name__ == "__main__":
    main()
