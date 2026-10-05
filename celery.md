# Celery self-exploration

### 2026-10-05 Erstes Ausprobieren. Begriffe

- application: Celery-Instanz, mit Celery() instanziert
- task message: "when you send a task message in Celery" -> Es gibt Task-Nachrichten, und die kann man versenden
- task registry: Mapping von Task-Namen zu deren eigentlichen Funktionen, "local task registry" -> lokal für die Applikation? gibt es auch globale?
- workers: Weiß noch nicht, was sie genau sind. mit `app.worker_main(argv=...)` kann man Worker anlegen und starten. Komische Syntax.

