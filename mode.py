# -*- coding:utf-8 -*-
import json
import base64
import numpy as np


def handler(event, context):
    s = json.loads(str(base64.b64decode(json.dumps(event['body'])), encoding='utf-8'))
    a = np.array(s['data'])
    n = len(a)
    ans = []
    for i in range(0, n):
        me = np.argmax(np.bincount(a[i]))
        ans.append(me)

    ans = np.array(ans)
    result = {'ans': ans.tolist()}
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }
