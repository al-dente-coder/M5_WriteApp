import html
import os
import subprocess

import streamlit as st

st.title("名前入力")

name = st.text_input("名前を入力してください")


def run_upload(m5_project_path, user_name):
    """
    引数で受け取った値を環境変数やオプション経由でM5に渡して、書き込みを行う

    :param user_name: ユーザ名
    :param m5_project_path: m5に書き込みたいプログラムの名前
    :param age: 年齢(入力は任意)
    """
    # 引数を環境変数に登録
    env = os.environ.copy()
    env["USER_NAME"] = user_name
    cmd = ["pio", "run", "-d", str(m5_project_path)]
    # 書き込みの為のオプションを追加
    cmd.extend(["-t", "upload"])

    return cmd, subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env,
    )


def render_log(output_box, lines):
    """
    書き込み中に受け取ったメッセージをを画面に表示するための関数
    """
    escaped = html.escape("\n".join(lines))
    log_html = f"""
    <div style="
        height:320px;
        overflow-y:scroll;
        padding:8px;
        background-color:#0f172a;
        color:#e2e8f0;
        font-family:monospace;
        border-radius:4px;
        border:1px solid #1f2937;
        white-space:pre-wrap;
    ">{escaped}</div>
    """
    output_box.markdown(log_html, unsafe_allow_html=True)


# app
if st.button("書き込み"):
    if name.strip():
        # m5への書き込み
        cmd, process = run_upload(m5_project_path="m5project", user_name=name)
        # 書き込み中のメッセージを表示
        lines = []
        assert process.stdout is not None  # 空でないことを確認
        # ログ出力エリア
        output_box = st.empty()
        for line in process.stdout:
            line = line.rstrip("\n")
            lines.append(line)
            render_log(output_box, lines)
    else:
        st.warning("名前を入力してください。")
