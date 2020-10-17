import urllib.request
import urllib.parse
import requests            #导入request模块
import json



url = 'http://47.102.118.1:8089/api/team/problem/16'
response = requests.get(url)                       #用导入的request模块的get方法访问URL
with open('waiting problem.json', 'w') as f:
    f.write(response.text)           # 自带文件关闭功能，不需要再写f.close()
print(response.status_code)            #调用response里的status_code方法查看状态码

##↑ 取得未通过的列表

##↓ 取得未通过列表的第一个题目
i=0
for i in range(200):
   if(response.text[i]=='}'):
      k=i
      break
print("未通过列表的第一个题目:")
print(response.text[1:k+1])     
with open('cutproblem.json', 'w') as f:
    f.write(response.text[1:k+1])           
##↑ 取得未通过列表的第一个题目

    
with open('cutproblem.json', 'r') as f:
   temp = json.loads(f.read())
   author=(temp["author"])
   uuid=(temp["uuid"])
   print('')
   print('')
   print("请求文档与地址：http://47.102.118.1:8089/api/challenge/start/%s"%uuid)
   print("{")
   print(
      "{"
		"teamid: 16 ,",
		"token: d74d6a5c-409c-41d5-b066-533e48ae1425"
       "}"
        )
   print("}")


