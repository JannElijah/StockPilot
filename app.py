import streamlit as st
import pandas as pd
import qrcode
import altair as alt
from io import BytesIO
from supabase import create_client, Client
import time

# ==============================================================================
# 1. SETUP & THEME CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="StockPilot Pro", 
    page_icon="🚀", 
    layout="wide",
    initial_sidebar_state="collapsed" # Collapsed by default for login screen
)

# Custom CSS for a Modern "Dark Glass" Look
st.markdown("""
<style>
    .stApp { background-color: #0e1117; }
    div[data-testid="metric-container"] {
        background-color: #262730;
        border: 1px solid #464b5f;
        padding: 15px 25px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        transition: transform 0.2s;
    }
    div[data-testid="metric-container"]:hover {
        transform: scale(1.02);
        border-color: #ff4b4b;
    }
    .stButton>button { border-radius: 20px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 2. SECURITY SYSTEM
# ==============================================================================
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def check_password():
    """Simple password protection for the app."""
    if st.session_state.authenticated:
        return True
        
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("## 🔒 Access Restricted")
        st.info("Please sign in to access the StockPilot Database.")
        password = st.text_input("Admin Password", type="password")
        
        if st.button("Login", type="primary"):
            # Verify against secrets
            if password == st.secrets["ADMIN_PASSWORD"]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ Incorrect Password")
    return False

# STOP EXECUTION IF NOT LOGGED IN
if not check_password():
    st.stop()

# ==============================================================================
# 3. APP LOGIC (Only runs after login)
# ==============================================================================

# Connect to Supabase
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
except Exception:
    st.error("⚠️ Database connection failed. Check .streamlit/secrets.toml")
    st.stop()

# --- HELPER FUNCTIONS ---
def fetch_data():
    response = supabase.table("inventory").select("*").execute()
    df = pd.DataFrame(response.data)
    if not df.empty:
        df = df.sort_values(by="id")
    return df

def add_item(name, category, price, quantity):
    try:
        supabase.table("inventory").insert({
            "name": name, "category": category, "price": price, "quantity": quantity
        }).execute()
        return True
    except Exception as e:
        return str(e)

def update_item(id, name, category, price, quantity):
    try:
        supabase.table("inventory").update({
            "name": name, "category": category, "price": price, "quantity": quantity
        }).eq("id", id).execute()
        return True
    except Exception as e:
        return str(e)

def delete_item(id):
    try:
        supabase.table("inventory").delete().eq("id", id).execute()
        return True
    except Exception as e:
        return str(e)

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#000000", back_color="#ffffff")
    buf = BytesIO()
    img.save(buf)
    return buf.getvalue()

# --- SIDEBAR ---
with st.sidebar:
    st.title("🚀 StockPilot")
    st.caption(f"Logged in as Admin")
    
    if st.button("🔒 Logout"):
        st.session_state.authenticated = False
        st.rerun()
        
    st.divider()
    menu = st.radio("Navigate", ["Dashboard", "Inventory", "Manage Items"])
    st.divider()
    st.info("💡 Pro Tip: Download CSVs for weekly reports.")

# --- DASHBOARD PAGE ---
if menu == "Dashboard":
    st.header("📊 Executive Overview")
    df = fetch_data()
    
    if df.empty:
        st.warning("Inventory is empty.")
    else:
        # Metrics
        c1, c2, c3, c4 = st.columns(4)
        total_val = (df['price'] * df['quantity']).sum()
        c1.metric("Total SKUs", len(df))
        c2.metric("Low Stock", len(df[df['quantity'] < 10]), delta_color="inverse")
        c3.metric("Asset Value", f"${total_val:,.2f}")
        c4.metric("Avg Price", f"${df['price'].mean():,.2f}")
        
        st.divider()
        
        # Charts Row
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            st.subheader("📦 Stock Levels")
            bar_chart = alt.Chart(df).mark_bar().encode(
                x=alt.X('name', sort='-y', title='Product'),
                y=alt.Y('quantity'),
                color='category',
                tooltip=['name', 'price', 'quantity']
            ).properties(height=300)
            st.altair_chart(bar_chart, use_container_width=True)
            
        with col_chart2:
            st.subheader("💰 Value Distribution")
            # Calculate value per category
            df['total_value'] = df['price'] * df['quantity']
            pie_chart = alt.Chart(df).mark_arc(innerRadius=50).encode(
                theta=alt.Theta(field="total_value", type="quantitative"),
                color=alt.Color(field="category", type="nominal"),
                tooltip=['category', 'total_value']
            ).properties(height=300)
            st.altair_chart(pie_chart, use_container_width=True)

# --- INVENTORY PAGE ---
elif menu == "Inventory":
    st.header("📦 Live Inventory")
    df = fetch_data()
    if not df.empty:
        search = st.text_input("🔍 Search...", placeholder="Product name...")
        if search:
            df = df[df['name'].str.contains(search, case=False)]
            
        max_qty = int(df['quantity'].max()) if not df.empty else 100
        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True,
            column_config={
                "price": st.column_config.NumberColumn(format="$%.2f"),
                "quantity": st.column_config.ProgressColumn(
                    "Stock", format="%d", min_value=0, max_value=max_qty
                ),
                "created_at": st.column_config.DatetimeColumn(format="D MMM YYYY")
            }
        )
    else:
        st.info("No items found.")

# --- MANAGE ITEMS PAGE ---
elif menu == "Manage Items":
    st.header("🛠️ Operations")
    tab1, tab2, tab3 = st.tabs(["Add", "Edit", "Delete"])
    df = fetch_data()
    
    with tab1:
        with st.form("new"):
            c1, c2 = st.columns(2)
            n_name = c1.text_input("Name")
            n_cat = c2.selectbox("Category", ["Electronics", "Clothing", "Home", "Food", "Other"])
            c3, c4 = st.columns(2)
            n_price = c3.number_input("Price", 0.01)
            n_qty = c4.number_input("Qty", 1)
            if st.form_submit_button("Save", type="primary"):
                if add_item(n_name, n_cat, n_price, n_qty):
                    st.toast("Saved!")
                    time.sleep(1)
                    st.rerun()
                    
    with tab2:
        if not df.empty:
            edit_id = st.selectbox("Edit Item", df['id'])
            row = df[df['id'] == edit_id].iloc[0]
            with st.form("edit"):
                c1, c2 = st.columns(2)
                e_name = c1.text_input("Name", row['name'])
                e_cat = c2.selectbox("Cat", ["Electronics", "Clothing", "Home", "Other"], index=0)
                c3, c4 = st.columns(2)
                e_price = c3.number_input("Price", value=float(row['price']))
                e_qty = c4.number_input("Qty", value=int(row['quantity']))
                if st.form_submit_button("Update"):
                    if update_item(edit_id, e_name, e_cat, e_price, e_qty):
                        st.toast("Updated!")
                        time.sleep(1)
                        st.rerun()
            
            # QR Code
            st.divider()
            qr_img = generate_qr(f"ID:{edit_id}|{row['name']}")
            st.image(qr_img, width=150, caption="Product QR")

    with tab3:
        if not df.empty:
            del_id = st.selectbox("Delete Item", df['id'], key="del")
            if st.button("🗑️ Delete", type="primary"):
                if delete_item(del_id):
                    st.toast("Deleted!")
                    time.sleep(1)
                    st.rerun()