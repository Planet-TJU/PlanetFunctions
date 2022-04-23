# -*- coding:utf-8 -*-
import json
import numpy as np
import base64


def handler(event, context):
    s = json.loads(str(base64.b64decode(json.dumps(event["body"])), encoding="utf-8"))
    a = np.array(s['list'])
    amin = a.min()
    amax = a.max()
    a = (a - amin) / (amax - amin)
    result = {'ans': a.tolist()}

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }