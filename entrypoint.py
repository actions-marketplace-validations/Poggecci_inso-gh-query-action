from datetime import datetime
import json
import os
from exportMetricsForCourseMilestone import write_milestone_data_to_csv
from generateTeamMetrics import getTeamMetricsForMilestone

from getTeamMembers import get_team_members


def main():
    config_file = os.getenv("CONFIG_FILE")
    gh_api_token = os.getenv("GH_API_TOKEN")

    if not gh_api_token:
        print("GitHub API token is required.")
        exit(1)
    with open(config_file) as course_config:
        course_data = json.load(course_config)
    organization = course_data["organization"]
    teams_and_teamdata = course_data["teams"]
    if (
        course_data.get("milestoneStartsOn", None) is None
        or not course_data["milestoneStartsOn"]
        or course_data["milestoneStartsOn"] is None
        or course_data.get("milestoneEndsOn", None) is None
        or course_data["milestoneEndsOn"] is None
        or not course_data["milestoneEndsOn"]
    ):
        startDate = datetime.now()
        endDate = datetime.now()
        useDecay = False
    else:
        startDate = datetime.fromisoformat(course_data["milestoneStartsOn"])
        endDate = datetime.fromisoformat(course_data["milestoneEndsOn"])
        useDecay = True

    print("Organization: ", organization)

    team_metrics = {}
    for team, teamdata in teams_and_teamdata.items():
        print("Team: ", team)
        print("Managers: ", teamdata["managers"])
        print("Milestone: ", teamdata["milestone"])
        members = get_team_members(organization, team)
        team_metrics[team] = getTeamMetricsForMilestone(
            org=organization,
            team=team,
            milestone=teamdata["milestone"],
            milestoneGrade=teamdata["milestoneGrade"],
            members=members,
            managers=teamdata["managers"],
            startDate=startDate,
            endDate=endDate,
            useDecay=useDecay,
        )
        workspace_path = "/github/workspace"
        # Combine the workspace path with the CSV file name
        csv_file_path = f"{workspace_path}/{teamdata['milestone']}-{team}-{organization}.csv"
        write_milestone_data_to_csv(
            team_metrics[team], csv_file_path
        )


if __name__ == "__main__":
    main()
