---
title: "Chrome sur Android crée des passkeys automatiquement après un login mot de passe"
publishDate: 2025-12-20
img: "/assets/passkeys_auto_chrome_android.jpg"
img_alt: "Écran WebAuthn/Passkeys illustrant une authentification sans mot de passe"
description: |
  Chrome pour Android (à partir de Chrome 142) permet de déclencher la création automatique d’une passkey via WebAuthn (Conditional Create) après une connexion par mot de passe : un levier concret pour accélérer la transition vers le passwordless.
tags:
  - Veille
  - Cybersécurité
  - Développement Web
  - Passkeys
  - WebAuthn
---

Depuis Chrome 142 sur Android, un site peut demander à Google Password Manager de créer une passkey automatiquement après qu’un utilisateur se soit connecté avec un mot de passe enregistré, grâce à une fonctionnalité WebAuthn appelée Conditional Create (mediation: "conditional").


L’utilisateur n’est pas interrompu : Chrome affiche ensuite une confirmation et un bouton pour gérer la passkey dans le gestionnaire.
Chrome for Developers
Pourquoi c’est important côté dev (sécurité + produit)

Les passkeys réduisent fortement le risque de phishing (plus de mot de passe à voler), et cette nouveauté résout un frein majeur : l’adoption (les utilisateurs ne “prennent pas le temps” de créer une passkey).


Pour une équipe produit, ça se traduit souvent par : moins de resets de mot de passe, moins de comptes compromis, et une conversion vers le passwordless sans friction.
Ce qu’il faut faire :

Côté web, déclencher la création via navigator.credentials.create(...) avec mediation: "conditional" après un login mot de passe réussi (si le navigateur le supporte).

Côté Android natif, l’équivalent existe via Credential Manager avec une requête de création “conditionnelle” (isConditionalCreateRequest).

Prévoir une détection de capacité (Conditional Create) pour garder un fallback propre (création manuelle) selon le navigateur/appareil.