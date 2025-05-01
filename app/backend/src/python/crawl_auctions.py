import requests
import json
import sys

# eBay API 설정
API_URL = "https://api.ebay.com/buy/browse/v1/item_summary/search"
HEADERS = {
    "Content-Type": "application/json",
}

# 경매 데이터를 수집하는 함수
def fetch_auctions(query="laptop"):
    headers = {
        **HEADERS,
        "Authorization": f"Bearer {access_token}",
    }

    params = {
        "q": query,
        "filter": "buyingOptions:{AUCTION}",
        "sort": "popularityRank",
        "limit": 10,
    }
    response = requests.get(API_URL, headers=HEADERS, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching auctions: {response.status_code} - {response.text}")
        return {}

if __name__ == "__main__":
    # 명령줄 인수로 ACCESS_TOKEN과 검색어(query) 전달
    if len(sys.argv) < 2:
        print("Usage: python crawl_auctions.py <ACCESS_TOKEN> [query]")
        sys.exit(1)

    access_token = sys.argv[1]
    query = sys.argv[2] if len(sys.argv) > 2 else "laptop"

    data = fetch_auctions(access_token, query)
    print(json.dumps(data, indent=2))


# def fetch_auction_data():
#     # 크롤링하여 경매 데이터를 가져옴 (예시 데이터 사용)
#     data = [
#         {"id": 1, "title": "Item A", "currentBid": 100, "endTime": "2024-12-30T12:00:00Z"},
#         {"id": 2, "title": "Item B", "currentBid": 200, "endTime": "2024-12-31T14:00:00Z"}
#     ]
#     return data 

# if __name__ ==  "__main__":
#     auction_data = fetch_auction_data()
#     print(json.dumps(auction_data))