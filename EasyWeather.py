import requests
import json
import api_k
import datetime


current_weather_request = requests.get(api_k.key_current())
five_day_request = requests.get(api_k.key_forecast())


def pull_current_temp():

    # temp for today
    temp_json_keys = current_weather_request.json()
    parse_for_temp = temp_json_keys['main']
    current_temp = round(parse_for_temp.get('temp'))

    # description of weather
    parse_for_descript = temp_json_keys['weather']
    current_descript = parse_for_descript[0]['description']

    return current_temp, current_descript


def get_weather_tomorrow():

    # temp for tomorrow
    forecast_json_keys = five_day_request.json()
    parse_for_temp = forecast_json_keys['list']
    temp_tomorrow = parse_for_temp[1]['main'].get('temp')

    # description of weather
    tomorrow_descript = parse_for_temp[1]['weather'][0]['description']

    # get day of week
    parse_for_date = parse_for_temp[2]['dt_txt']
    tomorrow_day = convert_json_timedate(parse_for_date)

    return temp_tomorrow, tomorrow_descript, tomorrow_day


def get_weather_day_three():

    # temp for next day
    forecast_json_keys = five_day_request.json()
    parse_for_temp = forecast_json_keys['list']
    temp_next_day = parse_for_temp[10]['main'].get('temp')

    # description of weather
    next_descript = parse_for_temp[10]['weather'][0]['description']

    # get day of week
    parse_for_date = parse_for_temp[10]['dt_txt']
    day_three = convert_json_timedate(parse_for_date)

    return temp_next_day, next_descript, day_three


def get_weather_day_four():

    # temp for next day
    forecast_json_keys = five_day_request.json()
    parse_for_temp = forecast_json_keys['list']
    temp_next_day = parse_for_temp[18]['main'].get('temp')

    # description of weather
    next_descript = parse_for_temp[18]['weather'][0]['description']

    # get day of week
    parse_for_date = parse_for_temp[18]['dt_txt']
    day_four = convert_json_timedate(parse_for_date)

    return temp_next_day, next_descript, day_four


def get_weather_day_five():

    # temp for next day
    forecast_json_keys = five_day_request.json()
    parse_for_temp = forecast_json_keys['list']
    temp_next_day = parse_for_temp[26]['main'].get('temp')

    # description of weather
    next_descript = parse_for_temp[26]['weather'][0]['description']

    # get day of week
    parse_for_date = parse_for_temp[26]['dt_txt']
    day_five = convert_json_timedate(parse_for_date)

    return temp_next_day, next_descript, day_five


def determ_day_of_week(year, month, day):

    # parses date using datetime module - Return the day of the week as an integer,
    # where Monday is 0 and Sunday is 6
    parse_date = datetime.date(year, month, day).weekday()
    if parse_date == 0:
        return 'Monday'
    elif parse_date == 1:
        return 'Tuesday'
    elif parse_date == 2:
        return 'Wednesday'
    elif parse_date == 3:
        return 'Thursday'
    elif parse_date == 4:
        return 'Friday'
    elif parse_date == 5:
        return 'Saturday'
    elif parse_date == 6:
        return 'Sunday'
    else:
        return 'Error: Could not pull date information'


def convert_json_timedate(date):
    day_of_week_str = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    year = day_of_week_str.year
    month = day_of_week_str.month
    day = day_of_week_str.day

    return determ_day_of_week(year, month, day)


def main():

    print('Here is today\'s forcast:')

    current_temp, current_decript = pull_current_temp()
    print('The current temperature is {:d} degrees. '
          '\nThe type of weather you will enjoy is {}.\n'
          .format(current_temp, current_decript))

    tomorrow_temp, tomorrow_descript, tomorrow_day = get_weather_tomorrow()
    print('{}:\nThe temperature {} will be {:.0f} degrees. '
          '\nThe type of weather you will enjoy is {}.\n'
          .format(tomorrow_day, tomorrow_day, tomorrow_temp, tomorrow_descript))

    next_temp, next_descript, day_three = get_weather_day_three()
    print('{}:\nThe temperature {} will be {:.0f} degrees. '
          '\nThe type of weather you will enjoy is {}.\n'
          .format(day_three, day_three, next_temp, next_descript))

    day_four_temp, day_four_descript, day_four = get_weather_day_four()
    print('{}:\nThe temperature {} will be {:.0f} degrees. '
          '\nThe type of weather you will enjoy is {}.\n'
          .format(day_four, day_four, day_four_temp, day_four_descript))

    day_five_temp, day_five_descript, day_five = get_weather_day_five()
    print('{}:\nThe temperature {} will be {:.0f} degrees. '
          '\nThe type of weather you will enjoy is {}.\n'
          .format(day_five, day_five, day_five_temp, day_five_descript))
    print(input('Press enter to exit'))


if __name__ == '__main__':
    main()