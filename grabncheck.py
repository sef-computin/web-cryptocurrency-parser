from proxy_grabber import ProxyGrabber

def proxy_grab(objectgrabber, constlim):
    flag = True
    n=0
    while(flag):
        try:
            objectgrabber.grab_proxies(proxy_limit=10)
            flag = False
        except:
            if (n>constlim):break
            n+=1
            print("exception")
            flag = True
    print("proxies grabbed")
#
# while (flag):
#     try:
#         objectgrabber.check_proxies()
#         flag = False
#     except:
#         print("exception")
#         flag = True
#
#print("proxies checked")
def write_file(txt, object):
    with open(txt, "w") as file:
        for proxy in object.get_proxy_list(): file.write(proxy+"\n")

def main():
    objectgrabber = ProxyGrabber()
    print("object created")
    constlim = 100
    proxy_grab(objectgrabber, constlim)
    write_file("proxylist.txt", objectgrabber)

if __name__ == '__main__':
    main()