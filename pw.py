#! python3
# pw.py - パスワード管理プログラム(脆弱性あり)

PASSWORDS = { 'email' : 'jfdkalfjioap',
              'blog' : 'jfla;jdijraiojgia;',
              'luggage': '12345'}

import sys
sys.path.append('C:\\Users\\gongo\\Anaconda3\\pkgs\\python-3.7.4-h5263a28_0\\lib\\site-packages')
import pyperclip,re

if len(sys.argv) < 2:
    print('使い方: python pw.py [アカウント名]')
    print('パスワードをクリップボードにコピーします')
    sys.exit()

account = sys.grev[1] # 最初のコマンドライン引数がアカウント名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[accout])
    print(account + 'のパスワードをクリップボードにコピーしました')
else:
    print(account + 'というアカウントはありません')
