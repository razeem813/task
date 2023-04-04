import calendar
from flask import Flask, request

app = Flask(__name__)

def get_month_events(month):
    # Convert month string to numerical representation
    month_num = list(calendar.month_abbr).index(month.capitalize())

    # Dictionary of month to events mapping
    month_events = {
        1: ["New Year's Day", "Martin Luther King Jr. Day"],
        2: ["Groundhog Day", "Valentine's Day", "President's Day"],
        3: ["St. Patrick's Day", "Spring Equinox"],
        4: ["April Fools' Day", "Easter", "Earth Day"],
        5: ["Cinco de Mayo", "Mother's Day", "Memorial Day"],
        6: ["Father's Day", "Summer Solstice"],
        7: ["Independence Day"],
        8: ["International Youth Day"],
        9: ["Labor Day", "Autumn Equinox"],
        10: ["Columbus Day", "Halloween"],
        11: ["Veterans Day", "Thanksgiving", "Black Friday"],
        12: ["Hanukkah", "Christmas Eve", "Christmas Day", "New Year's Eve"]
    }

    # Retrieve events for input month
    events = month_events.get(month_num, [])

    return events
@app.route('/recomend', methods=['GET'])
def recomend():
    month = request.args.get('month')
    m1=month[0:3]
    events = get_month_events(m1)
    return events


app.run(debug=True)