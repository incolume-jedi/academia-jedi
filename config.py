from pathlib import Path

from dynaconf import Dynaconf, Validator

settings = Dynaconf(
    envvar_prefix='ACADEMIA_JEDI',
    load_dotenv=True,
    settings_files=[
        Path(__file__).parent.joinpath('settings.toml'),
        Path(__file__).parent.joinpath('.secrets.toml'),
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
