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

```markdown
default:
  password = "123@pwd"

development:

production:
  password = "sek@987342$"

testing:
  password = 777777



```



settings.from_env('production').PASSWORD == "sek@987342$"
