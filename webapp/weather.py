from flask import current_app
import requests

def get_weather(city): 
    weather_url = current_app.config['WEATHER_URL']                
    params = {'q': city, 
              'type': 'like', 
              'units': 'metric',
              'lang': 'ru', 
              'APPID': current_app.config['WEATHER_API_APPID'] 
             }
    try:         
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()        
        if 'list' in weather:
            try:
                return weather['list'][0]
            except(IndexError, TypeError):
                return False
    except(requests.RequestException, ValueError):
        print("Сетевая ошибка.")
        return False
    return False            


if __name__ == "__main__":
    print(get_weather("Moscow,RU"))



