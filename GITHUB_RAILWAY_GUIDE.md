# 📚 GitHub Setup Guide for Railway Deployment

## 🎯 **QUICK GITHUB SETUP:**

### **Step 1: Create GitHub Repository**
1. Go to https://github.com/new
2. Repository name: `harvestlink`
3. Description: `AI-powered SMS/USSD system for African farmers`
4. Set to Public (for free Railway deployment)
5. Click "Create repository"

### **Step 2: Push Your Code**
```bash
# In your harvestlink folder:
git init
git add .
git commit -m "Initial HarvestLink commit"

# Connect to GitHub (replace YOUR_USERNAME):
git remote add origin https://github.com/YOUR_USERNAME/harvestlink.git
git branch -M main
git push -u origin main
```

### **Step 3: Verify Upload**
- Go to your GitHub repository
- You should see all files: app.py, requirements.txt, railway.json, etc.

## 🚀 **RAILWAY DEPLOYMENT:**

### **Step 1: Sign up at Railway**
1. Go to https://railway.app
2. Click "Sign up with GitHub"
3. Authorize Railway access

### **Step 2: Deploy from GitHub**
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose your "harvestlink" repository
4. Railway auto-detects Python

### **Step 3: Set Environment Variables**
In Railway dashboard → Variables tab:
```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
```

### **Step 4: Get Your URLs**
Railway provides:
- App URL: `https://your-app-name.railway.app`
- SMS Webhook: `https://your-app-name.railway.app/sms`
- USSD Webhook: `https://your-app-name.railway.app/ussd`

## 🎯 **TWILIO SETUP:**

### **Step 1: Create Twilio Account**
1. Go to https://twilio.com
2. Sign up (free tier available)
3. Get Account SID and Auth Token
4. Purchase phone number ($1/month)

### **Step 2: Configure Webhooks**
In Twilio Console → Phone Numbers:
- SMS Webhook: `https://your-app-name.railway.app/sms`
- USSD Webhook: `https://your-app-name.railway.app/ussd`

## ✅ **TESTING:**

### **Test SMS:**
```
Send SMS to your Twilio number:
"maize 50kg Nairobi traditional humid"

Expected response:
"🧠 HARVESTLINK AI ANALYSIS
📊 LOSS PREDICTION: HIGH risk
🎯 Confidence: 81.7%..."
```

### **Test USSD:**
```
Dial *123# on your phone
Follow menu: 1 → 1 → 50kg → 1 → 1 → 2

Expected response:
"🧠 AI ANALYSIS
📊 LOSS PREDICTION: HIGH risk..."
```

## 🎉 **SUCCESS!**

**You now have HarvestLink running on Railway:**
- ✅ FREE deployment (no credit card)
- ✅ Professional URLs
- ✅ Automatic deployments
- ✅ SMS + USSD support
- ✅ Advanced AI capabilities
- ✅ Ready for African farmers!

**🌾 Railway + HarvestLink = Free deployment for African farmers!**
