Here is the complete, corrected, and formatted README.md file. I have cleaned up the chat interface text, fixed the code blocks, and linked your profile URLs correctly.

You can copy and paste this entire block:

code
Markdown
download
content_copy
expand_less
# 🚀 StockPilot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

**StockPilot** is a professional Inventory Management System designed to bridge the gap between physical stock and digital tracking. By integrating a real-time **Supabase** cloud database with **Streamlit**, it allows businesses to track assets, visualize value distribution, and auto-generate QR codes for seamless inventory control.

---

<div align="center">
  <img src="dashboard.png" alt="StockPilot Dashboard" width="100%">
</div>

---

### StockPilot Pro 📦
**Turn your manual inventory spreadsheets into a modern, automated dashboard.**

📂 **Source Material**
*   **Real-time Database:** Connects directly to Supabase (PostgreSQL).
*   **Live Analytics:** Tracks Total SKUs, Low Stock Alerts, and Asset Value.

<br>

### 🚀 Key Features

*   📊 **Executive Dashboard:** Uses Altair charts for interactive visualization of stock levels and value distribution.
*   ☁️ **Cloud Database:** Fully integrated with **Supabase** for persistent, secure data storage (CRUD).
*   📱 **QR Code Generation:** Auto-generates unique QR codes for every product using the `qrcode` library.
*   🔒 **Secure Access:** Built-in Admin Authentication system to protect sensitive database operations.
*   📉 **Smart Alerts:** Visual progress bars and toast notifications for low-stock items.
*   📥 **Data Export:** One-click CSV export for reporting and external analysis.
*   🎨 **Modern UI:** A custom-styled interface featuring Dark Mode, Glassmorphism cards, and responsive tabs.

### 🛠️ Tech Stack

*   **Frontend:** Streamlit (Custom CSS styling)
*   **Backend:** Python 3.x
*   **Database:** Supabase (PostgreSQL)
*   **Visualization:** Altair & Pandas
*   **Utilities:** Qrcode, Pillow

---

## 📦 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JannElijah/StockPilot.git
   cd StockPilot

Create a Virtual Environment (Optional but recommended):

code
Bash
download
content_copy
expand_less
python -m venv venv

# Windows:
.\venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

Install dependencies:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt

Set up Secrets:
Create a folder named .streamlit and a file inside named secrets.toml:

code
Toml
download
content_copy
expand_less
[secrets]
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_anon_key"
ADMIN_PASSWORD = "StockPilot2025!"

Run the application:

code
Bash
download
content_copy
expand_less
streamlit run app.py
🔑 Configuration

To use the Database features, you need a Supabase Project.

Get a free project at Supabase.

Run the SQL query provided in the repo to create the inventory table.

Enter the URL and Key in the secrets.toml file (Step 4 above).

👤 Author

Jann Elijah B. Limpiado
3rd Year IT Student

![alt text](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)


![alt text](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)

Created for Portfolio 2025

code
Code
download
content_copy
expand_less