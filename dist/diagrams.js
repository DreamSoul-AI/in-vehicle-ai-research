"use strict";

(() => {
  const dialog = document.getElementById("diagram-dialog");
  if (!dialog) return;
  const image = document.getElementById("diagram-view-image");
  const title = document.getElementById("diagram-view-title");
  const label = document.getElementById("diagram-zoom-label");
  const original = document.getElementById("diagram-original");
  const scroll = dialog.querySelector(".diagram-view-scroll");
  let scale = 100;

  function setScale(value) {
    scale = Math.max(50, Math.min(500, value));
    image.style.width = scale + "%";
    label.textContent = scale + "%";
  }

  document.addEventListener("click", (event) => {
    const opener = event.target.closest("[data-diagram-src]");
    if (opener) {
      image.src = opener.dataset.diagramSrc;
      image.alt = opener.dataset.diagramTitle;
      title.textContent = opener.dataset.diagramTitle;
      original.href = opener.dataset.diagramSrc;
      setScale(100);
      dialog.showModal();
      scroll.scrollLeft = 0;
      scroll.scrollTop = 0;
      return;
    }
    const zoom = event.target.closest("[data-diagram-zoom]");
    if (zoom && dialog.open) {
      if (zoom.dataset.diagramZoom === "reset") {
        setScale(100);
        scroll.scrollLeft = 0;
        scroll.scrollTop = 0;
      } else {
        setScale(scale + (zoom.dataset.diagramZoom === "in" ? 25 : -25));
      }
    }
    if (event.target.closest(".diagram-close") && dialog.open) dialog.close();
  });
  dialog.addEventListener("click", (event) => {
    if (event.target !== dialog) return;
    const box = dialog.getBoundingClientRect();
    if (
      event.clientX < box.left || event.clientX > box.right ||
      event.clientY < box.top || event.clientY > box.bottom
    ) dialog.close();
  });
})();
