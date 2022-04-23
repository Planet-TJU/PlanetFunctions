# -*- coding:utf-8 -*-
import json
import base64
import numpy as np
def handler (event, context):
    # s=json.loads(str(base64.b64decode(json.dumps(event["body"])),encoding="utf-8"))
    s=json.loads(str(base64.b64decode(json.dumps(event['body'])),encoding="utf-8"))
    k=s['k']
    a=np.array(s['list'])
    l=len(a[0])
    midans=[]
    ans=[]
    if(k<=l):
        for i in range(0,len(a)):
            sa=np.sort(a[i])
            fsa=np.flipud(sa)
            for j in range(0,k):
                midans.append(fsa[j])
            ans.append(midans)
            midans=[]
        ans=np.array(ans)
        result={'ans': ans.tolist()}
    else:
        result={'ans': 'error!'}
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }