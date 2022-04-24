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
    ans = []

    for i in range(0, n):
        mida = a[i]
        for j in range(0, l):
            if (mida[j] < r1 or mida[j] > r2):
                ans.append(j)

    ans = list(set(ans))
    a = np.delete(a, ans, axis=1)

    result = {'ans': a.tolist()}

    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }