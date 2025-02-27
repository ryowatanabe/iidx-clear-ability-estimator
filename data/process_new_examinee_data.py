import csv
import argparse

def process_csv(input_file):
    """
    CSVファイルを読み込み、指定された形式でデータを出力する。
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            print("question_id,response")  # ヘッダー行の出力
            for row in reader:
                song_id = row['song_id']
                ec = row['ec']
                hc = row['hc']
                exh = row['exh']

                print(f"{song_id}_ec,{ec}")
                print(f"{song_id}_hc,{hc}")
                print(f"{song_id}_exh,{exh}")

    except FileNotFoundError:
        print(f"エラー：ファイル '{input_file}' が見つかりません。")
    except Exception as e:
        print(f"エラー：CSVファイルの処理中にエラーが発生しました：{e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSVファイルを読み込んで処理し、指定された形式でデータを出力する。")
    parser.add_argument("input_file", help="入力CSVファイル名")
    args = parser.parse_args()

    process_csv(args.input_file)
