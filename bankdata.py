import streamlit as st
import json
import os

DATA_FILE = "bank_data.json"

# --------------------------
# Utility functions
# --------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --------------------------
# Core Operations
# --------------------------
def add_account(data, name, pin, balance):
    if name in data:
        return f"⚠ Account for '{name}' already exists!"
    data[name] = {
        "account_holder": name,
        "pin": pin,
        "balance": balance
    }
    save_data(data)
    return f"✅ Account for {name} added successfully!"

def update_account(data, name, new_pin=None, new_balance=None):
    if name not in data:
        return f"❌ No account found for '{name}'"
    if new_pin:
        data[name]["pin"] = new_pin
    if new_balance is not None:
        data[name]["balance"] = new_balance
    save_data(data)
    return f"✅ Account for '{name}' updated successfully!"

def delete_account(data, name):
    if name not in data:
        return f"❌ Account for '{name}' not found!"
    del data[name]
    save_data(data)
    return f"🗑 Account for '{name}' deleted successfully!"

# --------------------------
# Streamlit UI
# --------------------------
st.title("🏦 Bank Account Management System")
st.write("Manage your bank accounts with add, update, delete, and view options.")

data = load_data()
menu = st.sidebar.selectbox("Select Action", ["Add Account", "Update Account", "Delete Account", "View All Accounts"])

# ADD ACCOUNT
if menu == "Add Account":
    st.subheader("➕ Add New Account")
    name = st.text_input("Enter account holder name").strip()
    pin = st.text_input("Enter 4-digit PIN", type="password")
    balance = st.number_input("Enter initial balance", min_value=0.0, step=100.0)

    if st.button("Create Account"):
        if name and pin:
            msg = add_account(data, name, pin, balance)
            st.success(msg)
        else:
            st.warning("Please enter all required fields!")

# UPDATE ACCOUNT
elif menu == "Update Account":
    st.subheader("🔄 Update Account Details")
    name = st.text_input("Enter existing account holder name").strip()
    new_pin = st.text_input("Enter new PIN (optional)", type="password")
    new_balance = st.number_input("Enter new balance (optional)", min_value=0.0, step=100.0)

    if st.button("Update"):
        if name:
            msg = update_account(data, name, new_pin if new_pin else None,
                                 new_balance if new_balance > 0 else None)
            st.success(msg)
        else:
            st.warning("Please enter an account name!")

# DELETE ACCOUNT
elif menu == "Delete Account":
    st.subheader("🗑 Delete Account")
    name = st.text_input("Enter account holder name to delete").strip()

    if st.button("Delete"):
        if name:
            msg = delete_account(data, name)
            st.warning(msg)
        else:
            st.warning("Please enter an account name!")

# VIEW ALL ACCOUNTS
elif menu == "View All Accounts":
    st.subheader("📋 All Account Details")
    if data:
        for acc, details in data.items():
            st.write(f"👤 *Name:* {details['account_holder']}")
            st.write(f"🔐 *PIN:* {details['pin']}")
            st.write(f"💰 *Balance:* ₹{details['balance']}")
            st.write("---")
    else:
        st.info("No accounts found.")