document.documentElement.classList.add("js");

(() => {
  const productButtons = Array.from(document.querySelectorAll("[data-product-target]"));
  const productPanels = Array.from(document.querySelectorAll("[data-product-panel]"));

  function selectProduct(productId) {
    productButtons.forEach((button) => {
      const selected = button.dataset.productTarget === productId;
      button.setAttribute("aria-pressed", String(selected));
    });
    productPanels.forEach((panel) => {
      const selected = panel.dataset.productPanel === productId;
      panel.classList.toggle("active", selected);
      panel.hidden = !selected;
    });
  }

  productButtons.forEach((button) => {
    button.addEventListener("click", () => {
      selectProduct(button.dataset.productTarget);
      if (window.history.replaceState) {
        window.history.replaceState(null, "", `#${button.dataset.productTarget}`);
      }
    });
  });

  if (productPanels.length) {
    const requested = window.location.hash.slice(1);
    const valid = productPanels.some((panel) => panel.dataset.productPanel === requested);
    selectProduct(valid ? requested : productPanels[0].dataset.productPanel);
  }

  document.querySelectorAll("[data-filter-group]").forEach((group) => {
    const groupName = group.dataset.filterGroup;
    const buttons = Array.from(group.querySelectorAll("[data-filter]"));
    const items = Array.from(document.querySelectorAll(`[data-${groupName}-product]`));
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        const filter = button.dataset.filter;
        buttons.forEach((item) => {
          item.setAttribute("aria-pressed", String(item === button));
        });
        items.forEach((item) => {
          const visible = filter === "all" || item.getAttribute("data-" + groupName + "-product") === filter;
          item.classList.toggle("is-hidden", !visible);
        });
      });
    });
  });

  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector(".nav-links");
  if (navToggle && navLinks) {
    const close = () => {
      navLinks.classList.remove("open");
      navToggle.setAttribute("aria-expanded", "false");
    };
    navToggle.addEventListener("click", () => {
      const expanded = navToggle.getAttribute("aria-expanded") === "true";
      navToggle.setAttribute("aria-expanded", String(!expanded));
      navLinks.classList.toggle("open", !expanded);
    });
    navLinks.querySelectorAll("a").forEach((link) => link.addEventListener("click", close));
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape") close();
    });
    document.addEventListener("click", (event) => {
      if (!navLinks.contains(event.target) && !navToggle.contains(event.target)) close();
    });
  }
})();
