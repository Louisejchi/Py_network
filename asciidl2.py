import os
from ftplib import FTP, error_perm

if os.path.exists('README'):
    raise IOError('Refusing to overwrite your README file')

def writeline(data):
    fd.write(data)
    fd.write(os.linesep)

try:
    f = FTP('10.22.23.179')  # 使用你自己的 FTP 伺服器地址
    #f.login("phil", "aloha802.3")
    f.login()

    # 列出根目錄內容
    print("Listing root directory:")
    f.retrlines('LIST')

    # 嘗試切換到 /home
   # try:
   #     f.cwd('/home')
   #     print("Changed to /home")
   #     f.retrlines('LIST')
   # except error_perm as e:
   #     print(f"Failed to change to /home: {e}")
   #     f.quit()
   #     exit()

    # 嘗試切換到 /home/ftpuser
    try:
        f.cwd('/phil')
        print("Changed to /home/phil")
        f.retrlines('LIST')
    except error_perm as e:
        print(f"Failed to change to /home/phil: {e}")
        f.quit()
        exit()

    # 開始下載 README 文件
    fd = open('demo.txt', 'w')
    f.retrlines('RETR demo', writeline)
    fd.close()
    f.quit()

except error_perm as e:
    print(f'FTP error: {e}')
except Exception as e:
    print(f'Error: {e}')
