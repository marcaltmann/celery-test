# Celery self-exploration

### 2026-10-05 Erstes Ausprobieren. Begriffe

- Dokumentation ist nicht die beste, sehr viel Historie und wichtige grundlegende Sachen vermischt mit speziellen Informationen,
  und man weiß noch nicht, was was ist. Man versteht auch das große ganze nicht, bzw. den Sinn der beschriebenen Objekte, Klassen etc.
- application: Celery-Instanz, mit Celery() instanziert
- task message: "when you send a task message in Celery" -> Es gibt Task-Nachrichten, und die kann man versenden
- task registry: Mapping von Task-Namen zu deren eigentlichen Funktionen, "local task registry" -> lokal für die Applikation? gibt es auch globale?
- Tasks können private oder shared sein, default=shared, d.h. sie werden zwischen versch./allen Apps geteilt
- Tasks sind an eine App gebunden (bound), d.h. sie bekommen die default-Konfiguration dieser App?
- Task decorators @app.task sind der aktuelle/moderne Weg, einen Task zu definieren
- workers: Weiß noch nicht, was sie genau sind. mit `app.worker_main(argv=...)` kann man Worker anlegen und starten. Komische Syntax.
- Hmm, es gibt etwas wie default apps, wenn man z.B. `current_app` importiert? Bad practice, apps sollten als Argumente übergeben werden. Warum?

