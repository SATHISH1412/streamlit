import streamlit as st

# Function to check login credentials (Replace this with your own authentication mechanism)
def authenticate(username, password):
    # Replace this with your authentication logic, e.g., check against a database
    return username == "abc" and password == "abc"

# Function to create login page
def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")
    
    if login_button:
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            return True
        else:
            st.error("Invalid credentials. Please try again.")
    return False

# Function to create subsequent pages
def page_one():
    st.title("Page One")
    st.write("This is page one content.")
    
def page_two():
    st.title("Page Two")
    st.write("This is page two content.")
    
def page_three():
    st.title("Page Three")
    st.write("This is page three content.")


# Main function to run the app
def main():
    st.set_page_config(page_title="Multi-Page Streamlit App", layout="centered")
    
    # Check if user is logged in
    is_authenticated = login_page()
    
    # Proceed to other pages if logged in
    if is_authenticated:
        page_selection = st.sidebar.radio("Go to:", ("Page One", "Page Two", "Page Three"))

        if page_selection == "Page One":
            page_one()
        elif page_selection == "Page Two":
            page_two()
        elif page_selection == "Page Three":
            page_three()

if __name__ == "__main__":
    main()
