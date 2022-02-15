# -*- coding: utf-8 -*-
import glob
import json
import os
import re
from jsonschema import validate, ValidationError

# 禁止ファイル
prohibited_file_names = ["data.json", "schema.json", "misc.json", "static.json", "private.json", "include.json", "sitepolicy.json"]
# ファイル名パターン
file_name_pattern = "^[0-9a-zA-Z\-_]+\.json$"
file_name_p = re.compile(file_name_pattern)

files = glob.glob("./*.json")

success = True

for file in files:
    print("============================")
    file_name = os.path.basename(file)
    print(file_name)
    file_success = True

    # ファイル名が、禁止ファイル名になっているか？
    for prohibited_file_name in prohibited_file_names:
        if prohibited_file_name == file_name:
            print(u"ファイル名が禁止ファイル名になっています。禁止ファイル名：" + ', '.join(prohibited_file_names))
            success = False
            file_success = False
    if not(file_success):
        continue
    
    # ファイル名が、パターン通りか？
    match = file_name_p.match(file_name)
    if match is None:
        print(u"ファイル名パターンに一致しません。パターン：" + file_name_pattern)
        success = False
        file_success = False
    if not(file_success):
        continue

    # ファイルを読み込んで確認する
    with open(file) as f:
        df = json.load(f)
        schema_file_path = df["$schema"]
        with open(schema_file_path) as sf:
            # スキーマチェック
            schema = json.load(sf)
            try:
                validate(df, schema)
            except ValidationError as e:
                print(e)
                success = False
                file_success = False
        if not(file_success):
            continue
        # 重複チェック
        menu_name_list = []
        for menu in df["menus"]:
            menu_name_list.append(menu["name"])
        dup = [x for x in set(menu_name_list) if menu_name_list.count(x) > 1]
        if len(dup) >= 1:
            # 重複あり
            print(u"メニューに重複があります：" + ', '.join(dup))
            success = False
            file_success = False
        if not(file_success):
            continue

# 終了処理
print("============================")
if not(success):
    exit(1)
else:
    exit(0)