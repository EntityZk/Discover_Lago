# 🌊 Discover Lago

**Discover Lago** è una guida turistica web dedicata al **Lago Maggiore**, sviluppata in **HTML5** e **CSS3** come progetto per il laboratorio di **TPSIT**.

Il sito offre una panoramica completa delle bellezze del lago, delle attività all'aria aperta e delle informazioni pratiche per organizzare una visita, con un'interfaccia semplice, responsive e facilmente navigabile.

---

## 📄 Struttura del sito

Il progetto è composto da **quattro pagine HTML interconnesse**:

| Pagina | Contenuto |
|--------|-----------|
| **`index.html`** | Home page con presentazione del progetto e navigazione generale. |
| **`sezione-a.html`** | Le **5 località principali** del Lago Maggiore: Stresa, Verbania, Cannobio, Luino e Arona. |
| **`sezione-b.html`** | **4 attività ed escursioni** da provare: Mottarone, tour in battello, Val Grande e sport acquatici. |
| **`sezione-c.html`** | **Informazioni pratiche**: alloggi, trasporti e consigli di viaggio. |

Ogni pagina è collegata alle altre tramite un menu di navigazione condiviso, per garantire un'esperienza utente fluida.

---

## 🛠️ Tecnologie utilizzate

- **HTML5** — struttura semantica delle pagine
- **CSS3** — stile, layout e responsività
- **Git & GitHub** — versionamento e collaborazione
- **GitHub Issues & Pull Requests** — gestione del flusso di lavoro

---

## 🔀 Workflow Git/GitHub

Il progetto è stato sviluppato simulando un **ambiente di lavoro aziendale**, con ruoli e processi tipici di un team di sviluppo software:

1. **Setup iniziale**
   - Il **Project Manager** ha creato il repository su GitHub e configurato le **Issues** per tracciare le attività da svolgere.

2. **Sviluppo su branch separati**
   - Ogni sviluppatore ha lavorato su un branch dedicato:
     - `sezione-a` → località principali
     - `sezione-b` → attività ed escursioni
     - `sezione-c` → informazioni pratiche

3. **Pull Request e revisione**
   - Il contenuto di ciascun branch è stato pubblicato tramite **Pull Request**, sottoposto a revisione e corretto in base ai feedback ricevuti.

4. **Gestione dei conflitti**
   - È stato volutamente generato e risolto un **conflitto di fusione su `index.html`**, per testare la gestione di modifiche concorrenti sul ramo `main`.

---

## 🚀 Come eseguire il progetto

1. Clonare il repository:

   ```bash
   git clone https://github.com/<utente>/discover-lago.git
