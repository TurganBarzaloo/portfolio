# TODO — Portfolio (suivi Claude)

Suivi propre au dépôt portfolio (`C:\dev\portfolio`).

Périmètre Claude (cloisonnement documentaire) :
- **Écriture** : uniquement `C:\dev\portfolio\` (y compris `.claude\`).
- **Sources factuelles autorisées (lecture seule)** : `…\Portfolio-Technique\sources-publiques`
  (unique source de faits) · `…\Portfolio-Technique\validation` · `…\Portfolio-Technique\PUBLICATION-POLICY.md`.
- **Aucun accès** : le reste de `C:\Projets-Techniques` (privé) ni le dossier Obsidian Knowledge.
- Publier uniquement des fiches `approved`/`published`. Info manquante ou contradiction → **signaler à Stéphane**.
- Rien n'est commité/poussé sans accord ; `git push` = déploiement GitHub Pages.

Dernière mise à jour : 2026-09-28.

## En attente (priorité haute → basse)

- [ ] **Multilingue (i18n) — étendre aux 20 pages restantes.** Mécanique en place et EN LIGNE
  (générateur `tools/build_i18n.py` + `i18n/{en,ru,zh,es}.json`). Voir mémoire `portfolio-i18n.md`
  et le plan `C:\Users\smura\.claude\plans\comment-rendre-mon-site-wild-squirrel.md`.
  - **Fait (3 pages, 5 langues, en ligne)** : `index.html`, `pages/about.html`, `pages/vm302-station-dev-ia.html`.
  - **Restant (20 pages `pages/`)** : architecture, infrastructure, proxmox, reverse_proxy, gpu_passthrough,
    storage_zfs, os, network, ia_llm, rag, ia_image, speech_ai, vm301-hermes-opencode, docker, nextcloud,
    n8n, python, git, obsidian, devops.
  - Méthode par page : annoter `data-i18n` (ne PAS tagger code/produits/sigles) → traduire les clés dans
    les 4 JSON → ajouter la page à `PAGES` dans `tools/build_i18n.py` → `python tools/build_i18n.py` → vérifier.
  - ⚠️ `ia_llm.html`, `docker.html`, `infrastructure.html`, `gpu_passthrough.html` ont été **enrichies le 2026-09-28**
    (ComfyUI/plafond) : leur annotation devra couvrir ce nouveau contenu.

- [ ] **Relecture des traductions du pilote par Stéphane** (déjà en ligne) — surtout `about.html` :
  intitulés de la fonction publique territoriale (Ingénieur/Technicien Territorial, concours), titres de postes.
  Point ouvert : en-tête about dit « Ingénieur informatique », pied de page normalisé « Ingénieur Infrastructure ».

- [ ] **Reframe « État et ordre de démarrage des VM »** — reste `docker.html` et `network.html`,
  uniquement si une fiche approuvée le couvre (fait sur proxmox.html et gpu_passthrough.html).

- [ ] **Fiche « Claude Code avec Ollama distant »** : en `review` → exclue de la génération. Attendre `approved`.

## Fait (récent)

- [x] **2026-09-28** — ComfyUI + Ollama partage GPU (VM210) : panneaux sur `ia_llm.html` (mesures VRAM, RealVisXL/Open RAIL++)
  et `docker.html` (conteneur durci). Plafond 400 W reformulé en **diagnostic passé** (essais à 600 W) sur
  `gpu_passthrough.html` / `ia_llm.html` / `infrastructure.html`. Poussé (commit `f261ec9`).
- [x] **2026-09-20/28** — i18n : mécanique multilingue + pilote 3 pages (FR/EN/RU/ZH/ES). En ligne.
- [x] **2026-09-20** — Conformité logos : Git/Docker/Python/Tux officiels + mentions (`about.html#credits`) ;
  9 marques → icônes originales (`assets/*.svg`). Liste des demandes d'autorisation : `.claude/logo-authorization-requests.md`.
- [x] **2026-09-20** — Plafond électrique RTX 5090 (400 W diag) publié ; VM302 régularisée `approved`.
- [x] **2026-09-20** — Page VM302 (DeepSeek Harness) + tuiles accueil + badge « Open Source & fair-code » ;
  `devops.html` relancé « Outils libres & DevOps ».
- [x] **2026-08-31** — VM301 (Hermes + OpenCode) `verified` : Hermes `qwen3.6:35b`, OpenCode `qwen3-coder:30b`.
- [x] **2026-08-30** — Page VM301 + reverse_proxy (VM200) + n8n (VM300) publiés HTTPS.
- [x] **2026-08-14** — proxmox (intro + cycle de vie templates), python (ML/DL), obsidian, fusion git.html, rag.html.
