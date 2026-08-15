# TODO — Portfolio (suivi Claude)

Suivi propre au dépôt portfolio (`C:\dev\portfolio`).

Périmètre Claude (cloisonnement documentaire — note corrective 2026-08-14) :
- **Écriture** : uniquement `C:\dev\portfolio\` (y compris `.claude\`).
- **Sources factuelles autorisées (lecture seule)** : `…\Portfolio-Technique\sources-publiques`
  (unique source de faits) · `…\Portfolio-Technique\validation` · `…\Portfolio-Technique\PUBLICATION-POLICY.md`.
- **Aucun accès** : le reste de `C:\Projets-Techniques` (privé) ni le dossier Obsidian Knowledge.
- Publier uniquement des fiches `approved`/`published`. Info manquante ou contradiction → **signaler à Stéphane**
  et attendre une source publique corrigée par Codex (ne pas aller chercher dans une zone interdite).

Dernière mise à jour : 2026-08-14.

## En attente

- [x] **VM130 (`TEMPLATE.md`) — enrichissement intégré** (fiche finalisée). `proxmox.html` : panneau « Retour d'expérience — reconstruction du template » (reconstruction faite) + nouveau panneau « ♻️ Cycle de vie & types de templates » (schéma de cycle de vie + table des types de socles + principe « construction / validation / remplacement = 3 opérations distinctes »). Procédure d'exploitation (ISO vs image cloud, création pas-à-pas) volontairement non publiée.

- [ ] **Reframe éditorial : encart « État et ordre de démarrage des VM »** (titre allégé — sans « Preuve reproductible — » ; convention pour tous les reframes). À alimenter **uniquement** par une fiche `sources-publiques` approuvée (jamais par des données collées).
  - [x] **proxmox.html** — conforme à `proxmox.md` (approved) : commande avec `status`, **extrait assaini** 215 → 210 → 205 + ligne générique ; inventaire exhaustif exclu ; titre « État et ordre de démarrage des VM ».
  - [x] **GPU / VFIO** — conforme à `gpu-vfio.md` § « Exclusivité GPU et politique de démarrage » (approved) : contrôle d'exclusivité + extrait assaini (IA-Core / GPU-alternative). L'encart « 🔍 Vérifications » (commandes) a été remplacé.
  - [ ] **Docker**, **Réseau** — selon pertinence, si fiche approuvée existe.

## Fait

- [x] proxmox.html — intro « Pourquoi Proxmox ? » (scalabilité, agilité, gain de temps, clients Windows). — 2026-08-14
- [x] python.html — supplément ML/DL avec aperçu Wikipédia au survol (corrigé : sorti du panneau qui le rognait). — 2026-08-14
- [x] obsidian.html — « Vue graphe du vault » remontée avant « Structure du vault ». — 2026-08-14
- [x] Fusion Git → `git.html` ; suppression de `git-audit.html` et `git-strategie.html`. — 2026-08-14
- [x] proxmox.html / gpu_passthrough.html — encart « état et ordre de démarrage des VM » conforme aux fiches approuvées. — 2026-08-14
- [x] rag.html — ajout « Comprendre le RAG » + « Pourquoi pgvector plutôt que Qdrant » (conforme à `rag-pgvector.md`, maj 14/08). — 2026-08-14
