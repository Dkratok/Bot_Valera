import requests
import json


def get_rate_responce(cur_id, date=0):
    if date != 0:
        req_url = 'http://www.nbrb.by/API/ExRates/Rates/' + str(cur_id) + '?onDate=' + date
    else:
        req_url = 'http://www.nbrb.by/API/ExRates/Rates/' + str(cur_id);
    r = requests.get(req_url)
    if r.status_code == 200:
        return r.content
    else:
        return 'Unexpected response status code: '+str(r.status_code)


def get_rate_from_json(json_string):
    if str(json_string).startswith('Unexpected response status code:'):
        return 'запрос недоступен'
    else:
        json_content = json.loads(json_string);
        return json_content["Cur_OfficialRate"]



