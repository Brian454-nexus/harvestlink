# 📱 WHATSAPP SETUP GUIDE FOR HARVESTLINK

## 🎯 **OVERVIEW**
WhatsApp is perfect for Kenyan farmers since 90%+ use it daily. This guide will help you set up WhatsApp Business API integration with HarvestLink.

## 🚀 **STEP 1: GET WHATSAPP BUSINESS API ACCESS**

### **Option A: Meta Business API (Recommended for Production)**

#### **1.1 Create Meta Developer Account**
1. **Go to:** [developers.facebook.com](https://developers.facebook.com)
2. **Click "Get Started"**
3. **Sign in with Facebook account**
4. **Complete developer verification**

#### **1.2 Create WhatsApp Business App**
1. **Click "Create App"**
2. **Select "Business"**
3. **Enter app details:**
   - **App Name:** `HarvestLink`
   - **App Contact Email:** Your email
   - **Business Account:** Select or create

#### **1.3 Add WhatsApp Business API**
1. **In your app dashboard**
2. **Click "Add Product"**
3. **Find "WhatsApp" → Click "Set up"**
4. **Follow the setup wizard**

#### **1.4 Get Your Credentials**
After setup, you'll get:
- **Phone Number ID:** `123456789012345`
- **Access Token:** `EAABwzLixnjYBO...`
- **Webhook Verify Token:** `harvestlink_verify_123`

### **Option B: Twilio WhatsApp (Easier for Testing)**

#### **1.1 Enable WhatsApp on Twilio**
1. **Go to Twilio Console**
2. **Navigate to Messaging → Try it out**
3. **Click "Send a WhatsApp message"**
4. **Follow the sandbox setup**

#### **1.2 Get Twilio WhatsApp Number**
- **Sandbox Number:** `+1 415 523 8886`
- **Test Message:** `join <your-sandbox-code>`

## 🔧 **STEP 2: CONFIGURE WHATSAPP WEBHOOK**

### **For Meta Business API:**

#### **2.1 Set Webhook URL**
1. **Go to WhatsApp → Configuration**
2. **Set Webhook URL:** `https://harvestlink.onrender.com/whatsapp`
3. **Set Verify Token:** `harvestlink_verify_123`
4. **Click "Verify and Save"**

#### **2.2 Subscribe to Events**
1. **Check "messages"**
2. **Check "message_deliveries"**
3. **Click "Subscribe"**

### **For Twilio WhatsApp:**

#### **2.1 Configure Webhook**
1. **Go to Phone Numbers → Manage → Active Numbers**
2. **Click on your WhatsApp number**
3. **Set Webhook URL:** `https://harvestlink.onrender.com/whatsapp`
4. **Set HTTP Method:** `POST`
5. **Save Configuration**

## 🌐 **STEP 3: UPDATE RENDER ENVIRONMENT VARIABLES**

### **Add These Environment Variables in Render:**

#### **For Meta Business API:**
```
WHATSAPP_PHONE_NUMBER_ID=123456789012345
WHATSAPP_ACCESS_TOKEN=EAABwzLixnjYBO...
```

#### **For Twilio WhatsApp:**
```
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=+14155238886
```

## 📱 **STEP 4: TEST WHATSAPP INTEGRATION**

### **4.1 Test Webhook Verification**
Visit: `https://harvestlink.onrender.com/whatsapp?hub.verify_token=harvestlink_verify_123&hub.challenge=test123`

**Expected Response:** `test123`

### **4.2 Test WhatsApp Message**
Send WhatsApp message to your business number:
```
"maize 100kg Nairobi dry storage"
```

**Expected Response:**
```
🧠 HARVESTLINK AI ANALYSIS

📊 LOSS PREDICTION: HIGH risk
🎯 Confidence: 81.7%
🚨 AI Emergency: High loss risk! Immediate actions:
1) Dry maize urgently (within 24 hours)
2) Apply pest treatment
3) Sell within 3 days

💰 AI PRICE FORECAST: 204 KES/kg (7-day)
📈 Price Trend: Rising

🤝 BUYER MATCHES: 6 found
1. AgriCorp Kenya (Nairobi) - 200-250 KES/kg
2. Grain Traders Co (Kisumu) - 180-220 KES/kg

🔮 AI RECOMMENDATION: Hold for better price
```

## 🎯 **STEP 5: PRODUCTION SETUP**

### **5.1 Get Production WhatsApp Number**
1. **Apply for WhatsApp Business verification**
2. **Submit business documents**
3. **Wait for approval (1-3 days)**
4. **Get your production number**

### **5.2 Update Environment Variables**
Replace sandbox credentials with production ones.

### **5.3 Test with Real Users**
- **Share your WhatsApp number** with farmers
- **Test with different crop types**
- **Monitor logs for any issues**

## 📊 **STEP 6: MONITORING & ANALYTICS**

### **6.1 Check Render Logs**
1. **Go to Render Dashboard**
2. **Click "harvestlink" service**
3. **Click "Logs" tab**
4. **Monitor WhatsApp webhook activity**

### **6.2 Meta Business Manager**
1. **Go to Business Manager**
2. **Navigate to WhatsApp → Analytics**
3. **View message statistics**

## 🚨 **TROUBLESHOOTING**

### **Common Issues:**

#### **Webhook Verification Failed**
- **Check verify token** matches exactly
- **Ensure webhook URL** is accessible
- **Check Render service** is running

#### **Messages Not Sending**
- **Verify access token** is valid
- **Check phone number ID** is correct
- **Ensure user has opted in**

#### **No Response from AI**
- **Check Render logs** for errors
- **Verify message format** is correct
- **Test with simple message** first

## 🌾 **EXPECTED RESULT**

Once set up, farmers can:
- ✅ **Send WhatsApp messages** to your business number
- ✅ **Get instant AI analysis** of their crops
- ✅ **Receive loss predictions** and recommendations
- ✅ **Get buyer matches** and price forecasts
- ✅ **Access emergency advice** when needed

## 📞 **SUPPORT**

If you encounter issues:
1. **Check Render logs** first
2. **Verify webhook configuration**
3. **Test with simple messages**
4. **Contact Meta/Twilio support** if needed

**Your HarvestLink WhatsApp integration will be live and ready to serve Kenyan farmers!** 🚀
