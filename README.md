# IIDX Clear Ability Estimator

beatmania IIDX ダブルプレイのクリア能力を推定するツールです。

[ereter.net](http://ereter.net/) を利用することができない九段以下のプレイヤーや、PC版 (INFINITAS) のプレイヤーのクリア能力を可視化することを目的としています。

[ereter.net](http://ereter.net/) のクリア能力計算アルゴリズムは公開されていませんが、項目応答理論 (IRT) の1PLモデルで難易度推定されたものと仮定して扱います。

## 要件

Python 3.x が必要です。

## 環境設定

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## データの準備

[ereter.net](http://ereter.net/) の難易度表のデータは `./data/model_data.csv` として用意されています。(ときどき更新します)

自分のクリア状況を表す `./data/new_examinee_data.csv` を用意してください。

`new_examinee_data.csv` は `song_id` と `result` の2カラムを持ちます。

- song_id
  - [ereter.net](http://ereter.net/) の song_id とゲージ種別を組み合わせた文字列
    - EASY : {song_id}_ec
    - HARD : {song_id}_hc
    - EXHARD : {song_id}_exh
- result
  - クリア状況
    - 未プレイ : -1
    - 未クリア : 0
    - クリア : 1

もっと一覧性のある形で管理したい場合、別の形式から変換して利用することもできます。

`song_id`, `ec`, `hc`, `exh` の4カラムを持つ csv ファイルを用意してください。この4つ以外のカラムは処理の上では無視されますので、曲名や難易度など管理上都合のよいカラムがあれば自由に追加してもかまいません。ファイル例としては `./data/clear_ability.csv` を参照してください。

- song_id
  - [ereter.net](http://ereter.net/) の song_id
- ec
  - EASY クリア状態
    - 未プレイ : -1
    - 未クリア : 0
    - クリア : 1
- hc
  - HARD クリア状態
  - 値の意味は ec と同様です
  - 実際にハードゲージで挑戦したことがあるかどうかに関わらず、他ゲージでプレイ済で未ハードであれば 0 (未クリア) としてください
- exh
  - EXHARD クリア状態
  - 値の意味は ec, hc と同様です
  - 実際にエクハゲージで挑戦したことがあるかどうかに関わらず、他ゲージでプレイ済で未エクハであれば 0 (未クリア) としてください

このようなファイルが用意されていれば、`process_new_examinee_data.py` スクリプトを利用して、`new_examinee_data.csv` を生成できます。

```bash
python process_new_examinee_data.py clear_ability.csv > new_examinee_data.csv
```

## 実行

`estimate_ability.py` スクリプトを実行して、クリア能力を推定します。

```bash
python estimate_ability.py ./data/model_data.csv ./data/new_examinee_data.csv
```


