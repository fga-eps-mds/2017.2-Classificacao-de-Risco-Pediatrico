# Arquivo: apps/risk_rating/forms.py
from django import forms
from apps.risk_rating.models import ClinicalState_28d
from apps.risk_rating.models import ClinicalState_29d_2m
from apps.risk_rating.models import ClinicalState_2m_3y


class ClinicalState_28dForm(forms.ModelForm):
    """
    Defining fields for under 28 days patient's clinical state
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
    Defining fields patients (29 days and 2 months old) clinical state
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
    Defining fields patients (29 days and 2 months old) clinical state
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
