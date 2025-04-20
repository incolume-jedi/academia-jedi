"""Estudo sobre compactação em runtime."""

import dataclasses
import inspect
import shutil
import zipfile
from collections.abc import Container
from pathlib import Path
from tempfile import gettempdir
from typing import Final
from incolume.academia_jedi import logger
from faker import Faker



@dataclasses.dataclass
class URL:
    """URL file compreess."""
    logger.info(inspect.stack()[0][3])

    z7: Final[str] = 'https://pastebin.com/raw/KGmnsB0j'
    zip: Final[str] = 'https://pastebin.com/raw/Zt9BHEF4'
    fifa23: Final[str] = 'https://pastebin.com/raw/gRhw1z3i'
    fifa22: Final[str] = 'https://pastebin.com/raw/6Tp8MFxF'
    fifa21: Final[str] = 'https://pastebin.com/raw/2TvfyBHm'
    fifa20: Final[str] = 'https://pastebin.com/raw/PxVMWeGt'
    fifa19: Final[str] = 'https://pastebin.com/raw/wAGxStyY'
    fifa18: Final[str] = 'https://pastebin.com/raw/gSpzqEub'
    fifa17: Final[str] = 'https://pastebin.com/raw/4H5493UF'


def set_env(count: int = 10, seed: int = 191) -> Path:
    """Set environment.

    Boilerplate for compress implementations.
    """
    logger.info(inspect.stack()[0][3])
    Faker.seed(seed)
    fake = Faker('pt-br')

    text: Final[str] = """
¹ E havia entre os fariseus um homem, chamado Nicodemos, príncipe dos judeus.
² Este foi ter de noite com Jesus, e disse-lhe: Rabi, bem sabemos que és
Mestre, vindo de Deus; porque ninguém pode fazer estes sinais que tu fazes,
 se Deus não for com ele.
³ Jesus respondeu, e disse-lhe: Na verdade, na verdade te digo que aquele que
 não nascer de novo, não pode ver o reino de Deus.
⁴ Disse-lhe Nicodemos: Como pode um homem nascer, sendo velho? Pode,
 porventura, tornar a entrar no ventre de sua mãe, e nascer?
⁵ Jesus respondeu: Na verdade, na verdade te digo que aquele que não nascer da
 água e do Espírito, não pode entrar no reino de Deus.
⁶ O que é nascido da carne é carne, e o que é nascido do Espírito é espírito.
⁷ Não te maravilhes de te ter dito: Necessário vos é nascer de novo.
⁸ O vento assopra onde quer, e ouves a sua voz, mas não sabes de onde vem, nem
 para onde vai; assim é todo aquele que é nascido do Espírito.
⁹ Nicodemos respondeu, e disse-lhe: Como pode ser isso?
¹⁰ Jesus respondeu, e disse-lhe: Tu és mestre de Israel, e não sabes isto?
¹¹ Na verdade, na verdade te digo que nós dizemos o que sabemos, e testificamos
 o que vimos; e não aceitais o nosso testemunho.
¹² Se vos falei de coisas terrestres, e não crestes, como crereis, se vos falar
 das celestiais?
¹³ Ora, ninguém subiu ao céu, senão o que desceu do céu, o Filho do homem, que
 está no céu.
¹⁴ E, como Moisés levantou a serpente no deserto, assim importa que o Filho do
 homem seja levantado;
¹⁵ Para que todo aquele que nele crê não pereça, mas tenha a vida eterna.
¹⁶ Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito,
 para que todo aquele que nele crê não pereça, mas tenha a vida eterna.
¹⁷ Porque Deus enviou o seu Filho ao mundo, não para que condenasse o mundo,
 mas para que o mundo fosse salvo por ele.
¹⁸ Quem crê nele não é condenado; mas quem não crê já está condenado,
 porquanto não crê no nome do unigênito Filho de Deus.
¹⁹ E a condenação é esta: Que a luz veio ao mundo, e os homens amaram
 mais as trevas do que a luz, porque as suas obras eram más.
²⁰ Porque todo aquele que faz o mal odeia a luz, e não vem para a luz,
 para que as suas obras não sejam reprovadas.
²¹ Mas quem pratica a verdade vem para a luz, a fim de que as suas obras sejam
 manifestas, porque são feitas em Deus.
²² Depois disto foi Jesus com os seus discípulos para a terra da Judeia;
 e estava ali
 com eles, e batizava.
²³ Ora, João batizava também em Enom, junto a Salim, porque havia ali
 muitas águas; e vinham ali, e eram batizados.
²⁴ Porque ainda João não tinha sido lançado na prisão.
²⁵ Houve então uma questão entre os discípulos de João e os judeus acerca da
 purificação.
²⁶ E foram ter com João, e disseram-lhe: Rabi, aquele que estava contigo além
do Jordão, do qual tu deste testemunho, ei-lo batizando,
 e todos vão ter com ele.
²⁷ João respondeu, e disse: O homem não pode receber coisa alguma,
 se não lhe for dada do céu.
²⁸ Vós mesmos me sois testemunhas de que disse: Eu não sou o Cristo,
 mas sou enviado adiante dele.
²⁹ Aquele que tem a esposa é o esposo; mas o amigo do esposo, que lhe assiste
 e o ouve, alegra-se muito com a voz do esposo. Assim, pois, já este meu gozo
   está cumprido.
³⁰ É necessário que ele cresça e que eu diminua.
³¹ Aquele que vem de cima é sobre todos; aquele que vem da terra é da terra e
 fala da terra. Aquele que vem do céu é sobre todos.
³² E aquilo que ele viu e ouviu isso testifica; e ninguém
 aceita o seu testemunho.
³³ Aquele que aceitou o seu testemunho, esse confirmou que Deus é verdadeiro.
³⁴ Porque aquele que Deus enviou fala as palavras de Deus; pois não lhe dá
 Deus o Espírito por medida.
³⁵ O Pai ama o Filho, e todas as coisas entregou nas suas mãos.
³⁶ Aquele que crê no Filho tem a vida eterna; mas aquele que não crê no
Filho não verá a vida, mas a ira de Deus sobre ele permanece.

João 3:1-36"""
    dout: Path = (
        Path(gettempdir()) / __name__.split('.')[-1]
    )  # output directory
    source: Path = dout / 'source'  # source files dir
    source.mkdir(exist_ok=True, parents=True)
    fout: Path = dout / 'archives.zip'

    # Create the files into source with content (John 3, hole bible)
    [
        source.joinpath(file).write_text(text)
        for file in (fake.file_name(extension='txt') for _ in range(count))
    ]
    # Create the zipfile
    with zipfile.ZipFile(
        file=fout,
        mode='w',
        compression=zipfile.ZIP_LZMA,  # algoritm compress
        compresslevel=9,  # compress level
    ) as zip_handler:
        [
            zip_handler.write(file, arcname=file.relative_to(dout))
            for file in source.iterdir()
        ]
    shutil.rmtree(source)
    return fout


def gen_zip(
    members: Container[Path],
    zipname: Path | None = None,
    dout: Path | None = None,
) -> Path:
    """Generate zipfile for path."""
    logger.info(inspect.stack()[0][3])
    zipname = zipname or Path('archives.zip')
    dout = dout or Path()
    with zipfile.ZipFile(
        file=zipname,
        mode='w',
        compression=zipfile.ZIP_LZMA,  # algoritm compress
        compresslevel=9,  # compress level
    ) as handler:
        [handler.write(file, arcname=file.name) for file in members]
    return zipname
