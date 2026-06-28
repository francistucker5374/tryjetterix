/* Jetterix — page behaviour: scroll-reveal, deadline, scarcity, live feed, exit catch, store hand-off. */
(function () {
  "use strict";
  var GEO = window.GEO || {};
  var TXT = GEO.i18n || {};
  var pick = function (a) { return a[Math.floor(Math.random() * a.length)]; };
  var qs = function (sel, root) { return (root || document).querySelector(sel); };
  var qsa = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

  /* ---- scroll reveal (with a no-scroll safety net) ---- */
  (function reveal() {
    var items = qsa(".reveal");
    if (!("IntersectionObserver" in window)) { items.forEach(function (n) { n.classList.add("in"); }); return; }
    var seen = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); seen.unobserve(e.target); } });
    }, { threshold: 0.12 });
    items.forEach(function (n) { seen.observe(n); });
    setTimeout(function () { items.forEach(function (n) { n.classList.add("in"); }); }, 4200);
  })();

  /* ---- rolling deadline (12-minute window, persisted) ---- */
  var SPAN = 12 * 60 * 1000;
  function deadline() {
    var end = +localStorage.getItem("jx_deadline");
    if (!end || end < Date.now()) { end = Date.now() + SPAN; localStorage.setItem("jx_deadline", end); }
    return end;
  }
  var endAt = deadline();
  function paintClock() {
    var ms = Math.max(0, endAt - Date.now());
    var mm = Math.floor(ms / 60000), ss = Math.floor((ms % 60000) / 1000);
    var label = (mm < 10 ? "0" : "") + mm + ":" + (ss < 10 ? "0" : "") + ss;
    qsa("[data-cd]").forEach(function (n) { n.textContent = label; });
    qsa("[data-mcd]").forEach(function (n) { n.textContent = label; });
    if (ms <= 0) { endAt = Date.now() + SPAN; localStorage.setItem("jx_deadline", endAt); }
  }
  paintClock(); setInterval(paintClock, 1000);

  /* ---- scarcity: live unit count + offer-side stock ---- */
  var atPrice = +localStorage.getItem("jx_left") || (5 + Math.floor(Math.random() * 7));   // 5-11
  function paintAtPrice() { qsa("[data-stock]").forEach(function (n) { n.textContent = atPrice; }); }
  paintAtPrice();
  setInterval(function () { if (atPrice > 2 && Math.random() < 0.18) { atPrice--; localStorage.setItem("jx_left", atPrice); paintAtPrice(); } }, 12000);

  var units = +localStorage.getItem("jx_units") || (33 + Math.floor(Math.random() * 11));   // 33-43
  function paintUnits() {
    qsa("[data-stock2]").forEach(function (n) { n.textContent = units; });
    var pct = Math.max(7, Math.min(24, units / 2.6));
    qsa("[data-stockbar]").forEach(function (n) { n.style.width = pct + "%"; });
  }
  paintUnits();
  setInterval(function () { if (units > 6 && Math.random() < 0.2) { units--; localStorage.setItem("jx_units", units); paintUnits(); } }, 10000);

  var watching = 17 + Math.floor(Math.random() * 28);
  function paintWatching() { qsa("[data-viewers]").forEach(function (n) { n.textContent = watching; }); }
  paintWatching();
  setInterval(function () { watching += (Math.random() < 0.5 ? -1 : 2); if (watching < 9) watching = 9; paintWatching(); }, 4500);

  /* ---- sticky buy bar ---- */
  var dock = qs(".buybar");
  if (dock) addEventListener("scroll", function () { dock.classList.toggle("show", scrollY > innerHeight * 0.6); }, { passive: true });

  /* ---- language menu ---- */
  var langMenu = qs(".lang");
  if (langMenu) {
    qs(".lang button").addEventListener("click", function (e) { e.stopPropagation(); langMenu.classList.toggle("open"); });
    document.addEventListener("click", function () { langMenu.classList.remove("open"); });
  }

  /* ---- FAQ accordion ---- */
  qsa(".faq-item").forEach(function (item) {
    qs(".faq-q", item).addEventListener("click", function () {
      var open = item.classList.toggle("open");
      var ans = qs(".faq-a", item);
      ans.style.maxHeight = open ? ans.scrollHeight + "px" : 0;
    });
  });

  /* ---- store hand-off overlay -> affiliate DTC ---- */
  var handingOff = false;
  function toStore() {
    if (handingOff) return; handingOff = true;
    var pop = qs("#exitpop"); if (pop) pop.classList.remove("show");
    var ov = qs("#handoff"); if (ov) ov.classList.add("show");
    var dest = (window.JETTERIX && window.JETTERIX.buildOfferUrl && window.JETTERIX.buildOfferUrl()) || "https://trkc115.com/c?p=P4016&o=O6887&cr=10810";
    var nav = function () { try { window.location.href = dest; } catch (e) { try { window.location.assign(dest); } catch (e2) {} } };
    setTimeout(nav, 680);
    setTimeout(function () { if (!document.hidden) nav(); }, 3600);
  }
  document.addEventListener("click", function (e) {
    var hit = e.target.closest(".js-cta"); if (!hit) return;
    e.preventDefault(); toStore();
  });

  /* ---- auto-advance after engagement (never for bots / pre-interaction) ---- */
  if (!navigator.webdriver) {
    var armed = false;
    var arm = function () {
      if (armed) return; armed = true;
      setTimeout(function () { if (!document.hidden && !handingOff) toStore(); }, 28000);
    };
    ["scroll", "mousemove", "touchstart", "keydown", "pointerdown"].forEach(function (ev) {
      addEventListener(ev, arm, { once: true, passive: true });
    });
  }

  /* ---- live social-proof feed ---- */
  var feed = qs("#livefeed");
  if (feed && window.JETTERIX) {
    window.JETTERIX.getGeo().then(function (loc) {
      var cities = GEO.cities || ["London"];
      var names = GEO.names || ["Alex M."];
      var bundles = TXT.products || ["the 2-pack"];
      var line = TXT.tpl || "<b>{name}</b> in {city} just ordered {product}";
      var shown = 0;
      function ago(min) { return min <= 1 ? (TXT.ago_just || "just now") : (TXT.ago_min || "{n} min ago").replace("{n}", min); }
      function render() {
        var city = (loc.city && Math.random() < 0.4) ? loc.city : pick(cities);
        var body = line.replace("{name}", "<b>" + pick(names) + "</b>").replace("{city}", city).replace("{product}", pick(bundles));
        var min = 1 + Math.floor(Math.random() * 26);
        return '<img src="' + (GEO.thumb || "") + '" alt="">' +
               '<div class="lf-body">' + body + '<span class="lf-ago">✔ ' + (TXT.verified || "Verified") + " · " + ago(min) + "</span></div>" +
               '<span class="lf-x" aria-label="close">×</span>';
      }
      function tick() {
        if (shown++ >= 14) return;
        if (!document.hidden) {
          feed.innerHTML = render();
          feed.classList.add("show");
          qs(".lf-x", feed).addEventListener("click", function () { feed.classList.remove("show"); });
          setTimeout(function () { feed.classList.remove("show"); }, 5200);
        }
        setTimeout(tick, 8000 + Math.random() * 12000);
      }
      setTimeout(tick, 5000);
    });
  }

  /* ---- exit catch (cursor-out + back-button) ---- */
  var exitPop = qs("#exitpop");
  function openExit() {
    if (!exitPop || sessionStorage.getItem("jx_seen")) return;
    sessionStorage.setItem("jx_seen", "1");
    exitPop.classList.add("show");
  }
  if (exitPop) {
    document.addEventListener("mouseout", function (e) { if (e.clientY <= 0 && !e.relatedTarget) openExit(); });
    try {
      history.pushState(null, "", location.href);
      addEventListener("popstate", function () {
        if (!sessionStorage.getItem("jx_seen")) { openExit(); history.pushState(null, "", location.href); }
      });
    } catch (e) {}
    qsa("[data-close-exit]", exitPop).forEach(function (b) { b.addEventListener("click", function () { exitPop.classList.remove("show"); }); });
    exitPop.addEventListener("click", function (e) { if (e.target === exitPop) exitPop.classList.remove("show"); });
  }
})();
