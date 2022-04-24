# -*- coding:utf-8 -*-
import json
import base64
import numpy as np
def handler (event, context):
    s=json.loads(str(base64.b64decode(json.dumps(event['body'])),encoding='utf-8'))
    k=s['k']
    a=s['data']
    n=len(a)
    l=len(a[0])
    midans=[]
    ans=[]
    for i in range(0,n):
        mida=a[i]
        for j in range(0,l):
            if(j !=0 and (abs(mida[j]-mida[j-1])>k)):
                midans.append(1)
            else:
                midans.append(0)
        ans.append(midans)
        midans=[]
    ans=np.array(ans)
    result={'ans': ans.tolist()}
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }