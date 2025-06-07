# Secrets Dynaconf

---

O arquivo de secredo é configurado no config do dynaconf.

```python
    settings_files=[
        Path(__file__).parent.joinpath('settings/settings.yml'),
        *Path(__file__).parent.rglob('settings/.secrets.ya?ml'),
        *Path(__file__).parent.rglob('credentials/*.json'),
    ],
```

E podem ser nos formatos yaml, json, ini e toml

Conteúdo para `.secrets.yml`

```yaml
default:
  password: 123@pwd

development:

production:
  password: sek@987342$

testing:
  password: 777777

```

Conteúdo para `.secrets.json`
```json
{
  "default": {
    "password": "123@pwd"
  },
  "development": null,
  "production": {
    "password": "sek@987342$"
  },
  "testing": {
    "password": 777777
  }
}
```

Conteúdo para `.secrets.toml`

```toml
[default]
password = "123@pwd"

[production]
password = "sek@987342$"

[testing]
password = 777777
```


No carregamento de qualquer um destes, os ambientes são separados.

```python

  settings.from_env('production').PASSWORD == "sek@987342$"
  settings.from_env('development').PASSWORD == "123@pwd"
  settings.from_env('testing').PASSWORD == "777777"
  settings.PASSWORD == "123@pwd"
```
