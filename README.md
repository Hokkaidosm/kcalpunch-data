# kcalpunch-data

「[500キロカロリーパンチチャレンジ](https://500kcalpunch.hokkaidosm.net/)」（←構築中）などの「xキロカロリーパンチチャレンジ」で使用するメニューデータのレポジトリです。

## リポジトリ構造

* kcalpunch-data
  * .github -- GitHubで使用するActionsやIssuesのテンプレート
  * checker -- JSONデータのチェックを行うコード群
    * checker.py -- チェック用のスクリプト
  * schema -- JSONデータのスキーマ
    * v1.json -- 現行のスキーマ
  * ここに各メニューのJSONファイルを置きます
 
 ## 各メニューのJSONファイルの構造
 
 ☆最新のスキーマファイルと併せて確認してください
 
 * $schema -- スキーマの設定　必ず `./schema/v1.json` を指定してください
 * name -- データタイトル。「○○でxキロカロリーパンチチャレンジ」の「○○」で使用します
 * date -- メニュー基準日。このファイルを作るのに参照したメニューの参照日を入力します
 * menus -- メニューデータの配列
   * name -- メニュー名。**同じファイル内での重複はできません**。同じメニュー名でカロリー設定が異なる場合はカテゴリを付するなど区別が必要です
   * calories -- 主に「エネルギー」欄に記載されているカロリーを **「キロカロリー」単位で**記載します
 
 ## 作業手順
 
 1. 【推奨】あらかじめIssuesにIssueが立っていないことを確認します
 2. 【推奨】作業の重複を防ぐためIssueを立てます（テンプレート「メニューの追加・更新」をご利用ください）
 3. ファイル名を決めます。ファイル名の「.json」を除いた部分が、パスに該当します（ mcdonalds.json→https://500kcalpunch.hokkaidosm.net/mcdonalds ）
   * 次のファイル名は、システムの都合上使用できません
     * data.json
     * schema.json
     * misc.json
     * static.json
     * private.json
     * include.json
     * sitepolicy.json
   * また、ファイル名には「半角英数字」「-」「\_」のみが使用できます
 4.  上の「各メニューのJSONファイルの構造」に従ってJSONファイルを作ります
 5.  【推奨】ルートフォルダで `python ./checker/checker.py` を実行して、JSONチェッカーを走らせます
 6.  問題がなければPRを作成します
   * 作成時に、 `close !(2で作成したIssueの番号)` を説明に入れておくと、PRのマージ時に自動的にIssueが閉じられます
   * このときに↑のチェッカーが走ります
 7.  PRを当方で確認し、問題がなければマージします（マージ後、Web側をこちらで更新します）
