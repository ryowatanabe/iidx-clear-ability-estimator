import pandas as pd
import numpy as np

# 既存のモデルデータを生成
np.random.seed(0)
model_data = pd.DataFrame({
    'song_id': range(1, 101),
    'difficulty': np.random.normal(0, 1, 100)
})
model_data.to_csv('model_data.csv', index=False)

# 新しい受験者データを生成
new_examinee_data = pd.DataFrame({
    'song_id': range(1, 101),
    'result': np.random.randint(0, 2, 100)
})
new_examinee_data.to_csv('new_examinee_data.csv', index=False)

# 新しい受験者データ(欠損値込み)を生成
new_examinee_data = pd.DataFrame({
    'song_id': range(1, 101),
    'result': np.random.randint(-1, 2, 100)
})
new_examinee_data.to_csv('new_examinee_data_with_absence.csv', index=False)

print('サンプルデータが生成されました。')