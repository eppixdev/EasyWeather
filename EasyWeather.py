import requests
import json
import api_k
import pprint

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


def get_temp_tomorrow():

    # temp for tomorrow
    forecast_json_keys = five_day_request.json()
    parse_for_temp = forecast_json_keys['list']
    temp_tomorrow = parse_for_temp[1]['main'].get('temp')

    # description of weather
    tomorrow_descript = parse_for_temp[1]['weather'][0]['description']

    return temp_tomorrow, tomorrow_descript


def get_temp_next_day():

    # temp for next day
    forecast_json_keys = five_day_request.json()
    parse_for_temp = forecast_json_keys['list']
    temp_next_day = parse_for_temp[11]['main'].get('temp')

    # description of weather
    next_descript = parse_for_temp[11]['weather'][0]['description']

    return temp_next_day, next_descript


def main():
    current_temp, current_decript = pull_current_temp()
    print('The current temperature is {:d} degrees. '
          'The type of weather you will enjoy is {}.'
          .format(current_temp, current_decript))

    tomorrow_temp, tomorrow_descript = get_temp_tomorrow()
    print('The temperature tomorrow will be {:.0f} degrees. '
          'The type of weather you will enjoy is {}.'
          .format(tomorrow_temp, tomorrow_descript))

    next_temp, next_descript = get_temp_next_day()
    print('The temperature the day after will be {:.0f} degrees. '
          'The type of weather you will enjoy is {}.'
          .format(next_temp, next_descript))


if __name__ == '__main__':
    main()