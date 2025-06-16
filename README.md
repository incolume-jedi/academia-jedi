# Academia JEDI

Codigo produzidos pela academia da guilda JEDI (Junta Especializada de Desenvolvimento e Inovação) Incolume em https://discord.gg/eBNamXVtBW

Estes códigos, foram e/ou serão desenvolvidos para treinamento da guilda.

Todo o conteúdo criado, produzido e armazenado, para fins de aprendizado, é de livre acesso aos membros da guilda JEDI Incolume.

A partir desta versão há utilização em conjunto dos gerenciadores de pacotes `uv` e `poetry`.

Instalação do `uv` com detalhes disponível em `https://docs.astral.sh/uv/getting-started/installation/`

- Unixlike
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   ou
   
   ```bash
   wget -qO- https://astral.sh/uv/install.sh | sh
   ```

- Windows
   ```bash
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```


- Na raiz do projeto execute: 
   - `uv venv -p <python-version> `;
   - `source .venv/Script/activate` (para windows)
   - `source .venv/bin/activate` (para unix like)
   - `uvx poetry install`;

- Para outros gerenciadores de pacotes, utilize Python conforme a versão indicada, atualmente Python 3.10+.

- Para ativar a configuração fina do `git` em ambientes Unix-Like, execute: `sh settings/gitconfig.sh`

As dependências estão contidas em pyproject.toml;
