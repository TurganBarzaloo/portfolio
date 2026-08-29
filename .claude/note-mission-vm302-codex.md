# Note de mission — Codex : cible VM302 « Station de développement assistée par IA locale »

**Émetteur :** Claude (mainteneur de `C:\dev\portfolio`), à la demande de Stéphane.
**Destinataire :** Codex (mainteneur des sources `…\Portfolio-Technique\`).
**Date :** 2026-08-30.
**Statut de la brique :** *Planifié* (aucun déploiement — ne pas présenter comme actif).

> Rappel de cloisonnement : Claude n'écrit pas dans les sources ; cette note est un **intrant** pour que Codex
> crée/mette à jour les fiches et fichiers projet côté `…\Portfolio-Technique\`. Le portfolio ne publiera VM302
> qu'à partir d'une fiche `approved`.

---

## 1. Objet

Préciser la cible de **VM302** : une **station Windows 11 de développement** (Python, HTML/JS, …)
**assistée par IA en local**, consommant le **modèle publié sur VM210** (Ollama / RTX 5090), avec une chaîne
d'outils **100 % open source**. Remplace l'ancienne désignation « OpenClaw », puis l'intitulé provisoire
« OpenCode + PyCharm + Codeium ».

**Changement notable à acter :** on écarte **Codeium** (propriétaire, orienté cloud) au profit d'un
**plugin open source compatible Ollama** (Continue.dev). Rationnel en §4.

## 2. Fichiers à mettre à jour (côté Codex)

- **`stack-ia-cible`** (fiche de la pile IA cible) : ajouter/mettre à jour la section **VM302 — Station Dev IA**.
- **Fichier(s) « projet »** (INDEX / présentation-générale / suivi) : refléter la cible VM302 et son statut *planifié*.
- **TODO projet** (côté Codex) : ajouter les jalons de §6.
- Vérifier la **cohérence** avec `vm200-reverse-proxy`, `vm210` et `rag-pgvector` (réutilisation d'Ollama et des embeddings existants).

## 3. Cible fonctionnelle à décrire dans la fiche

Station de dev W11 offrant : **complétion inline** (tab), **chat de code**, **édition/agent multi-fichiers**,
et **chat sur le dépôt** (RAG codebase) — le tout servi par l'infrastructure locale, sans dépendance cloud.

Découpage en couches :

| Couche | Rôle | Choix cible (OSS) |
|---|---|---|
| IDE + assistance inline | éditer, compléter, chatter dans l'IDE | **PyCharm CE** + **Continue.dev** (Apache-2.0, Ollama natif, `@codebase`) |
| Agent terminal | édition dirigée, git-aware | **OpenCode** et/ou **Aider** (à départager en banc de test) |
| Modèles de code | complétion FIM + chat/édition | **Qwen2.5-Coder** : petit (1.5b/3b) pour la complétion, grand (14b/32b) pour chat/édition |
| Service de modèle | endpoint d'inférence | **Ollama sur VM210** (existant), option passerelle **LiteLLM** (endpoint OpenAI-compatible unifié) |
| Indexation codebase | « chat sur mon repo » local | embeddings **bge-m3** + **pgvector** (VM215) — déjà en place |
| Qualité (non-IA) | lint/format/preview | `ruff`/`black` (Python), `prettier`/`eslint` (HTML/JS), live-preview |

## 4. Décisions et justifications (à consigner)

1. **Plugin JetBrains open source compatible Ollama = Continue.dev** (et non Codeium). Motif : souveraineté +
   licence open source + Ollama natif + indexation `@codebase` réutilisant bge-m3/pgvector déjà déployés.
2. **Modèle de complétion distinct du modèle de chat** : la complétion tab exige une **latence < 1 s** → petit
   modèle FIM toujours chargé ; chat/édition sur un modèle plus grand à la demande. Famille **Qwen2.5-Coder**
   (Apache-2.0) pour rester pleinement open source.
3. **OpenCode vs Aider** : à **comparer sur banc de test** (économie de tokens, discipline des diffs, intégration
   git) avant d'en faire la référence terminal. Ne pas trancher dans la fiche tant que le banc n'a pas eu lieu.
4. **Passerelle LiteLLM (recommandée dès le départ)** : exposer VM210 via un endpoint **OpenAI-compatible unique**
   afin que tous les outils pointent la même URL (journalisation/quotas, changement de modèle sans reconfigurer
   chaque outil). Décision d'architecture à acter tôt.

## 5. Contraintes / limites à documenter (honnêteté)

- **Exclusivité GPU** : la RTX 5090 est exclusive et **VM210 sert déjà OpenWebUI/RAG**. Arbitrer la **contention**
  (petit modèle de complétion résident vs gros modèle à la demande) ; dimensionner la VRAM (32 Go).
- **Qualité des modèles locaux** : excellents en complétion/éditions moyennes, **en-deçà des modèles frontier**
  sur des refactors agentic complexes — calibrer les attentes (c'est le prix de la souveraineté).
- **Fraîcheur de l'écosystème** : versions/licences des plugins évoluent vite → **vérifier maintenance et licence**
  au moment de figer (Continue, OpenCode, Aider).
- **Poste Windows** : VM302 = **W11** (pas Linux) ; vérifier la compatibilité des outils (Aider/OpenCode via
  terminal/WSL le cas échéant).

## 6. Jalons proposés (pour la TODO Codex)

1. Publier **Qwen2.5-Coder** (petit + grand) sur Ollama VM210 et valider le débit LAN.
2. Installer **PyCharm CE + Continue.dev** sur VM302, pointer Ollama VM210 ; valider complétion + chat.
3. Activer **`@codebase`** de Continue sur bge-m3/pgvector ; valider le « chat sur repo ».
4. Banc de test **OpenCode vs Aider** ; consigner le choix.
5. (Option archi) Mettre **LiteLLM** en façade de VM210 ; re-router les outils.
6. Ajouter la chaîne **qualité** (ruff/prettier/eslint + preview).
7. Une fois la fiche `stack-ia-cible`/VM302 **approved**, notifier Claude pour publication portfolio.

## 7. Ce que Claude a déjà fait côté portfolio

- `architecture.html` : nœud **302** renommé « **Station Dev IA (W11)** — Dév Python/HTML assisté par IA locale
  (VM210) · PyCharm + Continue · OpenCode / Aider · **planifié** » (statut inchangé : planifié).
- En attente d'une fiche approuvée pour, le cas échéant, une page ou un encart dédiés.

## 8. Alternatives OSS écartées / à garder en réserve (traçabilité)

Zed, Void (éditeurs AI-natifs), Cline/Roo Code (agents VS Code/VSCodium), **Tabby** (serveur de complétion
auto-hébergé dédié), **vLLM** (service haute concurrence si Ollama sature). Non retenues en cible initiale pour
limiter le nombre de composants, mais pertinentes en évolution.
