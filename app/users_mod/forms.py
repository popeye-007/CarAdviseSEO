from flask_wtf import Form
from wtforms import BooleanField, StringField, EmailField, \
     PasswordField 
from wtforms.validators import DataRequired, Email , EqualTo

class CreateUserForm(Form):
    name = StringField('User Name', 
                        [DataRequired(
                            message='This is a required field.')
                        ]
                        )
    email = EmailField('Email', 
                        [Email(),
                        DataRequired(
                            message='This is a required field.')
                        ]
                        )
    password = PasswordField('Password', 
                            [EqualTo(
                                fieldname='confirm_password', 
                                message='Passwords Don\'t match!'),
                             DataRequired(message='This is a required field.')
                            ]
                            )
    # confirm_password = PasswordField('Confirm Password', 
    #                         [EqualTo(
    #                             fieldname='password', 
    #                             message='Password mismatch!'),
    #                          DataRequired(message='This is a required field.')
    #                         ]
    #                         )

    is_active = BooleanField('Active', default="checked"
                            )
