import requests
from bs4 import BeautifulSoup
import datetime


def get_weather_data():
    url = 'https://tianqi.moji.com/weather/china/shaanxi/xian'
    res = requests.get(url)
    html_doc = res.text
    # print(html_doc)
    soup = BeautifulSoup(html_doc, 'html.parser')
    weather_info = soup.find('div', {'class': 'wea_weather clearfix'})
    # print(weather_info)
    temperature = weather_info.find('em').get_text()
    # print(temperature)
    weather = weather_info.find('b').get_text()
    # print(weather)
    update_time = weather_info.find('strong').get_text()[2:]
    AQI = soup.find('div', {'class': 'wea_alert clearfix'}).find('em').get_text()
    # print(AQI)
    about = soup.find('div', {'class': 'wea_about clearfix'})
    # print(about)
    humidity = about.find('span').get_text().split(' ')[1]
    speed = about.find('em').get_text()

    tips = soup.find('div', {'class': 'wea_tips clearfix'}).find('em').get_text()[:-1]
    # print(tips)

    info_all = '墨迹天气提醒您\n' + '今天是{0}年{1}年{2}日,陕西省西安市的天气({3})为：\n天气:{4}\n实时温度:{5}\n空气质量指数:{6}\n湿度:{7}\n风速:{8}\n今日天气提示:{9}'.format(
        str(datetime.date.today()).split('-')[0],
        str(datetime.date.today()).split('-')[1],
        str(datetime.date.today()).split('-')[2],
        update_time,
        weather,
        temperature + '℃', AQI,
        humidity, speed, tips)
    print(info_all)


if __name__ == '__main__':
    get_weather_data()
