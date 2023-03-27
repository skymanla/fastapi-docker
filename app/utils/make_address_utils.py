import re

korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')


def bun_ji(address: str):
    # 1. 한글부터 제거
    bun_ji = re.sub(korean, "", address)
    # 2. 공백 제거
    bun_ji = bun_ji.replace(" ", "")
    # 3. 하이픈으로 나누기
    bun_ji_list = bun_ji.split("-")
    # 4. dict 타입
    ji = None
    if len(bun_ji_list) > 1:
        ji = bun_ji_list[1].zfill(4)

    bun_ji_dict = {
        "bun": bun_ji_list[0].zfill(4),
        "ji": ji
    }
    return bun_ji_dict


def sido_gugun_code(bcode: str):
    # 앞에서 5자리
    sido_cd = bcode[:5]
    # 뒤에서 5자리
    gugun_cd = bcode[-5:]
    return {
        "sigunguCd": sido_cd,
        "bjdongCd": gugun_cd
    }


def dong_ho(obj: list):
    dong_ho_obj = []
    for _i, _v in enumerate(obj):
        int_ho_nm = int(_v['hoNm'])
        search_dong = [item for item in dong_ho_obj if item['dong'] == _v['dongNm']]
        if not search_dong:
            dong_ho_obj.append({"dong": _v['dongNm'], "ho": [int_ho_nm]})
        else:
            search_index = next((index for (index, item) in enumerate(dong_ho_obj) if item['dong'] == _v['dongNm']))
            if int_ho_nm not in dong_ho_obj[search_index]['ho']:
                dong_ho_obj[search_index]['ho'].append(int_ho_nm)
                dong_ho_obj[search_index]['ho'].sort()

    if dong_ho_obj:
        dong_ho_obj.sort(key=lambda x: x.get('dong'))
        return dong_ho_obj

    return dong_ho_obj
