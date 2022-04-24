# -*- coding:utf-8 -*-
import json
import base64
import numpy as np


def handler(event, context):
    s = json.loads(str(base64.b64decode(json.dumps(event['body'])), encoding='utf-8'))
    a = np.array(s['data'], dtype=np.float)
    n = len(a)
    l = len(a[0])
    midans = []
    for i in range(0, n):
        mida = a[i]
        for j in range(0, l):
            if (np.isnan(mida[j])):
                a[i][j] = 0

    # midans=list(set(midans))
    # a=np.delete(a,midans,axis=1)
    result = {'ans': a.tolist()}
    print(midans)

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }