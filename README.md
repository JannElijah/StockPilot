# 🚀 StockPilot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

**StockPilot** is a professional Inventory Management System designed to bridge the gap between physical stock and digital tracking. By integrating a real-time **Supabase** cloud database with **Streamlit**, it allows businesses to track assets, visualize value distribution, and auto-generate QR codes for seamless inventory control.

---

<div align="center"> 
  <!-- INSTRUCTIONS: Take a screenshot of your dashboard, name it 'dashboard.png', and put it in your folder -->
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

### 📦 How to Run Locally

**1. Clone the repository:**

```bash
git clone https://github.com/JannElijah/stock-pilot.git
cd stock-pilot

2. Create a Virtual Environment (Optional but recommended):

code
Bash
download
content_copy
expand_less
python -m venv venv

Windows:

code
Bash
download
content_copy
expand_less
.\venv\Scripts\activate

Mac/Linux:

code
Bash
download
content_copy
expand_less
source venv/bin/activate

3. Install dependencies:

code
Bash
download
content_copy
expand_less
pip install -r requirements.txt

4. Set up Secrets:
Create a folder named .streamlit and a file inside named secrets.toml:

code
Toml
download
content_copy
expand_less
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_anon_key"
ADMIN_PASSWORD = "StockPilot2025!"

5. Run the application:

code
Bash
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

code
Code
download
content_copy
expand_less
### 2. How to fix the Image (Important)

In the code above, I added this line:
`<img src="dashboard.png" ... >`

For the image to actually show up:
1.  Take a nice screenshot of your Dashboard.
2.  Rename the file to `dashboard.png`.
3.  **Drag and drop** that file into your `StockPilot` folder (the same place where `app.py` is).
4.  Push the changes to GitHub.

If you don't do this, you will see a broken image icon.

Try pasting this new code and let me know if the "Preview" looks cleaner!