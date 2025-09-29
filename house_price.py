"""import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('house_prices.csv')


# Encode location
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])  # City=0, Town=1, Village=2

# Features & target
X = df[['Location', 'Area', 'BHK']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title('🏠 House Price Prediction App')

# Inputs
location = st.selectbox('Select Location', ['City', 'Town', 'Village'])
area = st.number_input('Enter Area (in sqft):', min_value=500, max_value=5000, step=50)
bhk = st.number_input('Enter BHK:', min_value=1, max_value=10, step=1)

# Predict button
if st.button('Predict Price'):
    loc_value = le.transform([location])[0]
    prediction = model.predict([[loc_value, area, bhk]])[0]
    st.success(f'Predicted House Price: ₹ {prediction:,.0f}')

# Show dataset
st.subheader('📋 Dataset Preview')
st.dataframe(df)

# Visualization
st.subheader('📊 Price vs Area')
fig, ax = plt.subplots()
scatter = ax.scatter(df['Area'], df['Price'], c=df['Location'], cmap='viridis')
ax.set_xlabel('Area (sqft)')
ax.set_ylabel('Price (₹)')
st.pyplot(fig)
"""


"""import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


# Load dataset
df = pd.read_csv('house_prices.csv')

# Encode location
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])  # City=0, Town=1, Village=2

# Features & target
X = df[['Location', 'Area', 'BHK']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.title('🏠 House Price Prediction App')

# Create session_state dataframe for storing predictions
if 'predictions' not in st.session_state:
    st.session_state.predictions = pd.DataFrame(columns=['Location','Area','BHK','Predicted Price'])

# Inputs
location = st.selectbox('Select Location', ['City', 'Town', 'Village'])
area = st.number_input('Enter Area (in sqft):', min_value=500, max_value=5000, step=50)
bhk = st.number_input('Enter BHK:', min_value=1, max_value=10, step=1)

# Predict Button
if st.button('Predict Price'):
    loc_value = le.transform([location])[0]
    predicted_price = model.predict([[loc_value, area, bhk]])[0]
    
    # Append prediction to session_state dataframe
    new_row = pd.DataFrame({
        'Location': [location],
        'Area': [area],
        'BHK': [bhk],
        'Predicted Price': [f'₹ {predicted_price:,.0f}']
    })
    st.session_state.predictions = pd.concat([st.session_state.predictions, new_row], ignore_index=True)
    
    st.success(f'Predicted House Price: ₹ {predicted_price:,.0f}')

# Show Predictions Preview
st.subheader("💡 Predictions Preview")
st.dataframe(st.session_state.predictions)

# Show dataset
st.subheader('📋 Dataset Preview')
st.dataframe(df)

# Visualization
st.subheader('📊 Price vs Area')
fig, ax = plt.subplots()
scatter = ax.scatter(df['Area'], df['Price'], c=df['Location'], cmap='viridis')
ax.set_xlabel('Area (sqft)')
ax.set_ylabel('Price (₹)')
st.pyplot(fig)
"""

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# ===== Custom CSS for styling =====
st.markdown(
    """
    <style>
    /* Full app background */
    .stApp {
        background-color: #f7f7f7;  /* light grey */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333333;
    }

    /* Main title style */
    .stTitle {
        color: #1a1a1a;
        font-size: 36px;
        font-weight: bold;
        text-align: center;
    }

    /* Subheaders */
    .stSubheader {
        color: #1f4e79;
        font-size: 24px;
        font-weight: bold;
    }

    /* Dataframe style */
    .dataframe, .stDataFrame {
        background-color: #ffffff; /* white background */
        border: 1px solid #cccccc;
        border-radius: 5px;
    }

    /* Streamlit button */
    div.stButton > button:first-child {
        background-color: #1f4e79;
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        padding: 8px 18px;
        margin: 5px 0;
    }
    div.stButton > button:first-child:hover {
        background-color: #14406c;
        color: white;
    }

    /* Inputs */
    .stNumberInput, .stSelectbox {
        border-radius: 5px;
    }

    /* Chart background */
    .stPlotlyChart, .stImage {
        background-color: #f7f7f7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== Load dataset =====
df = pd.read_csv('house_prices.csv')

# Encode location
le = LabelEncoder()
df['Location'] = le.fit_transform(df['Location'])

# Features & target
X = df[['Location', 'Area', 'BHK']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# ===== Streamlit UI =====
st.title('🏠 House Price Prediction App')

# Session state for storing predictions
if 'predictions' not in st.session_state:
    st.session_state.predictions = pd.DataFrame(columns=['Location','Area','BHK','Predicted Price'])

# Inputs
location = st.selectbox('Select Location', ['City', 'Town', 'Village'])
area = st.number_input('Enter Area (in sqft):', min_value=500, max_value=5000, step=50)
bhk = st.number_input('Enter BHK:', min_value=1, max_value=10, step=1)

# Predict Button
if st.button('Predict Price'):
    loc_value = le.transform([location])[0]
    predicted_price = model.predict([[loc_value, area, bhk]])[0]
    
    # Append new prediction
    new_row = pd.DataFrame({
        'Location': [location],
        'Area': [area],
        'BHK': [bhk],
        'Predicted Price': [f'₹ {predicted_price:,.0f}']
    })
    st.session_state.predictions = pd.concat([st.session_state.predictions, new_row], ignore_index=True)
    
    st.success(f'Predicted House Price: ₹ {predicted_price:,.0f}')

# ===== Predictions Preview =====
st.subheader("💡 Predictions Preview")
st.dataframe(st.session_state.predictions)

# ===== Dataset Preview =====
st.subheader('📋 Dataset Preview')
st.dataframe(df)

# ===== Visualization =====
st.subheader('📊 Price vs Area')
fig, ax = plt.subplots()
scatter = ax.scatter(df['Area'], df['Price'], c=df['Location'], cmap='viridis', s=80, alpha=0.7, edgecolors='k')
ax.set_xlabel('Area (sqft)', fontsize=14)
ax.set_ylabel('Price (₹)', fontsize=14)
ax.set_title('House Price vs Area', fontsize=16, fontweight='bold')
st.pyplot(fig)
