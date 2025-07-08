import datetime
from operator import itemgetter
from collections import defaultdict

tasks = [
    {"name": "Task A", "deadline": "2025-07-12", "priority": 5, "estimated_time": 3},
    {"name": "Task B", "deadline": "2025-07-09", "priority": 3, "estimated_time": 2},
    {"name": "Task C", "deadline": "2025-07-10", "priority": 4, "estimated_time": 4},
    {"name": "Task D", "deadline": "2025-07-08", "priority": 5, "estimated_time": 1},
    {"name": "Task E", "deadline": "2025-07-15", "priority": 2, "estimated_time": 5}
]

daily_work_hours = 8

today = datetime.date.today()
for task in tasks:
    deadline = datetime.datetime.strptime(task["deadline"], "%Y-%m-%d").date()
    days_left = max((deadline - today).days, 1)
    task["deadline_date"] = deadline
    task["urgency"] = 1 / days_left
    task["score"] = task["priority"] * 0.7 + task["urgency"] * 10 * 0.3

tasks.sort(key=itemgetter("score"), reverse=True)

schedule = defaultdict(list)
day_pointer = today
hours_left = daily_work_hours

for task in tasks:
    time_needed = task["estimated_time"]
    while time_needed > 0:
        if hours_left == 0:
            day_pointer += datetime.timedelta(days=1)
            hours_left = daily_work_hours

        time_slot = min(time_needed, hours_left)
        schedule[day_pointer].append((task["name"], time_slot))
        time_needed -= time_slot
        hours_left -= time_slot

for day in sorted(schedule.keys()):
    print(f"\n🗓 {day.strftime('%A, %Y-%m-%d')}")
    for task_name, hours in schedule[day]:
        print(f"  - {task_name}: {hours} hour(s)")
