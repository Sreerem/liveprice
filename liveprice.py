import websocket
import json

def on_message(ws, message):
    data = json.loads(message)
    price = data['p']
    print(f"Live BTC/USDT Price: ${price}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")

def on_open(ws):
    subscribe_message = {
        "method": "SUBSCRIBE",
        "params": ["btcusdt@trade"],
        "id": 1
    }
    ws.send(json.dumps(subscribe_message))

if __name__ == "__main__":
    socket_url = "wss://stream.binance.com:9443/ws/btcusdt@trade"
    ws = websocket.WebSocketApp(
        socket_url,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    print("Connecting to Binance WebSocket for real-time BTC/USDT trades...")
    ws.run_forever()
