import os,sys,time,requests
GL = "\033[96;1m" # Blue aqua
BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33;1m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0;1m"     # White
R = "\033[31m"    # Red
C = "\033[36;1m"    # Cyan
logo = GG+"""
============================================
|            Trojans Attack                |
|                                          |
| Author : MiSetya                         |
| Team   : Light Cyber Indonesia           |
| Contact: 0823-8623-4828                  |
| Thanks to : Light Cyber Indonesia        |
============================================"""

def run(x):
        for n in x+"\n":
                sys.stdout.write(n)
                sys.stdout.flush()
                time.sleep(0.1)
def main():
        os.system('clear')
        print logo
        print
        no = raw_input(G+"["+C+"?"+W+"]["+R+"TARGET"+W+"]>> "+G)
        run(Y+" Mengecek nomor HP Target ...")
        time.sleep(4)
        if no < 5:
                print R+"Target Tidak Ditemukan!"
                sys.exit()
        elif '62' in no or '+62' in no or '08' in no:
                print Y+"["+C+"Lokasi"+W+"]: "+G+"Indonesia"
                time.sleep(4)
                serang(no)
        else:
                print R+"Tool tidak mendukung! "+no
                print G+"Tool Hanya bisa digunakan nomor Indonesia"
                sys.exit()

def serang(no):
        os.system('clear')
        print logo
        print
        run(W+"Mulai Menyerang !!!")
        time.sleep(2)
        while True:
                try:
                        print C+"Sukses menyerang target >> "+Y+no
                except:
                        pass

if __name__ == '__main__':
        try:
                main()
        except requests.exceptions.ConnectionError:
                print R+"Koneksi Error"
                sys.exit()
