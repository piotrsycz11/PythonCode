
# File Translator

File Translator to aplikacja desktopowa stworzona przy użyciu biblioteki Tkinter w Pythonie. Umożliwia ona tłumaczenie tekstu zawartego w dokumentach Word (.docx) z języka polskiego na angielski i odwrotnie, korzystając z API Eden AI.

## Funkcje

- Wybór dokumentu Word do tłumaczenia
- Wybór kierunku tłumaczenia (polski -> angielski, angielski -> polski)
- Tłumaczenie tekstu przy użyciu wybranego dostawcy tłumaczeń przez API Eden AI
- Zapis przetłumaczonego tekstu do nowego dokumentu Word

## Wymagania

- Python 3.x
- Moduł `tkinter` dla Pythona
- Moduł `requests`
- Moduł `json`
- Moduł `python-docx`
- Klucz API do Eden AI

## Instalacja

Aby skorzystać z aplikacji, należy zainstalować wymagane zależności. Można to zrobić, uruchamiając poniższą komendę w terminalu:

```bash
pip install requests python-docx
```

## Konfiguracja

Przed użyciem aplikacji należy uzyskać klucz API od Eden AI i wprowadzić go do zmiennej `API_KEY` w kodzie.

## Uruchomienie

Aplikację można uruchomić, wykonując plik skryptu Pythona w terminalu lub środowisku programistycznym:

```bash
python file_translator.py
```

## Użycie

1. Uruchom aplikację.
2. Kliknij przycisk "Wybierz plik" i wybierz dokument Word, który chcesz przetłumaczyć.
3. Wybierz kierunek tłumaczenia (polski -> angielski lub angielski -> polski).
4. Kliknij przycisk "Tłumacz", aby rozpocząć proces tłumaczenia.
5. Zapisz przetłumaczony dokument, gdy pojawi się taka możliwość.

## Licencja

Projekt jest udostępniony na licencji MIT.
