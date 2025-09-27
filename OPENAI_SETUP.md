# OpenAI API Setup Guide

## Setting up GPT-4o-mini Integration

To enable the advanced GPT-4o-mini features in HarvestLink, you need to configure your OpenAI API key.

### Step 1: Get OpenAI API Key

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the API key (starts with `sk-`)

### Step 2: Configure Environment Variable

#### For Local Development:
1. Create a `.env` file in your project root
2. Add your API key:
```
OPENAI_API_KEY=sk-your-actual-api-key-here
```

#### For Render Deployment:
1. Go to your Render dashboard
2. Select your HarvestLink service
3. Go to Environment tab
4. Add new environment variable:
   - Key: `OPENAI_API_KEY`
   - Value: `sk-your-actual-api-key-here`

### Step 3: Test the Integration

Once configured, the web interface will show:
- 🤖 GPT-4o-mini Crop Conditions Analysis
- 🧠 Smart Recommendations
- 📊 Market Intelligence

### Features Enabled with OpenAI:

1. **Natural Language Analysis**: GPT analyzes crop conditions from text descriptions
2. **Smart Recommendations**: AI-generated actionable advice for farmers
3. **Market Intelligence**: Advanced market analysis and trends
4. **Hybrid AI System**: Combines custom ML models with GPT reasoning

### Cost Information:

- GPT-4o-mini is very cost-effective
- Typical usage: $0.001-0.01 per analysis
- Free tier available for testing

### Troubleshooting:

If you see "AI analysis requires OpenAI API key configuration":
1. Check that the environment variable is set correctly
2. Verify the API key is valid
3. Ensure you have credits in your OpenAI account

The system will work without the API key, but GPT features will be disabled.
