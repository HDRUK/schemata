document.addEventListener("DOMContentLoaded", function () {
  function applyZoom() {
    document.querySelectorAll(".mermaid svg").forEach(function (svg) {
      if (svg.dataset.zoomReady) return;
      svg.dataset.zoomReady = "true";

      const wrapper = svg.parentElement;
      wrapper.style.cursor = "zoom-in";
      wrapper.title = "Click to expand";

      const hint = document.createElement("div");
      hint.textContent = "click to expand";
      hint.style.cssText =
        "text-align:center;font-size:0.72rem;opacity:0.45;margin-top:4px;font-family:var(--md-text-font,sans-serif)";
      wrapper.insertAdjacentElement("afterend", hint);

      wrapper.addEventListener("click", function () {
        const overlay = document.createElement("div");
        overlay.style.cssText = [
          "position:fixed", "inset:0", "z-index:9999",
          "background:rgba(0,0,0,0.82)",
          "display:flex", "align-items:center", "justify-content:center",
          "cursor:zoom-out", "padding:24px", "box-sizing:border-box",
        ].join(";");

        const clone = svg.cloneNode(true);
        clone.removeAttribute("width");
        clone.removeAttribute("height");
        clone.style.cssText = [
          "max-width:95vw", "max-height:92vh",
          "width:auto", "height:auto",
          "background:#fff", "padding:28px", "border-radius:10px",
          "box-shadow:0 8px 40px rgba(0,0,0,0.5)",
        ].join(";");

        overlay.appendChild(clone);
        document.body.appendChild(overlay);

        function close() { overlay.remove(); }
        overlay.addEventListener("click", close);
        document.addEventListener("keydown", function esc(e) {
          if (e.key === "Escape") { close(); document.removeEventListener("keydown", esc); }
        });
      });
    });
  }

  // Mermaid renders asynchronously — watch for SVGs appearing in the DOM
  const observer = new MutationObserver(applyZoom);
  observer.observe(document.body, { childList: true, subtree: true });
  // Fallback for diagrams already present
  setTimeout(applyZoom, 800);
});
