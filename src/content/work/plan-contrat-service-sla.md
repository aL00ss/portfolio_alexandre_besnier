---
title: "Plan de contrat de service (SLA) — définitions et avoirs"
description: "plan de SLA"
publishDate: 2025-10-06

img: "/assets/SLA.png"
img_alt: "Tableau de bord illustrant des indicateurs de service"
tags: 
- Compétence 1
---

## Plan proposé (SLA)

1. Périmètre et parties prenantes: services couverts, exclusions, contacts, périodes de service.
2. Priorisation: définition d’impact/urgence, matrice priorité, cas d’usage.
3. Engagements de service: disponibilités cibles, GTI/GTR par priorité, fenêtres de maintenance.
4. Mesure: méthodes de calcul, sources de données, fréquence de collecte, zones d’exclusion.
5. Reporting et comité de suivi: indicateurs, seuils d’alerte, plans d’action.
6. Support et escalade: canaux, horaires, niveaux d’escalade, astreinte.
7. Sécurité et conformité: exigences (MFA, sauvegardes, journalisation), confidentialité des données.
8. Révision: modalités d’évolution du SLA et gestion du changement.

## Définitions

- Incident: interruption non planifiée ou dégradation de la qualité d’un service.
- Problème: cause racine d’un ou plusieurs incidents; conduit à des actions correctives (RCA, contournement).
- SLA (Service Level Agreement): accord formalisant les objectifs de service (disponibilité, GTI/GTR, qualité) et le pilotage associé.
- Centre de service (Service Desk): point de contact unique pour les utilisateurs; enregistre, classe, informe et coordonne la résolution.
- GTI (Garantie de Temps d’Intervention): délai cible entre l’ouverture d’un ticket priorisé et la prise en charge effective.
- GTR (Garantie de Temps de Rétablissement): délai cible pour restaurer le service (résolution ou contournement accepté).
- Temps d’indisponibilité (calcul):
  - Disponibilité (%) = (Temps total d’observation − Indisponibilité non planifiée) / Temps total d’observation × 100
  - Indisponibilité (%) = 100 − Disponibilité (%)
  - Exemple mensuel (30 jours): 30 × 24 = 720 h. Une indisponibilité de 3 h ⇒ Disponibilité = (720 − 3)/720 = 99,58 %, Indisponibilité = 0,42 %.

## Avoirs service

Définition: un « avoir » est un crédit commercial (remise ou compensation) appliqué à la facture de service lorsque les engagements du SLA ne sont pas tenus, selon des règles prévues au contrat.

Proposition de barème (exemple pédagogique):

| Indisponibilité mensuelle (%) | Avoir appliqué sur la mensualité |
| --- | --- |
| ≤ 0,10 % | 0 % |
| > 0,10 % et ≤ 0,50 % | 2 % |
| > 0,50 % et ≤ 1,00 % | 5 % |
| > 1,00 % et ≤ 2,00 % | 10 % |
| > 2,00 % | 20 % |


---