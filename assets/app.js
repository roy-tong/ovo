const preview = document.querySelector('.task-preview');
if (preview) {
  const buttons = preview.querySelectorAll('[data-select]');
  const panels = preview.querySelectorAll('[data-plate]');
  function selectExample(active) {
    buttons.forEach((button) => button.setAttribute('aria-pressed', String(button === active)));
    panels.forEach((panel) => { panel.hidden = panel.dataset.plate !== active.dataset.select; });
  }
  buttons.forEach((button) => button.addEventListener('click', () => selectExample(button)));
  selectExample(buttons[0]);
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
