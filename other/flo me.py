# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 14:09:13 2017

@author: VX
"""
import numpy as np
# import math
g = 9.807
T = 50 #(oC)
D = 20 #(cm)
V = 3  #(m/s)
Ep = 0 #()
pi = 3.1415926

print ('ex8-5')
print ('由題目得知，溫度={}(oC), 直徑={}(cm), 速度={}(m/s), 粗糙度={}(x)\n'.format(T, D, V, Ep))

print ('1. 求圓相關數值')
print ('  (1) 求 雷諾數(Re)')
print ('      "公式 : Re = (Rho * V * D) / Mu = (V * D) / mu"')
print ('      雖然我們不知道 mu,但因為 T = 50(oC),所以 mu查表可得 1.76e-5(m^2 / s),代回 Reyode number公式')
mu = 1.76e-5 # mu常數
Re = (V * (D / 100)) / mu # Reyode number公式
print ('      Re = ({}(m/s) * {}(m)) / {}(m^2/s) = {:.0f} (x)\n'.format(V, D/100, mu, Re))

print ('  (2) 求 摩擦因子(f)')
print ('      "公式 : 1 / squart(f) = -1.8 log(((Ep / D) / 3.7) ^ 1.11 + 6.9 / Re)"')
f = 1 / (-1.8 * np.log10(((Ep / (10 * D)) / 3.7) ** 1.11 + (6.9 / Re))) ** 2 # 摩擦公式
print ('      f = 1 / (-1.8 * log10((({} / (10 * {})) / 3.7) ^ 1.11 + (6.9 / {:.0f}))) ** 2 = {:.5f}(x)'.format(Ep, D, Re, f))
print ()

print ('  (3) 求 單位管長頭損(hf/l)')
print ('      "公式 : hf / l = f * (1 / D) * (V ^ 2 / 2 g)"')
hfpl = f * (1 / (0.01 * D)) * (V ** 2 / (2 * g)) # 管長損失公式
print ('      hf / l = {:.5f} * (1 / {}) * ({} ^ 2 / 2g) = {:.4f}'.format(f, D/100, V, hfpl))
print ()

print ('2. 推至方管數值')
print ('   我們發現方程式未知數個數過多無法計算，但發現其方程式是可以循環得解的，因次我們使用疊代法')
print ()

a1 = float(input('請輸入您想開始逼近的值 : ')) # 逼近數(使用者自訂)
a2 = 0 
index = 1 # 索引

# 疊代
while np.abs(((a1-a2)/a1))>0.01: # 誤差精度，若疊代精度不夠，則繼續循環下去
    
    # 當趨近的值相等時，提早跳出循環，避免計算機過多疊代
    if not a1==a2: # 可解決溢值問題
        # a1, a2 = math.floor(a1 * (10 ** 10)) / (10 ** 10), math.floor(a2 * (10 ** 10))/(10 ** 10) # 找到了靠
        # 公式區
        a1, a2 = round(a1 * (10 ** 10)) / (10 ** 10), round(a2 * (10 ** 10)) / (10 ** 10)
        Dh = (4 * np.square(a1)) / (4 * a1)
        Vh = (pi * np.square(0.01 * D) * 3 / 4)/ np.square(a1)
        Reh = (Vh * Dh) / mu
        fh = 1 / np.square(-1.8 * np.log10(((Ep / (10 * Dh)) / 3.7) ** 1.11 + (6.9 / Reh)))
        a2 = (fh * np.square(0.03 * pi) / (hfpl * 2 * g)) ** (1 / 5)
        
        # 打印區
        print ('   第{}次疊代'.format(index))
        print ('   {:<5} = {:<12.10f} (m)'.format('old_a', a1))
        print ('   {:<5} = {:<12.4f} (m)'.format('Dh', Dh))
        print ('   {:<5} = {:<12.3f} (m/s)'.format('Vh', Vh))
        print ('   {:<5} = {:<12.0f} (x)'.format('Reh', Reh))
        print ('   {:<5} = {:<12.5f} (x)'.format('fh', fh))
        print ('   {:<5} = {:<12.10f} (m)'.format('new_a', a2))
        print ()
        
        # 記步 及 趨近
        index += 1
        a1, a2 = round(a2, 10), round(a1, 10) # 把四捨五入加在這就不會溢值，加在if 沒用
        # a1, a2 = math.floor(a2*(10**10))/(10**10), math.floor(a1*(10**10))/(10**10) # 若有四捨六入五留雙問題用無條間消去法

print ('在最後的疊代我們得知 {:.4f}(m)是我們的答案'.format(a1))

# 清除變數
del(D, Dh, Ep, Re, Reh, T, V, Vh, f, fh, g, hfpl, mu, pi)







