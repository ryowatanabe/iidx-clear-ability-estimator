# IIDX Clear Ability Estimator

beatmania IIDX ダブルプレイのクリア能力を推定するツールです。

ereter.net に登録されていない九段以下のプレイヤーや、PC版 (INFINITAS) のプレイヤーのクリア能力を可視化することを目的としています。

ereter.net のクリア能力計算アルゴリズムは公開されていませんが、項目応答理論 (IRT) の1PLモデルで難易度推定されたものと仮定して扱います。

## 要件

Python 3.x が必要です。

## 環境設定

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## データの準備

ereter.netの難易度表のデータは ./data/model_data.csv として用意されています。

自分のクリア状況を表す ./data/new_examinee_data.csv を作成してください。

new_examinee_data.csv は song_id と result の2カラムを持ちます。

- song_id
  - ereter.net の song_id とゲージ種別を組み合わせた文字列
    - EASY : {song_id}_ec
    - HARD : {song_id}_hc
    - EXHARD : {song_id}_exh
- result
  - クリア状況
    - 未プレイ : -1
    - 未クリア : 0
    - クリア : 1

## 実行

`estimate_ability.py` スクリプトを実行して、クリア能力を推定します。

```bash
python estimate_ability.py　./data/model_data.csv ./data/new_examinee_data.csv
```


