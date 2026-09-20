# Demandes d'autorisation d'usage de logos — à préparer

But : si l'on souhaite un jour afficher les **logos officiels** de ces marques sur le portfolio
(au lieu des icônes originales de remplacement), il faut d'abord obtenir l'autorisation écrite
et/ou respecter la charte. Ce fichier tient la liste et l'état. Interne au dépôt — **non publié**.

Contexte : au 2026-09-20, les logos officiels de ces marques ont été **remplacés par des icônes
originales** (style trait bleu, évoquant la fonction sans copier le logo) dans `assets/`. Les noms
de fichiers sont inchangés. Anciennes versions redessinées : historique git.

Déjà conformes (logo officiel + mention sur about.html#credits) — PAS de demande nécessaire :
Git (CC BY 3.0), Tux (Larry Ewing), Docker, Python (PSF).

## À demander / vérifier (par ordre de restriction)

| Marque | Contact pour la demande | Politique / réf. | Exigence |
|---|---|---|---|
| GitLab | **intellectualproperty@gitlab.com** (demandes de permission) ; #brand (Slack) | handbook.gitlab.com/handbook/legal/trademarks-at-gitlab/ | Autorisation écrite (Master Authorization) pour usage nom/logo sur site tiers |
| AMD | **amd.trademarks@amd.com** (AMD Law Department) | amd.com/en/legal/trademarks.html · media-library | Licence limitée aux produits contenant un CPU/GPU AMD ; sinon permission écrite |
| GitHub | **trademarks@github.com** | docs.github.com/.../github-logo-policy · github.com/logos | Lien/référence OK, pas pour un produit à soi, ne pas modifier ; au-delà → permission écrite |
| Proxmox | **office@proxmox.com** (Proxmox Server Solutions GmbH, Vienne) | proxmox.com/en/about/company-details/media-kit | Logo pour promouvoir Proxmox uniquement, non modifié ; sinon permission écrite |
| Ollama | **hello@ollama.com** (agent copyright/marque, ToS) | ollama.com/terms | ToS ne concèdent aucun droit sur la marque sans permission |
| Obsidian | Pas d'e-mail public dédié → « Contact us » sur obsidian.md/brand + help.obsidian.md (éditeur : Dynalist Inc.) | obsidian.md/brand | Éditorial/identification OK sans modifier ; commercial → contacter |
| n8n | Voir e-mail de l'imprint **n8n.io/imprint** (n8n GmbH) — ne pas deviner l'adresse | n8n.io/brandguidelines/ | Éditorial/éducatif OK en suivant la charte ; commercial → permission |
| NVIDIA | Pas d'e-mail public dédié fiable → page « Logo & Brand » (section demande d'approbation) ; si partenaire : représentant marketing régional | nvidia.com/en-us/about-nvidia/legal-info/logo-brand-usage/ | Approbation écrite préalable obligatoire pour tout usage du logo |
| NGINX / F5 | Pas d'e-mail public dédié → service juridique F5 via canaux corporate/legal officiels | f5.com/company/policies/trademarks | Permission écrite requise ; aucun droit sans accord explicite |

## Éléments à préparer pour chaque demande
- Identité : Stéphane Muraro — portfolio.stephanemuraro.fr (site personnel, non commercial).
- Usage visé : afficher le logo officiel non modifié pour **identifier** la techno employée
  (usage nominatif/éditorial), sans implication d'affiliation ni d'approbation.
- Engagement : respecter la charte (couleurs, proportions, clear-space, pas de modification),
  afficher la mention légale exigée, lien vers le site officiel si demandé.
- Joindre : URL de la/les page(s) où le logo apparaîtrait.

## Rappel méthode (cloisonnement)
Claude ne télécharge/n'intègre pas lui-même les logos de marque. Une fois l'autorisation obtenue,
Stéphane (ou son agent local) dépose le fichier officiel dans `assets/` sous le nom existant ;
Claude vérifie le rendu et ajoute/contrôle la mention.
