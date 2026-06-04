import streamlit as st
import time

# ページの設定：layoutを"wide"にして横幅を最大化します
st.set_page_config(page_title="転倒予防「ながら」エクササイズ", page_icon="🏃‍♂️", layout="wide")

# --- セッション状態（アプリの記憶）の初期化 ---
if "step" not in st.session_state:
    st.session_state.step = "menu"
if "difficulty" not in st.session_state:
    st.session_state.difficulty = None
if "evaluation" not in st.session_state:
    st.session_state.evaluation = ""

# --- タイトル表示 ---
st.title("🏃‍♂️ 転倒予防！「ながら」エクササイズ【トライアル版】")
st.write("要支援高齢者向けのバランス＆脳トレアプリ（全6ステージ）")
st.markdown("---")

# ==========================================
# ステップ1：難易度選択メニュー画面
# ==========================================
if st.session_state.step == "menu":
    st.markdown("### 🌟 挑戦する難易度を選んでください")
    st.write("ご自身の体調に合わせて、無理のないレベルから始めましょう。")
    
    if st.button("🟢 難易度 E（易しい：座って足踏み ＋ ランダムじゃんけん）", use_container_width=True):
        st.session_state.difficulty = "E"
        st.session_state.step = "safety_check"
        st.rerun()
        
    if st.button("🟡 難易度 D（やや易：立ったまま ＋ 赤マークで拍手）", use_container_width=True):
        st.session_state.difficulty = "D"
        st.session_state.step = "safety_check"
        st.rerun()
        
    if st.button("🟠 難易度 C（ふつう：立ったまま足踏み ＋ 3の倍数で拍手）", use_container_width=True):
        st.session_state.difficulty = "C"
        st.session_state.step = "safety_check"
        st.rerun()

    if st.button("🔴 難易度 B（やや難：立ったまま足踏み ＋ 3の倍数で拍手【難しい】）", use_container_width=True):
        st.session_state.difficulty = "B"
        st.session_state.step = "safety_check"
        st.rerun()

    if st.button("🟣 難易度 A（難しい：片脚立ち（支持あり） ＋ 言葉の逆唱）", use_container_width=True):
        st.session_state.difficulty = "A"
        st.session_state.step = "safety_check"
        st.rerun()

    if st.button("⚫ 難易度 S（超難しい：片脚立ち（支持あり） ＋ 後出し負けじゃんけん）", use_container_width=True):
        st.session_state.difficulty = "S"
        st.session_state.step = "safety_check"
        st.rerun()

# ==========================================
# ステップ2：安全確認画面
# ==========================================
elif st.session_state.step == "safety_check":
    st.warning("⚠️ トレーニングを始める前の安全確認")
    
    if st.session_state.difficulty == "E":
        st.write("今回は【座った姿勢】で行います。背もたれのある安定した椅子に深く腰掛け、周りにぶつかる物がないか確認してください。")
    elif st.session_state.difficulty in ["A", "S"]:
        st.write("今回は【片脚立ち（支持あり）】を行います。必ず【椅子の背もたれや頑丈な手すり】の横に立ち、いつでも掴まれる準備をしてください。")
    else:
        st.write("今回は【立った姿勢】で行います。周りに掴まれる『椅子』や『手すり』はありますか？足元に物が散らばっていませんか？")
        
    ready = st.checkbox("はい、安全な環境が準備できました。")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("メニューに戻る", use_container_width=True):
            st.session_state.step = "menu"
            st.rerun()
    with col2:
        if st.button("ルール説明へ進む", disabled=not ready, type="primary", use_container_width=True):
            st.session_state.step = "training_ready"
            st.rerun()

# ==========================================
# ステップ3：ルール説明画面（全難易度別）
# ==========================================
elif st.session_state.step == "training_ready":
    st.info("💡 ルール説明")
    
    if st.session_state.difficulty == "E":
        st.subheader("メニュー：座位足踏みじゃんけん")
        st.markdown("""
        1. 椅子に深く座り、自分のペースでトントンと**足踏み**を始めてください。
        2. 画面に **「✊・✌️・✋」** がランダムに表示されます。
        3. 画面の手に対して、声を出して**「勝つ手」**をポンポン出してください！
        """)
    elif st.session_state.difficulty == "D":
        st.subheader("メニュー：ストップ＆ゴー")
        st.markdown("""
        1. 椅子の横に**まっすぐ立って**姿勢をキキープしてください（不安なら手を添えて）。
        2. 画面のマークが **「キープ（緑）」** の間は動かずじっとします。
        3. マークが **「👏手を叩く（赤）」** に変わったら、その場で1回拍手してください！
        """)
    elif st.session_state.difficulty == "C":
        st.subheader("メニュー：ナンバー・クラップ")
        st.markdown("""
        1. 椅子の後ろに立ち、いつでも掴まれるようにして**足踏み**を始めてください。
        2. 画面に**1から15までの数字が順番に**表示されます。
        3. 数字が **3の倍数（3, 6, 9, 12, 15）** かどうかを頭で計算し、3の倍数の瞬間だけ**手を1回叩いて**ください！
        4. 画面の案内は変化しません。自分の頭の計算だけが頼りです！
        """)
    elif st.session_state.difficulty == "B":
        st.subheader("メニュー：ナンバー・クラップ【難しい】")
        st.markdown("""
        1. 椅子の後ろに立ち、いつでも掴まれるようにして**足踏み**を始めてください。
        2. 画面に **1から20までの数字が「ランダム（バラバラ）」に** 表示されます！
        3. 画面にパッと出た数字が **3の倍数（3, 6, 9, 12, 15, 18）** だったら、素早く**手を1回叩いて**ください！
        4. 文字のヒントや背景色はバラバラに変わるので、惑わされずに数字をよく計算しましょう！
        """)
    elif st.session_state.difficulty == "A":
        st.subheader("メニュー：リバース＆ストレート・ワード")
        st.markdown("""
        1. **片手で椅子をしっかり掴み**、どちらかの足を上げて**片脚立ち**になります。
        2. 画面の指示（そのまま読む、または逆から読む）に合わせて、表示された単語を声に出します。
        3. ルールが途中で変わるので、騙されないように声を出し、バランスをキープしてください！
        """)
    elif st.session_state.difficulty == "S":
        st.subheader("メニュー：片脚立ち・後出し負けじゃんけん")
        st.markdown("""
        1. **片手で椅子をしっかり掴み**、どちらかの足を上げて**片脚立ち**になります。
        2. 画面に **「✊・✌️・✋」** がランダムに表示されます。
        3. 画面の手に対して、声を出して**「わざと負ける手」**を素早く出してください！
        4. 脳が大混乱しますが、足元のバランスが崩れないように集中しましょう！
        """)
        
    if st.button("スタート！", type="primary", use_container_width=True):
        st.session_state.step = "training_running"
        st.rerun()

# ==========================================
# ステップ4：トレーニング実行画面（全画面・超巨大化仕様）
# ==========================================
elif st.session_state.step == "training_running":
    placeholder = st.empty()
    
    # 共通で使用するランダム背景色リスト
    import random
    colors = [
        {"bg": "#ff4b4b", "text": "white"},   # 赤
        {"bg": "#f0f2f6", "text": "#31333F"}, # 白
        {"bg": "#2b82d6", "text": "white"},   # 青
        {"bg": "#2bd677", "text": "white"}    # 緑
    ]
    
    # --- 難易度E：座位足踏み・ランダムじゃんけん ---
    if st.session_state.difficulty == "E":
        janken_options = [
            {"name": "グー", "emoji": "✊"},
            {"name": "チョキ", "emoji": "✌️"},
            {"name": "パー", "emoji": "✋"}
        ]
        for i in range(10):
            current_hand = random.choice(janken_options)
            with placeholder.container():
                st.markdown(f"<div style='text-align: center; background-color: #2b82d6; padding: 80px 20px; border-radius: 15px; width: 100%;'>"
                            f"<h1 style='color: white; font-size: 50px; margin: 0 0 30px 0;'>座って足踏みしながら【勝つ手】を出して！</h1>"
                            f"<div style='font-size: 160px; line-height: 1.2;'>{current_hand['emoji']}</div>"
                            f"<h1 style='color: white; font-size: 90px; margin: 20px 0 0 0;'>{current_hand['name']}</h1>"
                            f"</div>", unsafe_allow_html=True)
                time.sleep(2.0)
                
    # --- 難易度D：ストップ＆ゴー ---
    elif st.session_state.difficulty == "D":
        commands = ["🟢 キープ", "🟢 キープ", "👏手を叩く！", "🟢 キープ", "🟢 キープ", "👏手を叩く！", "🟢 キープ", "👏手を叩く！", "🟢 キープ", "🟢 キープ", "👏手を叩く！"]
        for cmd_text in commands:
            with placeholder.container():
                bg_color = "#ff4b4b" if "手を叩く" in cmd_text else "#2bd677"
                st.markdown(f"<div style='text-align: center; background-color: {bg_color}; padding: 130px 20px; border-radius: 15px; width: 100%;'>"
                            f"<div style='font-size: 130px; color: white; font-weight: bold; line-height: 1.2;'>{cmd_text}</div>"
                            f"<h1 style='color: white; font-size: 50px; margin: 40px 0 0 0;'>まっすぐ立つ姿勢</h1>"
                            f"</div>", unsafe_allow_html=True)
                time.sleep(1.3)

    # --- 難易度C：ナンバー・クラップ（順番通り・文字ヒント排除仕様） ---
    elif st.session_state.difficulty == "C":
        for i in range(1, 16):
            current_color = random.choice(colors)
            with placeholder.container():
                # 3の倍数かどうかにかかわらず、下部の文字指示は常に固定して脳に計算させます
                st.markdown(f"<div style='text-align: center; background-color: {current_color['bg']}; padding: 100px 20px; border-radius: 15px; width: 100%;'>"
                            f"<div style='font-size: 160px; color: {current_color['text']}; line-height: 1.2;'>{i}</div>"
                            f"<h1 style='color: {current_color['text']}; font-size: 60px; margin: 30px 0 0 0;'>⚠️ 3の倍数なら手を叩く！</h1>"
                            f"</div>", unsafe_allow_html=True)
                time.sleep(1.0)

    # --- 難易度B：ナンバー・クラップ【難しい】（ランダム数字・文字ヒント排除仕様） ---
    elif st.session_state.difficulty == "B":
        random_numbers = random.sample(range(1, 21), 15)
        
        for num in random_numbers:
            current_color = random.choice(colors)
            with placeholder.container():
                # 文字での「手を叩く！」「足踏みキープ」というヒントを完全に無くし、常に同じ警告を表示します
                st.markdown(f"<div style='text-align: center; background-color: {current_color['bg']}; padding: 100px 20px; border-radius: 15px; width: 100%;'>"
                            f"<div style='font-size: 160px; color: {current_color['text']}; line-height: 1.2;'>{num}</div>"
                            f"<h1 style='color: {current_color['text']}; font-size: 60px; margin: 30px 0 0 0;'>⚠️ 3の倍数なら手を叩く！</h1>"
                            f"</div>", unsafe_allow_html=True)
                time.sleep(1.2)

    # --- 難易度A：リバース＆ストレート・ワード ---
    elif st.session_state.difficulty == "A":
        words = ["さくら", "たぬき", "めだか", "すいか", "おてだま", "きつね", "ひこうき"]
        mode_options = ["ストレート", "リバース"]
        chosen_words = random.sample(words, 5) if len(words) >= 5 else words
        
        for word in chosen_words:
            current_mode = random.choice(mode_options)
            if current_mode == "ストレート":
                title_text = "✨ そのまま声に出して！ ✨"
                bg_color = "#2bd677"
            else:
                title_text = "🔥 逆から声に出して！ 🔥"
                bg_color = "#ffaa00"
                
            for countdown in range(3, 0, -1):
                with placeholder.container():
                    st.markdown(f"<div style='text-align: center; background-color: {bg_color}; padding: 80px 20px; border-radius: 15px; width: 100%;'>"
                                f"<h1 style='color: white; font-size: 50px; margin: 0 0 20px 0;'>{title_text}</h1>"
                                f"<div style='font-size: 120px; color: white; font-weight: bold; line-height: 1.2;'>{word}</div>"
                                f"<h1 style='color: white; font-size: 45px; margin: 30px 0 0 0;'>次の問題まで あと {countdown} 秒</h1>"
                                f"</div>", unsafe_allow_html=True)
                time.sleep(1.1)

    # --- 難易度S：片脚立ち・後出し負けじゃんけん ---
    elif st.session_state.difficulty == "S":
        janken_options = [
            {"name": "グー", "emoji": "✊"},
            {"name": "チョキ", "emoji": "✌️"},
            {"name": "パー", "emoji": "✋"}
        ]
        for i in range(8):
            current_hand = random.choice(janken_options)
            for countdown in range(3, 0, -1):
                with placeholder.container():
                    st.markdown(f"<div style='text-align: center; background-color: #d62b2b; padding: 80px 20px; border-radius: 15px; width: 100%;'>"
                                f"<h1 style='color: white; font-size: 50px; margin: 0 0 30px 0;'>⚠️ わざと【負ける手】を出して！ ⚠️</h1>"
                                f"<div style='font-size: 150px; line-height: 1.2;'>{current_hand['emoji']}</div>"
                                f"<h1 style='color: white; font-size: 70px; margin: 10px 0 20px 0;'>{current_hand['name']}</h1>"
                                f"<h1 style='color: white; font-size: 45px; margin: 0;'>片脚立ちをキープ！ あと {countdown} 秒</h1>"
                                f"</div>", unsafe_allow_html=True)
                time.sleep(1.0)
                
    # 全モード共通の終了画面
    with placeholder.container():
        st.markdown("<div style='text-align: center; background-color: #f0f2f6; padding: 15px 20px; border-radius: 15px; width: 100%;'><div style='font-size: 150px; font-weight: bold; color: #31333F;'>終了！</div></div>", unsafe_allow_html=True)
        time.sleep(1.2)
                
    st.session_state.step = "result_input"
    st.rerun()

# ==========================================
# ステップ5：結果入力画面
# ==========================================
elif st.session_state.step == "result_input":
    st.success("🎉 お疲れ様でした！トレーニング終了です。")
    st.write("ご自身のバランスや課題の出来栄えはどうでしたか？")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("完璧にできた！", use_container_width=True):
            st.session_state.evaluation = "🥇 素晴らしい！完璧です！この調子で脳と体の若々しさを保ちましょう！"
            st.session_state.step = "show_evaluation"
            st.rerun()
    with col2:
        if st.button("少しふらついた・間違えた", use_container_width=True):
            st.session_state.evaluation = "🥈 惜しい！良いトレーニングになりましたね。無理せず安全第一で続けましょう。"
            st.session_state.step = "show_evaluation"
            st.rerun()
    with col3:
        if st.button("難しかった", use_container_width=True):
            st.session_state.evaluation = "🥉 挑戦したことが素晴らしいです！次はもう一つ下の難易度で、のんびり練習してみませんか？"
            st.session_state.step = "show_evaluation"
            st.rerun()

# ==========================================
# ステップ6：最終判定・再挑戦画面
# ==========================================
elif st.session_state.step == "show_evaluation":
    st.balloons()
    st.markdown(f"### 今日の判定\n{st.session_state.evaluation}")
    
    if st.button("メニュー（難易度選択）に戻る", use_container_width=True):
        st.session_state.step = "menu"
        st.session_state.difficulty = None
        st.rerun()