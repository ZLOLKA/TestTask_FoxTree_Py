from TestTask_FoxTree.celery import app
import requests
import json
from datetime import datetime
from .models import BankRate


class Error:
    def __init__(self, str_error: str, type_error: str, name_url: str):
        self.str_error = str_error
        self.type_error = type_error
        self.name_url = name_url


@app.task
def get_exchange_rates():
    # Banking servers URLs
    nbrb = "https://www.nbrb.by/api/exrates/rates?periodicity=0"
    belarusbank = "https://belarusbank.by/api/kursExchange?city=Минск"
    alfabank = "https://developerhub.alfabank.by:8273/partner/1.0.0/public/rates"
    tracked_currencies = ("USD", "EUR", "RUB")

    # Getting json from servers
    error_list = []
    res_nbrb = None
    res_belarusbank = None
    res_alfabank = None
    try:
        res_nbrb = requests.get(nbrb).text
    except requests.exceptions.RequestException as exp:
        error_list.append(Error(exp.args[0], str(type(exp))[8:-2], "NBRB"))
    try:
        res_belarusbank = requests.get(belarusbank).text
    except requests.exceptions.RequestException as exp:
        error_list.append(Error(exp.args[0], str(type(exp))[8:-2], "BelarusBank"))
    try:
        res_alfabank = requests.get(alfabank).text
    except requests.exceptions.RequestException as exp:
        if len(error_list) == 2:
            raise exp
        else:
            error_list.append(Error(exp.args[0], str(type(exp))[8:-2], "AlfaBank"))

    # Getting data from json
    kwargs = {}
    if res_nbrb is not None:
        for data in json.loads(res_nbrb):
            if data["Cur_Abbreviation"] in tracked_currencies:
                kwargs[f"nbrb_{data['Cur_Abbreviation']}"] = data["Cur_OfficialRate"]
    if res_belarusbank is not None:
        json_res_belarusbank = json.loads(res_belarusbank)[0]
        for name in json_res_belarusbank:
            if not len(name) > 7 and name[:3] in tracked_currencies:
                kwargs[f"belarus_{name[:3]}_{'sell' if name[4:] == 'in' else 'buy'}"] = json_res_belarusbank[name]
    if res_alfabank is not None:
        for data in json.loads(res_alfabank)["rates"]:
            if data["buyIso"] == "BYN" and data["sellIso"] in tracked_currencies:
                s = f"alfa_{data['sellIso']}_"
                kwargs[s+"sell"] = data["sellRate"]
                kwargs[s+"buy"] = data["buyRate"]

    data = BankRate(date=datetime.now(), **kwargs)
    data.save()

    # Error output
    if error_list:
        error_str = "Error list:\n"
        for error in error_list:
            error_str += f"---|  {error.name_url} {error.type_error}: {error.str_error}\n"
        raise ConnectionError(error_str)
