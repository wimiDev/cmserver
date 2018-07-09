from django.db import models
class User(models.Model):

    UserName = models.CharField(max_length=20)
    UserPass = models.CharField(max_length=20)

    ONLINE = 'ONLINE'
    OFFLINE = 'OFFLINE'
    LOGIN_STATE = (
        (ONLINE, 'online'),
        (OFFLINE, 'offline'),
    )
    #logon state
    LoginState = models.CharField(
                     max_length=20,
                     choices = LOGIN_STATE,
                     default=OFFLINE,
    )

    NORMAL = 'NORMAL'
    FROZEN = 'FROZEN'
    ACCOUNT_STATE = (
    	(NORMAL,'normal'),
    	(FROZEN,'frozen'),
    )
    #account state
    AccountState = models.CharField(
    	max_length=20,
    	choices = ACCOUNT_STATE,
    	default = NORMAL,
    )