# Accounts Forms
from django.forms import (
    ModelForm,
    TextInput,
    EmailInput,
    EmailField,
    CharField,
    NumberInput,
    Form,
    PasswordInput,
)
from accounts.constants import FormsClasses, FormHelpText, FormLabels, FormPlaceholder
from utils.base_utils import get_model

User = get_model(app_name="accounts", model_name="User")


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "age"]
        widgets = {}
        help_texts = {}
        for field in fields:
            input_option = TextInput
            if field == "email":
                input_option = EmailInput
            elif field == "age":
                input_option = NumberInput
            widgets[field] = input_option(
                attrs={
                    "class": FormsClasses.INPUT,
                    "placeholder": FormPlaceholder.REGISTER[field],
                    "label": FormLabels.REGISTER[field],
                }
            )
            if field in ["username", "email"]:
                help_texts[field] = FormHelpText.REGISTER[field]


class LoginForm(Form):
    username = CharField(
        max_length=100,
        required=True,
        label=FormLabels.LOGIN["username"],
        widget=TextInput(
            attrs={
                "class": FormsClasses.INPUT,
                "placeholder": FormPlaceholder.LOGIN["username"],
            }
        ),
    )
    password = CharField(
        max_length=100,
        required=True,
        label=FormLabels.LOGIN["password"],
        widget=PasswordInput(
            attrs={
                "class": FormsClasses.PASSWORD_INPUT,
                "placeholder": FormPlaceholder.LOGIN["password"],
            }
        ),
    )


class PasswordResetForm(Form):
    email = EmailField(
        max_length=254,
        required=True,
        label=FormLabels.PASSWORD_RESET["email"],
        help_text=FormHelpText.PASSWORD_RESET["email"],
        widget=EmailInput(
            attrs={
                "class": FormsClasses.INPUT + " text-black",
                "placeholder": FormPlaceholder.PASSWORD_RESET["email"],
                "pattern": "[^@]+@[^@]+\.[^@]+",
                "title": "Enter a valid email address",
            }
        ),
    )


class PasswordResetDoneForm(Form):
    otp1 = CharField(
        required=True,
        widget=TextInput(attrs={"class": FormsClasses.OTP_CLASS}),
    )
    otp2 = CharField(
        required=True,
        widget=TextInput(attrs={"class": FormsClasses.OTP_CLASS}),
    )
    otp3 = CharField(
        required=True,
        widget=TextInput(attrs={"class": FormsClasses.OTP_CLASS}),
    )
    otp4 = CharField(
        required=True,
        widget=TextInput(attrs={"class": FormsClasses.OTP_CLASS}),
    )
    otp5 = CharField(
        required=True,
        widget=TextInput(attrs={"class": FormsClasses.OTP_CLASS}),
    )
    otp6 = CharField(
        required=True,
        widget=TextInput(attrs={"class": FormsClasses.OTP_CLASS}),
    )
