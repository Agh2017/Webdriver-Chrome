import requests, time

link = '''https://google.com
https://ya.ru
https://mail.ru
https://yocity12.com
https://bosch12.ru'''
links = link.split('\n')


def responseGet(link, N):
    for i in range(N):
        response = requests.get(link)
        # print(response.text)
        #print(response.status_code)
        assert response.status_code == 200, "response is wrong"
    return


for i in range(len(links)):
    t = time.time()
    responseGet(links[i],N=100)
    print(links[i], ' done, time:', (time.time()-t))
