import streamlit as st

# Function to set background from a URL
def set_background_url(image_url):
    css = f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the page config
st.set_page_config(layout="wide")

# Use any direct image URL here
image_url = "https://images.unsplash.com/photo-1506744038136-46273834b3fb"  # Replace with your desired image URL
set_background_url(image_url)

# Add some test content
st.title("Streamlit App with Online Background Image")
st.write("This background image is loaded from a URL.")
