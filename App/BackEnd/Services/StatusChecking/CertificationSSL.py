import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime, timezone


class CertificationSSL:
    def check_ssl_certificate(url: str, timeout: float = 3.0):
        """
        Проверяет SSL-сертификат сайта по URL.
        """
        parsed = urlparse(url)
        host = parsed.hostname
        port = parsed.port or 443

        # Контекст с проверкой сертификата
        ctx = ssl.create_default_context()
        ctx.check_hostname = True
        ctx.verify_mode = ssl.CERT_REQUIRED

        try:
            with socket.create_connection((host, port), timeout=timeout) as sock:
                # ВАЖНО: указываем server_hostname=host для SNI
                with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                    cert = ssock.getpeercert()

            not_before = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
            not_after = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
            now = datetime.now(timezone.utc)

            return {
                "ok": True,
                "url": url,
                "host": host,
                "issuer": dict(x[0] for x in cert['issuer']),
                "subject": dict(x[0] for x in cert['subject']),
                "not_before": not_before.isoformat(),
                "not_after": not_after.isoformat(),
                "expired": now > not_after,
                "valid_now": not_before <= now <= not_after,
            }
        except Exception as e:
            return {"ok": False, "url": url, "error": str(e)}


# def main():
#     url = ("https://www.google.com/")
#     print(check_ssl_certificate(url))
#
#
# if __name__ == "__main__":
#     main()
