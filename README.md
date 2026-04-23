# ICAR-IIRR IP Management Portal 🌾🔬

A centralized, secure web application designed to manage and track Intellectual Property (IP) assets, commercialization records, and critical docketing deadlines for the ICAR-Indian Institute of Rice Research.

## 🚀 Features
* **Role-Based Access Control:** Secure Admin and Scientist portals with Two-Factor Authentication (2FA) via Email.
* **Central Repository:** Manage 4 distinct asset types: Varieties & Hybrids, Patents & Designs, Creative/Brand Assets, and Licenses.
* **Bulk Data Operations:** One-click CSV export and intelligent bulk CSV import with duplicate prevention.
* **Financial Tracking:** Real-time dashboard calculating total revenue from license fees and royalties.
* **Automated Docketing:** Interactive calendar and dashboard alerts for upcoming patent expirations, office actions, and hearings.
* **Dynamic Analytics:** Visual portfolio distribution using Chart.js.

## 💻 Tech Stack
* **Backend:** Python, Flask, Flask-SQLAlchemy, Flask-Login, Flask-Mail
* **Database:** SQLite
* **Frontend:** HTML5, CSS3, JavaScript (Chart.js, FullCalendar.io)
* **Document Processing:** python-docx, CSV/IO parsing

## 🛠️ Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/suhas107/IP-MANAGEMENT-portal.git](https://github.com/suhas107/IP-MANAGEMENT-portal.git)
   cd IP-MANAGEMENT-portal