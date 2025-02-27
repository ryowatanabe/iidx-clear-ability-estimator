import numpy as np
import pandas as pd

def estimate_ability(model_data_path, examinee_data_path):
    """
    項目応答理論 (IRT) の手法を用いて、新規受験者の能力推定を行う。

    Args:
        model_data_path (str): 既存モデルデータのCSVファイルのパス。
        examinee_data_path (str): 新規受験者の正誤データのCSVファイルのパス。

    Returns:
        float: 推定された受験者の能力パラメータ。
    """
    # CSVファイルを読み込む
    model_data = pd.read_csv(model_data_path)
    examinee_data = pd.read_csv(examinee_data_path)
    examinee_data['result'] = examinee_data['result'].replace(-1, np.nan)

    # 既存モデルデータと受験者データを結合する
    merged_data = pd.merge(model_data, examinee_data, on='song_id')

    # 困難度パラメータと正誤データをnumpy配列に変換する
    difficulty = merged_data['difficulty'].values
    result = merged_data['result'].values

    # 能力パラメータの初期値を設定する
    theta = 0.0

    # ニュートン法を用いて、尤度関数を最大化する
    for i in range(100):  # 最大100回繰り返す
        # 尤度関数とその導関数を計算する
        p = 1.0 / (1.0 + np.exp(-(theta - difficulty)))
        log_likelihood = np.nansum(result * np.log(p) + (1 - result) * np.log(1 - p))
        dlog_likelihood = np.nansum(result - p)
        d2log_likelihood = -np.nansum(p * (1 - p))

        # パラメータを更新する
        theta = theta - dlog_likelihood / d2log_likelihood

        # 収束判定
        if np.abs(dlog_likelihood) < 0.001:
            break

    return theta

if __name__ == "__main__":
    # コマンドライン引数からファイルパスを取得する
    import sys
    if len(sys.argv) != 3:
        print("Usage: python estimate_ability.py model_data.csv new_examinee_data.csv")
        sys.exit(1)

    model_data_path = sys.argv[1]
    examinee_data_path = sys.argv[2]

    # 能力を推定する
    ability = estimate_ability(model_data_path, examinee_data_path)

    # 結果を出力する
    print(f"推定された能力: {ability}")
