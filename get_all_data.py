import pandas as pd

def get(path):
    all_sheets = pd.read_excel(path, sheet_name=None)

    combined_df = (
        pd.concat(
            all_sheets.copy(),
            ignore_index=False
        )
        .reset_index(level=0)
        .rename(columns={'level_0': '城市'})
    )

    # print(combined_df)
    # print(combined_df.info())
    return combined_df

# print(get("./data/data.xlsx"))
