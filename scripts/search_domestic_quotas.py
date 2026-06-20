#!/usr/bin/env python3
"""搜索国内限额相关消息（QDII/跨境投资/外汇限额等）"""
import requests, json, os

def main():
    api_key = os.environ.get('TAVILY_API_KEY', '')
    if not api_key:
        print("错误: TAVILY_API_KEY 未设置")
        return 1

    headers = {'Content-Type': 'application/json'}
    queries = [
        'A股 跨境投资 额度 限额 最新消息',
        'QDII 额度 限制',
        '外汇 资本流动 限制 额度',
    ]

    for q in queries:
        print(f'\n🔍 搜索: {q}')
        try:
            resp = requests.post(
                'https://api.tavily.com/search',
                json={'api_key': api_key, 'query': q, 'search_depth': 'basic', 'max_results': 5},
                headers=headers, timeout=15
            )
            if resp.status_code == 200:
                results = resp.json().get('results', [])
                for r in results:
                    title = r.get('title', '')
                    url = r.get('url', '')
                    txt = r.get('content', '')[:300]
                    print(f'  - [{title}]({url})')
                    if txt:
                        print(f'    {txt}')
            else:
                print(f'  (搜索出错: {resp.status_code})')
        except Exception as e:
            print(f'  (搜索失败: {e})')
    return 0

if __name__ == '__main__':
    exit(main())
