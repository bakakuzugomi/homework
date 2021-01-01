# 結果

2021.0001854612124958264700753047

# 100年かかるプログラム

このプログラムで馬鹿正直にすべての組み合わせ方を試した場合100年かかる計算になりました。

このアルゴリズムでは隣同士を並列にするか判定を行っているため 10,20,30,40 と 40,10,20,30 の抵抗の並びでは別の答えが出ます。

例として、

10,20,30,40 では隣同士の抵抗 30,40 を並列にすることができますが 40,10,20,30 では 30,40 は隣同士ではないため並列にすることができません。

また、抵抗の並び方の数は (使う抵抗の数)!個あります。

一つの並びの抵抗の、直列並列の組み合わせを全て試す時、かかる時間は

python

| 使用する抵抗の数 | 実行時間 |
| :---: | :---: |
| 7 | 0.2 s |
| 8 | 3.1 s |
| 9 | 51.3 s |
| 10 | 960.0 s |

このようになります。

よって抵抗10個の場合、計算時間は 10! * 960s = 3483648000s = 110年 かかります。

### 意味わからん

そんなに留年するのは嫌なので、適当に抵抗の並び方を選んで結果の誤差が一番低い物を提出したいと思います。

今年の運をここで使おうと思います。

# アルゴリズムについて

このプログラムでは相互再帰とbit全探索を使っています。

主に3つの関数からできています。

## 結果を比較する関数 anscomp
```
def anscomp(x):
    global ans
    if abs(gool-ans) > abs(gool-x):
        ans = x
        print(ans)
```

これは名の通り引数に計算した抵抗値を受け取り誤差が小さい時答えを書き換えるだけです。

## 直列接続を決める関数 series

これは抵抗を直列接続するかどうかをbit全探索で決める関数です。

抵抗並びのリストを受け取りその間に1か0を入れ1で囲われている部分を直列接続します。

### 例

    [10,20,30,40]             #入力された抵抗値

    [1,10,1,20,1,30,0,40,1]   #抵抗の間に1か0を入れる
    
    [10,20,70]                #1で囲われている30と40を直列接続

そうして得られたリストを次の処理(parallel)に送ります。

```
def series(l):
    for a in range(2**(len(l)-1)):
        a = '1' + '{:b}'.format(a).zfill(len(l)-1) + '1'
        d = []　 #出力する配列を格納する
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
        if len(d) == 1:    #リストに抵抗が一つしかないなら答えと比較
            anscomp(d[0])
        else:              #並列処理へ
            parallel(d)
```

## 並列接続を決める関数 parallel

これはseries関数の並列版です。

1で囲われている部分を並列にしているだけです。

一つ違うところは並列接続するところがなければcontinueすることです。

この処理のおかげで抵抗のリストはだんだんと少なくなっていきます。

```
def parallel(l,foco,fols):
    for a in range(2**(len(l)-1)):
        a = '1' + '{:b}'.format(a).zfill(len(l)-1) + '1'
        if not('0' in a):       #ここが少し違う
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
        if len(d) == 1:
            anscomp(d[0])
        else:       #直列処理へ
            series(d)
```

## 他

この二つの関数が相互再帰することで抵抗が一つの値に収束します。

また、実際のコードでは接続の順番を保持するため少し変数が増えています。

# 感想

こんなに時間がかかるとは思わなかった。

均衡接続は考慮できなかった。

コード書くのは楽しかった。

もっとメモ化とかで効率よくできそうだけど技術力が足らなかった。ちくしょうめ。

是非実行してみてください。
