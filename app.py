import requests
import PySimpleGUI as sg
from bs4 import BeautifulSoup

layout = [
    [sg.Text('Sign: '),sg.Input(key='-SIGN_TYPE-'),sg.OptionMenu(values=['daily-today','daily-yesterday','daily-tomorrow','weekly','monthly'], default_value='daily-today',key='-DATE_TYPE-')],
    [sg.Multiline(size=(80,10),disabled=True,key='-MAIN-')],
    [sg.Text('Love: '), sg.Text('',key='-LOVE-')],
    [sg.Text('Friend: '), sg.Text('',key='-FRIEND-')],
    [sg.Text('Career: '), sg.Text('',key='-CAREER-')],
    [sg.Button('Try'),sg.Button('Cancel')]
]

window = sg.Window('Horoscope',layout)

def horoscope(sign, date):
    match sign:
        case "Aries":
            sign = '1'
        case "Taurus":
            sign = '2'
        case "Gemini":
            sign = '3'
        case "Cancer":
            sign = '4'
        case "Leo":
            sign = '5'
        case "Virgo":
            sign = '6'
        case "Libra":
            sign = '7'
        case "Scorpio":
            sign = '8'
        case "Sagittarius":
            sign = '9'
        case "Capricorn":
            sign = '10'
        case "Aquarius":
            sign = '11'
        case "Pisces":
            sign = '12' 
    url= "https://www.horoscope.com/us/horoscopes/general/horoscope-general-"+date+".aspx?sign="+sign+""
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    main = soup.find("div", class_="main-horoscope").p.text
    love = soup.find(id="src-horo-matchlove").p.text
    friend = soup.find(id="src-horo-matchfriend").p.text
    career = soup.find(id="src-horo-matchcareer").p.text
    horoscope_Info = {}
    horoscope_Info['Main'] = main
    horoscope_Info['Love'] = love
    horoscope_Info['Friend'] = friend
    horoscope_Info['Career'] = career
    return horoscope_Info

while True:
    event,values=window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event=='Try':
        sign_type = values['-SIGN_TYPE-'].capitalize()
        date_type = values['-DATE_TYPE-']
        horoscope_info = horoscope(sign_type, date_type)
        window['-MAIN-'].update(horoscope_info['Main'])
        window['-LOVE-'].update(horoscope_info['Love'])
        window['-FRIEND-'].update(horoscope_info['Friend'])
        window['-CAREER-'].update(horoscope_info['Career'])
window.close()
