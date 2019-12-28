import os


# os.system('adb shell am start com.ss.android.article.news/com.ss.android.article.news.activity.MainActivity')

# os.system('adb shell input tap 100 100')

# os.system('adb shell input text "python"')
# os.system('adb shell input tap 650 100')
# os.system('adb shell input tap 600 200')

os.system('abd shell ime set com.android.adbkeyboard/.AdbIME')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'购物津贴200-20！轻松凑神单！【拍下立减2元，领.券再减1元，到手2.1元！~】当代流行的洗脸方式！天然好棉，干湿两用，不掉絮，无漂白剂，无荧光剂，亲肤柔软；哪里需要擦哪里~'))
os.system('adb shell input keyevent 66')

os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'-----------------'))
os.system('adb shell input keyevent 66')

os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'植护洗脸巾女一次性洁面巾棉柔巾家用清洁抽取式擦脸巾美容化妆棉'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'【原价】5.1元'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'【券后价】4.1元'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'【用花生日记再省】0.4元'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'-----------------'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'【注册邀请码】iwpu3v8'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'-----------------'))
os.system('adb shell input keyevent 66')
os.system('adb shell am broadcast -a ADB_INPUT_TEXT --es msg "{:s}"'.format(r'复製这条（qwooYOnWmpk）,进入【Tao宝】即可下单'))
os.system('adb shell input keyevent 66')

# os.system('adb shell input tap 100 480')

# os.system('adb shell input tap 360 720')