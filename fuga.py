import itertools
import datetime

#抵抗の数とリスト
R = [100,200,330,470,1000,4700,5600,10000,47000,100000]
N = len(R)
#時間図るためやつ
start = datetime.datetime.now()
#目標と答えを格納する箱
gool = 2021
ans = 0
ansco = ''
ansls = []


def anscomp(x,xc,xl):
    global ans,ansco,ansls
    if abs(gool-ans) > abs(gool-x):
        ans = x
        ansco = xc
        ansls = xl
        print(ans,ansls,ansco)

def series(l,foco,fols):
    for a in range(2**(len(l)-1)):
        co,ls = foco,fols
        a = '1' + '{:b}'.format(a).zfill(len(l)-1) + '1'
        d = []
        t = 0
        for e in range(len(a)-1):
            if a[e] == '1' and a[e+1] == '1':
                d.append(l[e])
            elif a[e+1] == '1':
                t += l[e]
                d.append(t)
                t = 0
            else:
                t += l[e]
        if len(d) > 1:
            parallel(d,co+[a],ls+[l])
        else:
            anscomp(d[0],co+[a],ls+[l])

def parallel(l,foco,fols):
    for a in range(2**(len(l)-1)):
        co,ls = foco,fols
        a = '1' + '{:b}'.format(a).zfill(len(l)-1) + '1'
        if not('0' in a):
            continue
        d = []
        t = 0
        for e in range(len(a)-1):
            if a[e] == '1' and a[e+1] == '1':
                d.append(l[e])
            elif a[e+1] == '1':
                t += 1/l[e]
                d.append(1/t)
                t = 0
            else:
                t += 1/l[e]
        if len(d) > 1:
            series(d,co+[a],ls+[l])
        else:
            anscomp(d[0],co+[a],ls+[l])

for i in range(3,N+1):
    print('------------------'+str(i)+'------------------')
    L = list(itertools.permutations(R,i))
    L = L[529977:]
    for l in L:
        series(l,[],[])

#出力
print(ans,ansls,ansco)
print(datetime.datetime.now()-start)
