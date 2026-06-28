/* Jetterix — offer config, click-id capture, geo. Affiliate link assembled at click time.
 *
 * PRIMARY NETWORK = OasisAds (trkc115). Per-page window.GEO supplies {net,o,cr,s2tag}.
 *   URL = https://trkc115.com/c?p=P4016&o=<o>&cr=<cr>&s2=<s2tag>[&s3=<clickid>]
 *
 * FALLBACK NETWORK = Blitz (bikiraibn, affiliate 2397) — DE/FR only, kept warm.
 *   To switch a geo to Blitz: in build.py set that geo's net="blitz" + bc=<creative>,
 *   and this file routes it to https://bikiraibn.com/?a=2397&c=<bc>&s1=<s2tag>.
 *   Blitz DTC creatives: DE c=9439 ($50) · FR c=9566 ($60, pays more than Oasis -> 1st switch).
 */
(function () {
  "use strict";

  var OASIS = { base: "https://trkc115.com/c", p: "P4016" };
  var BLITZ = { base: "https://bikiraibn.com/", a: "2397" };

  // ---- capture inbound click-ids ONCE (first-touch) ----
  var TRACK_KEYS = ["gclid", "fbclid", "ttclid", "msclkid", "utm_source", "utm_campaign", "utm_medium", "s1", "s2", "s3"];
  function captureClickIds() {
    try {
      var q = new URLSearchParams(location.search);
      var store = JSON.parse(localStorage.getItem("jx_track") || "{}");
      TRACK_KEYS.forEach(function (k) { var v = q.get(k); if (v && !store[k]) store[k] = v; });
      if (!store._ts) store._ts = Date.now();
      if (!store._lp) store._lp = location.pathname;
      localStorage.setItem("jx_track", JSON.stringify(store));
    } catch (e) {}
  }
  captureClickIds();
  function getTrack() { try { return JSON.parse(localStorage.getItem("jx_track") || "{}"); } catch (e) { return {}; } }

  // ---- build the outbound affiliate URL (call at click time) ----
  function buildOfferUrl() {
    var g = window.GEO || {};
    var t = getTrack();
    var clickid = t.gclid || t.fbclid || t.ttclid || t.msclkid || "";
    var net = g.net || "oasis";
    var u;
    if (net === "blitz") {
      u = new URL(BLITZ.base);
      u.searchParams.set("a", BLITZ.a);
      if (g.bc) u.searchParams.set("c", g.bc);
      u.searchParams.set("s1", g.s2tag || ("jx-" + (g.code || "xx")));
      if (clickid) u.searchParams.set("s2", clickid);
    } else { // oasis (default)
      u = new URL(OASIS.base);
      u.searchParams.set("p", OASIS.p);
      if (g.o) u.searchParams.set("o", g.o);
      if (g.cr) u.searchParams.set("cr", g.cr);
      u.searchParams.set("s2", g.s2tag || ("jx-" + (g.code || "xx")));
      if (clickid) u.searchParams.set("s3", clickid);
    }
    return u.toString();
  }

  // ---- visitor geo for the live feed (keyless ipwho.is -> geojs -> page default) ----
  function getGeo() {
    return new Promise(function (resolve) {
      try {
        var cached = JSON.parse(localStorage.getItem("jx_geo") || "null");
        if (cached && cached.cc) return resolve(cached);
      } catch (e) {}
      var def = { cc: (window.GEO && window.GEO.cc) || "US", city: null };
      var done = false;
      function finish(geo) { if (done) return; done = true; try { localStorage.setItem("jx_geo", JSON.stringify(geo)); } catch (e) {} resolve(geo); }
      var timer = setTimeout(function () { finish(def); }, 3000);
      function tryGeojs() {
        fetch("https://get.geojs.io/v1/ip/geo.json", { cache: "no-store" })
          .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
          .then(function (d) { clearTimeout(timer); finish({ cc: (d && d.country_code) || def.cc, city: (d && d.city) || null }); })
          .catch(function () { clearTimeout(timer); finish(def); });
      }
      fetch("https://ipwho.is/", { cache: "no-store" })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
        .then(function (d) { if (d && d.success !== false && d.country_code) { clearTimeout(timer); finish({ cc: d.country_code, city: d.city || null }); } else tryGeojs(); })
        .catch(tryGeojs);
    });
  }

  window.JETTERIX = { buildOfferUrl: buildOfferUrl, getGeo: getGeo, getTrack: getTrack };
})();
