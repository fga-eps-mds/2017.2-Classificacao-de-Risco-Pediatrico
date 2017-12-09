from django.db import models
from django.utils.translation import ugettext as _


class Symptoms_28d(models.Model):

    class Meta:
        abstract = True

    dispneia = models.BooleanField(
        verbose_name=("Dispneia"),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=("Icterícia"),
        default=False,
        blank=True
    )

    perdada_consciencia = models.BooleanField(
        verbose_name=("Perda de Consciência"),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=("Cianose"),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=("Febre"),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=("Soluços"),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=("Prostração"),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=("Vômitos"),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=("Tosse"),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=("Coriza"),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=("Obstrução Nasal"),
        default=False,
        blank=True
    )

    convunsao_no_momento = models.BooleanField(
        verbose_name=("Convulsão no momento"),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=("Diarréia"),
        default=False,
        blank=True
    )

    choro_inconsolavel = models.BooleanField(
        verbose_name=("Choro Inconsolável"),
        default=False,
        blank=True
    )

    dificuldade_evacuar = models.BooleanField(
        verbose_name=("Dificuldade de Evacuar"),
        default=False,
        blank=True
    )

    nao_suga_seio = models.BooleanField(
        verbose_name=("Não suga o seio"),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=("Manchas na pele"),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=("Salivação"),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=("Queda"),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=("Chiado no peito"),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=("Diminuição da Diurese"),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=("Dor abdominal"),
        default=False,
        blank=True
    )

    dor_de_ouvido = models.BooleanField(
        verbose_name=("Dor de ouvido"),
        default=False,
        blank=True
    )

    fontanela_abaulada = models.BooleanField(
        verbose_name=("Fontanela abaulada"),
        default=False,
        blank=True
    )

    secrecao_no_umbigo = models.BooleanField(
        verbose_name=("Secreção no umbigo"),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=("Secreção ocular"),
        default=False,
        blank=True
    )

    sangue_nas_fezes = models.BooleanField(
        verbose_name=("Sangue nas fezes"),
        default=False,
        blank=True
    )

    convulsao_hoje = models.BooleanField(
        verbose_name=("Relato de convulsão hoje"),
        default=False,
        blank=True
    )


class ClinicalState_28d(Symptoms_28d):

    patient_id = models.CharField(
        verbose_name=('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearning_28d(Symptoms_28d):

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


class Symptoms_29d_2m(models.Model):

    class Meta:
        abstract = True

    dispneia = models.BooleanField(
        verbose_name=("Dispneia"),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=("Icterícia"),
        default=False,
        blank=True
    )

    perdada_consciencia = models.BooleanField(
        verbose_name=("Perda de Consciência"),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=("Cianose"),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=("Febre"),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=("Soluços"),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=("Prostração"),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=("Vômitos"),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=("Tosse"),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=("Coriza"),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=("Obstrução Nasal"),
        default=False,
        blank=True
    )

    convunsao_no_momento = models.BooleanField(
        verbose_name=("Convulsão no momento"),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=("Diarréia"),
        default=False,
        blank=True
    )

    dificuldade_evacuar = models.BooleanField(
        verbose_name=("Dificuldade de Evacuar"),
        default=False,
        blank=True
    )

    nao_suga_seio = models.BooleanField(
        verbose_name=("Não suga o seio"),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=("Manchas na pele"),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=("Salivação"),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=("Queda"),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=("Chiado no peito"),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=("Diminuição da Diurese"),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=("Dor abdominal"),
        default=False,
        blank=True
    )

    dor_de_ouvido = models.BooleanField(
        verbose_name=("Dor de ouvido"),
        default=False,
        blank=True
    )

    fontanela_abaulada = models.BooleanField(
        verbose_name=("Fontanela abaulada"),
        default=False,
        blank=True
    )

    secrecao_no_umbigo = models.BooleanField(
        verbose_name=("Secreção no umbigo"),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=("Secreção ocular"),
        default=False,
        blank=True
    )

    sangue_nas_fezes = models.BooleanField(
        verbose_name=("Sangue nas fezes"),
        default=False,
        blank=True
    )

    convulsao_hoje = models.BooleanField(
        verbose_name=("Relato de convulsão hoje"),
        default=False,
        blank=True
    )


class ClinicalState_29d_2m(Symptoms_29d_2m):

    patient_id = models.CharField(
        verbose_name=('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=('ID do Classificador'),
        max_length=150,
        blank=True,
        unique=False
    )


class MachineLearning_29d_2m(Symptoms_29d_2m):

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

    dispneia = models.BooleanField(
        verbose_name=("Dispneia"),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=("Icterícia"),
        default=False,
        blank=True
    )

    perdada_consciencia = models.BooleanField(
        verbose_name=("Perda de Consciência"),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=("Cianose"),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=("Febre"),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=("Soluços"),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=("Prostração"),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=("Vômitos"),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=("Tosse"),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=("Coriza"),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=("Obstrução Nasal"),
        default=False,
        blank=True
    )

    convunsao_no_momento = models.BooleanField(
        verbose_name=("Convulsão no momento"),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=("Diarréia"),
        default=False,
        blank=True
    )

    dificuldade_evacuar = models.BooleanField(
        verbose_name=("Dificuldade de Evacuar"),
        default=False,
        blank=True
    )

    nao_suga_seio = models.BooleanField(
        verbose_name=("Não suga o seio"),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=("Manchas na pele"),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=("Salivação"),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=("Queda"),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=("Chiado no peito"),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=("Diminuição da Diurese"),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=("Dor abdominal"),
        default=False,
        blank=True
    )

    dor_de_ouvido = models.BooleanField(
        verbose_name=("Dor de ouvido"),
        default=False,
        blank=True
    )

    fontanela_abaulada = models.BooleanField(
        verbose_name=("Fontanela abaulada"),
        default=False,
        blank=True
    )

    secrecao_no_umbigo = models.BooleanField(
        verbose_name=("Secreção no umbigo"),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=("Secreção ocular"),
        default=False,
        blank=True
    )


class ClinicalState_2m_3y(Symptoms_2m_3y):

    patient_id = models.CharField(
        verbose_name=('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=('ID do Classificador'),
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

    perdada_consciencia = models.BooleanField(
        verbose_name=("Perda de Consciência"),
        default=False,
        blank=True
    )

    febre_maior_72h = models.BooleanField(
        verbose_name=("Febre Mais de 72 horas"),
        default=False,
        blank=True
    )

    febre_menos_72h = models.BooleanField(
        verbose_name=("Febre Menos de 72 horas"),
        default=False,
        blank=True
    )

    odinofagia = models.BooleanField(
        verbose_name=("Odinofagia"),
        default=False,
        blank=True
    )

    fascies_de_dor = models.BooleanField(
        verbose_name=("Fascies De Dor"),
        default=False,
        blank=True
    )

    tontura = models.BooleanField(
        verbose_name=("Tontura"),
        default=False,
        blank=True
    )

    corpo_estranho = models.BooleanField(
        verbose_name=("Corpo Estranho"),
        default=False,
        blank=True
    )

    dor_dentes = models.BooleanField(
        verbose_name=("Dor de dentes"),
        default=False,
        blank=True
    )

    disuria = models.BooleanField(
        verbose_name=("Disuria"),
        default=False,
        blank=True
    )

    urina_concentrada = models.BooleanField(
        verbose_name=("Urina Concentrada"),
        default=False,
        blank=True
    )

    dispneia = models.BooleanField(
        verbose_name=("Dispneia"),
        default=False,
        blank=True
    )

    dor_toracica = models.BooleanField(
        verbose_name=("Dor Toracica"),
        default=False,
        blank=True
    )

    choque_eletrico = models.BooleanField(
        verbose_name=("Choque Eletrico"),
        default=False,
        blank=True
    )

    quase_afogamento = models.BooleanField(
        verbose_name=("Quase Afogamento"),
        default=False,
        blank=True
    )

    artralgia = models.BooleanField(
        verbose_name=("Artralgia"),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=("Icterícia"),
        default=False,
        blank=True
    )

    perda_consciencia = models.BooleanField(
        verbose_name=("Perda de consciencia"),
        default=False,
        blank=True
    )

    palidez = models.BooleanField(
        verbose_name=("Palidez"),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=("Cianose"),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=("Soluços"),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=("Prostração"),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=("Febre"),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=("Vomitos"),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=("Tosse"),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=("Coriza"),
        default=False,
        blank=True
    )

    espirros = models.BooleanField(
        verbose_name=("Espirros"),
        default=False,
        blank=True
    )
    hiperemia_conjuntival = models.BooleanField(
        verbose_name=("Hiperemia Conjuntival"),
        default=False,
        blank=True
    )
    secrecao_ocular = models.BooleanField(
        verbose_name=("Secrecao Ocular"),
        default=False,
        blank=True
    )
    obstrucao_nasal = models.BooleanField(
        verbose_name=("Obstrução Nasal"),
        default=False,
        blank=True
    )
    convulsao = models.BooleanField(
        verbose_name=("Convulsão"),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=("Diarreia"),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=("Manchas na pele"),
        default=False,
        blank=True
    )
    queda = models.BooleanField(
        verbose_name=("Queda"),
        default=False,
        blank=True
    )
    hiporexia = models.BooleanField(
        verbose_name=("Hiporexia"),
        default=False,
        blank=True
    )
    salivacao = models.BooleanField(
        verbose_name=("Salivacao"),
        default=False,
        blank=True
    )

    constipacao = models.BooleanField(
        verbose_name=("Constipação"),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=("Chiado no Peito"),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=("Diminuição da Diurese"),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=("Dor Abdominal"),
        default=False,
        blank=True
    )

    otalgia = models.BooleanField(
        verbose_name=("Otalgia"),
        default=False,
        blank=True
    )

    epistaxe = models.BooleanField(
        verbose_name=("Epistaxe"),
        default=False,
        blank=True
    )

    otorreia = models.BooleanField(
        verbose_name=("Otorreia"),
        default=False,
        blank=True
    )

    edema = models.BooleanField(
        verbose_name=("Edema"),
        default=False,
        blank=True
    )

    adenomegalias = models.BooleanField(
        verbose_name=("Adenomegalias"),
        default=False,
        blank=True
    )

    dor_articular = models.BooleanField(
        verbose_name=("Dor Articular"),
        default=False,
        blank=True
    )

    dificulade_de_marchar = models.BooleanField(
        verbose_name=("Dificuldade Marchar"),
        default=False,
        blank=True
    )

    sonolencia = models.BooleanField(
        verbose_name=("Sonolência"),
        default=False,
        blank=True
    )

    dor_muscular = models.BooleanField(
        verbose_name=("Dor Muscular"),
        default=False,
        blank=True
    )

    dor_retroorbitaria = models.BooleanField(
        verbose_name=("Dor Retroorbitária"),
        default=False,
        blank=True
    )


class ClinicalState_3y_10y(Symptoms_3y_10y):

    patient_id = models.CharField(
        verbose_name=('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=('ID do Classificador'),
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
        verbose_name=("Febre a mais de 72 horas"),
        default=False,
        blank=True
    )

    menos_de_72h_febre = models.BooleanField(
        verbose_name=("Febre a menos de 72 horas"),
        default=False,
        blank=True
    )

    tontura = models.BooleanField(
        verbose_name=("Tontura"),
        default=False,
        blank=True
    )

    corpo_estranho = models.BooleanField(
        verbose_name=("Corpo estranho"),
        default=False,
        blank=True
    )

    dor_de_dente = models.BooleanField(
        verbose_name=("Dor de dente"),
        default=False,
        blank=True
    )

    disuria = models.BooleanField(
        verbose_name=("Disúria"),
        default=False,
        blank=True
    )

    urina_concentrada = models.BooleanField(
        verbose_name=("Urina concentrada"),
        default=False,
        blank=True
    )

    dispneia = models.BooleanField(
        verbose_name=("Dispneia"),
        default=False,
        blank=True
    )

    dor_toracica = models.BooleanField(
        verbose_name=("Dor torácica"),
        default=False,
        blank=True
    )

    choque_eletrico = models.BooleanField(
        verbose_name=("Choque elétrico"),
        default=False,
        blank=True
    )

    quase_afogamento = models.BooleanField(
        verbose_name=("Quase afogamento"),
        default=False,
        blank=True
    )

    artralgia = models.BooleanField(
        verbose_name=("Artralgia"),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=("Icterícia"),
        default=False,
        blank=True
    )

    perda_da_consciencia = models.BooleanField(
        verbose_name=("Perda da conciência"),
        default=False,
        blank=True
    )

    palidez = models.BooleanField(
        verbose_name=("Palidez"),
        default=False,
        blank=True
    )

    cianose = models.BooleanField(
        verbose_name=("Cianose"),
        default=False,
        blank=True
    )

    solucos = models.BooleanField(
        verbose_name=("Soluços"),
        default=False,
        blank=True
    )

    prostracao = models.BooleanField(
        verbose_name=("Prostração"),
        default=False,
        blank=True
    )

    febre = models.BooleanField(
        verbose_name=("Febre"),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=("Vômitos"),
        default=False,
        blank=True
    )

    tosse = models.BooleanField(
        verbose_name=("Tosse"),
        default=False,
        blank=True
    )

    coriza = models.BooleanField(
        verbose_name=("Coriza"),
        default=False,
        blank=True
    )

    espirros = models.BooleanField(
        verbose_name=("Espirros"),
        default=False,
        blank=True
    )

    hiperemia_conjuntival = models.BooleanField(
        verbose_name=("Hiperemia conjuntival"),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=("Secreção ocular"),
        default=False,
        blank=True
    )

    obstrucao_nasal = models.BooleanField(
        verbose_name=("Obstrução nasal"),
        default=False,
        blank=True
    )

    convulsao = models.BooleanField(
        verbose_name=("Convulsão"),
        default=False,
        blank=True
    )

    diarreia = models.BooleanField(
        verbose_name=("Diarreia"),
        default=False,
        blank=True
    )

    dificuldade_evacuar = models.BooleanField(
        verbose_name=("Dificuldade de evacuar"),
        default=False,
        blank=True
    )

    cefaleia = models.BooleanField(
        verbose_name=("Cefaléia"),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=("Manchas na pele"),
        default=False,
        blank=True
    )

    queda = models.BooleanField(
        verbose_name=("Queda"),
        default=False,
        blank=True
    )

    hiporexia = models.BooleanField(
        verbose_name=("Hiporexia"),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=("Salivação"),
        default=False,
        blank=True
    )

    hiporexia = models.BooleanField(
        verbose_name=("Hiporexia"),
        default=False,
        blank=True
    )

    constipacao = models.BooleanField(
        verbose_name=("Constipação"),
        default=False,
        blank=True
    )

    chiado_no_peito = models.BooleanField(
        verbose_name=("Chiado no peito"),
        default=False,
        blank=True
    )

    diminuicao_da_diurese = models.BooleanField(
        verbose_name=("Diminuição da diurese"),
        default=False,
        blank=True
    )

    dor_abdominal = models.BooleanField(
        verbose_name=("Dor abdominal"),
        default=False,
        blank=True
    )

    otalgia = models.BooleanField(
        verbose_name=("Otalgia"),
        default=False,
        blank=True
    )

    epistaxe = models.BooleanField(
        verbose_name=("Epistaxe"),
        default=False,
        blank=True
    )

    otorreia = models.BooleanField(
        verbose_name=("Otorréia"),
        default=False,
        blank=True
    )

    edema = models.BooleanField(
        verbose_name=("Edema"),
        default=False,
        blank=True
    )

    adenomegalias = models.BooleanField(
        verbose_name=("Adenomegalias"),
        default=False,
        blank=True
    )

    dor_articular = models.BooleanField(
        verbose_name=("Dor articular"),
        default=False,
        blank=True
    )

    dificuldade_de_marcha = models.BooleanField(
        verbose_name=("Dificuldade de marcha"),
        default=False,
        blank=True
    )

    sonolencia = models.BooleanField(
        verbose_name=("Sonolência"),
        default=False,
        blank=True
    )

    secrecao_ocular = models.BooleanField(
        verbose_name=("Secreção ocular"),
        default=False,
        blank=True
    )

    dor_muscular = models.BooleanField(
        verbose_name=("Dor muscular"),
        default=False,
        blank=True
    )

    dor_retroorbitaria = models.BooleanField(
        verbose_name=("Dor Retroorbitária"),
        default=False,
        blank=True
    )


class ClinicalState_10yMore(Symptoms_10yMore):

    patient_id = models.CharField(
        verbose_name=('ID do Paciente'),
        max_length=150,
        blank=True,
        unique=False
    )

    classifier_id = models.CharField(
        verbose_name=('ID do Classificador'),
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
