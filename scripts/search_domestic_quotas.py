#!/usr/bin/env python3
import requests, json, os

def main():
    api_key = os.environ.get('TAVILY_API_KEY', '')
    if not api_key:
        print("Error: TAVILY_API_KEY not set")
        return 1
    queries = [
        'A股 跨境投资 额度 限额 最新消息',
        'QDII 额度 限制',
        '外汇 资本流动 限制 额度',
    ]
    for q in queries:
        print(f'\nSearch: {q}')
        try:
            r = requests.post('https://api.tavily.com/search',
                json={'api_key': api_key, 'query': q, 'search_depth': 'basic', 'max_results': 5},
                timeout=15)
            if r.status_code == 200:
                for item in r.json().get('results', []):
                    t, u = item.get('title', ''), item.get('url', '')
                    c = item.get('content', '')[:300]
                    print(f'  - [{t}]({u})')
                    if c: print(f'    {c}')
            else:
                print(f'  (error: {r.status_code})')
        except Exception as e:
            print(f'  (failed: {e})')
    return 0

if __name__ == '__main__':
    exit(main())
