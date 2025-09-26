# 🆓 PythonAnywhere Deployment Guide (100% FREE Alternative)

## ✅ **PYTHONANYWHERE: SIMPLEST FREE DEPLOYMENT!**

### **Why PythonAnywhere?**
- ✅ **100% FREE** - No payment method required
- ✅ **Beginner-friendly** - Web-based interface
- ✅ **No CLI needed** - Upload files via browser
- ✅ **Python-focused** - Optimized for Python apps
- ✅ **Reliable** - Established platform
- ✅ **Easy setup** - No complex configuration

## 📋 **STEP-BY-STEP PYTHONANYWHERE DEPLOYMENT:**

### **Step 1: Create Account (2 minutes)**

1. **Sign up at PythonAnywhere:**
   - Go to https://pythonanywhere.com
   - Click "Create a Beginner account"
   - Choose username and password
   - Verify email address

### **Step 2: Upload Files (5 minutes)**

1. **Upload via Web Interface:**
   - Go to "Files" tab
   - Create folder: `harvestlink`
   - Upload all files:
     - `app.py`
     - `requirements.txt`
     - `seed_data.py`
     - `test_system.py`

2. **Files to Upload:**
   ```
   harvestlink/
   ├── app.py
   ├── requirements.txt
   ├── seed_data.py
   ├── test_system.py
   └── (other files)
   ```

### **Step 3: Install Dependencies (5 minutes)**

1. **Open Bash Console:**
   - Go to "Consoles" tab
   - Click "Bash" → "Start a new console"

2. **Install Dependencies:**
   ```bash
   cd harvestlink
   pip3.10 install --user flask twilio pandas numpy scikit-learn python-dotenv
   ```

### **Step 4: Create Web App (10 minutes)**

1. **Create Web App:**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Select Python 3.10
   - Set path: `/home/yourusername/harvestlink/app.py`

2. **Configure Web App:**
   ```
   Source code: /home/yourusername/harvestlink
   Working directory: /home/yourusername/harvestlink
   WSGI file: /var/www/yourusername_pythonanywhere_com_wsgi.py
   ```

### **Step 5: Set Environment Variables (5 minutes)**

1. **Edit WSGI File:**
   - Go to "Web" tab
   - Click "WSGI configuration file"
   - Add environment variables:

   ```python
   import os
   os.environ['TWILIO_ACCOUNT_SID'] = 'your_twilio_account_sid'
   os.environ['TWILIO_AUTH_TOKEN'] = 'your_twilio_auth_token'
   os.environ['TWILIO_PHONE_NUMBER'] = 'your_twilio_phone_number'
   ```

### **Step 6: Initialize Database (5 minutes)**

1. **Run Database Setup:**
   - Go to "Consoles" tab
   - Start new Bash console
   - Run:

   ```bash
   cd harvestlink
   python3.10 -c "from app import init_db; init_db(); print('Database initialized!')"
   python3.10 seed_data.py
   ```

### **Step 7: Configure Twilio Webhooks (5 minutes)**

1. **Get Your URL:**
   - PythonAnywhere provides: `https://yourusername.pythonanywhere.com`
   - SMS Webhook: `https://yourusername.pythonanywhere.com/sms`
   - USSD Webhook: `https://yourusername.pythonanywhere.com/ussd`

2. **Set Twilio Webhooks:**
   - Go to Twilio Console
   - Set webhook URLs to your PythonAnywhere URLs

### **Step 8: Test Your Deployment (5 minutes)**

1. **Test SMS:**
   ```
   Send SMS to your Twilio number:
   "maize 50kg Nairobi traditional humid"
   
   Expected response:
   "🧠 HARVESTLINK AI ANALYSIS
   📊 LOSS PREDICTION: HIGH risk..."
   ```

2. **Test USSD:**
   ```
   Dial *123# on your phone
   Follow menu: 1 → 1 → 50kg → 1 → 1 → 2
   
   Expected response:
   "🧠 AI ANALYSIS
   📊 LOSS PREDICTION: HIGH risk..."
   ```

## 🎯 **PYTHONANYWHERE ADVANTAGES:**

### **Free Tier Benefits:**
- ✅ **1 web app** - Perfect for HarvestLink
- ✅ **512MB RAM** - Sufficient for AI models
- ✅ **Custom domain** - Professional URLs
- ✅ **HTTPS support** - Secure connections
- ✅ **No payment method** - Sign up with email only
- ✅ **Web-based interface** - No CLI needed

### **Easy Management:**
- ✅ **File upload** - Drag and drop files
- ✅ **Console access** - Run commands in browser
- ✅ **Logs viewing** - Easy debugging
- ✅ **Environment variables** - Secure configuration
- ✅ **One-click restart** - Easy maintenance

## 🔧 **TROUBLESHOOTING:**

### **Common Issues:**

1. **Import Errors:**
   - Install missing packages in Bash console
   - Use `pip3.10 install --user package_name`

2. **Database Issues:**
   - Run database initialization in console
   - Check file permissions

3. **Web App Not Starting:**
   - Check WSGI configuration
   - Verify file paths are correct
   - Check console logs

4. **Environment Variables Not Working:**
   - Set variables in WSGI file
   - Restart web app after changes

### **Support:**
- PythonAnywhere Documentation: https://help.pythonanywhere.com
- PythonAnywhere Community: https://www.pythonanywhere.com/forums
- PythonAnywhere Status: https://status.pythonanywhere.com

## 📊 **PYTHONANYWHERE FREE TIER LIMITATIONS:**

### **What You Get:**
- ✅ 1 web app
- ✅ 512MB RAM
- ✅ Custom domain
- ✅ HTTPS support
- ✅ Console access
- ✅ File storage

### **Limitations:**
- ⚠️ App sleeps after 3 months of inactivity
- ⚠️ Limited CPU seconds per day
- ⚠️ No guaranteed uptime SLA

### **Solutions:**
- ✅ Use app regularly to prevent sleep
- ✅ Upgrade to paid plan ($5/month) for always-on
- ✅ Accept limitations for free tier

## 🎉 **PYTHONANYWHERE DEPLOYMENT SUCCESS!**

**PythonAnywhere is perfect for beginners:**
- ✅ No payment method required
- ✅ Web-based interface
- ✅ No CLI needed
- ✅ Easy file upload
- ✅ Reliable service
- ✅ Python-optimized

**Follow this guide and you'll have HarvestLink running on PythonAnywhere in under 30 minutes!**

**🌾 PythonAnywhere + HarvestLink = Free deployment for African farmers!**
