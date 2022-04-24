import json
import base64
import numpy as np


def handler(event, context):
    s = json.loads(str(base64.b64decode(json.dumps(event['body'])), encoding='utf-8'))
    a = np.array(s['data'])
    n = len(a)
    l = len(a[0])
    me = np.mean(a)
    st = np.std(a)
    r1 = me - 3 * st
    r2 = me + 3 * st
    midans = []
    ans = []
    for i in range(0, n):
        mida = a[i]
        for j in range(0, l):
            if (mida[j] >= r1 and mida[j] <= r2):
                midans.append(mida[j])
            else:
                midans.append(me)

        ans.append(midans)
        midans = []

    ans = np.array(ans)
    result = {'ans': ans.tolist(), "me": str(me), "st": str(st), "r1": str(r1), "r2": str(r2)}

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }