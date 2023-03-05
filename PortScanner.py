import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Bilinmeyen argüman girişi")

print("-"*50)
print("Hedef : "+target)
print("Başlama saati : "+str(datetime.now()))
print("-"*50)

try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} açık".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Çıkış yapılıor...")
    sys.exit()
except socket.gaierror:
    print("\n Hedef bulunmadı!")
    sys.exit()
except socket.error:
    print("Sunucu yanıt vermiyor!")
    sys.exit()