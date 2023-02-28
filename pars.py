import requests
from fake_useragent import UserAgent as ua
import json


class Parser:
    def __init__(self):
        pass

    def __str__(self):
        pass

    def sorted(self):
        data = self.buff_pars()
        data.sort(reverse=True)
        stroka = ''
        for i in range(len(data)):
            stroka += f'''<div class="item">
            <a href="{data[i][4]}">
                <center>
                    <img src="{data[i][5]}" alt="">
                </center>

                <div class="name">
                    <span>{data[i][1]}</span>
                </div>
                <div class="feauters">
                    <span>Цена Buff: {data[i][2]} RUB</span>
                    <span>Цена Steam: {data[i][3]} RUB</span>
                    <span>Разница: {data[i][0]}%</span>

                </div>
            </a>
        </div>'''
        return stroka

    def buff_pars(self):
        a = 1677141175789
        union = []
        for j in range(1,20):
            a += 2
            url = f'https://buff.163.com/api/market/goods?game=csgo&page_num=1&use_suggestion=0&_={a}'
            params = {
                "game": "csgo",
                "page_num": j,
                "_": a
            }
        

            header = {
                'User-Agent': 'ua().random'
            }
            r = requests.get(url, headers=header, params=params)
            information = json.loads(r.text)
            for i in range(20):
                name = information['data']['items'][i]["market_hash_name"]
                ssilka = information['data']['items'][i]["steam_market_url"]
                image = information['data']['items'][i]["goods_info"]["icon_url"]
                price_st = round(float(information['data']['items'][i]['goods_info']['steam_price_cny']) * 10.4, 2)
                price_buff = round(float(information['data']['items'][i]['sell_reference_price']) * 10.4, 2)
                difference = round((1-price_buff/price_st) * 100, 2)
                if (difference, name, price_buff, price_st, ssilka, image) in union:
                    continue
                union.append((difference, name, price_buff, price_st, ssilka, image))
        return union

    def parser_buff(self):
        with open("items_sorted.txt") as f:
            data = f.readline()
            cookies = {
                'Device-Id': 'YOUR DATA',
                'Locale-Supported': 'ru',
                'game': 'csgo',
                'session': 'YOUR DATA',
                'csrf_token': 'YOUR DATA',
            }
            params = {
                "game": "csgo",
                "page_num": "1",
                "search": data,
                "use_suggestion": "0",
                "_": "1677510244881"
            }
            headers = {
                "User-Agent": f"{ua().random}"
            }
            response = requests.get(f"https://buff.163.com/api/market/goods?game=csgo&page_num=1&search={params['search']}&use_suggestion=0&_=1677510244881", cookies=cookies, params=params, headers=headers).text
            print(response)