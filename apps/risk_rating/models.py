from django.db import models
from django.utils.translation import ugettext as _


class SymptomsFor28Days(models.Model):
    class Meta:
        abstract = True

    dispineia = models.BooleanField(
        verbose_name=_('Dispinéia'),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=_('Icterícia'),
        default=False,
        blank=True
    )

    perda_da_consciencia = models.BooleanField(
        verbose_name=_('Perda de Consciência'),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=_('Cianose'),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=_('Febre'),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=_('Soluços'),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=_('Prostração'),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=_('Vômitos'),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=_('Tosse'),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=_('Coriza'),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=_('Obstrução Nasal'),
        default=False,
        blank=True
    )

    convulcao_no_momento = models.BooleanField(
        verbose_name=_('Convulção no momento'),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=_('Diarréia'),
        default=False,
        blank=True
    )

    choro_inconsolavel = models.BooleanField(
        verbose_name=_('Choro Inconsolável'),
        default=False,
        blank=True
    )

    dificuldade_de_evacuar = models.BooleanField(
        verbose_name=_('Dificuldade de Evacuar'),
        default=False,
        blank=True
    )

    nao_suga_o_seio = models.BooleanField(
        verbose_name=_('Não suga o seio'),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=_('Manchas na pele'),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=_('Salivação'),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=_('Queda'),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=_('Chiado no peito'),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=_('Diminuição da Diurese'),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=_('Dor abdominal'),
        default=False,
        blank=True
    )

    dor_de_ouvido = models.BooleanField(
        verbose_name=_('Dor de ouvido'),
        default=False,
        blank=True
    )

    fontanela_abaulada = models.BooleanField(
        verbose_name=_('Fontanela abaulada'),
        default=False,
        blank=True
    )

    secrecao_no_umbigo = models.BooleanField(
        verbose_name=_('Secreção no umbigo'),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=_('Secreção ocular'),
        default=False,
        blank=True
    )

    sangue_nas_fezes = models.BooleanField(
        verbose_name=_('Sangue nas fezes'),
        default=False,
        blank=True
    )

    relato_de_convulsao_hoje = models.BooleanField(
        verbose_name=_('Relato de convulsão hoje'),
        default=False,
        blank=True
    )


class ClinicalStateFor28Days(SymptomsFor28Days):
    patient_id = models.CharField(
        verbose_name=_('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=_('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearningFor28Days(SymptomsFor28Days):
    CLASSIFICATION_TYPES = (
        (1, 'Atendimento Imediato'),
        (2, 'Atendimento Hospitalar'),
        (3, 'Atendimento Ambulatorial')
    )

    classification = models.IntegerField(
        verbose_name=_('Classification'),
        choices=CLASSIFICATION_TYPES,
        blank=False,
        default=0
    )


class SymptomsFor29daysTo2Months(models.Model):
    class Meta:
        abstract = True

    dispineia = models.BooleanField(
        verbose_name=_('Dispinéia'),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=_('Icterícia'),
        default=False,
        blank=True
    )

    perda_da_consciencia = models.BooleanField(
        verbose_name=_('Perda de Consciência'),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=_('Cianose'),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=_('Febre'),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=_('Soluços'),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=_('Prostração'),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=_('Vômitos'),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=_('Tosse'),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=_('Coriza'),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=_('Obstrução Nasal'),
        default=False,
        blank=True
    )

    convulsao = models.BooleanField(
        verbose_name=_('Convulsão'),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=_('Diarréia'),
        default=False,
        blank=True
    )

    dificuldade_de_evacuar = models.BooleanField(
        verbose_name=_('Dificuldade de Evacuar'),
        default=False,
        blank=True
    )

    nao_suga_o_seio = models.BooleanField(
        verbose_name=_('Não suga o seio'),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=_('Manchas na pele'),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=_('Salivação'),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=_('Queda'),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=_('Chiado no peito'),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=_('Diminuição da Diurese'),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=_('Dor abdominal'),
        default=False,
        blank=True
    )

    dor_de_ouvido = models.BooleanField(
        verbose_name=_('Dor de ouvido'),
        default=False,
        blank=True
    )

    fontanela_abaulada = models.BooleanField(
        verbose_name=_('Fontanela abaulada'),
        default=False,
        blank=True
    )

    secrecao_no_umbigo = models.BooleanField(
        verbose_name=_('Secreção no umbigo'),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=_('Secreção ocular'),
        default=False,
        blank=True
    )

    sangue_nas_fezes = models.BooleanField(
        verbose_name=_('Sangue nas fezes'),
        default=False,
        blank=True
    )

    relato_de_convulsao_hoje = models.BooleanField(
        verbose_name=_('Relato de convulsão hoje'),
        default=False,
        blank=True
    )


class ClinicalState_For_29DaysTo_2Months(SymptomsFor29daysTo2Months):
    patient_id = models.CharField(
        verbose_name=_('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=_('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearning_For_29DaysTo_2Months(SymptomsFor29daysTo2Months):
    CLASSIFICATION_TYPES = (
        (1, 'Atendimento Imediato'),
        (2, 'Atendimento Hospitalar'),
        (3, 'Atendimento Ambulatorial')
    )

    classification = models.IntegerField(
        verbose_name=_('Classification'),
        choices=CLASSIFICATION_TYPES,
        blank=False,
        default=0
    )


class Symptoms_2m_3y(models.Model):
    class Meta:
        abstract = True

    dispineia = models.BooleanField(
        verbose_name=_('Dispinéia'),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=_('Icterícia'),
        default=False,
        blank=True
    )

    perda_da_consciencia = models.BooleanField(
        verbose_name=_('Perda de Consciência'),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=_('Cianose'),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=_('Febre'),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=_('Soluços'),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=_('Prostração'),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=_('Vômitos'),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=_('Tosse'),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=_('Coriza'),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=_('Obstrução Nasal'),
        default=False,
        blank=True
    )

    convulcao_no_momento = models.BooleanField(
        verbose_name=_('Convulção no momento'),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=_('Diarréia'),
        default=False,
        blank=True
    )

    dificuldade_de_evacuar = models.BooleanField(
        verbose_name=_('Dificuldade de Evacuar'),
        default=False,
        blank=True
    )

    nao_suga_seio = models.BooleanField(
        verbose_name=_('Não suga o seio'),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=_('Manchas na pele'),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=_('Salivação'),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=_('Queda'),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=_('Chiado no peito'),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=_('Diminuição da Diurese'),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=_('Dor abdominal'),
        default=False,
        blank=True
    )

    dor_de_ouvido = models.BooleanField(
        verbose_name=_('Dor de ouvido'),
        default=False,
        blank=True
    )

    fontanela_abaulada = models.BooleanField(
        verbose_name=_('Fontanela abaulada'),
        default=False,
        blank=True
    )

    secrecao_no_umbigo = models.BooleanField(
        verbose_name=_('Secreção no umbigo'),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=_('Secreção ocular'),
        default=False,
        blank=True
    )


class ClinicalState_2m_3y(Symptoms_2m_3y):
    patient_id = models.CharField(
        verbose_name=_('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=_('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearning_2m_3y(Symptoms_2m_3y):
    CLASSIFICATION_TYPES = (
        (1, 'Atendimento Imediato'),
        (2, 'Atendimento Hospitalar'),
        (3, 'Atendimento Ambulatorial')
    )

    classification = models.IntegerField(
        verbose_name=_('Classification'),
        choices=CLASSIFICATION_TYPES,
        blank=False,
        default=0
    )


class Symptoms_3y_10y(models.Model):
    class Meta:
        abstract = True

    perda_da_consciencia = models.BooleanField(
        verbose_name=_('Perda de Consciência'),
        default=False,
        blank=True
    )

    febre_maior_72h = models.BooleanField(
        verbose_name=_('Febre Mais de 72 horas'),
        default=False,
        blank=True
    )

    febre_menos_72h = models.BooleanField(
        verbose_name=_('Febre Menos de 72 horas'),
        default=False,
        blank=True
    )

    odinofagia = models.BooleanField(
        verbose_name=_('Odinofagia'),
        default=False,
        blank=True
    )

    fascies_de_dor = models.BooleanField(
        verbose_name=_('Fascies De Dor'),
        default=False,
        blank=True
    )

    tontura = models.BooleanField(
        verbose_name=_('Tontura'),
        default=False,
        blank=True
    )

    corpo_estranho = models.BooleanField(
        verbose_name=_('Corpo Estranho'),
        default=False,
        blank=True
    )

    dor_dentes = models.BooleanField(
        verbose_name=_('Dor de dentes'),
        default=False,
        blank=True
    )

    disuria = models.BooleanField(
        verbose_name=_('Disuria'),
        default=False,
        blank=True
    )

    urina_concentrada = models.BooleanField(
        verbose_name=_('Urina Concentrada'),
        default=False,
        blank=True
    )

    dispineia = models.BooleanField(
        verbose_name=_('Dispinéia'),
        default=False,
        blank=True
    )

    dor_toracica = models.BooleanField(
        verbose_name=_('Dor Toracica'),
        default=False,
        blank=True
    )

    choque_eletrico = models.BooleanField(
        verbose_name=_('Choque Eletrico'),
        default=False,
        blank=True
    )

    quase_afogamento = models.BooleanField(
        verbose_name=_('Quase Afogamento'),
        default=False,
        blank=True
    )

    artralgia = models.BooleanField(
        verbose_name=_('Artralgia'),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=_('Icterícia'),
        default=False,
        blank=True
    )

    perda_consciencia = models.BooleanField(
        verbose_name=_('Perda de consciencia'),
        default=False,
        blank=True
    )

    palidez = models.BooleanField(
        verbose_name=_('Palidez'),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=_('Cianose'),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=_('Soluços'),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=_('Prostração'),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=_('Febre'),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=_('Vomitos'),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=_('Tosse'),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=_('Coriza'),
        default=False,
        blank=True
    )

    espirros = models.BooleanField(
        verbose_name=_('Espirros'),
        default=False,
        blank=True
    )
    hiperemia_conjuntival = models.BooleanField(
        verbose_name=_('Hiperemia Conjuntival'),
        default=False,
        blank=True
    )
    secrecao_ocular = models.BooleanField(
        verbose_name=_('Secrecao Ocular'),
        default=False,
        blank=True
    )
    obstrucao_nasal = models.BooleanField(
        verbose_name=_('Obstrução Nasal'),
        default=False,
        blank=True
    )
    convulsao = models.BooleanField(
        verbose_name=_('Convulsão'),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=_('Diarreia'),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=_('Manchas na pele'),
        default=False,
        blank=True
    )
    queda = models.BooleanField(
        verbose_name=_('Queda'),
        default=False,
        blank=True
    )
    hiporexia = models.BooleanField(
        verbose_name=_('Hiporexia'),
        default=False,
        blank=True
    )
    salivacao = models.BooleanField(
        verbose_name=_('Salivacao'),
        default=False,
        blank=True
    )

    constipacao = models.BooleanField(
        verbose_name=_('Constipação'),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=_('Chiado no Peito'),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=_('Diminuição da Diurese'),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=_('Dor Abdominal'),
        default=False,
        blank=True
    )

    otalgia = models.BooleanField(
        verbose_name=_('Otalgia'),
        default=False,
        blank=True
    )

    epistaxe = models.BooleanField(
        verbose_name=_('Epistaxe'),
        default=False,
        blank=True
    )

    otorreia = models.BooleanField(
        verbose_name=_('Otorreia'),
        default=False,
        blank=True
    )

    edema = models.BooleanField(
        verbose_name=_('Edema'),
        default=False,
        blank=True
    )

    adenomegalias = models.BooleanField(
        verbose_name=_('Adenomegalias'),
        default=False,
        blank=True
    )

    dor_articular = models.BooleanField(
        verbose_name=_('Dor Articular'),
        default=False,
        blank=True
    )

    dificulade_de_marchar = models.BooleanField(
        verbose_name=_('Dificuldade Marchar'),
        default=False,
        blank=True
    )

    sonolencia = models.BooleanField(
        verbose_name=_('Sonolência'),
        default=False,
        blank=True
    )

    dor_muscular = models.BooleanField(
        verbose_name=_('Dor Muscular'),
        default=False,
        blank=True
    )

    dor_retroorbitaria = models.BooleanField(
        verbose_name=_('Dor Retroorbitária'),
        default=False,
        blank=True
    )


class ClinicalState_3y_10y(Symptoms_3y_10y):
    patient_id = models.CharField(
        verbose_name=_('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=_('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearning_3y_10y(Symptoms_3y_10y):
    CLASSIFICATION_TYPES = (
        (1, 'Atendimento Imediato'),
        (2, 'Atendimento Hospitalar'),
        (3, 'Atendimento Ambulatorial')
    )

    classification = models.IntegerField(
        verbose_name=_('Classification'),
        choices=CLASSIFICATION_TYPES,
        blank=False,
        default=0
    )


class Symptoms_10yMore(models.Model):
    class Meta:
        abstract = True

    mais_de_72h_febre = models.BooleanField(
        verbose_name=_('Febre a mais de 72 horas'),
        default=False,
        blank=True
    )

    menos_de_72h_febre = models.BooleanField(
        verbose_name=_('Febre a menos de 72 horas'),
        default=False,
        blank=True
    )

    tontura = models.BooleanField(
        verbose_name=_('Tontura'),
        default=False,
        blank=True
    )

    corpo_estranho = models.BooleanField(
        verbose_name=_('Corpo estranho'),
        default=False,
        blank=True
    )

    dor_de_dente = models.BooleanField(
        verbose_name=_('Dor de dente'),
        default=False,
        blank=True
    )

    disuria = models.BooleanField(
        verbose_name=_('Disúria'),
        default=False,
        blank=True
    )

    urina_concentrada = models.BooleanField(
        verbose_name=_('Urina concentrada'),
        default=False,
        blank=True
    )

    dispineia = models.BooleanField(
        verbose_name=_('Dispinéia'),
        default=False,
        blank=True
    )

    dor_toracica = models.BooleanField(
        verbose_name=_('Dor torácica'),
        default=False,
        blank=True
    )

    choque_eletrico = models.BooleanField(
        verbose_name=_('Choque elétrico'),
        default=False,
        blank=True
    )

    quase_afogamento = models.BooleanField(
        verbose_name=_('Quase afogamento'),
        default=False,
        blank=True
    )

    artralgia = models.BooleanField(
        verbose_name=_('Artralgia'),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=_('Icterícia'),
        default=False,
        blank=True
    )

    perda_da_consciencia = models.BooleanField(
        verbose_name=_('Perda da conciência'),
        default=False,
        blank=True
    )

    palidez = models.BooleanField(
        verbose_name=_('Palidez'),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=_('Cianose'),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=_('Soluços'),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=_('Prostração'),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=_('Febre'),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=_('Vômitos'),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=_('Tosse'),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=_('Coriza'),
        default=False,
        blank=True
    )

    espirros = models.BooleanField(
        verbose_name=_('Espirros'),
        default=False,
        blank=True
    )

    hiperemia_conjuntival = models.BooleanField(
        verbose_name=_('Hiperemia conjuntival'),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=_('Secreção ocular'),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=_('Obstrução nasal'),
        default=False,
        blank=True
    )

    convulsao = models.BooleanField(
        verbose_name=_('Convulsão'),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=_('Diarreia'),
        default=False,
        blank=True
    )

    dificuldade_evacuar = models.BooleanField(
        verbose_name=_('Dificuldade de evacuar'),
        default=False,
        blank=True
    )

    cefaleia = models.BooleanField(
        verbose_name=_('Cefaléia'),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=_('Manchas na pele'),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=_('Queda'),
        default=False,
        blank=True
    )

    hiporexia = models.BooleanField(
        verbose_name=_('Hiporexia'),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=_('Salivação'),
        default=False,
        blank=True
    )

    hiporexia = models.BooleanField(
        verbose_name=_('Hiporexia'),
        default=False,
        blank=True
    )

    constipacao = models.BooleanField(
        verbose_name=_('Constipação'),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=_('Chiado no peito'),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=_('Diminuição da diurese'),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=_('Dor abdominal'),
        default=False,
        blank=True
    )

    otalgia = models.BooleanField(
        verbose_name=_('Otalgia'),
        default=False,
        blank=True
    )

    epistaxe = models.BooleanField(
        verbose_name=_('Epistaxe'),
        default=False,
        blank=True
    )

    otorreia = models.BooleanField(
        verbose_name=_('Otorréia'),
        default=False,
        blank=True
    )

    edema = models.BooleanField(
        verbose_name=_('Edema'),
        default=False,
        blank=True
    )

    adenomegalias = models.BooleanField(
        verbose_name=_('Adenomegalias'),
        default=False,
        blank=True
    )

    dor_articular = models.BooleanField(
        verbose_name=_('Dor articular'),
        default=False,
        blank=True
    )

    dificuldade_de_marcha = models.BooleanField(
        verbose_name=_('Dificuldade de marcha'),
        default=False,
        blank=True
    )

    sonolencia = models.BooleanField(
        verbose_name=_('Sonolência'),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=_('Secreção ocular'),
        default=False,
        blank=True
    )

    dor_muscular = models.BooleanField(
        verbose_name=_('Dor muscular'),
        default=False,
        blank=True
    )

    dor_retroorbitaria = models.BooleanField(
        verbose_name=_('Dor Retroorbitária'),
        default=False,
        blank=True
    )


class ClinicalState_10yMore(Symptoms_10yMore):
    patient_id = models.CharField(
        verbose_name=_('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=_('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearning_10yMore(Symptoms_10yMore):
    CLASSIFICATION_TYPES = (
        (1, 'Atendimento Imediato'),
        (2, 'Atendimento Hospitalar'),
        (3, 'Atendimento Ambulatorial')
    )

    classification = models.IntegerField(
        verbose_name=_('Classification'),
        choices=CLASSIFICATION_TYPES,
        blank=False,
        default=0
    )
