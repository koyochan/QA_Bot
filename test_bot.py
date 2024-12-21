import re

# FAQデータ
faq_data = {
    "営業時間": "営業時間は平日9:00～18:00、土日は10:00～16:00です。",
    "学べる言語": "当スクールではPython、JavaScript、C++、Flutterを教えています。",
    "受講料": "月額50,000円からです。詳細はカリキュラムページをご確認ください。",
    "無料体験": "無料体験は随時受け付けています。こちらからお申し込みください: [リンク]",
    "申し込み方法": "当スクールの公式サイトからお申し込みいただけます。[リンク]",
}

def chatbot_response(user_input):
    # 入力に応じた応答を検索
    for keyword, response in faq_data.items():
        if re.search(keyword, user_input, re.IGNORECASE):
            return response
    return "申し訳ありません。その質問には現在お答えできません。"

# チャットボット開始
print("ボット: こんにちは！PCN Shibuyaプログラミングスクールです。ご質問をどうぞ！")
while True:
    user_input = input("ユーザー: ")
    if user_input.lower() in ["終了", "exit", "quit"]:
        print("ボット: ご利用ありがとうございました！またお会いしましょう。")
        break
    bot_response = chatbot_response(user_input)
    print(f"ボット: {bot_response}")