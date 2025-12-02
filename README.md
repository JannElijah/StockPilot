
# 🚀 StockPilot

![Python](https://img.shields.io/badge/Python3.10%2Bblue) 
![Streamlit](https://img.shields.io/badge/StreamlitFrameworkFF4B4B) 
![Supabase](https://img.shields.io/badge/SupabaseDatabase3ECF8E)

StockPilot is a professional Inventory Management System designed to bridge the gap between physical stock and digital tracking. By integrating a realtime Supabase cloud database with Streamlit, it allows businesses to track assets, visualize value distribution, and autogenerate QR codes for seamless inventory control.

<br>

<div align="center">
  <img src="your_dashboard_screenshot.png" alt="StockPilot Dashboard" width="800">
</div>

 StockPilot Pro 📦
Turn your manual inventory spreadsheets into a modern, automated dashboard.

📂 Source Material
   Realtime Database: Connects directly to Supabase (PostgreSQL).
   Live Analytics: Tracks Total SKUs, Low Stock Alerts, and Asset Value.

<br>

🚀 Key Features

   📊 Executive Dashboard: Uses Altair charts for interactive visualization of stock levels and value distribution.
   ☁️ Cloud Database: Fully integrated with Supabase for persistent, secure data storage (CRUD).
   📱 QR Code Generation: Autogenerates unique QR codes for every product using the `qrcode` library.
   🔒 Secure Access: Builtin Admin Authentication system to protect sensitive database operations.
   📉 Smart Alerts: Visual progress bars and toast notifications for lowstock items.
   📥 Data Export: Oneclick CSV export for reporting and external analysis.
   🎨 Modern UI: A customstyled interface featuring Dark Mode, Glassmorphism cards, and responsive tabs.

🛠️ Tech Stack

   Frontend: Streamlit (Custom CSS styling)
   Backend: Python 3.x
   Database: Supabase (PostgreSQL)
   Visualization: Altair & Pandas
   Utilities: Qrcode, Pillow

📦 How to Run Locally

1. Clone the repository:

   bash
   git clone https://github.com/JannElijah/stockpilot.git
   cd stockpilot

Create a Virtual Environment (Optional but recommended):

code

download
content_copy
expand_less
python m venv venv

Windows

code

download
content_copy
expand_less
.\venv\Scripts\activate

Mac/Linux

code

download
content_copy
expand_less
source venv/bin/activate

Install dependencies:

code

download
content_copy
expand_less
pip install r requirements.txt

Set up Secrets:
Create a folder named .streamlit and a file inside named secrets.toml:

code
Toml
download
content_copy
expand_less
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_anon_key"
ADMIN_PASSWORD = "StockPilot2025!"

Run the application:

code

download
content_copy
expand_less
streamlit run app.py

🔑 Configuration

To use the Database features, you need a Supabase Project.

Create a free project at Supabase.com.

Run the SQL query provided in the repo to create the inventory table.

Add your URL and Anon Key to the secrets.toml file (Step 4 above).

👤 Author

Jann Elijah B. Limpiado
3rd Year IT Student

LinkedIn Profile

GitHub Profile

Created for Portfolio 2025
