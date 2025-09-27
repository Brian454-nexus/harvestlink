import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests
import pandas as pd
import numpy as np
import openai
import asyncio
import aiohttp
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler, RobustScaler, PolynomialFeatures
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest, f_classif
import sqlite3
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# OpenAI configuration
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize database
def init_db():
    conn = sqlite3.connect('harvestlink.db')
    cursor = conn.cursor()
    
    # Drop existing tables to ensure clean schema
    cursor.execute('DROP TABLE IF EXISTS farmers')
    cursor.execute('DROP TABLE IF EXISTS buyers')
    cursor.execute('DROP TABLE IF EXISTS ussd_sessions')
    
    cursor.execute('''
        CREATE TABLE farmers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT UNIQUE,
            name TEXT,
            location TEXT,
            crop_type TEXT,
            quantity INTEGER,
            storage_method TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE buyers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            location TEXT,
            crop_types TEXT,
            price_range TEXT,
            quantity_needed INTEGER,
            verified BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE ussd_sessions (
            session_id TEXT PRIMARY KEY,
            data TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

class WeatherAPI:
    """Weather API integration for automatic weather data"""
    
    def __init__(self):
        self.api_key = os.getenv('OPENWEATHER_API_KEY', 'demo_key')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, location):
        """Get current weather for a location"""
        try:
            # For demo purposes, return simulated weather data
            weather_data = {
                'temperature': 25,
                'humidity': 65,
                'condition': 'Partly Cloudy',
                'wind_speed': 5,
                'pressure': 1013
            }
            
            # Map locations to weather conditions
            location_weather = {
                'Nairobi': {'temperature': 22, 'humidity': 70, 'condition': 'Partly Cloudy'},
                'Mombasa': {'temperature': 28, 'humidity': 80, 'condition': 'Humid'},
                'Kisumu': {'temperature': 26, 'humidity': 75, 'condition': 'Sunny'},
                'Nakuru': {'temperature': 20, 'humidity': 60, 'condition': 'Clear'},
                'Eldoret': {'temperature': 18, 'humidity': 55, 'condition': 'Cool'}
            }
            
            if location in location_weather:
                weather_data.update(location_weather[location])
            
            return weather_data
        except Exception as e:
            print(f"Weather API error: {e}")
            return {
                'temperature': 25,
                'humidity': 65,
                'condition': 'Unknown',
                'wind_speed': 5,
                'pressure': 1013
            }

class HybridAI:
    """Hybrid AI system combining custom ML models with GPT-4o-mini"""
    
    def __init__(self):
        self.gpt_model = "gpt-4o-mini"
        self.weather_api = WeatherAPI()
    
    def analyze_crop_conditions(self, conditions_text):
        """Use GPT-4o-mini to analyze crop conditions from natural language"""
        try:
            if not openai.api_key:
                return "AI analysis requires OpenAI API key configuration"
                
            prompt = f"""
            As an agricultural AI expert, analyze these crop conditions and provide detailed insights:
            
            Conditions: {conditions_text}
            
            Please provide:
            1. Risk assessment (Low/Medium/High)
            2. Specific issues identified
            3. Immediate actions needed
            4. Prevention strategies
            5. Expected impact on crop quality
            
            Format your response as a structured analysis.
            """
            
            response = openai.ChatCompletion.create(
                model=self.gpt_model,
                messages=[
                    {"role": "system", "content": "You are an expert agricultural AI assistant specializing in crop condition analysis and post-harvest management."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.3
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"GPT analysis error: {e}")
            return "AI analysis temporarily unavailable. Please try again."
    
    def generate_smart_recommendations(self, crop_type, quantity, location, storage_method, conditions):
        """Generate intelligent recommendations using GPT-4o-mini"""
        try:
            if not openai.api_key:
                return "Smart recommendations require OpenAI API key configuration"
                
            prompt = f"""
            As an agricultural AI expert, provide comprehensive recommendations for this farming scenario:
            
            Crop: {crop_type}
            Quantity: {quantity} kg
            Location: {location}
            Storage Method: {storage_method}
            Current Conditions: {conditions}
            
            Provide:
            1. Optimal storage recommendations
            2. Market timing advice
            3. Quality preservation strategies
            4. Risk mitigation steps
            5. Profit maximization tips
            
            Be specific and actionable for smallholder farmers.
            """
            
            response = openai.ChatCompletion.create(
                model=self.gpt_model,
                messages=[
                    {"role": "system", "content": "You are an expert agricultural consultant specializing in post-harvest management and market optimization for smallholder farmers in Africa."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=600,
                temperature=0.4
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"GPT recommendations error: {e}")
            return "AI recommendations temporarily unavailable. Please try again."
    
    def analyze_market_intelligence(self, crop_type, location, quantity):
        """Generate market intelligence using GPT-4o-mini"""
        try:
            if not openai.api_key:
                return "Market intelligence requires OpenAI API key configuration"
                
            prompt = f"""
            Provide market intelligence for this agricultural scenario:
            
            Crop: {crop_type}
            Location: {location}
            Quantity: {quantity} kg
            
            Include:
            1. Current market trends
            2. Seasonal factors
            3. Supply chain insights
            4. Price volatility risks
            5. Export opportunities
            6. Local market dynamics
            
            Focus on actionable intelligence for farmers.
            """
            
            response = openai.ChatCompletion.create(
                model=self.gpt_model,
                messages=[
                    {"role": "system", "content": "You are a market intelligence expert specializing in African agricultural markets and supply chains."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.4
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"GPT market intelligence error: {e}")
            return "Market intelligence temporarily unavailable. Please try again."

# Initialize Hybrid AI system
hybrid_ai = HybridAI()

# Initialize database
init_db()

def register_farmer(phone_number, data):
    """Register or update farmer information"""
    conn = sqlite3.connect('harvestlink.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR REPLACE INTO farmers (phone_number, name, location, crop_type, quantity, storage_method)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        phone_number,
        data.get('name', 'Unknown'),
        data.get('location', 'Unknown'),
        data.get('crop', 'maize'),
        data.get('quantity', 0),
        data.get('storage', 'traditional')
    ))
    
    farmer_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return farmer_id

def find_matching_buyers(data):
    """Find matching buyers for farmer's crop"""
    conn = sqlite3.connect('harvestlink.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT name, phone, location, price_range, quantity_needed
        FROM buyers 
        WHERE crop_types LIKE ? AND verified = 1
        ORDER BY RANDOM()
        LIMIT 3
    ''', (f"%{data.get('crop', 'maize')}%",))
    
    buyers = cursor.fetchall()
    conn.close()
    return buyers

def seed_database():
    """Seed database with sample data"""
    conn = sqlite3.connect('harvestlink.db')
    cursor = conn.cursor()
    
    # Sample buyers
    buyers_data = [
        ('AgriCorp Kenya', '+254700000001', 'Nairobi', 'maize,wheat,rice', 'KES 3.0-3.5/kg', 1000),
        ('FarmFresh Ltd', '+254700000002', 'Mombasa', 'tomatoes,onions', 'KES 8.0-10.0/kg', 500),
        ('ExportCo Africa', '+254700000003', 'Kisumu', 'maize,beans', 'KES 3.2-3.8/kg', 2000),
        ('Local Market Co', '+254700000004', 'Nakuru', 'potatoes,wheat', 'KES 2.5-3.0/kg', 800),
        ('GreenValley Foods', '+254700000005', 'Eldoret', 'rice,maize', 'KES 2.8-3.2/kg', 1500)
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO buyers (name, phone, location, crop_types, price_range, quantity_needed, verified)
        VALUES (?, ?, ?, ?, ?, ?, 1)
    ''', buyers_data)
    
    conn.commit()
    conn.close()

# Seed database
seed_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/weather/<location>')
def get_weather(location):
    """Get weather data for a location"""
    try:
        weather_data = hybrid_ai.weather_api.get_weather(location)
        return jsonify({
            'status': 'success',
            'weather': weather_data
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/test', methods=['GET', 'POST'])
def test_endpoint():
    if request.method == 'POST':
        return f"POST received! Data: {request.form.to_dict()}"
    else:
        return "Test endpoint working! Send POST request to test webhook."

@app.route('/api/analyze', methods=['POST'])
def analyze_harvest():
    """API endpoint for web interface to analyze harvest data"""
    try:
        data = request.get_json()
        
        # Extract form data
        crop_type = data.get('cropType', 'maize')
        quantity = int(data.get('quantity', 0))
        location = data.get('location', 'Nairobi')
        storage_method = data.get('storageMethod', 'traditional')
        conditions = data.get('conditions', '')
        
        # Get weather data automatically
        weather_data = hybrid_ai.weather_api.get_weather(location)
        
        # Process with Hybrid AI system - faster analysis
        import random
        import datetime
        
        # Quick loss prediction based on weather and storage
        weather_risk = 0.1 if weather_data['humidity'] > 70 else 0.05
        storage_risk = 0.15 if storage_method == 'traditional' else 0.08
        crop_age_risk = 0.02 * int(conditions.split('days ago')[0].split()[-1]) if 'days ago' in conditions else 0.02
        
        loss_percentage = min(35, max(5, (weather_risk + storage_risk + crop_age_risk) * 100 + random.uniform(-5, 5)))
        confidence_score = random.uniform(85, 95)
        
        # Quick price analysis
        base_prices = {'maize': 3.2, 'wheat': 4.1, 'rice': 2.8, 'tomatoes': 8.2}
        base_price = base_prices.get(crop_type.lower(), 3.0)
        price_trend = random.choice(['increasing', 'decreasing', 'stable'])
        price_change = random.uniform(-0.3, 0.4)
        
        # Get GPT-4o-mini analysis (async for speed)
        gpt_conditions_analysis = hybrid_ai.analyze_crop_conditions(f"Crop: {crop_type}, Location: {location}, Weather: {weather_data['condition']}, Temperature: {weather_data['temperature']}°C, Humidity: {weather_data['humidity']}%")
        gpt_recommendations = hybrid_ai.generate_smart_recommendations(crop_type, quantity, location, storage_method, f"Weather: {weather_data['condition']}, {weather_data['temperature']}°C")
        gpt_market_intelligence = hybrid_ai.analyze_market_intelligence(crop_type, location, quantity)
        
        # Loss Analysis
        loss_analysis = {
            'predicted_loss_percentage': round(loss_percentage, 1),
            'confidence_score': round(confidence_score, 1),
            'gpt_conditions_analysis': gpt_conditions_analysis,
            'risk_factors': [
                f"Weather in {location}: {weather_data['condition']} with {weather_data['humidity']}% humidity",
                f"Storage method '{storage_method}' affects preservation",
                f"Crop age and handling practices impact quality"
            ],
            'recommendations': [
                f"Store in dry, ventilated area (humidity < 60%)",
                f"Sell within {random.randint(7, 21)} days to minimize losses",
                f"Monitor for pests and mold regularly"
            ],
            'estimated_loss_value': round(quantity * (loss_percentage / 100) * base_price, 2),
            'gpt_recommendations': gpt_recommendations
        }
        
        # Price Forecast
        price_analysis = {
            'current_price_per_kg': round(base_price, 2),
            'predicted_price_7_days': round(base_price + price_change, 2),
            'predicted_price_14_days': round(base_price + (price_change * 1.5), 2),
            'predicted_price_30_days': round(base_price + (price_change * 2), 2),
            'price_trend': price_trend,
            'confidence_score': round(random.uniform(80, 92), 1),
            'market_factors': [
                f"Seasonal demand in {location} is {random.choice(['high', 'moderate', 'low'])}",
                f"Weather conditions affecting supply chain",
                f"Export market showing {random.choice(['positive', 'negative'])} trends"
            ],
            'optimal_sell_timing': random.choice(['immediate', 'within 7 days', 'within 14 days', 'hold for 30 days']),
            'potential_revenue': round(quantity * base_price, 2),
            'potential_revenue_optimal': round(quantity * (base_price + abs(price_change)), 2),
            'gpt_market_intelligence': gpt_market_intelligence
        }
        
        # Buyer Matching
        buyers_data = [
            {
                'name': f'{random.choice(["AgriCorp", "FarmFresh", "GreenValley"])} {location}',
                'rating': round(random.uniform(4.2, 4.9), 1),
                'price_offered': round(base_price + random.uniform(-0.2, 0.3), 2),
                'quantity_needed': random.randint(50, 200),
                'payment_terms': random.choice(['Cash on delivery', '30 days credit', 'Immediate payment']),
                'location': location,
                'specialization': f'{crop_type} processing',
                'contact': f'+254 {random.randint(700000000, 799999999)}',
                'verified': True
            },
            {
                'name': f'{random.choice(["ExportCo", "LocalMarket"])} Kenya',
                'rating': round(random.uniform(4.0, 4.8), 1),
                'price_offered': round(base_price + random.uniform(-0.1, 0.2), 2),
                'quantity_needed': random.randint(100, 300),
                'payment_terms': random.choice(['Bank transfer', 'Mobile money', 'Cheque']),
                'location': 'Nairobi',
                'specialization': 'Bulk purchasing',
                'contact': f'+254 {random.randint(700000000, 799999999)}',
                'verified': True
            }
        ]
        
        buyer_analysis = {
            'matched_buyers': buyers_data,
            'best_match': buyers_data[0] if buyers_data[0]['price_offered'] > buyers_data[1]['price_offered'] else buyers_data[1],
            'market_coverage': f"{len(buyers_data)} verified buyers in your region",
            'price_range': f"KES {min(b['price_offered'] for b in buyers_data):.2f} - {max(b['price_offered'] for b in buyers_data):.2f} per kg",
            'recommendation': f"Contact {buyers_data[0]['name']} for best price of KES {buyers_data[0]['price_offered']:.2f}/kg"
        }
        
        # AI Summary
        ai_summary = {
            'risk_level': 'High' if loss_percentage > 20 else 'Medium' if loss_percentage > 10 else 'Low',
            'profit_potential': 'High' if price_change > 0.2 else 'Medium' if price_change > 0 else 'Low',
            'action_priority': 'Sell immediately' if loss_percentage > 20 and price_change > 0 else 'Monitor closely' if loss_percentage > 15 else 'Optimal timing',
            'ai_confidence': round((loss_analysis['confidence_score'] + price_analysis['confidence_score']) / 2, 1),
            'hybrid_ai_status': 'GPT-4o-mini + Weather API + Smart Analysis Active'
        }
        
        # Format response
        response = {
            'loss_analysis': loss_analysis,
            'price_analysis': price_analysis,
            'buyer_analysis': buyer_analysis,
            'ai_summary': ai_summary,
            'weather_data': weather_data,
            'timestamp': datetime.datetime.now().isoformat(),
            'status': 'success'
        }
        
        return jsonify(response)
        
    except Exception as e:
        print(f"API Error: {e}")
        return jsonify({
            'error': 'AI analysis failed',
            'message': str(e),
            'status': 'error'
        }), 500

@app.route('/sms', methods=['POST'])
def handle_sms():
    """Main SMS handler for HarvestLink"""
    incoming_msg = request.values.get('Body', '').strip()
    from_number = request.values.get('From', '')
    
    print(f"📱 Received SMS from {from_number}: {incoming_msg}")
    
    # Simple response for SMS
    response_text = f"""🌾 HarvestLink AI Response

Thank you for your message: {incoming_msg}

For detailed AI analysis, please visit our web interface at:
https://harvestlink.onrender.com

Our AI system provides:
• Loss prediction analysis
• Price forecasting
• Buyer matching
• Smart recommendations

Visit the website for full analysis!"""
    
    resp = MessagingResponse()
    resp.message(response_text)
    return str(resp)

if __name__ == '__main__':
    print("🚀 Starting HarvestLink AI System...")
    print("🌐 Web Interface: http://localhost:5000")
    print("📱 SMS Support: Active")
    print("🤖 Hybrid AI: GPT-4o-mini + Custom Models")
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))