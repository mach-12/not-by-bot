import streamlit as st
import random

def is_ai_generated(content):
    return random.choice([True, False])

def get_probability():
    return round(random.uniform(0.7, 1.0), 2)

def main():
    st.title("Not-By-Bot App")

    content = st.text_area("Enter your content:")

    if st.button("Check"):
        is_ai = is_ai_generated(content)
        probability = get_probability()

        if is_ai:
            st.markdown(f'<p style="color:red">AI Generated</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="color:green">Human Content</p>', unsafe_allow_html=True)

        st.write(f"Probability: {probability}")

if __name__ == "__main__":
    main()
