#!/bin/bash

# HarvestLink Deployment Script
echo "🌾 HarvestLink Deployment Script"
echo "================================"

# Check if Heroku CLI is installed
if ! command -v heroku &> /dev/null; then
    echo "❌ Heroku CLI not found. Please install it first:"
    echo "   https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Check if logged into Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo "❌ Not logged into Heroku. Please login first:"
    echo "   heroku login"
    exit 1
fi

# Create Heroku app (if it doesn't exist)
APP_NAME="harvestlink-$(date +%s)"
echo "📱 Creating Heroku app: $APP_NAME"
heroku create $APP_NAME

# Set environment variables
echo "🔧 Setting up environment variables..."
echo "Please enter your Twilio credentials:"
read -p "Twilio Account SID: " TWILIO_SID
read -p "Twilio Auth Token: " TWILIO_TOKEN
read -p "Twilio Phone Number: " TWILIO_PHONE

heroku config:set TWILIO_ACCOUNT_SID=$TWILIO_SID --app $APP_NAME
heroku config:set TWILIO_AUTH_TOKEN=$TWILIO_TOKEN --app $APP_NAME
heroku config:set TWILIO_PHONE_NUMBER=$TWILIO_PHONE --app $APP_NAME

# Deploy to Heroku
echo "🚀 Deploying to Heroku..."
git add .
git commit -m "Deploy HarvestLink to Heroku"
git push heroku main

# Get app URL
APP_URL=$(heroku apps:info --app $APP_NAME | grep "Web URL" | awk '{print $2}')
echo "✅ Deployment complete!"
echo "🌐 App URL: $APP_URL"
echo "📱 SMS Webhook URL: $APP_URL/sms"

echo ""
echo "🔧 Next Steps:"
echo "1. Configure Twilio webhook URL: $APP_URL/sms"
echo "2. Test with SMS: Send 'maize 50kg Nairobi traditional dry' to your Twilio number"
echo "3. Monitor logs: heroku logs --tail --app $APP_NAME"
echo "4. Scale if needed: heroku ps:scale web=1 --app $APP_NAME"

echo ""
echo "🎉 HarvestLink is now live and ready to empower African farmers!"
