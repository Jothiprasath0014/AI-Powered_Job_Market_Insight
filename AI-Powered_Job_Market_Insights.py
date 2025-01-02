## AI-Powered Job Market Insights

### - Overview:

'''
The "AI-Powered Job Market Insights" dataset provides a synthetic but realistic snapshot of the modern job market, particularly focusing on the role of artificial intelligence (AI) 
and automation across various industries. This dataset includes 500 unique job listings, each characterized by different factors like industry, company size, 
AI adoption level, automation risk, required skills, and job growth projections. It is designed to be a valuable resource for researchers, data scientists, and
policymakers exploring the impact of AI on employment, job market trends, and the future of work.

'''

### Loading and Understanding the data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 

warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv(r"F:\Data Science (Analytics)\Pyhton\Pandas\ai_job_market_insights.csv")
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df
print("DataSet Info: \n")
df.info()

print("\n Columns of the Data Set: \n")
df.columns.to_list()
print("Preview of the top Dataset: \n")
df.head()


print("\n Preview of the Bottom Dataset: \n")
df.tail()
print("\n Statstics Summary: \n")
df.describe(include="all")
print("\n Categorical Data Columns : \n")
df.select_dtypes(include='object').columns.to_list()
print("\n Numerical Data Columns : \n")
df.select_dtypes(include='number').columns.to_list()
#### Cleaning Data
# Checking for the NUll Values

print("\n Missing Values : \n")
df.isna().sum()
# Checking for Duplicates

if df.duplicated().sum() > 0:
    df.drop_duplicates(inplace=True)
    print(f"Duplicates: {df.duplicated().sum()}\n Duplicates Droped \n data frame shape is: {df.shape}")
else:
    print(f"Duplicates: {df.duplicated().sum()}\n No changes done. \n data frame shape is: {df.shape}")

#### Analyzing The Data
# getting unique values for categorical columns

print("\n Unique values for the categorical columns: \n")

for cate_col in df.select_dtypes(include='object').columns:
    print(f"{cate_col} : {df[cate_col].nunique()} Unique Values") 
# getting unique values for Numerical columns

print("\n Unique values for the Numerical columns: \n")

for Num_col in df.select_dtypes(include='number').columns:
    print(f"{Num_col} : {df[Num_col].nunique()} Unique Values")
Count_of_job_title = df.groupby('Industry')['Job_Title'].nunique()
Count_of_job_title

# Salary Distribution by Industry

plt.figure(figsize=(20, 10))
sns.boxplot(data=df, x='Industry', y='Salary_USD', palette='muted', hue='AI_Adoption_Level')
plt.xticks(rotation=45)
plt.title("Salary Distribution by Industry with AI_Adoption_Level")
plt.xlabel("Industry")
plt.ylabel("Salary_USD")
plt.show()


# Salary Distribution by Job_Title

plt.figure(figsize=(20, 10))
sns.boxplot(data=df, x='Job_Title', y='Salary_USD', hue='AI_Adoption_Level', palette='coolwarm')
plt.title("Salary Distribution by Job_title with AI_Adoption_Level")
plt.xlabel("Job_Title")
plt.ylabel("Salary")
plt.show()
# Salary Distribution by AI Adoption Levels

plt.figure(figsize=(20, 10))
sns.boxplot(data=df, x='AI_Adoption_Level', y='Salary_USD', palette='Set2')
plt.title("Salary Distribution by the AI_Adoption_Level with Company size")
plt.show()
# Remote friendly Jobs by salary

plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Remote_Friendly', y='Salary_USD')
plt.title("Remote-Friendly Jobs by salary")
plt.show()
# Distribution of Remote-Friendly

clr = plt.get_cmap('Pastel1_r').colors

df['Remote_Friendly'].value_counts().plot(kind='pie', startangle = 20, autopct = '%1.1f%%', figsize=(20, 8), 
                                          title='Distribution of Remote_Friendly', explode = (0.08, 0), shadow = True, colors = clr)
plt.show()
#  Job Growth Projection by Location

plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Location', hue='Job_Growth_Projection', palette='viridis')
plt.xticks(rotation=45)
plt.title("Job Growth Projection by Location")
plt.ylabel("No of Jobs")
plt.show()
#### Correlations
# Correlations between Salary, AI-Adoption-Level and Automation-Risk

# Encoding Categorical values to numbers for correlate.

encoded_data = df.copy()
encoded_data['AI_Adoption_Level'] = encoded_data['AI_Adoption_Level'].map({'Low': 1, 'Medium': 2, 'High': 3})
encoded_data['Automation_Risk'] = encoded_data['Automation_Risk'].map({'Low': 1, 'Medium': 2, 'High': 3})

corrrelation_Matrix = encoded_data[['Salary_USD', 'AI_Adoption_Level', 'Automation_Risk']].corr() # Correlating
# corrrelation_Matrix

# Heatmap visual for better Understanding

plt.figure(figsize=(12, 6))
sns.heatmap(corrrelation_Matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation between Salary_USD, AI_Adoption_Level and Automation_Risk")
plt.tight_layout()
plt.show()
# Skills Demanded in High-Growth Jobs

high_growth_jobs = df[df['Job_Growth_Projection'] == 'Growth'] # filtering the growth jobs

skills_demand = high_growth_jobs['Required_Skills'].value_counts()
skills_demand

# visualizing the required skills for high-growth jobs

plt.figure(figsize=(12, 6))
sns.barplot(x=skills_demand.values, y= skills_demand.index, hue= skills_demand.index, palette='mako')
plt.title("Skills Demanded in High growth Jobs")
plt.xlabel("No of Jobs")
plt.show()
# Skill Requirements

all_skills = [skills for subskill in df['Required_Skills'] for skills in subskill]
skill_count = pd.Series(all_skills).value_counts()
top_skill = skill_count.head(10)

# skills by Job_Title

grp_df = df.groupby('Job_Title')
count_by_role = grp_df['Required_Skills'].apply(lambda x : pd.Series(x).value_counts())

count_by_role
df.groupby(['Required_Skills', 'Job_Title']).size().unstack()
# Count of Job Titles

plt.figure(figsize=(12, 6))
sns.countplot(data= df, y='Job_Title', order=df['Job_Title'].value_counts().index, palette='mako')
plt.show()
# Job Counts by Location 

df.groupby('Job_Title')['Location'].value_counts().unstack()
# Automation-Risk 

df.groupby(['Automation_Risk', 'Job_Title']).size().unstack()
df.groupby(['Automation_Risk', 'Industry']).size().unstack()
df.groupby(['Automation_Risk', 'Location']).size().unstack()
