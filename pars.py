import requests
from fake_useragent import UserAgent as ua
import json


class Parser:


    def buff_pars_csgo(self):
        a = 1677141231389
        union = []
        for j in range(1,5):
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
                price_buff = round((float(information['data']['items'][i]['sell_reference_price']) * 10.4)/100*87, 2)
                difference = round((1-price_buff/price_st) * 100, 2)
                if (difference, name, price_buff, price_st, ssilka, image) in union:
                    continue
                union.append((difference, name, price_buff, price_st, ssilka, image))
        union.sort(reverse=True)
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


    
    def buff_pars_dota(self):
        a = 1678607519380
        union = []
        for j in range(1,5):
            a += 2
            params = {
                'game': 'dota2',
                'page_num': '1',
                'use_suggestion': '0',
                '_': f'{a}',
            }
            response = requests.get('https://buff.163.com/api/market/goods', params=params)
        

            header = {
                'User-Agent': 'ua().random'
            }
            r = requests.get('https://buff.163.com/api/market/goods', params=params, headers=header)
            information = json.loads(r.text)
            for i in range(20):
                name = information['data']['items'][i]["market_hash_name"]
                ssilka = information['data']['items'][i]["steam_market_url"]
                image = information['data']['items'][i]["goods_info"]["icon_url"]
                price_st = round(float(information['data']['items'][i]['goods_info']['steam_price_cny']) * 10.4, 2)
                price_buff = round((float(information['data']['items'][i]['sell_reference_price']) * 10.4)/100*87, 2)
                difference = round((1-price_buff/price_st) * 100, 2)
                if (difference, name, price_buff, price_st, ssilka, image) in union:
                    continue
                union.append((difference, name, price_buff, price_st, ssilka, image))
        union.sort(reverse=True)
        return union
    
    def buff_pars_rust(self):
        a = 1678607519380
        union = []
        for j in range(1,5):
            a += 2
            params = {
                'game': 'rust',
                'page_num': '1',
                'use_suggestion': '0',
                '_': f'{a}',
            }
            response = requests.get('https://buff.163.com/api/market/goods', params=params)
        

            header = {
                'User-Agent': 'ua().random'
            }
            r = requests.get('https://buff.163.com/api/market/goods', params=params, headers=header)
            information = json.loads(r.text)
            for i in range(20):
                name = information['data']['items'][i]["market_hash_name"]
                ssilka = information['data']['items'][i]["steam_market_url"]
                image = information['data']['items'][i]["goods_info"]["icon_url"]
                price_st = round(float(information['data']['items'][i]['goods_info']['steam_price_cny']) * 10.4, 2)
                price_buff = round((float(information['data']['items'][i]['sell_reference_price']) * 10.4)/100*87, 2)
                difference = round((1-price_buff/price_st) * 100, 2)
                if (difference, name, price_buff, price_st, ssilka, image) in union:
                    continue
                union.append((difference, name, price_buff, price_st, ssilka, image))
        union.sort(reverse=True)
        return union