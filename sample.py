import tkinter as tk
import random

# ランダムな秘密の数字を生成
secret = random.randint(1, 100)

def check_guess():
    global secret
    guess = entry.get()
    if not guess.isdigit():
        result_label.config(text="⚠️ 数字を入力してね！")
        return

    guess = int(guess)
    if guess < secret:
        result_label.config(text="🔼 もっと大きいよ！")
    elif guess > secret:
        result_label.config(text="🔽 もっと小さいよ！")
    else:
        result_label.config(text="🎉 正解！もう一回遊ぶ？")
        secret = random.randint(1, 100)  # 新しい数字を設定

# ウィンドウ作成
root = tk.Tk()
root.title("数当てゲーム")
root.geometry("300x200")

# ラベルと入力欄
label = tk.Label(root, text="1〜100の数字を入力してね")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack()

# 結果表示
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# ボタン
button = tk.Button(root, text="チェック！", command=check_guess)
button.pack()

# ウィンドウ開始
root.mainloop()
