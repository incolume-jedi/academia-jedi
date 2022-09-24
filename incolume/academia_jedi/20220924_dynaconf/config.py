
from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix="INCOLUME",
    settings_files=['settings.toml', '.secrets.toml'],
    validators=[
        Validator("NAME", must_exist=True, ne="App"),  # NAME deve existir != App
    ]
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
