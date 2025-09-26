# 🚀 Complete Render Deployment Guide for HarvestLink

## 📋 **STEP-BY-STEP RENDER DEPLOYMENT**

### **Prerequisites (5 minutes)**
- GitHub account (free)
- Twilio account (free tier)
- Your HarvestLink code ready

---

## **STEP 1: Prepare GitHub Repository (5 minutes)**

### **1.1 Create GitHub Repository**
1. Go to https://github.com/new
2. Repository name: `harvestlink`
3. Description: `AI-powered SMS/USSD system for African farmers`
4. Set to **Public** (required for free Render deployment)
5. Click "Create repository"

### **1.2 Upload Your Code**
```bash
# In your harvestlink folder, run these commands:
git init
git add .
git commit -m "Initial HarvestLink commit"

# Replace YOUR_USERNAME with your GitHub username:
git remote add origin https://github.com/YOUR_USERNAME/harvestlink.git
git branch -M main
git push -u origin main
```

### **1.3 Verify Upload**
- Go to your GitHub repository
- You should see all files: `app.py`, `requirements.txt`, etc.

---

## **STEP 2: Sign Up for Render (2 minutes)**

### **2.1 Create Render Account**
1. Go to https://render.com
2. Click "Get Started for Free"
3. Click "Sign up with GitHub"
4. Authorize Render to access your repositories
5. **No payment method required!**

---

## **STEP 3: Deploy from GitHub (10 minutes)**

### **3.1 Create New Web Service**
1. In Render dashboard, click "New +"
2. Select "Web Service"
3. Choose "Build and deploy from a Git repository"
4. Select your `harvestlink` repository
5. Click "Connect"

### **3.2 Configure Build Settings**
```
Name: harvestlink
Environment: Python 3
Region: Oregon (US West) - or closest to you
Branch: main
Root Directory: (leave empty)
Build Command: pip install -r requirements.txt
Start Command: python app.py
```

### **3.3 Advanced Settings**
- Click "Advanced"
- Python Version: `3.11.0`
- Click "Create Web Service"

---

## **STEP 4: Set Environment Variables (5 minutes)**

### **4.1 Get Twilio Credentials**
1. Go to https://twilio.com
2. Sign up for free account
3. Go to Console Dashboard
4. Copy your:
   - Account SID
   - Auth Token
5. Go to Phone Numbers → Manage → Active numbers
6. Purchase a phone number ($1/month)

### **4.2 Set Environment Variables in Render**
1. In your Render web service dashboard
2. Go to "Environment" tab
3. Add these variables:

```
TWILIO_ACCOUNT_SID = your_twilio_account_sid
TWILIO_AUTH_TOKEN = your_twilio_auth_token
TWILIO_PHONE_NUMBER = your_twilio_phone_number
PORT = 10000
```

### **4.3 Save and Deploy**
- Click "Save Changes"
- Render will automatically redeploy your app

---

## **STEP 5: Get Your URLs (2 minutes)**

### **5.1 Get Render URLs**
After deployment, Render provides:
- **App URL**: `https://harvestlink.onrender.com`
- **SMS Webhook**: `https://harvestlink.onrender.com/sms`
- **USSD Webhook**: `https://harvestlink.onrender.com/ussd`

### **5.2 Note Your URLs**
Copy these URLs - you'll need them for Twilio configuration.

---

## **STEP 6: Configure Twilio Webhooks (5 minutes)**

### **6.1 Set SMS Webhook**
1. Go to Twilio Console
2. Phone Numbers → Manage → Active numbers
3. Click your phone number
4. In "Messaging" section:
   - Webhook URL: `https://harvestlink.onrender.com/sms`
   - HTTP Method: POST
5. Click "Save Configuration"

### **6.2 Set USSD Webhook**
1. In the same phone number settings
2. In "Voice" section:
   - Webhook URL: `https://harvestlink.onrender.com/ussd`
   - HTTP Method: POST
3. Click "Save Configuration"

---

## **STEP 7: Test Your Deployment (5 minutes)**

### **7.1 Test SMS**
1. Send SMS to your Twilio number:
   ```
   "maize 50kg Nairobi traditional humid"
   ```

2. Expected response:
   ```
   🧠 HARVESTLINK AI ANALYSIS
   
   📊 LOSS PREDICTION: HIGH risk
   🎯 Confidence: 81.7%
   ⚠️ AI Alert: Moderate risk detected...
   
   💰 AI PRICE FORECAST: 213 KES/kg (7-day)
   📈 Price Trend: Rising
   
   🤝 BUYER MATCHES: 6 found
   1. AgriCorp Kenya (Nairobi) - 200-250 KES/kg
   2. Grain Traders Co (Kisumu) - 180-220 KES/kg
   
   🔮 AI RECOMMENDATION: Hold for better price
   📊 Cluster Group: 0
   
   Reply 'BUYERS' for contacts, 'ADVICE' for detailed AI tips, or 'LEARN' for how AI improves.
   ```

### **7.2 Test USSD**
1. Dial `*123#` on your phone
2. Follow menu:
   - Select "1" (Check Loss Risk)
   - Select "1" (Maize)
   - Enter "50kg"
   - Select "1" (Nairobi)
   - Select "1" (Traditional storage)
   - Select "2" (Humid weather)
3. Get AI analysis via guided menu

---

## **STEP 8: Monitor Your App (Ongoing)**

### **8.1 Check Render Dashboard**
- Go to your Render web service
- Monitor "Logs" tab for any errors
- Check "Metrics" tab for performance

### **8.2 Common Issues & Solutions**

**Issue: App not responding**
- Check if app is sleeping (free tier limitation)
- First request after sleep takes ~30 seconds
- Solution: Use uptime monitoring service

**Issue: SMS not working**
- Verify Twilio webhook URL is correct
- Check Render logs for errors
- Ensure environment variables are set

**Issue: USSD not working**
- Verify USSD webhook URL is correct
- Check if USSD provider supports your webhook
- Test webhook URL in browser first

---

## **🎯 RENDER FREE TIER LIMITATIONS**

### **What You Get:**
- ✅ 750 hours/month (31 days × 24 hours = 744 hours)
- ✅ 512MB RAM (sufficient for AI models)
- ✅ Custom domain
- ✅ Automatic HTTPS
- ✅ Environment variables
- ✅ GitHub integration

### **Limitations:**
- ⚠️ App sleeps after 15 minutes of inactivity
- ⚠️ First request after sleep takes ~30 seconds
- ⚠️ No guaranteed uptime SLA

### **Solutions:**
- ✅ Use uptime monitoring service (free)
- ✅ Upgrade to paid plan ($7/month) for always-on
- ✅ Accept sleep limitation for free tier

---

## **🎉 SUCCESS CHECKLIST**

- ✅ GitHub repository created and code uploaded
- ✅ Render account created (no payment method)
- ✅ Web service deployed from GitHub
- ✅ Environment variables set
- ✅ Twilio webhooks configured
- ✅ SMS test successful
- ✅ USSD test successful
- ✅ App running on Render

---

## **🚀 YOUR HARVESTLINK IS NOW LIVE!**

**Your URLs:**
- **App**: `https://harvestlink.onrender.com`
- **SMS**: `https://harvestlink.onrender.com/sms`
- **USSD**: `https://harvestlink.onrender.com/ussd`

**Features Working:**
- ✅ Advanced AI ensemble learning
- ✅ SMS interface for quick analysis
- ✅ USSD interface for guided experience
- ✅ Loss prediction with confidence scores
- ✅ Price forecasting
- ✅ Buyer matching
- ✅ Farmer clustering

**🌾 HarvestLink is now empowering African farmers via SMS and USSD!**

**Built with ❤️ for African farmers. Deployed for free on Render!**
