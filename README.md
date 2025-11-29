# Discord Webhook Python Script

A simple and lightweight Python script to send messages to Discord channels using webhooks.

## 📋 Overview

This project provides an easy-to-use Python script that leverages Discord's Webhook API to send customized messages directly to your Discord server channels. It's perfect for notifications, alerts, automated messages, or any scenario where you need to programmatically post content to Discord.

## ✨ Features

- 📬 Send text messages to any Discord channel via webhooks
- 🔧 Simple and easy to configure
- 🐍 Lightweight with minimal dependencies
- 📖 Well-documented and beginner-friendly

## 📦 Requirements

- Python 3.6 or higher
- `requests` library

## ⚙️ Setup

1. **Create a Discord Webhook:**
   - Go to your Discord server
   - Navigate to **Server Settings** → **Integrations** → **Webhooks**
   - Click **New Webhook**
   - Customize the webhook name and channel
   - Copy the **Webhook URL**

2. **Configure the script:**
   - Open `Main/Main.py`
   - Replace `"Your-Discord-Webhook-url"` with your actual webhook URL:

     ```python
     webhook_url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
     ```
For this you can use a .env if you know how to set it up but in this code it doesn't use one so just enter it into the script!

3. **Customize your message:**
   - Modify the `message_content` variable to set your desired message:

     ```python
     message_content = "Hello from my Python script!"
     ```

## 📝 Usage

Run the script to send your message:

**Expected output on success:**

```
Message sent successfully!
```

## 🔧 How It Works

The script uses Python's `requests` library to send a POST request to Discord's Webhook API:

1. Constructs a JSON payload with your message content
2. Sets the appropriate `Content-Type` header
3. Sends the request to the webhook URL
4. Validates the response status code (204 indicates success)

## 📁 Project Structure

```
Discord-Webhook-Python-Script/
├── Main/
│   └── Main.py      # Main script file
├── LICENSE          # MIT License
└── README.md        # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**[@glimmercharger](https://github.com/glimmercharger)**

GitHub Copilot was used to help the making of the ReadMe!

---

⭐ If you found this project helpful, please consider giving it a star!
