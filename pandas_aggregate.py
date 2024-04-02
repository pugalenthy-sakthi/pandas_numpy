import pandas as pd

data = {
  "x": [50, 40, 30],
  "y": [300, 1112, 42]
}

df = pd.DataFrame(data)

x = df.aggregate(["mean"])

print(x)