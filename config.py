"""config dynaconf Module."""

from pathlib import Path

from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    environment=True,
    envvar_prefix='AJEDII',
    load_dotenv=True,
    settings_files=[
        Path(__file__).parent.joinpath('settings.toml'),
        *Path(__file__).parent.rglob('.secrets.*'),
    ],
    environments=[
        'default',
        'development',
        'production',
        'testing',
    ],
    env_switcher='INCOLUME_MODE',
    validators=[
        Validator(
            'NAME',
            must_exist=True,
            ne='App',
        ),  # NAME deve existir != App
    ],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
