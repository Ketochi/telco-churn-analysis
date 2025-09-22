import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ======================
# --- PreProcess ---
# ======================
path = 'file_path/name'
df = pd.read_csv(path)  # Load dataset
pd.set_option('display.max_columns', None)

# Handle missing/invalid values in TotalCharges
df['TotalCharges'] = df['TotalCharges'].str.strip()
df['TotalCharges'] = df['TotalCharges'].replace('', np.nan)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])
df['TotalCharges'] = df['TotalCharges'].fillna(df['TotalCharges'].median())



# ==============================
# --- Feature Engineering ---
# ==============================
categorical = df.select_dtypes(include=['object', 'category']).columns.drop('Churn')
numerical = df.select_dtypes(exclude=['object', 'category']).columns


df['TenureGroup'] = pd.cut(df['tenure'],bins=[-1,12,24,60,np.inf],labels=['0-1yr','1-2yrs','2-5yrs','5+yrs'])
df['Churn'] = df['Churn'].map({'No':0,'Yes':1})

gross_margin = 0.7
churn_threshold = 0.04 # from our training model we found that the 4% was the optimal threshold from a profit perspective

segments = df.groupby(['Contract', 'PaymentMethod', 'TenureGroup','SeniorCitizen'],observed=True).agg(
    customer = ('customerID','count'),
    churn_rate = ('Churn','mean'),
    avg_revenue = ('MonthlyCharges','mean'),
    avg_tenure = ('tenure','mean')
).reset_index()
segments['expected_ltv'] = segments['avg_revenue'] * segments['avg_tenure'] * gross_margin
value_threshold = segments['expected_ltv'].median()
segments['retention_ROI'] = segments['expected_ltv'] * (1-segments['churn_rate'])

# Define threshold splits (Segments)
segments['risk_level'] = np.where(segments['churn_rate']>= churn_threshold,'High Risk','Low Risk')
segments['value_level'] = np.where(segments['expected_ltv'] >= value_threshold,'High Value','Low Value')

# Classify Segments into Quadrants
segments['priority'] = segments['value_level']+'&'+segments['risk_level']

# Rank segments by business impact
segments['impact'] = segments['customer']*segments['expected_ltv']*segments['churn_rate']

# Higher impact = bigger risk of revenue loss if churn is not managed
segments = segments.sort_values(by='impact',ascending=False)


print('These are the top 10 segments within each impact based customer class')
fraction = segments.groupby('priority')
for val in segments['priority'].unique():
    print(fraction.get_group(val).head(10))
print('Churn Rate' )
print(segments['churn_rate'].mean())


plt.figure(figsize=(10,6))
ax = sns.barplot(data=segments, x='Contract', y='impact', hue='priority')
for container in ax.containers:
    ax.bar_label(container,fmt='%.2f',label_type='edge')
plt.title("Impact by Priority & Contract")
plt.show()


plt.figure(figsize=(10,6))
ax = sns.barplot(data=segments, x='PaymentMethod', y='impact', hue='priority')
for container in ax.containers:
    ax.bar_label(container,fmt='%.2f',label_type='edge')
plt.title("Impact by Priority & Payment Method")
plt.show()


plt.figure(figsize=(10,6))
ax = sns.barplot(data=segments, x='TenureGroup', y='impact', hue='priority')
for container in ax.containers:
    ax.bar_label(container,fmt='%.2f',label_type='edge')
plt.title("Impact by Priority & Tenure Group")
plt.show()



plt.figure(figsize=(10,6))
ax = sns.barplot(data=segments, x='SeniorCitizen', y='impact', hue='priority')
for container in ax.containers:
    ax.bar_label(container,fmt='%.2f',label_type='edge')
plt.title("Impact by Priority & Age")
plt.show()


plt.figure(figsize=(12,6))
sns.barplot(
    data=segments,
    x='Contract',
    y='impact',
    hue='risk_level',
    estimator=sum,

)

plt.title('Impact by Contract Type and Risk Level')
plt.ylabel('Total Impact')
plt.show()

impact_pivot = segments.pivot_table(
    values='expected_ltv',
    index='TenureGroup',
    columns='PaymentMethod',
    aggfunc='sum',
    fill_value=0,observed=False
)

plt.figure(figsize=(12,6))
sns.heatmap(impact_pivot, cmap='YlOrRd', annot=True, fmt='.0f')
plt.title('Impact Heatmap by Tenure & Payment Method')
plt.show()

plt.figure(figsize=(12,6))
plt.scatter(
    segments['expected_ltv'],
    segments['churn_rate'],
    s=segments['impact'] / 50,  # scale bubble size
    alpha=0.6,
    c=segments['impact'],
    cmap='viridis'
)

plt.xlabel('Expected LTV')
plt.ylabel('Churn Rate')
plt.title('Impact Bubble Chart (Size = Impact)')
plt.colorbar(label='Impact')
plt.show()


heatmap_churn = segments.pivot_table(index='Contract', columns='TenureGroup',values = 'expected_ltv',observed=False)
heatmap_ltv = segments.pivot_table(index='Contract', columns='PaymentMethod',values = 'expected_ltv',observed=False)
heatmap_age = segments.pivot_table(index='Contract', columns='SeniorCitizen',values = 'expected_ltv',observed=False)

plt.figure(figsize=(10,8))
sns.heatmap(data=heatmap_churn,cmap='coolwarm',annot=True,fmt='.2f')
plt.title('Heatmap of Life Time Value by Tenure and Contract')
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(data=heatmap_ltv,cmap='coolwarm',annot=True,fmt='.2f')
plt.title('Heatmap of Life Time Value by Payment Method and Contract')
plt.show()

plt.figure(figsize=(10,8))
sns.heatmap(data=heatmap_age,cmap='coolwarm',annot=True,fmt='.2f')
plt.title('Heatmap of Life Time Value by Age and Contract')
plt.show()




