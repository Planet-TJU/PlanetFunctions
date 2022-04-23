# -*- coding:utf-8 -*-
import json
import base64
import numpy as np
def handler (event, context):
    s=json.loads(str(base64.b64decode(json.dumps(event["body"])),encoding="utf-8"))
    a=np.array(s['data'],dtype=np.float)
    k=s['k']
    ans=process(np.min(a,axis=k))
    result={'ans': ans}
    return {
        "statusCode": 200,
        "isBase64Encoded": False,
        "body": json.dumps(result),
        "headers": {
            "Content-Type": "application/json"
        }
    }
def process(x):
    shape=np.shape(x)
    if(len(shape)==0):
        return "None" if np.isnan(x) else str(x)
    elif(len(shape)==1):
        return [None if np.isnan(i) else i for i in x]
    elif(len(shape)==2):
        # 对二维向量中的nan进行替换为None
        # 取出每一行
        ans=[]
        for row in x:
            ans.append([None if np.isnan(i) else i for i in row])
        return ans