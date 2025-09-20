import asyncio
import aiodns
from urllib.parse import urlparse

class DNSCheck:
    async def resolve_url(url: str, server: str = "8.8.8.8", rdtype: str = "A", timeout: float = 5.0):
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        if not host:
            return {"ok": False, "url": url, "error": "Invalid host"}

        resolver = aiodns.DNSResolver(nameservers=[server], timeout=timeout)
        try:
            answers = await resolver.query(host, rdtype)
            results = [a.host for a in answers] if hasattr(answers[0], "host") else [str(a) for a in answers]
            return {"ok": True, "url": url, "results": results}
        except Exception as e:
            return {"ok": False, "url": url, "error": str(e)}


# async def main():
#     url = "https://google.com"
#     server = "8.8.8.8"
#     rdtype = "A"
#     timeout = 5.0
#     print(await resolve_url(url, server, rdtype, timeout))
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
