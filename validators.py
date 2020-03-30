from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_cpf(cpf):
    if(cpf != '00000000000'):
        # verificar o tamanho da string
        if len(cpf) != 11:
            raise ValidationError('O CPF deve conter exatamente 11 dígitos')

        # cpfs inválidos
        for i in range(10):
            if cpf == str(i) * 11:
                raise ValidationError('CPF inválido')

        # validação do primeiro dígito verificador
        s = 0
        for i in range(9):
            s += int(cpf[i]) * (10 - i)
        first_digit_valid = int(cpf[9]) == ((s * 10 % 11) % 10)

        # validação do segundo dígito verificador
        s = 0
        for i in range(10):
            s += int(cpf[i]) * (11 - i)
        second_digit_valid = int(cpf[10]) == ((s * 10 % 11) % 10)

        if not first_digit_valid or not second_digit_valid:
            raise ValidationError('CPF inválido')

def prevent_future_date(date):
    if date > timezone.now().date():
        raise ValidationError('Data no futuro')
