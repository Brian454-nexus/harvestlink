import sqlite3
import random
from datetime import datetime, timedelta

def seed_database():
    """Seed the database with sample buyers and farmers"""
    conn = sqlite3.connect('harvestlink.db')
    cursor = conn.cursor()
    
    # Sample buyers data
    buyers_data = [
        ('AgriCorp Kenya', '+254700123456', 'maize,wheat,beans', 'Nairobi', '200-250 KES/kg'),
        ('Fresh Produce Ltd', '+254700234567', 'tomatoes,beans', 'Mombasa', '150-200 KES/kg'),
        ('Grain Traders Co', '+254700345678', 'maize,rice,wheat', 'Kisumu', '180-220 KES/kg'),
        ('Farm Fresh Kenya', '+254700456789', 'all', 'Nakuru', 'Market rate'),
        ('Export Quality Foods', '+254700567890', 'maize,wheat', 'Eldoret', '220-280 KES/kg'),
        ('Local Market Hub', '+254700678901', 'all', 'Thika', 'Competitive rates'),
        ('Organic Farmers Coop', '+254700789012', 'beans,tomatoes', 'Meru', 'Premium rates'),
        ('Bulk Buyers Kenya', '+254700890123', 'maize,rice', 'Kakamega', 'Wholesale rates')
    ]
    
    # Insert buyers
    cursor.executemany('''
        INSERT OR REPLACE INTO buyers (name, phone, crops_interested, location, price_range)
        VALUES (?, ?, ?, ?, ?)
    ''', buyers_data)
    
    # Sample farmers data
    farmers_data = [
        ('+254700111111', 'John Mwangi', 'Nairobi', 'maize'),
        ('+254700222222', 'Mary Wanjiku', 'Mombasa', 'tomatoes'),
        ('+254700333333', 'Peter Ochieng', 'Kisumu', 'rice'),
        ('+254700444444', 'Grace Akinyi', 'Nakuru', 'wheat'),
        ('+254700555555', 'David Kimani', 'Eldoret', 'beans')
    ]
    
    # Insert farmers
    cursor.executemany('''
        INSERT OR REPLACE INTO farmers (phone, name, location, crops)
        VALUES (?, ?, ?, ?)
    ''', farmers_data)
    
    # Sample transactions for price forecasting
    transactions_data = []
    crops = ['maize', 'rice', 'wheat', 'beans', 'tomatoes']
    base_prices = {'maize': 200, 'rice': 300, 'wheat': 250, 'beans': 400, 'tomatoes': 150}
    
    for i in range(50):  # 50 sample transactions
        crop = random.choice(crops)
        base_price = base_prices[crop]
        price = base_price + random.randint(-50, 50)
        quantity = random.uniform(10, 100)
        
        transactions_data.append((
            random.randint(1, 5),  # farmer_id
            random.randint(1, 8),  # buyer_id
            crop,
            quantity,
            price,
            datetime.now() - timedelta(days=random.randint(1, 90))
        ))
    
    cursor.executemany('''
        INSERT INTO transactions (farmer_id, buyer_id, crop_type, quantity, price, transaction_date)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', transactions_data)
    
    conn.commit()
    conn.close()
    
    print("✅ Database seeded successfully!")
    print("📊 Added 8 buyers and 5 sample farmers")
    print("💰 Added 50 sample transactions for price forecasting")

if __name__ == '__main__':
    seed_database()
