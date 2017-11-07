# Arquivo: apps/risk_rating/forms.py
from django import forms
from apps.users.models import Patient
from apps.risk_rating.models import ClinicalState_28d

class ClinicalState_28dForm(forms.ModelForm):
    """
    Defining filds for under 28 days patient's clinical state
    """
    class Meta:
        model = ClinicalState_28d
        fields = ['patient_id', 'dispineia', 'ictericia', 'perdada_consciencia', 'cianose', 'febre',
                  'solucos', 'prostracao', 'vomitos', 'tosse', 'coriza', 'obstrucao_nasal', 'convulcao_no_momento',
                  'diarreia', 'choro_inconsolavel', 'dificuldade_evacuar', 'nao_suga_seio', 'manchas_na_pele',
                  'salivacao', 'chiado_no_peito', 'diminuicao_da_diurese', 'dor_abdominal', 'fontanela_abaulada',
                  'secrecao_no_umbigo', 'secrecao_ocular', 'sangue_nas_fezes','convulsao_hoje']
