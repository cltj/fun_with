from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.read_csv("myfile.csv")
df = df[['quantity','meter_category','unit_price','resource_group']]
df['Amount'] = df.quantity * df.unit_price
df = df[['resource_group','Amount']]


sns.set_theme()
plt.xticks(rotation=45)
sns.barplot(data=df, x="resource_group", y="Amount")
plt.savefig('save_as_a_transparent2_png.png', transparent=True)