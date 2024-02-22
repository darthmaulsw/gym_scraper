import sys
import os.path
import requests
from bs4 import BeautifulSoup


url = 'https://crossfitripcord.sites.zenplanner.com/leaderboard-day.cfm?type=DailyWorkout'
content = requests.get(url).content
soup = BeautifulSoup(content, 'html.parser')

workouts_content = soup.find("div", {"class": "workout"})

titles_list = workouts_content.find_all("div", {"class": "sectionTitle"})
exercise_list = workouts_content.find_all("div", {"class": "skillDesc"})

# for title in range(len(titles_list)):
#     print(titles_list[title].find("h2"))
# for exercise in range(len(exercise_list)):
#     print(exercise_list[exercise])

def titles_html_generator():
    titles_html = ""
    for title_num in range(len(titles_list)):
        title = titles_list[title_num].find("h2")
        titles_html += f"""
        <td>{title}</td>
        """
    return titles_html

def exercises_html_generator():
    exercises_html = ""
    for exercise_num in range(len(exercise_list)):
        exercise = exercise_list[exercise_num]
        exercises_html += f"""
        <td>{exercise}</td>
        """
    return exercises_html

def save_html_to_file():
    structure_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Workouts</title>
    </head>
    <body>
    <table>
    <tr>
    {titles_html_generator()}
    </tr>
    <tr>
    {exercises_html_generator()}
    </tr>
    </table>


    </body>
    </html>
    """
    with open('test.html', 'w') as f:
        f.writelines(structure_template)

save_html_to_file()

