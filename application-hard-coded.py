import pandas as pd

data = pd.read_csv('/Users/jackhobhouse/Expiring-Subscriptions.csv')

data.sort_values("id", inplace = True)

data.drop_duplicates(subset ="id",
                     keep = 'first', inplace = True)



data.to_csv("/Users/jackhobhouse/Expiring-Subscriptions-6.csv", index=False)
