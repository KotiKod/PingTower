from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from App.BackEnd.Models.Website import Website
from App.BackEnd.database.Repository.RepositorySQLite.WebsiteRepository import WebsiteRepository
import json


@method_decorator(csrf_exempt, name='dispatch')
class Router(View):
    """
    Упрощенный роутер для обработки POST запросов
    """

    def __init__(self, repo: WebsiteRepository):
        self.repo = repo
        super().__init__()

    def post(self, request, *args, **kwargs):
        try:
            # Парсим JSON данные
            data = json.loads(request.body)

            # Валидация
            if not data.get('url') or not data.get('user_id'):
                return JsonResponse(
                    {'error': 'url and user_id are required'},
                    status=400
                )

            # Создаем или обновляем запись
            website = Website(
                url=data['url'],
                user_id=data['user_id'],
                status_http=data.get('status_http', False),
                dns_check=data.get('dns_check', False),
                ssl_check=data.get('ssl_check', False),
                ep_check=data.get('ep_check', False),
                loading_check=data.get('loading_check', False),
                validation=data.get('validation', False),
                time_period=data.get('time_period', 300)
            )
            # website.url = data['url']
            # website.user_id = data['user_id']
            # website.status_http = data.get('status_http', False)
            # website.dns_check = data.get('dns_check', False)
            # website.ssl_check = data.get('ssl_check', False)
            # website.ep_check = data.get('ep_check', False)
            # website.loading_check = data.get('loading_check', False)
            # website.validation = data.get('validation', False)
            # website.time_period = data.get('time_period', 300)

            self.repo.create(website)

            return JsonResponse({
                'status': 'success',
                'action': 'created',
                # 'id': website.id,
                'url': website.url,
                'user_id': website.user_id
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
