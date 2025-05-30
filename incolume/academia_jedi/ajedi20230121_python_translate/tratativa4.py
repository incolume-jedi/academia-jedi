from googletrans import Translator

# ruff: noqa: D100

translator = Translator(
    service_urls=[
        'translate.google.com',
        'translate.google.co.kr',
    ],
)

translator.translate('안녕하세요.')
translator.translate('안녕하세요.', dest='ja')
translator.translate('veritas lux mea', src='la')
