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

| Marque | Exigence | Canal / politique | Statut |
|---|---|---|---|
| NVIDIA | Approbation écrite préalable obligatoire pour tout usage du logo | https://www.nvidia.com/en-us/about-nvidia/legal-info/logo-brand-usage/ | À demander |
| NGINX / F5 | Permission écrite requise ; aucun droit sans accord explicite | https://www.f5.com/company/policies/trademarks | À demander |
| GitLab | Autorisation signée (Master Authorization) pour usage nom/logo sur site tiers | https://handbook.gitlab.com/handbook/legal/trademarks-at-gitlab/ · brand : about.gitlab.com/press/press-kit/ | À demander |
| AMD | Licence limitée (produits contenant un processeur AMD) ; sinon permission écrite | https://www.amd.com/en/legal/terms-and-conditions/media-library.html | À demander (le CPU AMD est réellement utilisé → argument nominatif) |
| Ollama | ToS ne concèdent aucun droit sur la marque sans permission | https://ollama.com/terms · support@ollama.com | À demander |
| Obsidian | Usage éditorial/identification OK **sans modifier** ; commercial → contacter | https://obsidian.md/brand | Charte à respecter (logo officiel non modifié) — sinon demande |
| GitHub | Lien/référence OK, **pas pour un produit à soi**, **ne pas modifier** | https://docs.github.com/en/site-policy/other-site-policies/github-logo-policy · trademarks@github.com | Charte à respecter — sinon demande |
| Proxmox | Logo utilisable pour promouvoir Proxmox, **non modifié**, lien vers proxmox.com | https://www.proxmox.com/en/about/company-details/media-kit | Charte à respecter — sinon demande |
| n8n | Éditorial/éducatif OK en suivant la charte (couleurs, clear-space, non modifié) | https://n8n.io/brandguidelines/ | Charte à respecter — sinon demande |

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
