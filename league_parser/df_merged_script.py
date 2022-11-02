import pandas as pd
import os 

LANES = ["Top", "Jungle", "Mid", "Bot", "Support"]

final_df = pd.concat((pd.read_csv(f'df_{lane}.csv', index_col=0) for lane in LANES))

# for lane in LANES:
#     os.remove(f'df_{lane}.csv')
final_df = final_df.reset_index(drop=True)

final_df.to_csv("champion_stats.csv", index=False)
