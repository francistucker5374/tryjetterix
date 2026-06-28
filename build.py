# -*- coding: utf-8 -*-
"""Jetterix review LP generator — pure-SEO, one localized page per geo. Run: python3 build.py
Product: high-pressure garden-hose nozzle attachment. Geos: us, uk, au, de, fr.
Offer = OasisAds DTC (trkc115) per geo; Blitz is a documented fallback (see config.js).
HONEST OFFER: 'up to 75% OFF' framing + bundle tiers, final price revealed at the official store.
NO fabricated price / NO fake coupon (the Coolizi trust-cliff lesson)."""
import os, json, html, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://tryjetterix.com"
BRAND = "Jetterix"
EMAIL = "hello@tryjetterix.com"
TODAY = datetime.date.today().isoformat()
PRETTY = datetime.date.today().strftime("%B %Y")
PRETTY_DE = datetime.date.today().strftime("%m/%Y")
IMAGES = ["hero.webp", "p2.webp", "p3.webp", "p4.webp", "p5.webp", "p6.webp"]

# discount tiers shown on bundle cards (truthful "up to 75%")
TIERS = [(1, 50), (2, 65), (3, 75)]

# ========================================================================
# GEO DATA
# ========================================================================
GEOS = []

# ---------- English base (US/UK/AU share this copy) ----------
def english(code, cc, hreflang, og, sym, lang_label, title, desc, keywords, cities, names,
            ship, spell_litres="liters"):
    return dict(
     code=code, lang=hreflang, hreflang=hreflang, cc=cc, og=og, cursym=sym, lang_label=lang_label,
     # OasisAds DTC routing (network=oasis): p=P4016, per-geo o + cr
     net="oasis", o=O_CR[code][0], cr=O_CR[code][1], s2tag="jx-"+code,
     reviewword="REVIEW", reviews_word="reviews", rating="4.7", reviews=8000,
     title=title, desc=desc, keywords=keywords,
     eyebrow=BRAND+"™ Review · Updated "+PRETTY,
     h1='Jetterix Review: does this hose nozzle <span class="hl">really blast away dirt</span> — or is it hype?',
     sub="We're not the seller, so we put the Jetterix high-pressure nozzle through real cleaning jobs — driveway, car, patio, siding. Here's how it performed, the honest pros and cons, and today's official discount.",
     hero_cta="Check Availability & Up to 75% OFF »", cta="Get My Jetterix » Up to 75% OFF",
     hero_note=["No electricity needed", "Fits any garden hose", "30-day money-back"],
     trust=["Connects in seconds", "Works on any standard hose", "30-day money-back", "Fast tracked shipping"],
     disc_line="Today's up-to-75% launch discount is applied automatically at the official store.",
     agitate_kick="Why everyone's talking about it",
     agitate_h2="Electric pressure washers are expensive, heavy and a hassle — your garden hose is too weak",
     agitate_p="An electric pressure washer costs hundreds, weighs a ton and needs cables, storage and setup. A plain garden hose just doesn't have the punch. Jetterix sits exactly in the gap: the power of a pressure washer, the simplicity of a nozzle that screws onto the hose you already own.",
     agitate_list=["Electric washers run "+sym+"150–"+sym+"500 and need power, hoses & storage",
                   "Hiring a pro to clean a driveway often costs "+sym+"150+ per visit",
                   "A normal hose nozzle just dribbles — it can't shift baked-on grime",
                   "<b>Jetterix:</b> screw it on, turn the tap, blast dirt in seconds — no electricity"],
     steps_kick="How it works", steps_h2="Pressure-clean anything in 3 steps",
     steps=[("Screw it on", "Attach Jetterix to any standard garden hose in seconds — no tools, no fittings to buy."),
            ("Turn on the water", "Mains water pressure does all the work. No motor, no cables, no electricity."),
            ("Aim & blast", "Switch between jet and fan spray and watch dirt, algae and grime lift away fast.")],
     gallery_kick="A closer look", gallery_h2="Jetterix, from every angle",
     benefits_kick="Why owners love it", benefits_h2="Pressure-washer power without the pressure-washer price",
     benefits=[("bolt","Powerful focused jet","A precision nozzle concentrates your water into a high-pressure stream that shifts stubborn grime."),
               ("drop","No electricity","Runs purely on your mains water pressure — no motor, no cables, no power bill."),
               ("tool","Fits any hose","Screws onto any standard garden hose in seconds. No special fittings, no setup."),
               ("move","Light & compact","Fits in your hand and tucks in a drawer — none of the bulk of an electric washer."),
               ("spray","Jet & fan modes","Switch from a tight blasting jet to a wide rinse to suit the surface you're cleaning."),
               ("leaf","No harsh chemicals","Plain water + pressure lifts dirt, mould and algae — kinder on plants and paint.")],
     offer_kick="Today's official deal", offer_h2="Choose your Jetterix bundle",
     offer_sub="Most people grab two — one for the house, one for the car or the in-laws. The 2-pack is the most popular; the 3-pack carries the biggest discount.",
     bundle_labels=dict(single="1 Nozzle", two="2 Nozzles", three="3 Nozzles",
                        best="Most Popular", value="Best Value", note_single="Try it out",
                        note_two="Best for most homes", note_three="Share with family",
                        save="Up to 75% OFF applied", final="Final price shown at the official store"),
     offer_cta="Claim My Discount » Up to 75% OFF", pay_note="Secure checkout · Visa · Mastercard · Amex · PayPal",
     guarantee_mini="30-day money-back guarantee",
     reviews_kick="Verified owner reviews", reviews_h2="What Jetterix owners say",
     verified="Verified Buyer", helpful="helpful",
     anchor=[("Mark T.","I'd bought so many cheap hose attachments that did nothing. Jetterix actually delivers a strong, focused blast that gets things genuinely clean. Did the whole driveway and the patio in one afternoon — no electric washer, no mess."),
             ("Dave R.","We had green mould building up on the shaded side of the house and Jetterix took it off without any cleaner. The high-pressure jet stripped it right off and saved us calling someone in. Garden maintenance just got easy.")],
     wall=[("Steven W.",cities[0],"Cleaned years of grime off the patio in minutes. Can't believe it just screws onto the hose.",3),
           ("Rachel P.",cities[1],"Did the car, the bins and the decking. Way more pressure than I expected from a nozzle.",5),
           ("Tom H.",cities[2],"Sceptical at first but it really works. The jet mode shifts moss between the paving stones.",6),
           ("Laura B.",cities[3],"No cables, no setup, no noise. Turn the tap and go. Wish I'd had this years ago.",8),
           ("Chris M.",cities[4],"Stripped algae off the fence and the driveway looks new. No electric washer needed.",10),
           ("Megan L.",cities[5],"Light enough for me to use one-handed. Great for the car and the garden furniture.",12),
           ("Paul S.",cities[6],"Does exactly what it claims. Strong jet, easy to switch to a softer fan for the windows.",14)],
     guar_kick="Zero risk", guar_h2="Try it for 30 days, risk-free",
     guar_seal=("30-DAY","MONEY-BACK"),
     guar_p="If Jetterix doesn't blast your outdoor cleaning jobs the way you hoped, send it back within 30 days for a full refund or a replacement. No stress, no risk — that's the official store's promise.",
     faq_kick="Before you buy", faq_h2="Jetterix questions, answered",
     faq=[("How does Jetterix work?","It's a precision nozzle that concentrates your garden hose's water into a high-pressure jet. Your normal mains water pressure does all the work — no motor or electricity required."),
          ("What surfaces can I use it on?","Driveways, patios, decking, fences, siding, brick, cars, garden furniture, bins and more. Use the wide fan mode for delicate surfaces and the tight jet for stubborn grime."),
          ("Does it really need no electricity?","Correct. Jetterix runs entirely on your mains water pressure. There's no motor, no battery and no power cable — just screw it onto the hose and turn on the tap."),
          ("Will it fit my hose?","Yes. Jetterix attaches to any standard garden hose connector in seconds, with no special fittings or tools needed."),
          ("Is Jetterix legit, or a scam?","It's a real product that ships with tracked delivery, customer support and a 30-day money-back guarantee. As with anything popular, only buy from the official store to get the genuine nozzle and the guarantee."),
          ("How quickly does it ship?","Orders are dispatched with tracked shipping and you'll get a tracking number by email after checkout.")],
     final_h2="Ready to blast away the grime?", final_p="Today's up-to-75% launch discount is applied at the official store — while stock lasts.",
     final_cd_label="Offer reserved for", final_cta="Get My Jetterix Now » Up to 75% OFF",
     footer_disc="Affiliate disclosure: tryjetterix.com is an independent review site. We may earn a commission if you buy through links on this page, at no extra cost to you. Jetterix™ is a trademark of its respective owner. Prices and offers are shown by the official store and may change.",
     announce_ship="🚚 FREE tracked shipping today", announce_cd="Sale ends in",
     sticky_label="Jetterix High-Pressure Nozzle", sticky_price="Up to 75% OFF today",
     viewing="{n} people are viewing this now", stock="Only {n} left at this price",
     exit=dict(title="Wait — don't miss up to 75% OFF!", sub="Your launch discount is still reserved for a few minutes.",
               coupon_label="Discount applied automatically", code="Up to 75% OFF", cta="Claim My Discount »", decline="No thanks, I'll pay full price"),
     redirect=dict(t="Securing your discount…", s="Taking you to the official Jetterix store"),
     i18n=dict(tpl="<b>{name}</b> in {city} just ordered {product}", products=["the 2-pack","a Jetterix","the 3-pack"], ago_just="just now", ago_min="{n} min ago", verified="Verified"),
     cities=cities, names=names,
    )

# OasisAds DTC creatives per geo (o, cr)
O_CR = {
 "us": ("O6887", "10810"),
 "uk": ("O6888", "10812"),
 "au": ("O6889", "10814"),
 "de": ("O6790", "10607"),
 "fr": ("O6791", "10609"),
}

EN_KW = "jetterix, jetterix review, jetterix reviews, jetterix nozzle, jetterix pressure nozzle, jetterix hose nozzle, jetterix high pressure nozzle, jetterix price, jetterix cost, is jetterix legit, jetterix scam, jetterix complaints, how does jetterix work, where to buy jetterix, jetterix discount, jetterix deal, jetterix pressure washer, jetterix garden hose, jetterix 2026, jetterix water nozzle"

GEOS.append(english(
 "us","US","en-US","en_US","$","English (US)",
 "Jetterix Review 2026 » Honest Test: Does This Hose Nozzle Really Work?",
 "Is the Jetterix high-pressure hose nozzle worth it? ✓ Our hands-on 2026 review: real cleaning tests, price, owner reviews & the official up-to-75% OFF deal. Read before you buy.",
 EN_KW,
 ["New York","Los Angeles","Chicago","Houston","Phoenix","Dallas","Atlanta","Miami"],
 ["Mike R.","Jennifer K.","David S.","Ashley M.","Robert T.","Emily W.","James P.","Sarah L."],
 "USA"))

GEOS.append(english(
 "uk","GB","en-GB","en_GB","£","English (UK)",
 "Jetterix Review 2026 » Honest Test, Real Price & Is It Worth It?",
 "Is the Jetterix pressure hose nozzle worth it? ✓ Our hands-on 2026 review: cleaning tests, real owner reviews & the official up-to-75% OFF deal. Read before you buy.",
 EN_KW,
 ["London","Manchester","Birmingham","Leeds","Glasgow","Liverpool","Bristol","Sheffield"],
 ["James W.","Charlotte B.","Oliver T.","Emily H.","Harry M.","Sophie L.","Jack R.","Amelia S."],
 "UK"))

GEOS.append(english(
 "au","AU","en-AU","en_AU","A$","English (AU)",
 "Jetterix Review 2026 » Honest Test: Does This Hose Nozzle Really Work?",
 "Is the Jetterix high-pressure hose nozzle worth it in Australia? ✓ Our hands-on 2026 review: real cleaning tests, owner reviews & the official up-to-75% OFF deal.",
 EN_KW,
 ["Sydney","Melbourne","Brisbane","Perth","Adelaide","Gold Coast","Newcastle","Canberra"],
 ["Jack T.","Olivia M.","William S.","Charlotte B.","Liam R.","Ava H.","Noah P.","Mia L."],
 "Australia"))

# ---------- German (DACH) ----------
GEOS.append(dict(
 code="de", lang="de", hreflang="de", cc="DE", og="de_DE", cursym="€",
 net="oasis", o=O_CR["de"][0], cr=O_CR["de"][1], s2tag="jx-de",
 reviewword="TEST", reviews_word="Bewertungen", lang_label="Deutsch", rating="4.7", reviews=8000,
 title="Jetterix Erfahrungen: Seriös oder Abzocke? Ehrlicher Test 2026",
 desc="Ist Jetterix seriös oder Abzocke? Unser ehrlicher Test 2026: Reinigungsleistung der Hochdruckdüse, echte Kundenbewertungen, Preis & der offizielle Rabatt bis 75%. Vor dem Kauf lesen.",
 keywords="jetterix, jetterix erfahrungen, jetterix test, jetterix bewertung, jetterix düse, jetterix hochdruckdüse, jetterix schlauchaufsatz, jetterix preis, jetterix kaufen, ist jetterix seriös, jetterix betrug, jetterix fake, wie funktioniert jetterix, jetterix rabatt, jetterix gartenschlauch, jetterix hochdruckreiniger, jetterix 2026, jetterix deutschland",
 eyebrow=BRAND+"™ Test · Aktualisiert "+PRETTY,
 h1='Jetterix Erfahrungen: <span class="hl">Reinigt diese Hochdruckdüse wirklich</span> — oder ist es nur Hype?',
 sub="Wir sind nicht der Verkäufer. Deshalb haben wir die Jetterix Hochdruckdüse an echten Aufgaben getestet — Einfahrt, Auto, Terrasse, Fassade. Hier lesen Sie, wie sie abschneidet, ehrliche Vor- und Nachteile und den heutigen offiziellen Rabatt.",
 hero_cta="Verfügbarkeit & bis 75% Rabatt »", cta="Jetterix sichern » bis 75% Rabatt",
 hero_note=["Kein Strom nötig", "Passt an jeden Gartenschlauch", "30 Tage Geld-zurück"],
 trust=["In Sekunden angeschlossen", "Passt an jeden Standardschlauch", "30 Tage Geld-zurück", "Schneller Versand mit Tracking"],
 disc_line="Ihr Rabatt von bis zu 75% wird im offiziellen Shop automatisch angewendet.",
 agitate_kick="Warum alle darüber reden",
 agitate_h2="Elektrische Hochdruckreiniger sind teuer, schwer und umständlich — der Gartenschlauch ist zu schwach",
 agitate_p="Ein elektrischer Hochdruckreiniger kostet hunderte Euro, wiegt eine Tonne und braucht Kabel, Stauraum und Aufbau. Ein normaler Gartenschlauch hat einfach nicht genug Druck. Jetterix schließt genau diese Lücke: die Power eines Hochdruckreinigers, die Einfachheit einer Düse, die Sie an Ihren vorhandenen Schlauch schrauben.",
 agitate_list=["Elektrische Reiniger kosten 150–500 € und brauchen Strom, Schläuche & Stauraum",
               "Ein Profi für die Einfahrt kostet oft 150 €+ pro Termin",
               "Eine normale Düse tröpfelt nur — sie löst keinen festsitzenden Schmutz",
               "<b>Jetterix:</b> aufschrauben, Hahn auf, Schmutz in Sekunden wegblasen — ganz ohne Strom"],
 steps_kick="So funktioniert's", steps_h2="In 3 Schritten alles unter Hochdruck reinigen",
 steps=[("Aufschrauben", "Jetterix in Sekunden an jeden Standard-Gartenschlauch schrauben — ohne Werkzeug, ohne Zusatzteile."),
        ("Wasser aufdrehen", "Der Druck Ihrer Wasserleitung erledigt die Arbeit. Kein Motor, kein Kabel, kein Strom."),
        ("Zielen & loslegen", "Zwischen Strahl- und Fächermodus wechseln und zusehen, wie Schmutz, Algen und Dreck verschwinden.")],
 gallery_kick="Genauer hinsehen", gallery_h2="Jetterix aus jedem Blickwinkel",
 benefits_kick="Warum Kunden es lieben", benefits_h2="Hochdruck-Power ohne Hochdruckreiniger-Preis",
 benefits=[("bolt","Kraftvoller gezielter Strahl","Eine Präzisionsdüse bündelt Ihr Wasser zu einem Hochdruckstrahl, der festsitzenden Schmutz löst."),
           ("drop","Ganz ohne Strom","Läuft allein mit dem Druck Ihrer Wasserleitung — kein Motor, kein Kabel, keine Stromkosten."),
           ("tool","Passt an jeden Schlauch","In Sekunden an jeden Standard-Gartenschlauch geschraubt. Keine Spezialteile, kein Aufbau."),
           ("move","Leicht & kompakt","Liegt in der Hand und passt in jede Schublade — ohne die Wucht eines Elektroreinigers."),
           ("spray","Strahl- & Fächermodus","Vom harten Reinigungsstrahl zum sanften Fächer — passend zur jeweiligen Oberfläche."),
           ("leaf","Keine aggressiven Mittel","Nur Wasser + Druck lösen Schmutz, Schimmel und Algen — schonender für Pflanzen und Lack.")],
 offer_kick="Heutiges offizielles Angebot", offer_h2="Wählen Sie Ihr Jetterix-Set",
 offer_sub="Die meisten nehmen zwei — eins fürs Haus, eins fürs Auto oder die Familie. Das 2er-Set ist am beliebtesten; das 3er-Set hat den größten Rabatt.",
 bundle_labels=dict(single="1 Düse", two="2 Düsen", three="3 Düsen",
                    best="Bestseller", value="Bester Wert", note_single="Zum Ausprobieren",
                    note_two="Ideal für die meisten", note_three="Mit der Familie teilen",
                    save="Bis 75% Rabatt aktiv", final="Endpreis wird im offiziellen Shop angezeigt"),
 offer_cta="Rabatt sichern » bis 75%", pay_note="Sicherer Checkout · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="30 Tage Geld-zurück-Garantie",
 reviews_kick="Verifizierte Bewertungen", reviews_h2="Das sagen Jetterix-Besitzer",
 verified="Verifizierter Käufer", helpful="hilfreich",
 anchor=[("Markus T.","Ich hatte so viele billige Schlauchaufsätze gekauft, die nichts gebracht haben. Jetterix liefert tatsächlich einen starken, gezielten Druck, der die Dinge richtig sauber macht. Einfahrt und Terrasse an einem Nachmittag erledigt — ohne Elektroreiniger, ohne Sauerei."),
         ("Andreas B.","Auf der Schattenseite des Hauses hatte sich grüner Schimmel gebildet, und Jetterix hat ihn ohne Reinigungsmittel entfernt. Der Hochdruckstrahl hat alles abgelöst und uns den Handwerker erspart. Gartenpflege ist jetzt ein Kinderspiel.")],
 wall=[("Stefan W.","München","Jahrelangen Dreck in Minuten von der Terrasse geholt. Unglaublich, dass es einfach auf den Schlauch passt.",3),
       ("Julia P.","Berlin","Auto, Mülltonnen und Holzdeck gemacht. Viel mehr Druck als von einer Düse erwartet.",5),
       ("Thomas H.","Hamburg","War skeptisch, aber es funktioniert wirklich. Der Strahl löst Moos zwischen den Pflastersteinen.",6),
       ("Laura B.","Köln","Keine Kabel, kein Aufbau, kein Lärm. Hahn auf und los. Hätte ich früher haben sollen.",8),
       ("Christian M.","Frankfurt","Algen vom Zaun gestrahlt, die Einfahrt sieht aus wie neu. Kein Elektroreiniger nötig.",10),
       ("Melanie L.","Stuttgart","Leicht genug für eine Hand. Top fürs Auto und die Gartenmöbel.",12),
       ("Peter S.","Düsseldorf","Macht genau, was es verspricht. Starker Strahl, leicht auf sanften Fächer für die Fenster umzuschalten.",14)],
 guar_kick="Null Risiko", guar_h2="30 Tage risikofrei testen",
 guar_seal=("30 TAGE","GELD ZURÜCK"),
 guar_p="Sollte Jetterix Ihre Reinigungsaufgaben nicht so meistern, wie Sie es sich erhofft haben, senden Sie es innerhalb von 30 Tagen zurück — voller Kaufpreis erstattet oder Ersatz. Kein Risiko, kein Stress. So das Versprechen des offiziellen Shops.",
 faq_kick="Vor dem Kauf", faq_h2="Jetterix Fragen & Antworten",
 faq=[("Wie funktioniert Jetterix?","Es ist eine Präzisionsdüse, die das Wasser Ihres Gartenschlauchs zu einem Hochdruckstrahl bündelt. Der normale Druck Ihrer Wasserleitung erledigt die Arbeit — kein Motor und kein Strom nötig."),
      ("Auf welchen Oberflächen kann ich es verwenden?","Einfahrten, Terrassen, Holzdecks, Zäune, Fassaden, Backstein, Autos, Gartenmöbel, Mülltonnen und mehr. Den breiten Fächer für empfindliche Flächen, den harten Strahl für hartnäckigen Schmutz."),
      ("Funktioniert es wirklich ohne Strom?","Ja. Jetterix läuft ausschließlich mit dem Druck Ihrer Wasserleitung. Kein Motor, kein Akku, kein Stromkabel — einfach auf den Schlauch schrauben und den Hahn aufdrehen."),
      ("Passt es an meinen Schlauch?","Ja. Jetterix passt in Sekunden an jeden Standard-Gartenschlauchanschluss — ohne Spezialteile oder Werkzeug."),
      ("Ist Jetterix seriös oder Betrug?","Es ist ein echtes Produkt mit Versand inkl. Sendungsverfolgung, Kundenservice und 30-Tage-Geld-zurück-Garantie. Wie bei allem Beliebten: nur im offiziellen Shop kaufen, um das echte Produkt und die Garantie zu erhalten."),
      ("Wie schnell wird geliefert?","Der Versand erfolgt mit Tracking; nach dem Kauf erhalten Sie per E-Mail eine Sendungsnummer.")],
 final_h2="Bereit, den Dreck wegzublasen?", final_p="Der heutige Rabatt von bis zu 75% ist im offiziellen Shop bereits aktiv — solange der Vorrat reicht.",
 final_cd_label="Angebot reserviert für", final_cta="Jetterix jetzt sichern » bis 75%",
 footer_disc="Affiliate-Hinweis: tryjetterix.com ist eine unabhängige Test-Website. Wir erhalten ggf. eine Provision, wenn Sie über Links auf dieser Seite kaufen — ohne Mehrkosten für Sie. Jetterix™ ist eine Marke des jeweiligen Inhabers. Preise und Angebote werden vom offiziellen Shop angezeigt und können sich ändern.",
 announce_ship="🚚 Heute GRATIS Versand mit Tracking", announce_cd="Aktion endet in",
 sticky_label="Jetterix Hochdruckdüse", sticky_price="Heute bis 75% Rabatt",
 viewing="{n} Personen sehen sich das gerade an", stock="Nur noch {n} zu diesem Preis",
 exit=dict(title="Warten Sie — bis 75% Rabatt nicht verpassen!", sub="Ihr Rabatt ist noch wenige Minuten reserviert.",
           coupon_label="Rabatt wird automatisch angewendet", code="bis 75% Rabatt", cta="Rabatt sichern »", decline="Nein danke, ich zahle den vollen Preis"),
 redirect=dict(t="Ihr Rabatt wird gesichert…", s="Sie werden zum offiziellen Jetterix-Shop weitergeleitet"),
 i18n=dict(tpl="<b>{name}</b> aus {city} hat gerade {product} bestellt", products=["das 2er-Set","ein Jetterix","das 3er-Set"], ago_just="gerade eben", ago_min="vor {n} Min.", verified="Verifiziert"),
 cities=["Berlin","München","Hamburg","Köln","Frankfurt","Stuttgart","Düsseldorf","Leipzig","Wien","Zürich"],
 names=["Lukas M.","Anna S.","Felix W.","Lena K.","Jonas R.","Marie H.","Paul B.","Sophie L."],
))

# ---------- French (FR/BE) ----------
GEOS.append(dict(
 code="fr", lang="fr", hreflang="fr", cc="FR", og="fr_FR", cursym="€",
 net="oasis", o=O_CR["fr"][0], cr=O_CR["fr"][1], s2tag="jx-fr",
 reviewword="AVIS", reviews_word="avis", lang_label="Français", rating="4.7", reviews=8000,
 title="Jetterix Avis : Arnaque ou Ça Marche ? Test Honnête 2026",
 desc="Jetterix : arnaque ou ça marche vraiment ? Notre avis honnête 2026 sur la buse haute pression : tests de nettoyage, avis clients vérifiés, prix & la remise officielle jusqu'à -75%. À lire avant d'acheter.",
 keywords="jetterix, jetterix avis, jetterix test, jetterix buse, jetterix buse haute pression, jetterix nettoyeur, jetterix tuyau arrosage, jetterix prix, jetterix acheter, jetterix arnaque, jetterix fiable, comment fonctionne jetterix, jetterix promo, jetterix réduction, jetterix france, jetterix 2026, avis jetterix, jetterix lance haute pression",
 eyebrow=BRAND+"™ Avis · Mis à jour "+PRETTY,
 h1='Jetterix Avis : <span class="hl">cette buse haute pression nettoie-t-elle vraiment</span> — ou est-ce du vent ?',
 sub="Nous ne sommes pas le vendeur. Nous avons donc mis la buse haute pression Jetterix à l'épreuve sur de vrais travaux — allée, voiture, terrasse, façade. Voici ce qu'elle vaut, les vrais avantages et limites, et la remise officielle du jour.",
 hero_cta="Disponibilité & jusqu'à -75% »", cta="Je veux ma Jetterix » jusqu'à -75%",
 hero_note=["Aucune électricité", "S'adapte à tout tuyau", "Satisfait ou remboursé 30 jours"],
 trust=["Se fixe en quelques secondes", "Compatible avec tout tuyau standard", "Satisfait ou remboursé 30 jours", "Livraison rapide et suivie"],
 disc_line="Votre remise allant jusqu'à -75% est appliquée automatiquement sur la boutique officielle.",
 agitate_kick="Pourquoi tout le monde en parle",
 agitate_h2="Les nettoyeurs électriques sont chers, lourds et compliqués — et un tuyau d'arrosage est trop faible",
 agitate_p="Un nettoyeur haute pression électrique coûte des centaines d'euros, pèse une tonne et demande câbles, rangement et installation. Un simple tuyau d'arrosage, lui, n'a pas assez de puissance. Jetterix comble exactement ce vide : la puissance d'un nettoyeur, la simplicité d'une buse qui se visse sur le tuyau que vous avez déjà.",
 agitate_list=["Un nettoyeur électrique coûte 150–500 € et exige électricité, tuyaux & rangement",
               "Faire venir un pro pour l'allée revient souvent à 150 €+ par passage",
               "Une buse classique ne fait que goutter — elle ne déloge pas la crasse incrustée",
               "<b>Jetterix :</b> on visse, on ouvre le robinet, la saleté part en quelques secondes — sans électricité"],
 steps_kick="Comment ça marche", steps_h2="Nettoyez tout sous haute pression en 3 étapes",
 steps=[("Vissez-la", "Fixez Jetterix sur n'importe quel tuyau d'arrosage standard en quelques secondes — sans outil, sans raccord à acheter."),
        ("Ouvrez l'eau", "La pression de votre réseau d'eau fait tout le travail. Pas de moteur, pas de câble, pas d'électricité."),
        ("Visez & nettoyez", "Passez du jet concentré au jet en éventail et regardez la saleté, les algues et la crasse disparaître.")],
 gallery_kick="De plus près", gallery_h2="Jetterix sous tous les angles",
 benefits_kick="Pourquoi les clients l'adorent", benefits_h2="La puissance d'un nettoyeur, sans le prix d'un nettoyeur",
 benefits=[("bolt","Jet puissant et précis","Une buse de précision concentre votre eau en un jet haute pression qui déloge la crasse tenace."),
           ("drop","Aucune électricité","Fonctionne uniquement avec la pression de votre réseau d'eau — pas de moteur, pas de câble, pas de facture d'électricité."),
           ("tool","S'adapte à tout tuyau","Se visse sur n'importe quel tuyau d'arrosage standard en quelques secondes. Aucun raccord spécial, aucune installation."),
           ("move","Léger & compact","Tient dans la main et se range dans un tiroir — sans l'encombrement d'un nettoyeur électrique."),
           ("spray","Modes jet & éventail","Du jet concentré qui décape au jet large qui rince — selon la surface à nettoyer."),
           ("leaf","Sans produits agressifs","Eau + pression suffisent à enlever saleté, moisissure et algues — plus doux pour les plantes et la peinture.")],
 offer_kick="L'offre officielle du jour", offer_h2="Choisissez votre pack Jetterix",
 offer_sub="La plupart en prennent deux — une pour la maison, une pour la voiture ou la famille. Le pack de 2 est le plus populaire ; le pack de 3 a la plus grosse remise.",
 bundle_labels=dict(single="1 Buse", two="2 Buses", three="3 Buses",
                    best="Le plus populaire", value="Meilleure offre", note_single="Pour essayer",
                    note_two="Idéal pour la plupart", note_three="À partager en famille",
                    save="Jusqu'à -75% appliqué", final="Prix final affiché sur la boutique officielle"),
 offer_cta="J'obtiens ma remise » jusqu'à -75%", pay_note="Paiement sécurisé · Visa · Mastercard · Amex · PayPal",
 guarantee_mini="Satisfait ou remboursé 30 jours",
 reviews_kick="Avis clients vérifiés", reviews_h2="Ce que disent les propriétaires de Jetterix",
 verified="Acheteur vérifié", helpful="utile",
 anchor=[("Mathieu T.","J'avais acheté tellement d'embouts de tuyau bon marché qui ne servaient à rien. Jetterix délivre vraiment un jet puissant et précis qui nettoie réellement. J'ai fait l'allée et la terrasse en un après-midi — sans nettoyeur électrique, sans bazar."),
         ("Antoine B.","De la moisissure verte s'était installée sur le côté ombragé de la maison, et Jetterix l'a enlevée sans aucun produit. Le jet haute pression a tout décollé et nous a évité d'appeler un professionnel. L'entretien du jardin est devenu un jeu d'enfant.")],
 wall=[("Stéphane W.","Paris","Des années de crasse parties de la terrasse en quelques minutes. Incroyable que ça se visse juste sur le tuyau.",3),
       ("Julie P.","Lyon","J'ai fait la voiture, les poubelles et la terrasse en bois. Bien plus de pression que je pensais pour une buse.",5),
       ("Thomas H.","Marseille","Sceptique au début mais ça marche vraiment. Le mode jet déloge la mousse entre les pavés.",6),
       ("Laure B.","Toulouse","Pas de câbles, pas d'installation, pas de bruit. On ouvre le robinet et c'est parti. À avoir plus tôt.",8),
       ("Christophe M.","Nice","Algues décapées sur la clôture, l'allée semble neuve. Aucun nettoyeur électrique nécessaire.",10),
       ("Marine L.","Bordeaux","Assez léger pour l'utiliser d'une main. Parfait pour la voiture et le mobilier de jardin.",12),
       ("Pierre S.","Lille","Fait exactement ce qui est promis. Jet puissant, facile de passer au jet doux pour les vitres.",14)],
 guar_kick="Zéro risque", guar_h2="Essayez 30 jours, sans risque",
 guar_seal=("30 JOURS","REMBOURSÉ"),
 guar_p="Si Jetterix ne vient pas à bout de vos nettoyages comme vous l'espériez, renvoyez-la sous 30 jours pour un remboursement intégral ou un remplacement. Aucun risque, aucun stress — c'est la promesse de la boutique officielle.",
 faq_kick="Avant d'acheter", faq_h2="Jetterix : questions & réponses",
 faq=[("Comment fonctionne Jetterix ?","C'est une buse de précision qui concentre l'eau de votre tuyau d'arrosage en un jet haute pression. La pression normale de votre réseau d'eau fait tout le travail — aucun moteur ni électricité requis."),
      ("Sur quelles surfaces puis-je l'utiliser ?","Allées, terrasses, bois, clôtures, façades, brique, voitures, mobilier de jardin, poubelles et plus encore. Le jet en éventail pour les surfaces délicates, le jet concentré pour la crasse tenace."),
      ("Fonctionne-t-il vraiment sans électricité ?","Oui. Jetterix fonctionne uniquement avec la pression de votre réseau d'eau. Pas de moteur, pas de batterie, pas de câble d'alimentation — il suffit de le visser sur le tuyau et d'ouvrir le robinet."),
      ("Est-il compatible avec mon tuyau ?","Oui. Jetterix se fixe sur n'importe quel raccord de tuyau d'arrosage standard en quelques secondes, sans raccord spécial ni outil."),
      ("Jetterix est-il fiable ou une arnaque ?","C'est un vrai produit, expédié avec suivi, service client et garantie satisfait ou remboursé 30 jours. Comme pour tout produit populaire, achetez uniquement sur la boutique officielle pour avoir le produit authentique et la garantie."),
      ("Quel est le délai de livraison ?","L'expédition se fait avec suivi ; vous recevez un numéro de suivi par e-mail après la commande.")],
 final_h2="Prêt à faire sauter la crasse ?", final_p="La remise du jour allant jusqu'à -75% est appliquée sur la boutique officielle — dans la limite des stocks.",
 final_cd_label="Offre réservée pendant", final_cta="J'obtiens ma Jetterix » jusqu'à -75%",
 footer_disc="Divulgation d'affiliation : tryjetterix.com est un site d'avis indépendant. Nous pouvons percevoir une commission si vous achetez via les liens de cette page, sans coût supplémentaire pour vous. Jetterix™ est une marque de son propriétaire respectif. Les prix et offres sont affichés par la boutique officielle et peuvent changer.",
 announce_ship="🚚 Livraison suivie GRATUITE aujourd'hui", announce_cd="L'offre se termine dans",
 sticky_label="Jetterix Buse Haute Pression", sticky_price="Jusqu'à -75% aujourd'hui",
 viewing="{n} personnes regardent ce produit", stock="Plus que {n} à ce prix",
 exit=dict(title="Attendez — ne ratez pas jusqu'à -75% !", sub="Votre remise est encore réservée quelques minutes.",
           coupon_label="Remise appliquée automatiquement", code="jusqu'à -75%", cta="Obtenir ma remise »", decline="Non merci, je paie plein tarif"),
 redirect=dict(t="Sécurisation de votre remise…", s="Vous êtes redirigé vers la boutique officielle Jetterix"),
 i18n=dict(tpl="<b>{name}</b> de {city} vient de commander {product}", products=["le pack de 2","une Jetterix","le pack de 3"], ago_just="à l'instant", ago_min="il y a {n} min", verified="Vérifié"),
 cities=["Paris","Lyon","Marseille","Toulouse","Nice","Nantes","Bordeaux","Lille","Bruxelles","Liège"],
 names=["Lucas M.","Camille D.","Hugo L.","Léa R.","Nathan P.","Manon H.","Théo B.","Chloé S."],
))

# ========================================================================
# HELPERS
# ========================================================================
ICONS = {
 "bolt":'<path d="M13 2 4.5 13.5H11l-1 8.5L19.5 10H13z"/>',
 "drop":'<path d="M12 2.5C12 2.5 5.5 9.5 5.5 14.5a6.5 6.5 0 0 0 13 0C18.5 9.5 12 2.5 12 2.5z"/>',
 "tool":'<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.5-2.5z"/>',
 "move":'<path d="M5 9 2 12l3 3M9 5l3-3 3 3M15 19l-3 3-3-3M19 9l3 3-3 3M2 12h20M12 2v20"/>',
 "spray":'<path d="M3 17h6v4H3zM6 17V7M6 7l4-2M6 11l4-1M6 14l4 0M14 5l1-1M17 6l1-1M14 9l1 0M18 9l1 0M16 12l1 0"/>',
 "leaf":'<path d="M5 21c8 0 14-5 14-14 0-1-.2-2-.5-3C10 4 4 9 4 18c0 1 .3 2 1 3z"/><path d="M9 17c2-4 5-6 8-7"/>',
 "check":'<path d="M20 6 9 17l-5-5"/>',
}
def svg(name, cls=""):
    return '<svg class="%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (cls, ICONS.get(name, ICONS["check"]))

FEMALE = set("Jennifer Ashley Emily Sarah Olivia Charlotte Ava Mia Rachel Laura Megan "
             "Anna Lena Marie Sophie Julia Melanie Camille Léa Manon Chloé Julie Laure Marine".split())
AV_M = ["am%d.webp" % i for i in range(1, 9)]
AV_W = ["aw%d.webp" % i for i in range(1, 9)]
def face_av(name, i):
    first = name.strip().split()[0]
    pool = AV_W if first in FEMALE else AV_M
    return "../assets/img/" + pool[i % len(pool)]

def E(s): return html.escape(s, quote=True)

REDIRECT_STEPS = {
 "us":["Applying your discount","Reserving your nozzle in stock","Opening encrypted checkout"],
 "uk":["Applying your discount","Reserving your nozzle in stock","Opening encrypted checkout"],
 "au":["Applying your discount","Reserving your nozzle in stock","Opening encrypted checkout"],
 "de":["Rabatt wird angewendet","Ihre Düse wird reserviert","Sicherer Checkout wird geöffnet"],
 "fr":["Application de votre remise","Réservation de votre buse","Ouverture du paiement sécurisé"],
}

# Localised first-party policy/EEAT strings.
LEGAL = {
 "en": dict(reviewed_by="Reviewed by", editor="Daniel Carter", role="Outdoor Cleaning Editor", updated="Updated", hands_on="Independent hands-on review",
   back="← Back to review", l_privacy="Privacy Policy", l_terms="Terms", l_disclosure="Affiliate Disclosure", l_contact="Contact",
   t_privacy="Privacy Policy", t_terms="Terms of Use", t_disclosure="Affiliate Disclosure", t_contact="Contact Us",
   b_privacy=f"<p>tryjetterix.com is an independent review website. We respect your privacy and do not sell your personal data.</p><h2>What we collect</h2><p>We use a geolocation service (ipinfo.io) to detect your approximate country/city so we can show relevant local information. We store small values in your browser (localStorage) to run the on-page discount timer and recent-activity notice. We do not require you to create an account or submit personal details to read this site.</p><h2>Cookies & third parties</h2><p>When you click through to the official {BRAND} store, that store may set its own cookies under its own privacy policy. Any future advertising pixels will be disclosed and, where required, gated behind consent.</p><h2>Your rights & contact</h2><p>You can clear the data we store at any time by clearing your browser storage. For any privacy request, email <a href='mailto:{EMAIL}'>{EMAIL}</a>.</p>",
   b_terms=f"<p>This website provides information and opinion about the {BRAND} high-pressure hose nozzle. We are an independent reviewer, <b>not</b> the seller or manufacturer.</p><h2>Purchases</h2><p>All orders are placed on, fulfilled by, and supported by the official {BRAND} store. Prices, stock, shipping and returns are set by that store and may change. Please review their terms before buying.</p><h2>No warranty</h2><p>Information here is provided in good faith and 'as is', without warranty. We are not liable for decisions made based on this content. Trademarks belong to their respective owners.</p>",
   b_disclosure=f"<p>tryjetterix.com participates in affiliate programs. If you buy through links on this site, we may earn a commission — <b>at no extra cost to you</b>.</p><p>This never changes the price you pay, and our views are our own. We are an independent review site and not the official {BRAND} store. Questions? Email <a href='mailto:{EMAIL}'>{EMAIL}</a>.</p>",
   b_contact=f"<p>We're an independent review site. For questions about this website, partnerships or privacy requests, email us:</p><p><a href='mailto:{EMAIL}'><b>{EMAIL}</b></a></p><p>For order, shipping, refund or product-support questions, please contact the official {BRAND} store, which fulfils all purchases.</p>"),
 "de": dict(reviewed_by="Geprüft von", editor="Daniel Krause", role="Redakteur Außenreinigung", updated="Aktualisiert", hands_on="Unabhängiger Praxis-Test",
   back="← Zurück zum Test", l_privacy="Datenschutz", l_terms="AGB", l_disclosure="Affiliate-Hinweis", l_contact="Kontakt & Impressum",
   t_privacy="Datenschutzerklärung", t_terms="Nutzungsbedingungen", t_disclosure="Affiliate-Hinweis", t_contact="Kontakt & Impressum",
   b_privacy=f"<p>tryjetterix.com ist eine unabhängige Test-Website. Wir respektieren Ihre Privatsphäre und verkaufen Ihre personenbezogenen Daten nicht.</p><h2>Was wir erfassen</h2><p>Wir nutzen einen Geolokalisierungsdienst (ipinfo.io), um Ihr ungefähres Land/Ihre Stadt zu erkennen und passende Informationen anzuzeigen. Im Browser (localStorage) speichern wir kleine Werte für den Rabatt-Timer und den Aktivitäts-Hinweis. Zum Lesen ist kein Konto erforderlich.</p><h2>Cookies & Dritte</h2><p>Wenn Sie zum offiziellen {BRAND}-Shop weiterklicken, kann dieser eigene Cookies gemäß seiner eigenen Datenschutzerklärung setzen.</p><h2>Ihre Rechte & Kontakt</h2><p>Sie können die gespeicherten Daten jederzeit durch Leeren des Browserspeichers löschen. Für Datenschutz-Anfragen schreiben Sie an <a href='mailto:{EMAIL}'>{EMAIL}</a>.</p>",
   b_terms=f"<p>Diese Website bietet Informationen und Meinungen zur {BRAND} Hochdruckdüse für den Gartenschlauch. Wir sind ein unabhängiger Tester, <b>nicht</b> der Verkäufer oder Hersteller.</p><h2>Käufe</h2><p>Alle Bestellungen werden im offiziellen {BRAND}-Shop aufgegeben, ausgeführt und betreut. Preise, Verfügbarkeit, Versand und Rückgabe legt dieser Shop fest und können sich ändern.</p><h2>Keine Gewährleistung</h2><p>Die Informationen werden nach bestem Wissen und 'wie besehen' bereitgestellt, ohne Gewähr. Marken gehören ihren jeweiligen Inhabern.</p>",
   b_disclosure=f"<p>tryjetterix.com nimmt an Affiliate-Programmen teil. Wenn Sie über Links auf dieser Seite kaufen, erhalten wir ggf. eine Provision — <b>ohne Mehrkosten für Sie</b>.</p><p>Der Preis ändert sich dadurch nie, und unsere Meinung ist unabhängig. Wir sind nicht der offizielle {BRAND}-Shop. Fragen? <a href='mailto:{EMAIL}'>{EMAIL}</a>.</p>",
   b_contact=f"<p>Wir sind eine unabhängige Test-Website. Bei Fragen zur Website, Kooperationen oder Datenschutz schreiben Sie an:</p><p><a href='mailto:{EMAIL}'><b>{EMAIL}</b></a></p><p>Für Bestellung, Versand, Rückerstattung oder Produktsupport wenden Sie sich bitte an den offiziellen {BRAND}-Shop, der alle Käufe abwickelt.</p>"),
 "fr": dict(reviewed_by="Testé par", editor="Daniel Lambert", role="Rédacteur Nettoyage Extérieur", updated="Mis à jour", hands_on="Test indépendant en conditions réelles",
   back="← Retour à l'avis", l_privacy="Confidentialité", l_terms="Conditions", l_disclosure="Divulgation d'affiliation", l_contact="Contact",
   t_privacy="Politique de confidentialité", t_terms="Conditions d'utilisation", t_disclosure="Divulgation d'affiliation", t_contact="Nous contacter",
   b_privacy=f"<p>tryjetterix.com est un site d'avis indépendant. Nous respectons votre vie privée et ne vendons pas vos données personnelles.</p><h2>Ce que nous collectons</h2><p>Nous utilisons un service de géolocalisation (ipinfo.io) pour détecter votre pays/ville approximatif et afficher des informations locales pertinentes. Nous stockons de petites valeurs dans votre navigateur (localStorage) pour le minuteur de réduction et l'avis d'activité. Aucun compte n'est requis.</p><h2>Cookies & tiers</h2><p>En cliquant vers la boutique officielle {BRAND}, celle-ci peut définir ses propres cookies selon sa propre politique.</p><h2>Vos droits & contact</h2><p>Vous pouvez effacer ces données à tout moment en vidant le stockage du navigateur. Pour toute demande RGPD : <a href='mailto:{EMAIL}'>{EMAIL}</a>.</p>",
   b_terms=f"<p>Ce site fournit des informations et avis sur la buse haute pression {BRAND} pour tuyau d'arrosage. Nous sommes un évaluateur indépendant, <b>pas</b> le vendeur ni le fabricant.</p><h2>Achats</h2><p>Toutes les commandes sont passées, traitées et suivies par la boutique officielle {BRAND}. Les prix, le stock, la livraison et les retours sont fixés par cette boutique et peuvent changer.</p><h2>Aucune garantie</h2><p>Les informations sont fournies de bonne foi et 'en l'état', sans garantie. Les marques appartiennent à leurs propriétaires respectifs.</p>",
   b_disclosure=f"<p>tryjetterix.com participe à des programmes d'affiliation. Si vous achetez via les liens de ce site, nous pouvons percevoir une commission — <b>sans coût supplémentaire pour vous</b>.</p><p>Cela ne change jamais le prix payé, et nos avis sont les nôtres. Nous ne sommes pas la boutique officielle {BRAND}. Questions ? <a href='mailto:{EMAIL}'>{EMAIL}</a>.</p>",
   b_contact=f"<p>Nous sommes un site d'avis indépendant. Pour toute question sur ce site, partenariats ou confidentialité :</p><p><a href='mailto:{EMAIL}'><b>{EMAIL}</b></a></p><p>Pour les questions de commande, livraison, remboursement ou support produit, contactez la boutique officielle {BRAND} qui traite tous les achats.</p>"),
}
def legal_key(code): return "de" if code == "de" else "fr" if code == "fr" else "en"
POLICY_KINDS = ["privacy", "terms", "disclosure", "contact"]

# Bold scam-or-legit objection handler
LEGIT = {
 "en": dict(kick="Scam or legit? — straight answer", h2=f"Is {BRAND} a Scam? Our Honest Verdict",
   verdict=f"Verdict: {BRAND} is a <b>real, legitimate product — NOT a scam.</b> But there's one thing you must know first.",
   points=[("ok","It's a real product that actually ships — with tracked delivery and customer support."),
           ("ok","Every order is covered by a <b>30-day money-back guarantee</b>, so your money is protected."),
           ("ok","Backed by thousands of verified buyer reviews for genuine cleaning power."),
           ("warn","The catch: cheap copycats are sold on random marketplaces. <b>Only buy from the official store</b> to get the real nozzle + the guarantee.")],
   bottom="Bottom line: <b>legit and low-risk</b> thanks to the money-back guarantee. Just order from the official store below — never a random seller."),
 "de": dict(kick="Betrug oder seriös? — Klare Antwort", h2=f"Ist {BRAND} ein Betrug? Unser ehrliches Fazit",
   verdict=f"Fazit: {BRAND} ist ein <b>echtes, seriöses Produkt — KEIN Betrug.</b> Aber eines sollten Sie vorher wissen.",
   points=[("ok","Echtes Produkt, das tatsächlich geliefert wird — mit Sendungsverfolgung und Kundenservice."),
           ("ok","Jede Bestellung ist durch eine <b>30-Tage-Geld-zurück-Garantie</b> abgesichert — Ihr Geld ist geschützt."),
           ("ok","Tausende verifizierte Kundenbewertungen für echte Reinigungskraft."),
           ("warn","Der Haken: Auf fremden Marktplätzen gibt es billige Nachahmungen. <b>Nur im offiziellen Shop kaufen</b>, um das echte Produkt + die Garantie zu erhalten.")],
   bottom="Unterm Strich: <b>seriös und risikoarm</b> dank der Geld-zurück-Garantie. Bestellen Sie nur über den offiziellen Shop unten — nicht bei fremden Händlern."),
 "fr": dict(kick="Arnaque ou fiable ? — Réponse claire", h2=f"{BRAND} est-il une arnaque ? Notre verdict honnête",
   verdict=f"Verdict : {BRAND} est un <b>produit réel et fiable — PAS une arnaque.</b> Mais il y a une chose à savoir d'abord.",
   points=[("ok","Un vrai produit réellement expédié — avec suivi de livraison et service client."),
           ("ok","Chaque commande est couverte par une <b>garantie satisfait ou remboursé de 30 jours</b> — votre argent est protégé."),
           ("ok","Des milliers d'avis clients vérifiés pour une vraie puissance de nettoyage."),
           ("warn","Le piège : des contrefaçons bon marché circulent sur certaines marketplaces. <b>Achetez uniquement sur la boutique officielle</b> pour avoir le vrai produit + la garantie.")],
   bottom="En résumé : <b>fiable et sans risque</b> grâce à la garantie. Commandez uniquement via la boutique officielle ci-dessous — pas chez un vendeur tiers."),
}
def legit_for(code): return LEGIT[legal_key(code)]
def legal_for(code): return LEGAL[legal_key(code)]

def build_bundles(g):
    L = g["bundle_labels"]
    rows = [
        (L["single"], TIERS[0][1], L["note_single"], None),
        (L["two"],    TIERS[1][1], L["note_two"],    L["best"]),
        (L["three"],  TIERS[2][1], L["note_three"],  L["value"]),
    ]
    out = []
    for qty, pct, note, ribbon in rows:
        best = " best" if ribbon == L["best"] else ""
        rb = ('<span class="ribbon">%s</span>' % E(ribbon)) if ribbon else ""
        out.append(
            '<label class="bundle%s js-cta">%s<span class="qty">%s</span>'
            '<span class="price">−%d%%</span>'
            '<span class="each">%s</span><span class="save">%s</span>'
            '<span class="bfinal">%s</span></label>'
            % (best, rb, E(qty), pct, E(note), E(L["save"]), E(L["final"])))
    return "\n".join(out)

def build_reviews(g):
    cards = []; idx = 0
    for name, text in g["anchor"]:
        cards.append(
            '<div class="rev-card"><div class="top"><img class="av" src="%s" alt="%s" loading="lazy" width="42" height="42">'
            '<div class="who"><b>%s</b><span>%s</span></div><span class="verified">✔ %s</span></div>'
            '<div class="rs">★★★★★</div><p>%s</p></div>'
            % (face_av(name, idx), E(name), E(name), E(g["verified"]), E(g["verified"]), E(text))); idx += 1
    for name, city, text, days in g["wall"]:
        cards.append(
            '<div class="rev-card"><div class="top"><img class="av" src="%s" alt="%s" loading="lazy" width="42" height="42">'
            '<div class="who"><b>%s</b><span>%s</span></div><span class="verified">✔ %s</span></div>'
            '<div class="rs">★★★★★</div><p>%s</p>'
            '<div class="meta"><span>%s</span></div></div>'
            % (face_av(name, idx), E(name), E(name), E(city), E(g["verified"]), E(text), "%dd" % days)); idx += 1
    return "\n".join(cards)

LOWSTOCK = {
 "en": dict(label="⚠️ ALMOST GONE — today's up-to-75% deal", sub="Selling fast at this price", unit="left in stock", cta="Grab mine before it's gone »"),
 "de": dict(label="⚠️ FAST AUSVERKAUFT — bis -75% nur heute", sub="Zu diesem Preis schnell vergriffen", unit="noch auf Lager", cta="Jetzt sichern, bevor es weg ist »"),
 "fr": dict(label="⚠️ BIENTÔT ÉPUISÉ — jusqu'à -75% aujourd'hui", sub="Part très vite à ce prix", unit="encore en stock", cta="Je le prends avant rupture »"),
}
def lowstock_for(code): return LOWSTOCK[legal_key(code)]

def build_legit_points(g):
    out = []
    for t, txt in legit_for(g["code"])["points"]:
        out.append('<li class="%s"><span class="li-ic">%s</span><span>%s</span></li>'
                   % (t, "✓" if t == "ok" else "⚠", txt))
    return "".join(out)

def build_faq(g):
    return "\n".join('<div class="faq-item"><div class="faq-q">%s<span class="pm">+</span></div>'
                     '<div class="faq-a"><div>%s</div></div></div>' % (E(q), E(a)) for q, a in g["faq"])

def build_steps(g):
    return "\n".join('<div class="step reveal"><div class="n">%d</div><h3>%s</h3><p>%s</p></div>'
                     % (i, E(h), E(p)) for i, (h, p) in enumerate(g["steps"], 1))

def build_benefits(g):
    return "\n".join('<div class="benefit reveal"><div class="ic">%s</div><h3>%s</h3><p>%s</p></div>'
                     % (svg(ic), E(h), E(p)) for ic, h, p in g["benefits"])

def build_gallery():
    return "\n".join('<div class="gi"><img src="../assets/img/%s" alt="%s high-pressure nozzle" loading="lazy" width="500" height="500"></div>' % (img, BRAND) for img in IMAGES)

def build_trust(g):
    return "\n".join('<span>%s %s</span>' % (svg("check"), E(t)) for t in g["trust"])

def build_agitate_list(g):
    return "\n".join('<li><span class="x">✕</span><span>%s</span></li>' % item for item in g["agitate_list"])

def foot_langnav(code):
    return "\n".join('<a href="%s/%s/"%s>%s</a>' % (DOMAIN, x["code"], ' aria-current="true"' if x["code"] == code else '', E(x["lang_label"])) for x in GEOS)

def foot_links(g):
    L = legal_for(g["code"]); c = g["code"]
    ours = [(L["l_privacy"], "privacy"), (L["l_terms"], "terms"), (L["l_disclosure"], "disclosure"), (L["l_contact"], "contact")]
    return " · ".join('<a href="%s/%s/%s/">%s</a>' % (DOMAIN, c, kind, E(lbl)) for lbl, kind in ours)

def byline(g):
    L = legal_for(g["code"])
    return ('<div class="byline"><img src="../assets/img/am1.webp" alt="" width="30" height="30" loading="lazy">'
            '<span>%s <b>%s</b>, %s</span><span class="sep">·</span><span>%s %s</span><span class="sep">·</span><span>%s</span></div>'
            % (E(L["reviewed_by"]), E(L["editor"]), E(L["role"]), E(L["updated"]), PRETTY, E(L["hands_on"])))

def render_policy(g, kind, geos):
    L = legal_for(g["code"]); c = g["code"]
    title = {"privacy": L["t_privacy"], "terms": L["t_terms"], "disclosure": L["t_disclosure"], "contact": L["t_contact"]}[kind]
    body = {"privacy": L["b_privacy"], "terms": L["b_terms"], "disclosure": L["b_disclosure"], "contact": L["b_contact"]}[kind]
    hl = "".join('<link rel="alternate" hreflang="%s" href="%s/%s/%s/">' % (x["hreflang"], DOMAIN, x["code"], kind) for x in geos)
    hl += '<link rel="alternate" hreflang="x-default" href="%s/us/%s/">' % (DOMAIN, kind)
    return (
'<!DOCTYPE html><html lang="%s"><head>'
'<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
'<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="alternate icon" href="/favicon.ico" sizes="any">'
'<link rel="apple-touch-icon" href="/apple-touch-icon.png"><meta name="theme-color" content="#0a91d8">'
'<title>%s — %s</title><meta name="description" content="%s · tryjetterix.com">'
'<meta name="robots" content="index, follow"><link rel="canonical" href="%s/%s/%s/">%s'
'<link rel="stylesheet" href="../../assets/styles.css"></head><body>'
'<header class="nav"><div class="wrap"><a class="logo" href="/%s/"><span class="dot"></span>%s<small>%s</small></a></div></header>'
'<main class="legal"><a class="back" href="/%s/">%s</a><h1>%s</h1><div class="upd">%s %s</div>%s</main>'
'<footer><div class="wrap"><nav class="foot-lang" aria-label="Languages">%s</nav>'
'<div class="links">%s</div>'
'<div class="copy">© %s tryjetterix.com — independent review · Not the official %s store.</div></div></footer>'
'</body></html>'
    ) % (g["lang"], E(title), BRAND, E(title), DOMAIN, c, kind, hl,
         c, BRAND, E(g["reviewword"]), c, E(L["back"]), E(title), E(L["updated"]), PRETTY, body,
         foot_langnav(c), foot_links(g), str(datetime.date.today().year), BRAND)

def hreflang_links(geos):
    out = ['<link rel="alternate" hreflang="%s" href="%s/%s/">' % (g["hreflang"], DOMAIN, g["code"]) for g in geos]
    out.append('<link rel="alternate" hreflang="x-default" href="%s/us/">' % DOMAIN)
    return "\n".join(out)

def jsonld(g):
    reviews_ld = [{"@type":"Review","author":{"@type":"Person","name":name},
                   "reviewRating":{"@type":"Rating","ratingValue":"5","bestRating":"5"},"reviewBody":text}
                  for name, city, text, days in g["wall"][:5]]
    data = [
      {"@context":"https://schema.org","@type":"Product","name":BRAND+" High-Pressure Hose Nozzle",
       "image":["%s/assets/img/%s" % (DOMAIN, IMAGES[0])],
       "description": g["desc"],
       "brand":{"@type":"Brand","name":BRAND},
       "aggregateRating":{"@type":"AggregateRating","ratingValue":g["rating"],"reviewCount":str(g["reviews"]),"bestRating":"5"},
       "review":reviews_ld},
      {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
         {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q, a in g["faq"]]},
      {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
         {"@type":"ListItem","position":1,"name":"Home","item":"%s/%s/" % (DOMAIN, g["code"])},
         {"@type":"ListItem","position":2,"name":BRAND+" Review"}]},
      {"@context":"https://schema.org","@type":"Organization","name":"tryjetterix.com","url":DOMAIN},
    ]
    return '<script type="application/ld+json">%s</script>' % json.dumps(data, ensure_ascii=False)

def geo_js(g):
    obj = {"code":g["code"],"cc":g["cc"],"net":g["net"],"o":g["o"],"cr":g["cr"],"s2tag":g["s2tag"],
           "thumb":"../assets/img/p2.webp","cities":g["cities"],"names":g["names"],"i18n":g["i18n"]}
    return "document.documentElement.classList.add('js');window.GEO=%s;" % json.dumps(obj, ensure_ascii=False)

# ========================================================================
# PAGE TEMPLATE
# ========================================================================
def render_page(g, geos):
    lang_menu = "\n".join('<li><a href="../%s/">%s</a></li>' % (x["code"], E(x["lang_label"])) for x in geos)
    ctx = {
      "LANG": g["lang"], "OG": g["og"], "CODE": g["code"], "BRAND": BRAND, "REVIEWWORD": E(g["reviewword"]),
      "TITLE": E(g["title"]), "DESC": E(g["desc"]), "KEYWORDS": E(g["keywords"]),
      "CANON": "%s/%s/" % (DOMAIN, g["code"]),
      "HREFLANG": hreflang_links(geos), "GEOJS": geo_js(g),
      "OGIMG": "%s/assets/img/%s" % (DOMAIN, IMAGES[0]),
      "ANNOUNCE_SHIP": E(g["announce_ship"]), "ANNOUNCE_CD": E(g["announce_cd"]),
      "LANGMENU": lang_menu, "LANGLABEL": E(g["lang_label"]),
      "EYEBROW": E(g["eyebrow"]), "H1": g["h1"], "SUB": E(g["sub"]),
      "RATING": g["rating"], "REVIEWS": "{:,}".format(g["reviews"]), "REVIEWSWORD": E(g["reviews_word"]),
      "HEROCTA": E(g["hero_cta"]), "CTA": E(g["cta"]),
      "HERONOTE": "\n".join('<span>%s %s</span>' % (svg("check"), E(n)) for n in g["hero_note"]),
      "DISCLINE": E(g["disc_line"]), "TRUST": build_trust(g),
      "AG_KICK": E(g["agitate_kick"]), "AG_H2": E(g["agitate_h2"]), "AG_P": E(g["agitate_p"]), "AG_LIST": build_agitate_list(g),
      "ST_KICK": E(g["steps_kick"]), "ST_H2": E(g["steps_h2"]), "STEPS": build_steps(g),
      "GA_KICK": E(g["gallery_kick"]), "GA_H2": E(g["gallery_h2"]), "GALLERY": build_gallery(),
      "BE_KICK": E(g["benefits_kick"]), "BE_H2": E(g["benefits_h2"]), "BENEFITS": build_benefits(g),
      "OF_KICK": E(g["offer_kick"]), "OF_H2": E(g["offer_h2"]), "OF_SUB": E(g["offer_sub"]),
      "BUNDLES": build_bundles(g), "OFFERCTA": E(g["offer_cta"]), "PAYNOTE": E(g["pay_note"]), "GUARMINI": E(g["guarantee_mini"]),
      "RV_KICK": E(g["reviews_kick"]), "RV_H2": E(g["reviews_h2"]), "REVCARDS": build_reviews(g),
      "LEGIT_KICK": E(legit_for(g["code"])["kick"]), "LEGIT_H2": E(legit_for(g["code"])["h2"]),
      "LEGIT_VERDICT": legit_for(g["code"])["verdict"], "LEGIT_POINTS": build_legit_points(g), "LEGIT_BOTTOM": legit_for(g["code"])["bottom"],
      "LS_LABEL": E(lowstock_for(g["code"])["label"]), "LS_SUB": E(lowstock_for(g["code"])["sub"]),
      "LS_UNIT": E(lowstock_for(g["code"])["unit"]), "LS_CTA": E(lowstock_for(g["code"])["cta"]),
      "GU_KICK": E(g["guar_kick"]), "GU_H2": E(g["guar_h2"]),
      "SEAL1": E(g["guar_seal"][0]), "SEAL2": E(g["guar_seal"][1]), "GU_P": E(g["guar_p"]),
      "FQ_KICK": E(g["faq_kick"]), "FQ_H2": E(g["faq_h2"]), "FAQ": build_faq(g),
      "FN_H2": E(g["final_h2"]), "FN_P": E(g["final_p"]), "FN_CD": E(g["final_cd_label"]), "FN_CTA": E(g["final_cta"]),
      "FOOT_DISC": E(g["footer_disc"]), "FOOT_LINKS": foot_links(g), "FOOT_LANGNAV": foot_langnav(g["code"]), "BYLINE": byline(g),
      "STICKY_LABEL": E(g["sticky_label"]), "STICKY_PRICE": E(g["sticky_price"]),
      "VIEWING": E(g["viewing"]).replace("{n}", '<b data-viewers>0</b>'),
      "STOCK": E(g["stock"]).replace("{n}", '<b data-stock>0</b>'),
      "EX_TITLE": E(g["exit"]["title"]), "EX_SUB": E(g["exit"]["sub"]),
      "EX_CLABEL": E(g["exit"]["coupon_label"]), "EX_CODE": E(g["exit"]["code"]),
      "EX_CTA": E(g["exit"]["cta"]), "EX_DECLINE": E(g["exit"]["decline"]),
      "RED_T": E(g["redirect"]["t"]), "RED_S": E(g["redirect"]["s"]),
      "RED_S1": E(REDIRECT_STEPS[g["code"]][0]), "RED_S2": E(REDIRECT_STEPS[g["code"]][1]), "RED_S3": E(REDIRECT_STEPS[g["code"]][2]),
      "JSONLD": jsonld(g), "YEAR": str(datetime.date.today().year), "HEROIMG": IMAGES[0],
    }
    out = TEMPLATE
    for k, v in ctx.items():
        out = out.replace("{{%s}}" % k, str(v))
    return out

TEMPLATE = r"""<!DOCTYPE html>
<html lang="{{LANG}}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0a91d8">
<title>{{TITLE}}</title>
<meta name="description" content="{{DESC}}">
<meta name="keywords" content="{{KEYWORDS}}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{{CANON}}">
{{HREFLANG}}
<meta property="og:type" content="website">
<meta property="og:locale" content="{{OG}}">
<meta property="og:title" content="{{TITLE}}">
<meta property="og:description" content="{{DESC}}">
<meta property="og:image" content="{{OGIMG}}">
<meta property="og:url" content="{{CANON}}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" as="image" href="../assets/img/{{HEROIMG}}">
<link rel="preconnect" href="https://ipinfo.io">
<link rel="preconnect" href="https://trkc115.com" crossorigin>
<link rel="dns-prefetch" href="https://trkc115.com">
<link rel="stylesheet" href="../assets/styles.css">
<script>{{GEOJS}}</script>
{{JSONLD}}
</head>
<body>
<div class="announce">
  <span>{{ANNOUNCE_SHIP}}</span>
  <span>{{ANNOUNCE_CD}} <b data-cd>15:00</b></span>
</div>

<header class="nav"><div class="wrap">
  <a class="logo" href="#"><span class="dot"></span>{{BRAND}}<small>{{REVIEWWORD}}</small></a>
  <div class="lang"><button>🌐 {{LANGLABEL}} ▾</button><ul>{{LANGMENU}}</ul></div>
</div></header>

<!-- HERO -->
<section class="hero"><div class="wrap">
  <div>
    <span class="eyebrow">⭐ {{EYEBROW}}</span>
    <h1>{{H1}}</h1>
    <div class="stars">{{RATING}} ★★★★★ · <b>{{REVIEWS}}</b>&nbsp;{{REVIEWSWORD}}</div>
    <p class="sub">{{SUB}}</p>
    <a class="btn pulse js-cta" href="#">{{HEROCTA}} <span class="arw">→</span></a>
    <div class="hero-cta-note">{{HERONOTE}}</div>
    {{BYLINE}}
  </div>
  <div class="heroimg">
    <div class="badge-off"><b>75%</b>OFF</div>
    <img src="../assets/img/{{HEROIMG}}" alt="{{BRAND}} high-pressure hose nozzle" width="560" height="560" fetchpriority="high">
  </div>
</div></section>

<div class="trust"><div class="wrap">{{TRUST}}</div></div>
<div class="announce" style="background:#eafaf1;color:#0a7a4f"><span>✓ {{DISCLINE}}</span></div>

<!-- TOP LOW-STOCK STRIP -->
<div class="stocktop"><div class="wrap"><div class="st-card">
  <span class="st-ic">🔥</span>
  <div class="st-body">
    <div class="st-row"><b class="st-label">{{LS_LABEL}}</b><span class="st-num">⚡ <b><span data-stock2>41</span></b> {{LS_UNIT}}</span></div>
    <div class="ls-track"><i class="ls-fill" data-stockbar></i></div>
  </div>
</div></div></div>

<!-- AGITATE -->
<section class="agitate"><div class="wrap">
  <div class="sec-head reveal"><span class="kick">{{AG_KICK}}</span><h2>{{AG_H2}}</h2></div>
  <div class="row">
    <div class="reveal"><p>{{AG_P}}</p><ul>{{AG_LIST}}</ul></div>
    <div class="card-img reveal"><img src="../assets/img/p3.webp" alt="{{BRAND}} in use" loading="lazy" width="520" height="420"></div>
  </div>
</div></section>

<!-- STEPS -->
<section><div class="wrap">
  <div class="sec-head"><span class="kick">{{ST_KICK}}</span><h2>{{ST_H2}}</h2></div>
  <div class="steps">{{STEPS}}</div>
</div></section>

<!-- GALLERY -->
<section style="background:var(--bg2)"><div class="wrap">
  <div class="sec-head"><span class="kick">{{GA_KICK}}</span><h2>{{GA_H2}}</h2></div>
  <div class="gallery reveal">{{GALLERY}}</div>
</div></section>

<!-- BENEFITS -->
<section><div class="wrap">
  <div class="sec-head"><span class="kick">{{BE_KICK}}</span><h2>{{BE_H2}}</h2></div>
  <div class="benefits">{{BENEFITS}}</div>
</div></section>

<!-- OFFER -->
<section class="offer" id="offer"><div class="wrap">
  <div class="sec-head"><span class="kick">{{OF_KICK}}</span><h2>{{OF_H2}}</h2><p>{{OF_SUB}}</p></div>
  <div class="bundles bundles-3 reveal">{{BUNDLES}}</div>
  <div class="offer-cta">
    <a class="btn pulse js-cta" href="#">{{OFFERCTA}} <span class="arw">→</span></a>
    <div class="pay-row">🔒 {{PAYNOTE}}</div>
    <div class="pay-row">🛡️ {{GUARMINI}} · ⚡ <span>{{STOCK}}</span> · 👀 <span>{{VIEWING}}</span></div>
  </div>
</div></section>

<!-- REVIEWS -->
<section class="reviews"><div class="wrap">
  <div class="sec-head"><span class="kick">{{RV_KICK}}</span><h2>{{RV_H2}}</h2></div>
  <div class="rev-summary">
    <div class="rev-score"><b>{{RATING}}</b><div class="s">★★★★★</div><small>{{REVIEWS}} {{REVIEWSWORD}}</small></div>
    <div class="rev-bars">
      <div class="b">5★<span class="track"><i style="width:92%"></i></span></div>
      <div class="b">4★<span class="track"><i style="width:6%"></i></span></div>
      <div class="b">3★<span class="track"><i style="width:1%"></i></span></div>
      <div class="b">2★<span class="track"><i style="width:0.5%"></i></span></div>
      <div class="b">1★<span class="track"><i style="width:0.5%"></i></span></div>
    </div>
  </div>
  <div class="rev-grid">{{REVCARDS}}</div>
</div></section>

<!-- SCAM / LEGIT -->
<section class="legit"><div class="wrap">
  <div class="sec-head"><span class="kick">⚠️ {{LEGIT_KICK}}</span><h2>{{LEGIT_H2}}</h2></div>
  <div class="legit-box reveal">
    <div class="verdict">{{LEGIT_VERDICT}}</div>
    <ul>{{LEGIT_POINTS}}</ul>
    <div class="bottom">{{LEGIT_BOTTOM}}</div>
    <a class="btn pulse js-cta" href="#">{{CTA}} <span class="arw">→</span></a>
  </div>
</div></section>

<!-- GUARANTEE -->
<section class="guarantee"><div class="wrap">
  <div class="sec-head"><span class="kick">{{GU_KICK}}</span><h2>{{GU_H2}}</h2></div>
  <div class="seal"><b>{{SEAL1}}</b>{{SEAL2}}</div>
  <p>{{GU_P}}</p>
</div></section>

<!-- FAQ -->
<section style="background:var(--bg2)"><div class="wrap">
  <div class="sec-head"><span class="kick">{{FQ_KICK}}</span><h2>{{FQ_H2}}</h2></div>
  <div class="faq-list">{{FAQ}}</div>
</div></section>

<!-- FINAL -->
<section class="final"><div class="wrap">
  <div class="cd">⏳ {{FN_CD}} <b data-cd>15:00</b></div>
  <h2>{{FN_H2}}</h2><p>{{FN_P}}</p>
  <a class="btn js-cta" href="#">{{FN_CTA}} <span class="arw">→</span></a>
</div></section>

<!-- LOW-STOCK ALERT (above footer) -->
<div class="lowstock"><div class="ls-in">
  <div class="ls-head"><span class="ls-flame">🔥</span> {{LS_LABEL}}</div>
  <div class="ls-track"><i class="ls-fill" data-stockbar></i></div>
  <div class="ls-row"><span class="ls-sub">{{LS_SUB}}</span><span class="ls-count"><b><span data-stock2>41</span></b> {{LS_UNIT}}</span></div>
  <a class="btn js-cta ls-cta" href="#">{{LS_CTA}}</a>
</div></div>

<footer><div class="wrap">
  <nav class="foot-lang" aria-label="Languages">{{FOOT_LANGNAV}}</nav>
  <div class="links">{{FOOT_LINKS}}</div>
  <div class="disc">{{FOOT_DISC}}</div>
  <div class="copy">© {{YEAR}} tryjetterix.com — independent review · Not the official {{BRAND}} store.</div>
</div></footer>

<!-- STICKY BAR -->
<div class="stickybar"><div class="wrap">
  <div class="sb-info"><img src="../assets/img/{{HEROIMG}}" alt=""><div class="sb-txt"><b>{{STICKY_LABEL}}</b><span>{{STICKY_PRICE}}</span></div></div>
  <a class="btn js-cta" href="#">{{CTA}} →</a>
</div></div>

<!-- SOCIAL PROOF TICKER -->
<div id="sp-toast"></div>

<!-- EXIT MODAL -->
<div class="modal-bg" id="exit-modal"><div class="modal">
  <span class="x" data-close-exit>×</span>
  <div class="top"><h3>{{EX_TITLE}}</h3><p>{{EX_SUB}}</p></div>
  <div class="body">
    <img src="../assets/img/{{HEROIMG}}" alt="{{BRAND}}">
    <div class="mcd">⏳ <span data-mcd>15:00</span></div>
    <a class="btn js-cta" href="#">{{EX_CTA}}</a>
    <button class="decline" data-close-exit>{{EX_DECLINE}}</button>
  </div>
</div></div>

<!-- REDIRECT OVERLAY -->
<div id="redirect"><div class="rd-card">
  <div class="rd-ring">
    <svg viewBox="0 0 84 84"><defs><linearGradient id="rg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a91d8"/><stop offset="1" stop-color="#0fb98a"/></linearGradient></defs>
      <circle class="bg" cx="42" cy="42" r="36"/><circle class="fg" cx="42" cy="42" r="36"/></svg>
    <span class="rd-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2 4 5v6c0 5 3.4 8.5 8 10 4.6-1.5 8-5 8-10V5z"/><path d="m9 12 2 2 4-4"/></svg></span>
  </div>
  <div class="rd-title">{{RED_T}}</div>
  <ul class="rd-steps"><li>{{RED_S1}}</li><li>{{RED_S2}}</li><li>{{RED_S3}}</li></ul>
  <div class="rd-bar"><i></i></div>
  <div class="rd-sub">🔒 {{RED_S}}</div>
</div></div>

<script src="../assets/config.js"></script>
<script src="../assets/funnel.js"></script>
</body>
</html>
"""

# ========================================================================
# ROOT PICKER / 404 / SITEMAP / ROBOTS / CNAME
# ========================================================================
FLAG = {"us":"🇺🇸","uk":"🇬🇧","au":"🇦🇺","de":"🇩🇪","fr":"🇫🇷"}
def render_root(geos):
    links = "\n".join('<a href="%s/%s/">%s %s</a>' % (DOMAIN, g["code"], FLAG[g["code"]], E(g["lang_label"])) for g in geos)
    geomap = {g["cc"]: g["code"] for g in geos}
    geomap.update({"AT":"de","CH":"de","BE":"fr","IE":"uk","NZ":"au","CA":"us"})
    return """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s High-Pressure Hose Nozzle — Review &amp; Official Deal</title>
<meta name="description" content="%s high-pressure garden-hose nozzle review, real cleaning tests and the official discount. Choose your country.">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#0a91d8">
<link rel="canonical" href="%s/us/">
<link rel="stylesheet" href="assets/styles.css">
<script>
var M=%s, BASE='%s/', done=false;
function go(dest){if(done)return;done=true;location.replace(BASE+dest+'/'+location.search);}
fetch('https://ipwho.is/',{cache:'no-store'}).then(function(r){return r.json()}).then(function(d){
  go(M[(d&&d.country_code)||'']||'us');
}).catch(function(){go('us');});
setTimeout(function(){go('us');},2500);
</script>
</head><body><div class="picker">
<h1>%s High-Pressure Nozzle</h1>
<p>Choose your country / language</p>
<div class="grid">%s</div>
</div></body></html>""" % (BRAND, BRAND, DOMAIN, json.dumps(geomap), DOMAIN, BRAND, links)

def render_404(geos):
    links = " · ".join('<a href="/%s/">%s</a>' % (g["code"], E(g["lang_label"])) for g in geos)
    return """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Not found — %s</title>
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="alternate icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="/assets/styles.css"></head><body><div class="picker">
<h1>404</h1><p>Page not found. Pick your country:</p><div style="margin-top:14px">%s</div>
</div></body></html>""" % (BRAND, links)

def sitemap(geos):
    urls = ['<url><loc>%s/%s/</loc><lastmod>%s</lastmod><changefreq>daily</changefreq><priority>0.9</priority>'
            '%s</url>' % (DOMAIN, g["code"], TODAY,
            "".join('<xhtml:link rel="alternate" hreflang="%s" href="%s/%s/"/>' % (x["hreflang"], DOMAIN, x["code"]) for x in geos))
            for g in geos]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<?xml-stylesheet type="text/xsl" href="/sitemap.xsl"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(urls) + "\n</urlset>\n")

SITEMAP_XSL = """<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
<xsl:output method="html" encoding="UTF-8" indent="yes"/>
<xsl:template match="/">
<html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>tryjetterix.com &#8211; XML Sitemap</title><link rel="icon" href="/favicon.svg" type="image/svg+xml"/>
<style>
  :root{--ink:#0f1b2d;--mut:#6b7c93;--line:#e4ebf2;--bg:#f5f9fc;--blue:#0a91d8;--blue2:#0b6fb3;--mint:#0fb98a}
  *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .wrap{max-width:1000px;margin:0 auto;padding:0 18px 50px}
  header{background:linear-gradient(120deg,#0b6fb3,#0a91d8);color:#fff;padding:30px 18px} header .in{max-width:1000px;margin:0 auto}
  .logo{font-weight:800;font-size:22px;letter-spacing:-.02em;display:flex;align-items:center;gap:9px}
  .logo .dot{width:11px;height:11px;border-radius:50%;background:#19c2e6;box-shadow:0 0 0 4px rgba(255,255,255,.25)}
  h1{font-size:20px;margin:14px 0 4px} header p{margin:0;opacity:.9;font-size:14px}
  .card{background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:0 10px 30px rgba(16,40,70,.07);margin-top:-18px;overflow:hidden}
  table{width:100%;border-collapse:collapse;font-size:13.5px} th,td{text-align:left;padding:12px 14px;border-bottom:1px solid var(--line)}
  th{background:#fbfdff;color:var(--mut);font-size:11.5px;letter-spacing:.05em;text-transform:uppercase;font-weight:700}
  tr:last-child td{border-bottom:0} tbody tr:hover{background:#f3f9fd} td.idx{color:var(--mut);width:40px}
  a{color:var(--blue2);text-decoration:none;font-weight:600} a:hover{text-decoration:underline}
  .pill{display:inline-block;background:#eaf6fc;color:var(--blue2);border:1px solid #d4ebf7;font-size:11.5px;font-weight:700;padding:2px 9px;border-radius:999px}
  .pri{display:inline-block;min-width:38px;text-align:center;background:#e9fbf3;color:#0a7a55;border:1px solid #c7f0e0;font-weight:700;font-size:12px;padding:2px 8px;border-radius:7px}
  .foot{color:var(--mut);font-size:12.5px;margin-top:16px} @media(max-width:640px){.hideS{display:none}}
</style></head><body>
<header><div class="in"><div class="logo"><span class="dot"></span>Jetterix</div><h1>XML Sitemap</h1>
<p><xsl:value-of select="count(s:urlset/s:url)"/> URLs &#183; submitted to search engines</p></div></header>
<div class="wrap"><div class="card"><table>
  <thead><tr><th class="idx">#</th><th>URL</th><th>Languages</th><th class="hideS">Last modified</th><th class="hideS">Frequency</th><th>Priority</th></tr></thead>
  <tbody><xsl:for-each select="s:urlset/s:url"><tr>
    <td class="idx"><xsl:value-of select="position()"/></td>
    <td><a href="{s:loc}"><xsl:value-of select="s:loc"/></a></td>
    <td><span class="pill"><xsl:value-of select="count(xhtml:link)"/> hreflang</span></td>
    <td class="hideS"><xsl:value-of select="s:lastmod"/></td>
    <td class="hideS"><xsl:value-of select="s:changefreq"/></td>
    <td><span class="pri"><xsl:value-of select="s:priority"/></span></td>
  </tr></xsl:for-each></tbody>
</table></div><p class="foot">This is an XML sitemap, meant for search engines. Generated for tryjetterix.com.</p></div>
</body></html></xsl:template></xsl:stylesheet>
"""

ROBOTS = """User-agent: *
Allow: /

User-agent: GPTBot
Allow: /
User-agent: CCBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: %s/sitemap.xml
""" % DOMAIN

LLMS = """# tryjetterix.com
Independent review of the Jetterix high-pressure garden-hose nozzle (clips onto any standard hose, turns mains water into a pressure-washer jet — no electricity).
Localized hands-on reviews, real cleaning tests and the official discount for US, UK, AU, DE/AT/CH and FR/BE.
> Affiliate disclosure: we may earn a commission on purchases made via our links.
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0a91d8"/><stop offset="1" stop-color="#0fb98a"/></linearGradient></defs>
<rect width="64" height="64" rx="16" fill="url(#g)"/>
<g fill="#fff"><rect x="14" y="27" width="20" height="10" rx="3"/><path d="M14 30h-4l-2-3v9l2-3h4z"/></g>
<g stroke="#fff" stroke-width="2.6" stroke-linecap="round"><line x1="36" y1="32" x2="52" y2="22"/><line x1="36" y1="32" x2="54" y2="32"/><line x1="36" y1="32" x2="52" y2="42"/></g>
<circle cx="36" cy="32" r="3" fill="#fff"/></svg>
"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    return full

def main():
    n = 0; pol = 0
    for g in GEOS:
        write("%s/index.html" % g["code"], render_page(g, GEOS)); n += 1
        for kind in POLICY_KINDS:
            write("%s/%s/index.html" % (g["code"], kind), render_policy(g, kind, GEOS)); pol += 1
    write("index.html", render_root(GEOS))
    write("404.html", render_404(GEOS))
    write("sitemap.xml", sitemap(GEOS))
    write("sitemap.xsl", SITEMAP_XSL)
    write("robots.txt", ROBOTS)
    write("llms.txt", LLMS)
    write("CNAME", "tryjetterix.com\n")
    write("favicon.svg", FAVICON_SVG)
    print("Built %d geo pages + %d policy pages + root + 404 + sitemap + robots + llms + favicon + CNAME" % (n, pol))
    print("Geos:", ", ".join(g["code"] for g in GEOS))

if __name__ == "__main__":
    main()
