while True:
    while True:
        try:
            height = input('請輸入身高(cm)：')
            height = int(height)
            if not 200 > height > 140:
                print('我不相信')
                continue
            height /= 100
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
    while True:
        try:
            weight = input('請輸入體重(kg)：')
            weight = int(weight)
            if not 110 > weight > 30:
                print('我不相信')
                continue
            break
        except ValueError:
            print('輸入格式錯誤')
            continue
    bmi = weight / height**2
    print('你的BMI為%.1f:' % bmi, end='')
    if bmi > 24:
        print('好像有點過重，為了健康，最好多運動唷～～')
    elif bmi > 18.5:
        print('維持的不錯嘛，差我一點')
    else:
        print('輕到快被風吹走啦，還不多吃一點～！')
    if input('是否繼續(Y/N)：').upper() != 'Y':
        break
