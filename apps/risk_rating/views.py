from django.shortcuts import render


def risk_rating_view(request):
    return render(request, 'risk_rating/risk_rating.html')