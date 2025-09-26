# 🚀 Railway Deployment Guide (FREE Alternative to Heroku)

## ✅ **RAILWAY: COMPLETELY FREE, NO CREDIT CARD REQUIRED!**

### **Why Railway?**
- ✅ **100% FREE** - No credit card verification needed
- ✅ **$5 monthly credit** - More than enough for HarvestLink
- ✅ **Easy deployment** - GitHub integration
- ✅ **Automatic scaling** - Handles traffic spikes
- ✅ **Custom domains** - Professional URLs
- ✅ **Environment variables** - Secure configuration

## 📋 **STEP-BY-STEP RAILWAY DEPLOYMENT:**

### **Step 1: Prepare Your Code (5 minutes)**

1. **Create GitHub Repository:**
   ```bash
   # Initialize git repository
   git init
   git add .
   git commit -m "Initial HarvestLink commit"
   
   # Create GitHub repository
   # Go to https://github.com/new
   # Create repository named "harvestlink"
   
   # Push to GitHub
   git remote add origin https://github.com/yourusername/harvestlink.git
   git push -u origin main
   ```

### **Step 2: Railway Setup (10 minutes)**

1. **Sign up at Railway:**
   - Go to https://railway.app
   - Click "Sign up with GitHub"
   - Authorize Railway to access your repositories

2. **Deploy from GitHub:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your "harvestlink" repository
   - Railway will automatically detect Python

### **Step 3: Configure Environment Variables (5 minutes)**

1. **In Railway Dashboard:**
   - Go to your project
   - Click "Variables" tab
   - Add these environment variables:

   ```
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_PHONE_NUMBER=your_twilio_phone_number
   PORT=5000
   ```

2. **Get Twilio Credentials:**
   - Go to https://twilio.com
   - Sign up for free account
   - Get Account SID and Auth Token
   - Purchase phone number ($1/month)

### **Step 4: Update Code for Railway (5 minutes)**

1. **Create railway.json:**
   ```json
   {
     "build": {
       "builder": "NIXPACKS"
     },
     "deploy": {
       "startCommand": "python app.py",
       "healthcheckPath": "/",
       "healthcheckTimeout": 100,
       "restartPolicyType": "ON_FAILURE",
       "restartPolicyMaxRetries": 10
     }
   }
   ```

2. **Update app.py for Railway:**
   ```python
   # Add this at the end of app.py
   if __name__ == '__main__':
       port = int(os.environ.get('PORT', 5000))
       app.run(debug=False, host='0.0.0.0', port=port)
   ```

### **Step 5: Deploy (5 minutes)**

1. **Railway will automatically:**
   - Detect Python project
   - Install dependencies from requirements.txt
   - Start your application
   - Provide public URL

2. **Get Your URLs:**
   - Railway provides: `https://your-app-name.railway.app`
   - SMS Webhook: `https://your-app-name.railway.app/sms`
   - USSD Webhook: `https://your-app-name.railway.app/ussd`

### **Step 6: Configure Twilio Webhooks (5 minutes)**

1. **In Twilio Console:**
   - Go to Phone Numbers → Manage → Active numbers
   - Click your phone number
   - Set webhook URLs:
     - SMS: `https://your-app-name.railway.app/sms`
     - USSD: `https://your-app-name.railway.app/ussd`

### **Step 7: Test Your Deployment (5 minutes)**

1. **Test SMS:**
   ```
   Send SMS to your Twilio number:
   "maize 50kg Nairobi traditional humid"
   
   Expected response:
   "🧠 HARVESTLINK AI ANALYSIS
   📊 LOSS PREDICTION: HIGH risk
   🎯 Confidence: 81.7%..."
   ```

2. **Test USSD:**
   ```
   Dial *123# on your phone
   Follow menu: 1 → 1 → 50kg → 1 → 1 → 2
   
   Expected response:
   "🧠 AI ANALYSIS
   📊 LOSS PREDICTION: HIGH risk..."
   ```

## 🎯 **RAILWAY ADVANTAGES:**

### **Free Tier Benefits:**
- ✅ **$5 monthly credit** - More than enough for HarvestLink
- ✅ **512MB RAM** - Sufficient for AI models
- ✅ **1GB storage** - Plenty for database
- ✅ **Custom domains** - Professional URLs
- ✅ **Automatic HTTPS** - Secure connections
- ✅ **Zero downtime** - Reliable service

### **Easy Management:**
- ✅ **GitHub integration** - Automatic deployments
- ✅ **Environment variables** - Secure configuration
- ✅ **Logs dashboard** - Easy debugging
- ✅ **Metrics monitoring** - Performance tracking
- ✅ **One-click scaling** - Handle traffic spikes

## 🔧 **TROUBLESHOOTING:**

### **Common Issues:**

1. **Deployment Fails:**
   - Check requirements.txt has all dependencies
   - Verify Python version compatibility
   - Check Railway logs for errors

2. **Environment Variables Not Working:**
   - Ensure variables are set in Railway dashboard
   - Restart deployment after adding variables
   - Check variable names match exactly

3. **Webhooks Not Working:**
   - Verify URLs are correct in Twilio
   - Check Railway app is running
   - Test URLs in browser first

### **Support:**
- Railway Documentation: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Railway Status: https://status.railway.app

## 📊 **COST COMPARISON:**

| Platform | Free Tier | Credit Card Required | Monthly Cost |
|----------|-----------|---------------------|--------------|
| **Railway** | ✅ $5 credit | ❌ No | $0 |
| **Render** | ✅ 750 hours | ❌ No | $0 |
| **PythonAnywhere** | ✅ 1 web app | ❌ No | $0 |
| **Vercel** | ✅ Unlimited | ❌ No | $0 |
| **Heroku** | ❌ Discontinued | ✅ Yes | $7+ |

## 🎉 **RAILWAY DEPLOYMENT SUCCESS!**

**Railway is the perfect free alternative to Heroku:**
- ✅ No credit card verification required
- ✅ $5 monthly credit (more than enough)
- ✅ Easy GitHub integration
- ✅ Automatic deployments
- ✅ Professional URLs
- ✅ Reliable uptime

**Follow this guide and you'll have HarvestLink running on Railway in under 30 minutes!**

**🌾 Railway + HarvestLink = Free deployment for African farmers!**