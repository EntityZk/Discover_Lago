# Documentazione dell'esercitazione Git

Questa cartella è destinata alle prove reali richieste dalla traccia TPSIT. **Non inserire schermate ricostruite o descrizioni di operazioni non avvenute.**

## Conflitto di merge da svolgere in gruppo

1. Tutti aggiornano il branch locale `main` con `git pull origin main`.
2. Creare due branch separati, `titolo-a` e `titolo-b`.
3. Su entrambi i branch modificare **la stessa riga** di `index.html`, usando due titoli diversi.
4. Fare almeno un commit su ciascun branch e pubblicarli con `git push -u origin titolo-a` e `git push -u origin titolo-b`.
5. Integrare prima `titolo-a` in `main`.
6. Provare a integrare `titolo-b`: Git deve segnalare il conflitto sulla riga modificata da entrambi.
7. Aprire `index.html`, risolvere i marcatori `<<<<<<<`, `=======` e `>>>>>>>` scegliendo il contenuto concordato dal gruppo.
8. Verificare che non restino marcatori, poi eseguire `git add index.html` e completare il merge con `git commit`.
9. Pubblicare il risultato e verificare la versione finale su GitHub.

## Screenshot da salvare qui

Dopo aver svolto davvero i passaggi, salvare immagini leggibili che mostrino:

- i due branch e le rispettive modifiche;
- il messaggio di conflitto durante il merge di `titolo-b`;
- la risoluzione del conflitto in `index.html`;
- il commit finale di merge e la versione risultante.

Usare nomi descrittivi, per esempio `01-branch-titolo-a.png`, `02-conflitto-merge.png`, `03-risoluzione.png`, `04-merge-completato.png`.

## Registro delle prove

| Prova | Stato |
| --- | --- |
| Branch `titolo-a` creato e modificato | Da svolgere |
| Branch `titolo-b` creato e modificato sulla stessa riga | Da svolgere |
| Conflitto reale riprodotto | Da svolgere |
| Conflitto risolto e merge completato | Da svolgere |
| Screenshot salvati in questa cartella | Da svolgere |

Aggiornare il registro solo dopo aver verificato ogni passaggio.