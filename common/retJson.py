# -*- coding: utf-8 -*-
def retJson():
    '''
    返回所有可能状况的json模板
    '''
    ret_jsons = {
        # 成功
        "00000": {
            "msg": "success",
            "code": "00000",
            "pageNum": None,
            "hasNext": False,
            "data": None,
        },
        # 参数错误
        "10005": {
            "msg": "Missing the params",
            "code": "10005"
        },
        # 无结果
        "10008": {
            "msg": "Search no result",
            "code": "10008"
        },
        # 网络错误
        "10001": {
            "msg": "Network error",
            "code": "10001"
        }
    }

    return ret_jsons