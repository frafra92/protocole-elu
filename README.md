# Protocole Élu — prototype 1

Une page web unique (`index.html`), sans compte, sans cookie, sans collecte de données.

## Parcours
1. Appel entrant « Numéro masqué » → bouton vert pour répondre
2. Message mystérieux (texte tapé + voix grave) avec compte à rebours de localisation (10 s)
3. Autodestruction : écran qui tremble, caractères corrompus, 3-2-1, flash
4. « ACCEPTES-TU LA MISSION ? » → Accepter / Refuser
5. Mission révélée (avec note de consentement) ou écran de refus (avec bouton « j'ai changé d'avis »)

## Mise en ligne (gratuite, 2 minutes)
**Netlify Drop** : va sur app.netlify.com/drop, glisse le dossier `protocole-elu`. Tu obtiens une adresse en `https://…netlify.app`.
Alternative : GitHub Pages, ou un sous-dossier de ton site existant (ex. `/elu/`).

> Important : la page doit être en **https** (la synthèse vocale et les navigateurs mobiles l'exigent).
> Choisis une adresse **courte et définitive** : elle sera imprimée sur le T-shirt.

## Générer le QR code
```
pip install segno
python3 generer_qr.py https://ton-adresse.netlify.app
```
Produit `qr-protocole-elu.svg` (impression, vectoriel) et `.png` (écran).

## Checklist avant impression
- [ ] Tester sur un iPhone ET un Android (voix, vibration, animation)
- [ ] Scanner le QR code imprimé sur du tissu, à plat puis porté (plis)
- [ ] QR d'au moins 6-7 cm de côté, noir sur fond blanc, marge blanche autour conservée
- [ ] Vérifier que le son n'est pas coupé (mode silencieux) : le texte reste lisible sans voix
- [ ] Prévoir la suite : un 2ᵉ QR code = une URL différente (`/mission2/`) pour tester d'autres missions

## Limites connues
- iPhone : pas de vibration (Safari), voix selon les réglages du téléphone.
- La voix est celle du téléphone (synthèse). Une vraie voix enregistrée (fichier .mp3) sera plus convaincante en v2.
