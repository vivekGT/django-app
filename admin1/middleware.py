from django.shortcuts import redirect
from django.urls import reverse

class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            # List the URLs that require authentication after login
            restricted_urls = ['/upload-csv/',
            '/dashboard/',
            'success/',
            'upload-csv/',
            'Upload-csv/',
            'api/data/',
            'dashboard/',
            'analytics/',
            'data-analytics/',
        
               
            ]

            # Check if the current URL is in the restricted URLs list
            if request.path in restricted_urls:
                return redirect('login')

        response = self.get_response(request)
        return response
