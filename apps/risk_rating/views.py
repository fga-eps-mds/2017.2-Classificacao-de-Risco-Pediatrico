from django.shortcuts import render
from apps.risk_rating.ml_classifier import MachineLearning


ml = MachineLearning()


def risk_rating_view(request):
    if request.method == "POST":
        dispineia = check_patient_problem(request.POST.get("dispineia"))
        ictericia = check_patient_problem(request.POST.get("ictericia"))
        consciencia = check_patient_problem(request.POST.get("consciência"))
        cianose = check_patient_problem(request.POST.get("cianose"))
        febre = check_patient_problem(request.POST.get("febre"))
        solucos = check_patient_problem(request.POST.get("solucos"))
        prostracao = check_patient_problem(request.POST.get("prostracao"))
        vomitos = check_patient_problem(request.POST.get("vomitos"))
        tosse = check_patient_problem(request.POST.get("tosse"))
        coriza = check_patient_problem(request.POST.get("coriza"))
        obstrucaoNasal = check_patient_problem(request.POST.get("obstrucaoNasal"))
        convulsaoMomento = check_patient_problem(request.POST.get("convulsaoMomento"))
        diarreia = check_patient_problem(request.POST.get("diarreia"))
        choroIncosolavel = check_patient_problem(request.POST.get("choroIncosolavel"))
        dificuldadeEvacuar = check_patient_problem(request.POST.get("dificuldadeEvacuar"))
        naoSugaSeio = check_patient_problem(request.POST.get("naoSugaSeio"))
        manchaPele = check_patient_problem(request.POST.get("manchaPele"))
        salivacao = check_patient_problem(request.POST.get("salivacao"))
        queda = check_patient_problem(request.POST.get("queda"))
        chiadoPeito = check_patient_problem(request.POST.get("chiadoPeito"))
        diminuicaoDiurese = check_patient_problem(request.POST.get("diminuicaoDiurese"))
        dorAbdominal = check_patient_problem(request.POST.get("dorAbdominal"))
        dorOuvido = check_patient_problem(request.POST.get("dorOuvido"))
        fontanelaAbaulada = check_patient_problem(request.POST.get("fontanelaAbaulada"))
        secrecaoUmbigo = check_patient_problem(request.POST.get("secrecaoUmbigo"))
        secrecaoOcular = check_patient_problem(request.POST.get("secrecaoOcular"))
        sangueFezes = check_patient_problem(request.POST.get("sangueFezes"))
        convulsaoHoje = check_patient_problem(request.POST.get("convulsaoHoje"))

        patient = [[
            dispineia,
            ictericia,
            consciencia,
            cianose,
            febre,
            solucos,
            prostracao,
            vomitos,
            tosse,
            coriza,
            obstrucaoNasal,
            convulsaoMomento,
            diarreia,
            choroIncosolavel,
            dificuldadeEvacuar,
            naoSugaSeio,
            manchaPele,
            salivacao,
            queda,
            chiadoPeito,
            diminuicaoDiurese,
            dorAbdominal,
            dorOuvido,
            fontanelaAbaulada,
            secrecaoUmbigo,
            secrecaoOcular,
            sangueFezes,
            convulsaoHoje,
        ]]

        probability = ml.calc_probabilities(patient)
        classification = ml.classify_patient(patient)
        impact_list = ml.feature_importance()

        print(probability)
        print(classification)
        print(impact_list)

    return render(request, 'risk_rating/risk_rating.html')


def check_patient_problem(problem):
    if problem is not None:
        problem = 1
    else:
        problem = 0

    return problem
