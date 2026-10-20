# Discover Lago Maggiore

> Guida turistica dimostrativa dedicata alle località, alle esperienze e alle informazioni pratiche del Lago Maggiore.

Discover Lago è un progetto didattico di **TPSIT – classe 5ª superiore**. Il sito usa HTML semantico e CSS moderno per offrire una navigazione chiara, responsive e accessibile, senza framework JavaScript o dipendenze di build.

## Pagine

| File | Descrizione |
| --- | --- |
| `index.html` | Home page e accesso alle sezioni |
| `localita.html` | Stresa, Verbania, Cannobio, Luino e Arona |
| `escursioni.html` | Idee per trekking, battelli, natura e sport d'acqua |
| `alloggi_info.html` | Alloggi, trasporti e consigli di viaggio |
| `privacy.html` | Note sul progetto, contenuti esterni e privacy |
| `progetto.html` | Obiettivi, tecnologie e accessibilità del progetto |
| `404.html` | Pagina di errore per gli indirizzi non trovati |
| `scripts/check_site.py` | Controllo automatico dei metadati e dei collegamenti interni |
| `.github/workflows/validate-site.yml` | Avvia i controlli ad ogni push e pull request verso `main` |
| `style.css` | Sistema grafico condiviso e responsive |

## Tecnologie

- **HTML5**: struttura semantica, titoli gerarchici, metadati e attributi accessibili.
- **CSS3**: custom properties, Grid, Flexbox, layout responsive, stati focus e rispetto di `prefers-reduced-motion`.
- **Git e GitHub**: branch, commit, pull request e revisione delle modifiche.
- **GitHub Pages** (facoltativo): il progetto può essere pubblicato come sito statico dalla root del branch scelto.

## Controllo automatico

La GitHub Action `Validate static site` controlla le pagine HTML ad ogni push su `main` e nelle pull request dirette a `main`. Lo script verifica lingua, titolo, descrizione, viewport, ID duplicati e destinazioni dei collegamenti interni. È un controllo leggero: non sostituisce una prova manuale nel browser né verifica la disponibilità delle immagini esterne.

Per eseguirlo in locale con Python 3:

```bash
python3 scripts/check_site.py
```

## Avvio locale

Non è necessario installare pacchetti.

1. Scarica o clona il repository.
2. Apri `index.html` nel browser oppure usa l'estensione **Live Server** di Visual Studio Code.
3. Naviga tra le pagine dal menu principale.

## Workflow Git consigliato

Per mantenere `main` stabile, sviluppa le nuove funzionalità in branch dedicati e proponi le modifiche tramite pull request.

```bash
git switch main
git pull origin main
git switch -c feature/nome-modifica
# modifica e verifica i file
git add .
git commit -m "feat: descrizione breve"
git push -u origin feature/nome-modifica
```

Apri quindi una Pull Request verso `main`, controlla la differenza dei file e verifica la navigazione su desktop e mobile prima del merge.

### Convenzione per i commit

- `feat:` nuova funzionalità o sezione
- `style:` miglioramenti grafici e formattazione
- `fix:` correzione di un problema
- `docs:` documentazione
- `refactor:` riorganizzazione del codice senza cambiare il comportamento

## Controlli prima della consegna

- Tutti i collegamenti interni portano a file esistenti.
- Ogni pagina ha un titolo e una descrizione specifici.
- Le immagini hanno testi alternativi significativi e caricamento differito quando opportuno.
- La navigazione è utilizzabile da tastiera e l'utente può saltare direttamente al contenuto.
- Layout e animazioni rispettano gli schermi piccoli e le preferenze di movimento ridotto.
- Le informazioni su orari, servizi e disponibilità sono verificate su fonti ufficiali prima di essere usate per organizzare una visita.

## Crediti e limiti

Il sito ha finalità didattiche e non rappresenta un portale turistico ufficiale. Alcune immagini e i font vengono caricati da siti esterni; disponibilità, diritti d'uso e attribuzioni devono essere controllati prima di una pubblicazione pubblica. Il progetto non include backend, account o raccolta di dati tramite moduli.

## Gruppo e tracciamento TPSIT

- **PM / sviluppatore C:** [EntityZk](https://github.com/EntityZk)
- **Sviluppatore A:** [Tomino](https://github.com/Tomino)
- **Sviluppatore B:** [amadeiaca-creator](https://github.com/amadeiaca-creator)

### Issue di lavoro

- [Issue #2 — Sezione A: Località](https://github.com/EntityZk/Discover_Lago/issues/2) — assegnazione prevista: sviluppatore A.
- [Issue #3 — Sezione B: Esperienze ed escursioni](https://github.com/EntityZk/Discover_Lago/issues/3) — assegnata a sviluppatore B.
- [Issue #4 — Sezione C: Guida pratica](https://github.com/EntityZk/Discover_Lago/issues/4) — assegnata al PM / sviluppatore C.

### Stato della consegna

Questa sezione documenta la preparazione del repository, non sostituisce le prove del lavoro svolto da ciascun componente. I commit, le PR, le revisioni, le correzioni e il conflitto di merge vanno registrati solo dopo che sono realmente avvenuti. Le schermate del conflitto devono essere salvate in `documentazione/` durante l'esercitazione reale; non sono ancora attestate da questo documento.
