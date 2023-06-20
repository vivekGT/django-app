from django.shortcuts import redirect

class LoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if not request.user.is_authenticated:
          
            restricted_urls = [
                '/upload-csv/',
                '/dashboard/',
                '/success/',
                '/upload-csv/',
                '/Upload-csv/',
                '/api/data/',
                '/dashboard/',
                '/analytics/',
                '/data-analytics/',
                '/admin1/',
                '/sales_homepage/',
                '/client_admin/',
                '/Upload-csv/',
                '/dashboard/',
                '/analytics/',
                '/team_leader/',
                '/usermanagement/',
                '/billing_summary/',
                '/header/',
                '/team_scorecard/',
                '/teamleaderdetails/',
                '/sales_ex/',
                '/salesanalytics/',
                '/sales_table/',
                '/vechicle_table/',
                '/unique_tl/',
                '/uniquesales_ex/',
            ]

            
            if request.path in restricted_urls:
                
                return redirect('login')  

        response = self.get_response(request)
        return response
 