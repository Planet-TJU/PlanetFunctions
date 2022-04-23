# -*- coding:utf-8 -*-
import json
import base64
import numpy as np
def handler (event, context):
    s=json.loads(str(base64.b64decode(json.dumps(event['body'])),encoding='utf-8'))
    a=np.array(s['list'])
    k=s['k']
    ans=[]
    if(k==1):
        ans=np.corrcoef(a)
    elif(k==0):
        ans=np.corrcoef(a,rowvar=False)

    result={'ans': ans.tolist()}
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }