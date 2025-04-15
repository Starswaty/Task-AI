def create_features(data):
    data['Prev_Close'] = data['Close'].shift(1)
    data['Prev_Volume'] = data['Volume'].shift(1)
    data['MA_3'] = data['Close'].rolling(window=3).mean().shift(1)
    data['MA_7'] = data['Close'].rolling(window=7).mean().shift(1)
    data['Target'] = data['Close'].shift(-1)
    data.dropna(inplace=True)
    features = ['Prev_Close', 'Prev_Volume', 'MA_3', 'MA_7']
    return data[features], data['Target']

