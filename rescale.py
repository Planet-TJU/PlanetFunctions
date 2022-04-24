# -*- coding:utf-8 -*-
import json
import base64
import numpy as np
def handler (event, context):
     s=json.loads(str(base64.b64decode(json.dumps(event['body'])),encoding='utf-8'))
     l=s['left']
     r=s['right']
     a=np.array(s['data'],dtype=np.float)
     n=len(a)
     ans=[]
     midans=[]
     for i in range(0,n):
         mida=a[i]
         midans=[round( ((xx - min(mida)) / (1.0*(max(mida) - min(mida)))) * (r - l) + l, 2) for xx in mida]
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