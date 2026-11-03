import re

logs = [
    "2026-11-02 10:30:20 ERROR payment-service Failed",
    "2026-11-02 10:31:20 INFO order-service Started"
]

pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (\S+) (.+)"

for log in logs:

    match = re.match(pattern, log)

    if match:
        date, time, level, service, message = match.groups()

        print("Date:", date)
        print("Time:", time)
        print("Level:", level)
        print("Service:", service)
        print("Message:", message)
        print("-----------------")