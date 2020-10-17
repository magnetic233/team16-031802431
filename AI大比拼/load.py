import json

def loading():
    with open('problem.json', 'r') as f:

            temp = json.loads(f.read())
            
            data=(temp['data'])
            chanceleft=(temp["chanceleft"])
            expire=(temp["expire"])
            uuid=(temp["uuid"])
            
##            print("chanceleft:",chanceleft)
##            print("expire:",expire)
##            print("uuid:",uuid)
# 取出特定键的值
            taowatext = json.dumps(data)
            output = json.loads(taowatext)
            getimg = output['img']
##            print("img:",output['img'])
##            print("step:",output['step'])
##            print("swap:",output['swap'])
          
    with open("base64.txt","w") as f:
       f.write(getimg)  # 自带文件关闭功能，不需要再写f.close()
       k=[output['step'],output['swap'][0],output['swap'][1],uuid]

       return(k)
   
if __name__ == '__main__':
    loading()
