import streamlit as st
from utility_cust import execute_query, fetch_query

def add_customer(customer_id, name, email, phone):
    query = "INSERT INTO customers (customer_id, name, email, phone) VALUES (%s, %s, %s, %s)"
    data = (customer_id, name, email, phone)
    execute_query(query, data)
    st.success("Customer added successfully!")

def view_customers():
    query = "SELECT * FROM customers"
    result = fetch_query(query)
    if result:
        st.write(result)
    else:
        st.write("No customers found.")

def update_customer(customer_id, name, email, phone):
    query = """
    UPDATE customers
    SET name = %s, email = %s, phone = %s
    WHERE customer_id = %s
    """
    data = (name, email, phone, customer_id)
    execute_query(query, data)
    st.success("Customer updated successfully!")

def delete_customer(customer_id):
    query = "DELETE FROM customers WHERE customer_id = %s"
    data = (customer_id,)
    execute_query(query, data)
    st.success("Customer deleted successfully!")

def main():
    st.title("Customer Management System")

    menu = ["Add Customer", "View Customers", "Update Customer", "Delete Customer"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Add Customer":
        st.subheader("Add New Customer")
        customer_id = st.text_input("Customer ID")
        name = st.text_input("Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        if st.button("Add Customer"):
            add_customer(customer_id, name, email, phone)

    elif choice == "View Customers":
        st.subheader("View All Customers")
        view_customers()

    elif choice == "Update Customer":
        st.subheader("Update Customer Details")
        customer_id = st.text_input("Customer ID")
        name = st.text_input("New Name")
        email = st.text_input("New Email")
        phone = st.text_input("New Phone")
        if st.button("Update Customer"):
            update_customer(customer_id, name, email, phone)

    elif choice == "Delete Customer":
        st.subheader("Delete Customer")
        customer_id = st.text_input("Customer ID")
        if st.button("Delete Customer"):
            delete_customer(customer_id)

if __name__ == "__main__":
    main()
