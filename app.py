import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load and preprocess the data
df = pd.read_csv('selected_columns.csv')

# Preprocess the data
label_encoders = {}
categorical_columns = ['Marital_status', 'Application_mode', 'Course', 'Daytime_evening_attendance', 
                       'Scholarship_holder']

for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column].astype(str))
    label_encoders[column] = le

# Define the features and target
X = df.drop(columns=['Status'])
y = df['Status']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Define column name mapping for display
column_name_mapping = {
    'Marital_status': 'Marital Status',
    'Application_mode': 'Application Mode',
    'Course': 'Course',
    'Daytime_evening_attendance': 'Daytime/Evening Attendance',
    'Scholarship_holder': 'Scholarship Holder'
}

# Define mapping for marital status codes
marital_status_mapping = {
    1: 'single',
    2: 'married',
    3: 'widower',
    4: 'divorced',
    5: 'facto union',
    6: 'legally separated'
}

# Define mapping for application mode codes
application_mode_mapping = {
    1: '1st phase - general contingent',
    2: 'Ordinance No. 612/93',
    5: '1st phase - special contingent (Azores Island)',
    7: 'Holders of other higher courses',
    10: 'Ordinance No. 854-B/99',
    15: 'International student (bachelor)',
    16: '1st phase - special contingent (Madeira Island)',
    17: '2nd phase - general contingent',
    18: '3rd phase - general contingent',
    26: 'Ordinance No. 533-A/99, item b2) (Different Plan)',
    27: 'Ordinance No. 533-A/99, item b3 (Other Institution)',
    39: 'Over 23 years old',
    42: 'Transfer',
    43: 'Change of course',
    44: 'Technological specialization diploma holders',
    51: 'Change of institution/course',
    53: 'Short cycle diploma holders',
    57: 'Change of institution/course (International)'
}

# Define mapping for Daytime/Evening Attendance
attendance_mapping = {
    1: 'daytime',
    0: 'evening'
}

# Define mapping for Scholarship Holder
scholarship_holder_mapping = {
    1: 'yes',
    0: 'no'
}

# Define mapping for Course
course_mapping = {
    33: 'Biofuel Production Technologies',
    171: 'Animation and Multimedia Design',
    8014: 'Social Service (evening attendance)',
    9003: 'Agronomy',
    9070: 'Communication Design',
    9085: 'Veterinary Nursing',
    9119: 'Informatics Engineering',
    9130: 'Equinculture',
    9147: 'Management',
    9238: 'Social Service',
    9254: 'Tourism',
    9500: 'Nursing',
    9556: 'Oral Hygiene',
    9670: 'Advertising and Marketing Management',
    9773: 'Journalism and Communication',
    9853: 'Basic Education',
    9991: 'Management (evening attendance)'
}

# Streamlit app
st.title("Dropout Prediction Prototype")

st.sidebar.header("Student Information")

def user_input_features():
    marital_status = st.sidebar.selectbox(column_name_mapping['Marital_status'], list(marital_status_mapping.values()))
    application_mode = st.sidebar.selectbox(column_name_mapping['Application_mode'], list(application_mode_mapping.values()))
    course = st.sidebar.selectbox(column_name_mapping['Course'], list(course_mapping.values()))
    attendance = st.sidebar.selectbox(column_name_mapping['Daytime_evening_attendance'], list(attendance_mapping.values()))
    scholarship_holder = st.sidebar.selectbox(column_name_mapping['Scholarship_holder'], list(scholarship_holder_mapping.values()))
    
    data = {
        'Marital_status': list(marital_status_mapping.keys())[list(marital_status_mapping.values()).index(marital_status)],
        'Application_mode': list(application_mode_mapping.keys())[list(application_mode_mapping.values()).index(application_mode)],
        'Course': list(course_mapping.keys())[list(course_mapping.values()).index(course)],
        'Daytime_evening_attendance': list(attendance_mapping.keys())[list(attendance_mapping.values()).index(attendance)],
        'Scholarship_holder': list(scholarship_holder_mapping.keys())[list(scholarship_holder_mapping.values()).index(scholarship_holder)],
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Ensure input_df columns are in the same order as the training data
input_df = input_df[X_train.columns]

st.subheader('User Input parameters')

# Display user input with column names replaced for better readability
display_input_df = input_df.copy()
display_input_df.columns = [column_name_mapping[col] for col in display_input_df.columns]
display_input_df['Marital Status'] = display_input_df['Marital Status'].map(marital_status_mapping)
display_input_df['Application Mode'] = display_input_df['Application Mode'].map(application_mode_mapping)
display_input_df['Daytime/Evening Attendance'] = display_input_df['Daytime/Evening Attendance'].map(attendance_mapping)
display_input_df['Scholarship Holder'] = display_input_df['Scholarship Holder'].map(scholarship_holder_mapping)
display_input_df['Course'] = display_input_df['Course'].map(course_mapping)
st.write(display_input_df)

# Predict dropout
prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')
dropout_labels = ['No', 'Yes']

st.write("Prediction:", prediction)
st.write("Prediction Index:", prediction[0])

if isinstance(prediction[0], int):
    st.write(dropout_labels[prediction[0]])
else:
    st.write("Unexpected prediction value:", prediction[0])

st.subheader('Prediction Probability')

# Define label for each class
class_labels = {
    0: 'Enroll',
    1: 'Dropout',
    2: 'Graduate'
}

# Create DataFrame for prediction probabilities with descriptive column names
prediction_proba_df = pd.DataFrame(prediction_proba, columns=[class_labels[i] for i in range(prediction_proba.shape[1])])
st.write(prediction_proba_df)
