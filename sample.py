import random

print("🎮 数当てゲームを始めます！")
secret = random.randint(1, 100)
attempts = 0

while True:
    guess = input("1〜100の数字を入力してください: ")

    if not guess.isdigit():
        print("⚠️ 数字を入力してね！")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("🔼 もっと大きい数字だよ！")
    elif guess > secret:
        print("🔽 もっと小さい数字だよ！")
    else:
        print(f"🎉 正解！{attempts} 回で当たったよ！")
        break
