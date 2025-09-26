import requests
import json
import time

def test_harvestlink_system():
    """Test the HarvestLink system with sample SMS inputs"""
    
    # Test cases
    test_cases = [
        {
            "name": "Maize Harvest - Low Risk",
            "sms": "maize 30kg Nairobi improved dry",
            "expected": "loss prediction and buyer matches"
        },
        {
            "name": "Tomatoes Harvest - High Risk",
            "sms": "tomatoes 20kg Mombasa traditional humid",
            "expected": "high risk warning and urgent advice"
        },
        {
            "name": "Rice Harvest - Medium Risk",
            "sms": "rice 100kg Kisumu traditional rainy",
            "expected": "medium risk and price forecast"
        },
        {
            "name": "Invalid Format",
            "sms": "hello world",
            "expected": "welcome message and format instructions"
        }
    ]
    
    print("🧪 Testing HarvestLink System")
    print("=" * 50)
    
    # Test local endpoint (if running locally)
    base_url = "http://localhost:5000"
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📱 Test {i}: {test_case['name']}")
        print(f"Input: {test_case['sms']}")
        
        try:
            # Simulate SMS webhook request
            response = requests.post(
                f"{base_url}/sms",
                data={
                    'Body': test_case['sms'],
                    'From': '+254700111111'
                },
                timeout=10
            )
            
            if response.status_code == 200:
                print(f"✅ Response: {response.text[:100]}...")
            else:
                print(f"❌ Error: HTTP {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Connection Error: Make sure the Flask app is running locally")
            print("   Run: python app.py")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
        
        time.sleep(1)  # Rate limiting
    
    print("\n" + "=" * 50)
    print("🎯 Test Summary:")
    print("- SMS parsing and ML prediction")
    print("- Loss risk assessment")
    print("- Buyer matching")
    print("- Price forecasting")
    print("- Error handling")

def test_ml_models():
    """Test ML models directly"""
    print("\n🤖 Testing ML Models")
    print("=" * 30)
    
    try:
        from app import ml_system
        
        # Test loss prediction
        prediction, prob = ml_system.predict_loss(
            crop_type='maize',
            storage_method='traditional',
            weather_condition='humid',
            humidity=80,
            temperature=30,
            storage_days=10,
            pest_signs=1
        )
        
        print(f"✅ Loss Prediction: {prediction} (probabilities: {prob})")
        
        # Test farmer clustering
        farmer_data = [
            {'crop_type': 'maize', 'location': 'Nairobi', 'quantity': 50, 'storage_method': 'traditional'},
            {'crop_type': 'maize', 'location': 'Nairobi', 'quantity': 60, 'storage_method': 'improved'},
            {'crop_type': 'rice', 'location': 'Mombasa', 'quantity': 30, 'storage_method': 'traditional'}
        ]
        
        clusters = ml_system.cluster_farmers(farmer_data)
        print(f"✅ Farmer Clusters: {clusters}")
        
        # Test price forecasting
        price = ml_system.forecast_price('maize', 7)
        print(f"✅ Price Forecast: {price:.2f} KES/kg")
        
    except ImportError:
        print("❌ Cannot import ML system - run from project root")
    except Exception as e:
        print(f"❌ ML Test Error: {e}")

def test_database():
    """Test database operations"""
    print("\n💾 Testing Database")
    print("=" * 20)
    
    try:
        import sqlite3
        
        conn = sqlite3.connect('harvestlink.db')
        cursor = conn.cursor()
        
        # Test farmers table
        cursor.execute('SELECT COUNT(*) FROM farmers')
        farmer_count = cursor.fetchone()[0]
        print(f"✅ Farmers in DB: {farmer_count}")
        
        # Test buyers table
        cursor.execute('SELECT COUNT(*) FROM buyers')
        buyer_count = cursor.fetchone()[0]
        print(f"✅ Buyers in DB: {buyer_count}")
        
        # Test transactions table
        cursor.execute('SELECT COUNT(*) FROM transactions')
        transaction_count = cursor.fetchone()[0]
        print(f"✅ Transactions in DB: {transaction_count}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Database Error: {e}")

if __name__ == '__main__':
    print("🌾 HarvestLink System Test Suite")
    print("=" * 40)
    
    # Run all tests
    test_database()
    test_ml_models()
    test_harvestlink_system()
    
    print("\n🎉 Testing Complete!")
    print("\nNext Steps:")
    print("1. Set up Twilio account and phone number")
    print("2. Configure environment variables")
    print("3. Deploy to Heroku")
    print("4. Test with real SMS messages")
