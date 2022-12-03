import json
from datetime import datetime
from Meishiki import Meishiki


def main(request):
    body = json.loads(request)
    name = body["name"]
    birthday = body["birthday"]
    birthday_dt = datetime.strptime(birthday, "%Y%m%d")
    sex = body["sex"]

    birthtime_time = None
    if body["birthtime"]:
        birthtime = body["birthtime"]
        birthtime_dt = datetime.strptime(birthtime, "%H%M")
        birthtime_time = birthtime_dt.time()

    meishiki = Meishiki(birthdate=birthday_dt, birthtime=birthtime_time, sex=sex)
    meishiki.build_meishiki()
    meishiki.append_tsuhen()
    meishiki.append_twelve_fortune()
    result = meishiki.get_meishiki_table()
    print(result)

    return json.dumps(result)


if __name__ == "__main__":
    request_body = {"name": "a", "birthday": "19780627", "birthtime": "2238", "sex": "男性"}
    main(json.dumps(request_body))
