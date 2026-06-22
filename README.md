# 📧 Temp Mail Generator & Inbox Viewer

Generate a temporary email address instantly and monitor incoming emails directly from your terminal. 🚀

This tool creates a disposable email account using the Mail.tm API, continuously checks for new messages, and automatically opens received emails in your default web browser.

Perfect for:

* 🧪 Software Testing
* 🔐 Privacy Protection
* 🤖 Automation Projects
* 📝 Temporary Registrations
* 🛡️ Avoiding Spam in Personal Inbox

---

## ✨ Features

✅ Generate random temporary email addresses

✅ Automatically create Mail.tm accounts

✅ Real-time inbox monitoring

✅ Detect new emails automatically

✅ Save email content as HTML

✅ Open emails in browser instantly

✅ Generate fake identities using Faker

---

## 📸 Example Output

```text
👤 Name: John Smith
👩 Female: Emma Johnson
👨 Male: Michael Brown

🌐 Username: cyberghost123

📞 Phone: 555-123-4567

🏠 Address: 123 Main Street
🌍 Country: United States

📧 Email: x7k29m4pab@domain.com

Waiting for emails...
```

When a new email arrives:

```text
📨 New Mail Received!

From: noreply@example.com
Subject: Verify Your Account
```

The email is automatically opened in your browser.

---

## 🧠 How It Works

```text
Generate Random User
          ↓
Create Temporary Email
          ↓
Login & Obtain Token
          ↓
Monitor Inbox
          ↓
New Email Arrives
          ↓
Save as HTML
          ↓
Open in Browser
```

---

## 📂 Project Structure

```text
.
├── temp_mail.py
├── mail.html
├── requirements.txt
└── README.md
```

---

## ⚙️ Requirements

### 🐍 Python Version

```text
Python 3.8+
```

### 📦 Libraries

Install dependencies:

```bash
pip install requests faker
```

Imported modules:

```python
requests
faker
random
string
time
os
datetime
webbrowser
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/temp-mail-generator.git
cd temp-mail-generator
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run:

```bash
python temp_mail.py
```

The program will:

1️⃣ Generate a fake identity

2️⃣ Create a temporary email address

3️⃣ Login automatically

4️⃣ Start monitoring the inbox

5️⃣ Open received emails in your browser

---

## 📧 Temporary Email Example

```text
Email: a8x92bz7wq@domain.com
```

Use this email for:

* Website registrations
* Software testing
* Account verification
* One-time signups

---

## 📨 Email Monitoring

The script checks for new emails every:

```text
5 seconds
```

When a new email arrives:

* 📥 Downloads the message
* 💾 Saves HTML content
* 🌐 Opens it in browser
* 📄 Stores it as mail.html

---

## 🎭 Fake Data Generation

The script generates random information using Faker:

### 👤 Identity

* Full Name
* Male Name
* Female Name
* Username

### 📍 Location

* Address
* Country
* Latitude
* Longitude

### 📞 Contact

* Phone Number

### 🚗 Miscellaneous

* License Plate
* Date Information

---

## ⚠️ Limitations

* One inbox per execution
* Emails are temporary
* Mail.tm service availability affects functionality
* Previous inboxes are not stored permanently
* HTML emails overwrite existing mail.html

---

## 🚧 Future Improvements

* 📂 Store multiple emails separately
* 🖥️ GUI Interface
* 🔔 Desktop Notifications
* 📎 Attachment Downloads
* 🌙 Dark Mode Email Viewer
* 📜 Email History Management
* 🔍 Email Search Functionality

---

## 🛡️ Security Note

This project is intended for:

✅ Testing

✅ Development

✅ Educational Purposes

✅ Privacy Protection

Always comply with the terms of service of websites you use.

---

## 👨‍💻 Author

**Dhyey Lukhi**

🎓 Information Technology Student

🐙 GitHub: https://github.com/DhyeyLukhi

---

## ⭐ Support

If you found this project useful:

🌟 Star the repository

🍴 Fork the project

📢 Share it with fellow developers

Happy Testing! 🚀📧
