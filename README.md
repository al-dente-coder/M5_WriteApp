# M5 用書き込みアプリ

## 概要
PlatformIO を用いて M5Stack にプログラムをアップロードする際、  
**Web アプリ（Streamlit）上で入力した値をビルド時に取り込み、  
その値を使ってコンパイルおよび書き込みを行う**ことを目的として作成しました。

---

## 使い方

### 1. `platformio.ini` の設定
`m5project` フォルダ内にある `platformio.ini` を開き、以下の設定を追加します。

`-D` と `=` の後に指定した文字列は、**M5 側のプログラムでグローバルマクロ（定数）として使用できます**。

```ini
build_flags =
    -DUSER_NAME=\"${sysenv.USER_NAME}\"
```

### 2. streamlitの設定
入力項目の数や内容を変更した場合は、以下の箇所を修正してください。
環境変数名は、手順 1 で設定したマクロ名と一致させる必要があります。
```python
env["USER_NAME"] = user_name
```
```python
name = st.text_input("名前を入力してください")
```

### 3. 書き込み
以下のコマンドで Streamlit を起動し、Web 画面上で情報を入力後、書き込みを実行します。
```powershell
.venv\Scripts\activate # 仮想環境を使う場合
streamlit run app.py
```
