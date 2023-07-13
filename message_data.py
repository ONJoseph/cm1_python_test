import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV
data = pd.read_csv('message_data.csv')

# Parse message_time column as datetime
data['message_time'] = pd.to_datetime(data['message_time'], format='%Y-%m-%d %H:%M:%S.%f%z', errors='coerce')

# Identify first message sent by each user
first_messages = data.groupby('author_id')['message_time'].min().reset_index()

# Calculate daily count of messages and new users
daily_counts = data.resample('D', on='message_time').size()
daily_new_users = first_messages.resample('D', on='message_time').size()

# Calculate percentage of daily messages sent by new users
percentage_new_users = (daily_new_users / daily_counts) * 100

# Generate interactive chart
plt.figure(figsize=(10, 6))
percentage_new_users.plot(kind='line', marker='o')
plt.title('Percentage of Daily Messages Sent by New Users')
plt.xlabel('Date')
plt.ylabel('Percentage')
plt.grid(True)
plt.show()
