# IIDX Clear Ability Estimator

このプロジェクトは、IIDX（beatmania IIDX）のクリア能力を推定するためのものです。

## 環境設定

1.  **Pythonのインストール:**
    Python 3.x がインストールされていることを確認してください。インストールされていない場合は、[Pythonの公式サイト](https://www.python.org/downloads/) からダウンロードしてインストールしてください。

2.  **仮想環境の作成:**
    プロジェクトのディレクトリで仮想環境を作成します。

    ```bash
    python3 -m venv venv
    ```

3.  **仮想環境のアクティブ化:**
    作成した仮想環境をアクティブにします。

    ```bash
    source venv/bin/activate
    ```

4.  **依存関係のインストール:**
    `requirements.txt` ファイルを使用して、必要なライブラリをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

## 実行手順

1.  **データの準備:**
    *   `model_data.csv`: モデルデータ
    *   `new_examinee_data.csv`: 新しい被験者のデータ
    これらのCSVファイルがプロジェクトのルートディレクトリに存在することを確認してください。

2.  **クリア能力の推定:**
    `estimate_ability.py` スクリプトを実行して、クリア能力を推定します。

    ```bash
    python estimate_ability.py
    ```

3.  **サンプルデータの生成:**
    `generate_sample_data.py` スクリプトを実行して、サンプルデータを生成します。

    ```bash
    python generate_sample_data.py
    ```

## 注意事項

*   このプロジェクトを実行する前に、必要なデータファイルが揃っていることを確認してください。
*   仮想環境をアクティブにしてからスクリプトを実行してください。
