import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the emergency room visit data
df = pd.read_csv('emergency_room_visits.csv')

# Set up the Streamlit app
st.title('Emergency Room Visit Dashboard')

# Add filters
st.sidebar.header('Filters')
gender = st.sidebar.multiselect('Select Gender', df['gender'].unique(), default=df['gender'].unique())
triage_level = st.sidebar.multiselect('Select Triage Level', df['triage_level'].unique(), default=df['triage_level'].unique())
visit_reason = st.sidebar.multiselect('Select Visit Reason', df['visit_reason'].unique(), default=df['visit_reason'].unique())

# Filter the data based on user selections
filtered_df = df[(df['gender'].isin(gender)) & (df['triage_level'].isin(triage_level)) & (df['visit_reason'].isin(visit_reason))]

# Patient Age Distribution
st.subheader('Patient Age Distribution')
fig, ax = plt.subplots()
filtered_df['patient_age'].hist(bins=10, ax=ax)
ax.set_xlabel('Age')
ax.set_ylabel('Count')
st.pyplot(fig)

# Top Reasons for Emergency Room Visits
st.subheader('Top Reasons for Emergency Room Visits')
fig, ax = plt.subplots()
filtered_df['visit_reason'].value_counts().plot(kind='bar', ax=ax)
ax.set_xlabel('Visit Reason')
ax.set_ylabel('Count')
st.pyplot(fig)

# Average Wait Time by Triage Level
st.subheader('Average Wait Time by Triage Level')
fig, ax = plt.subplots()
filtered_df.groupby('triage_level')['wait_time_minutes'].mean().plot(kind='bar', ax=ax)
ax.set_xlabel('Triage Level')
ax.set_ylabel('Average Wait Time (minutes)')
st.pyplot(fig)

# Gender Distribution of Patients
st.subheader('Gender Distribution of Patients')
fig, ax = plt.subplots()
filtered_df['gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
ax.set_title('Gender Distribution')
st.pyplot(fig)

# Age vs Triage Level Relationship
st.subheader('Age vs Triage Level')
fig, ax = plt.subplots()
sns.boxplot(x='triage_level', y='patient_age', data=filtered_df, ax=ax)
ax.set_xlabel('Triage Level')
ax.set_ylabel('Patient Age')
st.pyplot(fig)
