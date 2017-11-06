from django.db import models
from apps.users.models import Patient

class ClinicalState_28d(models.Model):

    patient = models.CharField(
        verbose_name=('ID do Paciente'),
        max_length=150,
        blank=False,
        unique=False
    )

    # simptoms:
    dispineia = models.BooleanField(
        verbose_name=("Dispinéia"),
        default=False,
        blank=True
    )

    ictericia = models.BooleanField(
        verbose_name=("Icteria"),
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
        verbose_name=("Solucos"),
        default=False,
        blank=True
    )

    prostacao = models.BooleanField(
        verbose_name=("Prostação"),
        default=False,
        blank=True
    )

    vomitos = models.BooleanField(
        verbose_name=("Vômitos"),
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

    convulcao_no_momento = models.BooleanField(
        verbose_name=("Convulção no momento"),
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
        verbose_name=("Não sua o seio"),
        default=False,
        blank=True
    )

    manchas_na_pele = models.BooleanField(
        verbose_name=("Manchas na pele"),
        default=False,
        blank=True
    )

    salivacao = models.BooleanField(
        verbose_name=("Salivacao"),
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

    convulcao_hoje = models.BooleanField(
        verbose_name=("Relato de convulcão hoje"),
        default=False,
        blank=True
    )
