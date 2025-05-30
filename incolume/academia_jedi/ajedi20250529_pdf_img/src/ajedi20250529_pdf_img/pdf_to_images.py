"""PDF coverter to Image.

Script Python para converter cada página de um arquivo PDF
em imagens separadas.

Uso:
  python pdf_to_images.py <caminho_pdf_entrada> <diretorio_saida>
    [--formato FORMATO] [--dpi DPI]

Argumentos:
  caminho_pdf_entrada  Caminho para o arquivo PDF de entrada.
  diretorio_saida      Diretório onde as imagens serão salvas.

Opções:
  --formato FORMATO    Formato da imagem de saída (png,
     jpeg, tiff, etc.). Padrão: png.
  --dpi DPI            Resolução da imagem em pontos por
      polegada (DPI). Padrão: 300.
"""

# ruff: noqa: BLE001 T201

import argparse
from pathlib import Path

from pdf2image import convert_from_path


def converter_pdf_para_imagens(pdf_path:str, output_dir:str, formato='png', dpi=300):
    """Converte cada página de um PDF em arquivos de imagem.

    Args:
        pdf_path (str): Caminho para o arquivo PDF.
        output_dir (str): Diretório para salvar as imagens.
        formato (str): Formato da imagem (png, jpeg, etc.).
        dpi (int): Resolução da imagem em DPI.
    """
    pdf_path: Path = Path(pdf_path)
    output_dir: Path = Path(output_dir)

    if not pdf_path.is_file():
        print(f"Erro: Arquivo PDF não encontrado em '{pdf_path}'")
        return

    # Cria o diretório de saída se não existir
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Convertendo '{pdf_path.name}' para imagens...")
    try:
        # Converte o PDF em uma lista de objetos de imagem PIL
        imagens = convert_from_path(pdf_path, dpi=dpi, fmt=formato)

        # Salva cada imagem
        for i, imagem in enumerate(imagens, 1):
            nome_arquivo = f'{pdf_path.stem}_p{i:03}.{formato.lower()}'
            caminho_saida = output_dir / nome_arquivo
            imagem.save(caminho_saida, formato.upper())
            print(f"  - Página {i} salva como '{caminho_saida}'")

        print(
            f'\nConversão concluída! {len(imagens)}'
            " páginas salvas em '{output_dir}'.",
        )

    except Exception as e:
        print(f'Erro durante a conversão: {e}')
        print('Verifique se o poppler está instalado e no PATH do sistema.')
        print(
            'No Ubuntu/Debian: sudo apt-get update '
            '&& sudo apt-get install -y poppler-utils',
        )
        print('No macOS (com Homebrew): brew install poppler')
        print(
            'No Windows: Baixe o Poppler e adicione o diretório'
            " 'bin' ao PATH.",
        )


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Converte páginas de PDF em imagens.',
    )
    parser.add_argument(
        'caminho_pdf_entrada',
        help='Caminho para o arquivo PDF de entrada.',
    )
    parser.add_argument(
        'diretorio_saida',
        help='Diretório onde as imagens serão salvas.',
    )
    parser.add_argument(
        '--formato',
        default='png',
        help='Formato da imagem de saída (png,'
        ' jpeg, tiff, etc.). Padrão: png.',
    )
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='Resolução da imagem em pontos por '
        'polegada (DPI). Padrão: 300.',
    )

    args = parser.parse_args()

    converter_pdf_para_imagens(
        args.caminho_pdf_entrada,
        args.diretorio_saida,
        args.formato,
        args.dpi,
    )
