import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Load data
print("Loading sales data...")
df = pd.read_csv('data/TableauSalesData.csv')

# Create feature names
feature_names = ['Discount', 'Quantity']

# Prepare data with named features
X = pd.DataFrame(df[feature_names], columns=feature_names)
y = df['Profit']

# Create and train model
print("\nTraining model...")
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Test different discount rates
print("\nAnalyzing discount rates...")
avg_quantity = df['Quantity'].mean()
test_discounts = np.arange(0, 0.51, 0.01)

# Create DataFrame for predictions
test_data = pd.DataFrame({
    'Discount': test_discounts,
    'Quantity': [avg_quantity] * len(test_discounts)
}, columns=feature_names)

# Make predictions
predictions = model.predict(test_data)

# Create results DataFrame
results_df = pd.DataFrame({
    'discount_rate': test_discounts * 100,
    'predicted_profit': predictions
})

# Find best discount rate
best_result = results_df.loc[results_df['predicted_profit'].idxmax()]

# Print results
print("\n=== RESULTS ===")
print(f"\nBest Discount Rate: {best_result['discount_rate']:.1f}%")
print(f"Predicted Profit at this rate: ${best_result['predicted_profit']:.2f}")

current_avg_discount = df['Discount'].mean() * 100
current_avg_profit = df['Profit'].mean()

print(f"\nCurrent Average Discount: {current_avg_discount:.1f}%")
print(f"Current Average Profit: ${current_avg_profit:.2f}")

# Visualize results
plt.figure(figsize=(10, 6))
plt.plot(results_df['discount_rate'], results_df['predicted_profit'], 
         color='blue', label='Predicted Profit')
plt.scatter(best_result['discount_rate'], best_result['predicted_profit'], 
           color='red', s=100, label='Best Rate')

plt.title('Profit by Discount Rate', fontsize=14)
plt.xlabel('Discount Rate (%)')
plt.ylabel('Predicted Profit ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()

# Print recommendations
print("\n=== RECOMMENDATIONS ===")
if best_result['discount_rate'] < current_avg_discount:
    print("1. Consider REDUCING your average discount rate")
    print(f"   Current: {current_avg_discount:.1f}%")
    print(f"   Recommended: {best_result['discount_rate']:.1f}%")
else:
    print("1. Consider INCREASING your average discount rate")
    print(f"   Current: {current_avg_discount:.1f}%")
    print(f"   Recommended: {best_result['discount_rate']:.1f}%")

# Find profitable range
profitable_rates = results_df[results_df['predicted_profit'] > 0]
print(f"\n2. Profitable Discount Range:")
print(f"   From: {profitable_rates['discount_rate'].min():.1f}%")
print(f"   To: {profitable_rates['discount_rate'].max():.1f}%")

# Additional insights
print("\n3. Additional Insights:")
high_discount_profit = df[df['Discount'] > 0.3]['Profit'].mean()
low_discount_profit = df[df['Discount'] <= 0.3]['Profit'].mean()

if high_discount_profit < low_discount_profit:
    print("   - High discounts (>30%) are reducing average profits")
    print(f"   - Average profit with high discounts: ${high_discount_profit:.2f}")
    print(f"   - Average profit with low discounts: ${low_discount_profit:.2f}")

if best_result['predicted_profit'] > current_avg_profit:
    potential_increase = best_result['predicted_profit'] - current_avg_profit
    print(f"   - Potential profit increase per sale: ${potential_increase:.2f}")

