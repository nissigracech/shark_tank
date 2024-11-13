import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load the dataset from the same directory
df = pd.read_csv("dataset.csv")

# Function to get the top 5 brands per shark based on investment
def top_brands_per_shark(shark_column, amount_column):
    shark_investments = df[df[shark_column] > 0][['brand_name', amount_column]]
    top_brands = shark_investments.sort_values(by=amount_column, ascending=False).head(5)
    return top_brands

# Streamlit application
st.title("Top 5 Brands per Shark by Investment Amount")

# Dictionary for shark columns
sharks = {
    "Ashneer": "ashneer_deal",
    "Anupam": "anupam_deal",
    "Aman": "aman_deal",
    "Namita": "namita_deal",
    "Vineeta": "vineeta_deal",
    "Peyush": "peyush_deal",
    "Ghazal": "ghazal_deal"
}

# Loop through each shark and display top 5 brands
for shark, column in sharks.items():
    st.subheader(f"Top 5 Brands for {shark}")
    top_brands = top_brands_per_shark(column, 'deal_amount')
    st.dataframe(top_brands)

    # Plotting
    fig, ax = plt.subplots()
    sns.barplot(data=top_brands, x='brand_name', y='deal_amount', ax=ax)
    ax.set_title(f"Top 5 Brands for {shark} by Investment Amount")
    st.pyplot(fig)
