from django.core.exceptions import ValidationError


def validate_content ( value ):
	content = value
	if content == 'empty':
		raise ValidationError ("Cannot be empty")
	return value