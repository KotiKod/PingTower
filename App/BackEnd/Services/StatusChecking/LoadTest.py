import aiohttp
import asyncio
import time
from collections import Counter

async def fetch(session, url):
    start = time.time()
    try:
        async with session.get(url) as response:
            status = response.status
    except Exception as e:
        status = str(e)
    end = time.time()
    return status, end - start

async def load_test(url, num_requests=100, concurrency=10):
    sem = asyncio.Semaphore(concurrency)

    async def bound_fetch(session, url):
        async with sem:
            return await fetch(session, url)

    async with aiohttp.ClientSession() as session:
        tasks = [bound_fetch(session, url) for _ in range(num_requests)]
        results = await asyncio.gather(*tasks)
    return results

def test(url, num_requests=100, concurrency=10):

    start_time = time.time()
    results = asyncio.run(load_test(url, num_requests, concurrency))
    end_time = time.time()

    statuses, times = zip(*results)

    success_count = sum(1 for s in statuses if isinstance(s, int) and 200 <= s < 400)
    error_count = num_requests - success_count
    avg_time = sum(times) / len(times)

    status_counter = Counter(s if isinstance(s, int) else 'error' for s in statuses)

    report = {
        "url": url,
        "total_requests": num_requests,
        "successful_requests": success_count,
        "failed_requests": error_count,
        "error_percentage": round((error_count / num_requests) * 100, 2),
        "average_response_time_sec": round(avg_time, 3),
        "total_time_sec": round(end_time - start_time, 3),
        "status_breakdown": dict(status_counter)
    }

    return report

def main():
    url = "https://www.google.com"
    num_requests = 100
    concurrency = 10
    utest = test(url, num_requests, concurrency)
    print(utest)

if __name__ == "__main__":
    main()