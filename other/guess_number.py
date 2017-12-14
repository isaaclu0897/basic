import random

correct_number = random.randint(1, 1001)
min_number, max_number = 1, 1000
print('猜猜看我心裡在想什麼數字吧~')
while True:
    while True:
        print('輸入 1 個 {}~{} 之間的數字：'.format(min_number, max_number), end='')
        try:
            guess_number = int(input())
            if not (max_number >= guess_number >= min_number):
                raise ValueError()
            break
        except ValueError:
            print('只能輸入介於 {}~{} 之間的數字唷～！'.format(min_number, max_number))
    if guess_number == correct_number:
        print('恭喜你猜對了，正確數字是 {}，獎品是什麼都沒有～～'.format(correct_number))
        break
    elif guess_number > correct_number:
        max_number = guess_number
        print('好像猜太大囉，再小一點！')
    elif guess_number < correct_number:
        min_number = guess_number
        print('數字沒那麼小，再大一點！')
