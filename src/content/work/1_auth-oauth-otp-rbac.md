---
title: "Sécurité : Authentification (Google OAuth, identifiant/mot de passe, OTP) et gestion des rôles RBAC"
publishDate: 2026-02-05
img: /assets/google-auth-logo.jpg
img_alt: Image de couverture par defaut
description: "J’ai développé un système d’authentification et d’autorisations pour l’application (OAuth, OTP, RBAC)."

tags:
  - "Compétence - Gérer le patrimoine informatique"
  - "Compétence - Répondre aux incidents et aux demandes d’assistance et d’évolution"
  - "Compétence - Travailler en mode projet"
  - "Compétence - Mettre à disposition des utilisateurs un service informatique"
---
Authentification et gestion des accès (OAuth / OTP / RBAC)

1. **Objectif**

Lors de mon stage de 2e année, j’ai sécurisé l’accès à une application web (Python/Streamlit) en mettant en place plusieurs méthodes d’authentification (Google OAuth et email/mot de passe), un système d’activation/invitation, une réinitialisation sécurisée par OTP, et une gestion de droits par rôles (RBAC). L’objectif était d’obtenir une authentification exploitable en production, adaptée à des profils différents (administrateur, employés, bénévoles, etc.).

2. **Fonctionnalités**

- **Connexion via Google OAuth (Semaine 3)**
  - Intégration du flux OAuth/OpenID Connect dans Streamlit.
  - Chargement des identifiants (Client ID, Client Secret, Redirect URI) via `st.secrets` pour ne pas exposer de données sensibles.
  - Gestion des sessions utilisateur et persistance via cookies (important pour Streamlit à cause des rechargements).
  - Mise en place d’un mécanisme `state` signé (HMAC) avec durée de vie pour se protéger contre les attaques CSRF.
  - Création / mise à jour automatique des comptes via “upsert” en base (utilisateur reconnu à chaque connexion).

- **Gestion des rôles et permissions (RBAC)**
  - Préparation d’une couche dédiée aux rôles/permissions (différenciation des vues et limites selon le profil).
  - Attribution de rôles selon la fonction (administrateur, gestionnaire, employé, bénévole, etc.) afin de contrôler l’accès aux modules.

- **Activation et invitations (Semaine 4)**
  - Mise en place d’un système d’invitation permettant à un administrateur de rattacher un utilisateur à une fiche “Personne” existante.
  - Stockage des invitations dans une table dédiée (ex: `user_invites`) avec token, référence “Personne”, date de création et date d’expiration.
  - Ajout d’une page “Activer mon accès” pour finaliser l’accès via un code d’invitation.

- **Connexion par email / mot de passe (Semaine 4)**
  - Ajout d’une authentification interne email + mot de passe à la demande du client (alternative à Google).
  - Possibilité de choisir la méthode d’authentification (Google, email/mdp, activation par invitation).

- **Réinitialisation sécurisée du mot de passe par OTP (Semaine 4)**
  - Intégration de MailerSend pour l’envoi d’emails transactionnels (token stocké dans les secrets Streamlit).
  - Processus: saisie email -> envoi d’un lien/code OTP -> saisie OTP + nouveau mot de passe -> mise à jour après vérifications.
  - Sécurisation par durée de validité limitée + validation OTP obligatoire.

- **Correctifs et cohérence (Semaine 6)**
  - Revue/corrections ponctuelles liées à la cohérence RBAC et à la création de comptes (module “Personnes”, invitations, profils).

3. **Tests et validation**

- Tests fonctionnels en conditions proches du réel (multi-utilisateurs) : connexion, création/activation de compte, rôles, parcours de navigation (à détailler).
- Vérifications sur la persistance de session et la robustesse du flux OAuth (à détailler).

4. **Productions / preuves**

- <a href="/assets/BESNIER%20Alexandre%20CR%20S3.pdf" download>Télécharger le compte-rendu (PDF) - Semaine 3</a>
- <a href="/assets/BESNIER%20Alexandre%20CR%20S4.pdf" download>Télécharger le compte-rendu (PDF) - Semaine 4</a>

---
