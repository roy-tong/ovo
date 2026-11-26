const stage = document.querySelector('.stage');
if (stage) {
  const buttons = stage.querySelectorAll('[data-select]');
  const plates = stage.querySelectorAll('[data-plate]');
  buttons.forEach((button) => button.addEventListener('click', () => {
    buttons.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    plates.forEach((plate) => { plate.hidden = plate.dataset.plate !== button.dataset.select; });
  }));
  const motion = matchMedia('(prefers-reduced-motion: no-preference) and (pointer: fine)');
  stage.addEventListener('pointermove', (event) => {
    if (!motion.matches) return;
    const box = stage.getBoundingClientRect();
    stage.style.setProperty('--x', (0.5 - (event.clientY - box.top) / box.height) * 12 + 'deg');
    stage.style.setProperty('--y', ((event.clientX - box.left) / box.width - 0.5) * 16 + 'deg');
  });
  stage.addEventListener('pointerleave', () => {
    stage.style.removeProperty('--x');
    stage.style.removeProperty('--y');
  });
}
const filters = document.querySelectorAll('[data-filter]');
function applyFilter(value) {
  filters.forEach((button) => button.setAttribute('aria-pressed', String(button.dataset.filter === value)));
  document.querySelectorAll('[data-item]').forEach((item) => {
    item.hidden = value !== 'all' && item.dataset.item !== value;
  });
}
filters.forEach((button) => button.addEventListener('click', () => applyFilter(button.dataset.filter)));
window.addEventListener('hashchange', () => {
  const target = document.getElementById(location.hash.slice(1));
  if (target && target.hidden && target.dataset.item) {
    applyFilter('all');
    target.scrollIntoView();
  }
});
if ('IntersectionObserver' in window && matchMedia('(prefers-reduced-motion:no-preference)').matches) {
  const observer = new IntersectionObserver((entries) => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('entered');
      observer.unobserve(entry.target);
    }
  });
  document.querySelectorAll('.product,.case,.quick,.essay').forEach((item) => observer.observe(item));
}
document.documentElement.classList.add('enhanced');
document.querySelectorAll('.simulation').forEach((demo) => {
  const choices = demo.querySelectorAll('button');
  const output = demo.querySelector('output');
  choices.forEach((choice) => choice.addEventListener('click', () => {
    choices.forEach((button) => button.setAttribute('aria-pressed', String(button === choice)));
    output.textContent = choice.dataset.result;
  }));
});
