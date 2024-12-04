import pandas as pd

df = pd.DataFrame(
    {
        "a": list("abc"),
        "b": list("def"),
        "c": list("aaa"),
    }
)
print(df.apply(lambda row: set(x for x in row if not pd.isna(x)), axis=1))
