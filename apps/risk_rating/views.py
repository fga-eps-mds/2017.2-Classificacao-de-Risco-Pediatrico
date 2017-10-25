from django.shortcuts import render
from apps.risk_rating import ml_classifier


def risk_rating_view(request):
    if request.method == "POST":
        prostrado = check_patient_problem(request.POST.get("prostrado"))
        respiracao = check_patient_problem(request.POST.get("respiracao"))
        febre = check_patient_problem(request.POST.get("febre"))
        irritado = check_patient_problem(request.POST.get("irritado"))
        convulsao = check_patient_problem(request.POST.get("convulsao"))
        palido = check_patient_problem(request.POST.get("palido"))
        cabeca = check_patient_problem(request.POST.get("cabeca"))
        brincando = check_patient_problem(request.POST.get("brincando"))

        patient = {
            'prostrado': prostrado,
            'respiracao': respiracao,
            'febre': febre,
            'irritado': irritado,
            'convulsao': convulsao,
            'palido': palido,
            'cabeca': cabeca,
            'brincando': brincando
        }

        print(patient)
        print(ml_classifier.classify_csv())

    return render(request, 'risk_rating/risk_rating.html')


def check_patient_problem(problem):
    if problem is not None:
        problem = True
    else:
        problem = False

    return problem
