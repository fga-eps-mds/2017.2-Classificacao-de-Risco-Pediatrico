# Arquivo: apps/risk_rating/forms.py
from django import forms
from apps.risk_rating.models import ClinicalState_28d
from apps.risk_rating.models import ClinicalState_29d_2m
from apps.risk_rating.models import ClinicalState_2m_3y


class ClinicalState_28dForm(forms.ModelForm):
    """
    Defining filds for under 28 days patient's clinical state
    """
    class Meta:
        model = ClinicalState_28d
        fields = ['patient_id1', 'dispineia', 'ictericia',
                  'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse',
                  'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'choro_inconsolavel', 'dificuldade_evacuar',
                  'nao_suga_seio', 'manchas_na_pele', 'salivacao',
                  'chiado_no_peito', 'diminuicao_da_diurese', 'dor_abdominal',
                  'fontanela_abaulada', 'secrecao_no_umbigo',
                  'secrecao_ocular', 'sangue_nas_fezes', 'convulsao_hoje']


class ClinicalState_29d_2mForm(forms.ModelForm):
    """
    Defining filds patients (29 days and 2 months old) clinical state
    """
    class Meta:
        model = ClinicalState_29d_2m
        fields = ['patient_id2', 'dispineia', 'ictericia',
                  'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse',
                  'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'dificuldade_evacuar', 'nao_suga_seio',
                  'manchas_na_pele', 'salivacao', 'chiado_no_peito',
                  'diminuicao_da_diurese', 'dor_abdominal',
                  'fontanela_abaulada', 'secrecao_no_umbigo',
                  'secrecao_ocular', 'sangue_nas_fezes', 'convulsao_hoje']


class ClinicalState_2m_3yForm(forms.ModelForm):
    """
    Defining filds patients (29 days and 2 months old) clinical state
    """
    class Meta:
        model = ClinicalState_2m_3y
        fields = ['patient_id3', 'dispineia', 'ictericia',
                  'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse',
                  'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'dificuldade_evacuar', 'nao_suga_seio',
                  'manchas_na_pele', 'salivacao', 'chiado_no_peito',
                  'diminuicao_da_diurese', 'dor_abdominal',
                  'fontanela_abaulada', 'secrecao_no_umbigo',
                  'secrecao_ocular']

class ClinicalState_2y_10y(forms.ModelForm):
    """
    Defining filds patients (2 years and 3 years old) clinical state
    """
    class Meta:
        model = ClinicalState_3y_10y
        fields = ['patient_id4', 'perdada_consciencia', 'febre_maior_72h',
                  'febre_menos_72h', 'odinofagia', 'fascies_de_dor',
                  'tontura', 'corpo_estranho', 'dor_dentes',
                  'disuria', 'urina_concentrada', 'dispineia',
                  'dor_toracica', 'choque_eletrico', 'quase_afogamento',
                  'artralgia', 'ictericia', 'perda_consciencia',
                  'palidez', 'cianose', 'solucos',
                  'prostracao', 'febre', 'vomitos',
                  'tosse', 'coriza', 'espirros',
                  'hiperemia_conjuntival', 'secrecao_ocular',
                  'obstrucao_nasal', 'convulsao', 'diarreia',
                  'manchas_na_pele', 'queda', 'hiporexia', 'salivacao',
                  'constipacao', 'chiado_no_peito',
                  'diminuicao_da_diurese', 'dor_abdominal',
                  'otalgia', 'epistaxe', 'otorreia', 'edema', 'adenomegalias',
                  'dor_articular', 'dificulade_de_marchar', 'sonolencia',
                  'dor_muscular', 'dor_retroorbitaria']
