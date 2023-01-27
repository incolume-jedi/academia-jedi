from googletrans import Translator


def ex1():
    translator = Translator()
    translator.detect(text="이 문장은 한글로 쓰여졌습니다.")
    # <Detected lang=ko confidence=0.27041003>
    translator.detect("この文章は日本語で書かれました。")
    # <Detected lang=ja confidence=0.64889508>
    translator.detect("This sentence is written in English.")
    # <Detected lang=en confidence=0.22348526>
    translator.detect("Tiu frazo estas skribita en Esperanto.")
    # <Detected lang=eo confidence=0.10538048>


def run():
    ex1()


if __name__ == "__main__":  # pragma: no cover
    run()
