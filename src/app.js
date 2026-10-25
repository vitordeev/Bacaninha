const tabs = [...document.querySelectorAll('[data-category]')];
function selectCategory(tab) {
const category = window.BACANINHA_CATALOGO[tab.dataset.category];
tabs.forEach(item => { const selected = item === tab; item.setAttribute('aria-selected', String(selected)); item.tabIndex = selected ? 0 : -1; });
document.getElementById('panel').setAttribute('aria-labelledby', tab.id);
document.getElementById('menu-title').textContent = category.title;
document.getElementById('menu-description').textContent = category.description;
document.getElementById('flavors').replaceChildren(...category.items.map(name => {const li = document.createElement('li'); li.textContent = name; return li;}));
}
tabs.forEach((tab,index) => {
tab.addEventListener('click', () => selectCategory(tab));
tab.addEventListener('keydown', event => {
let next;
if(event.key==='ArrowRight') next=(index+1)%tabs.length;
if(event.key==='ArrowLeft') next=(index+tabs.length-1)%tabs.length;
if(event.key==='Home') next=0;
if(event.key==='End') next=tabs.length-1;
if(next!==undefined){event.preventDefault();selectCategory(tabs[next]);tabs[next].focus();}
});
});
selectCategory(tabs[0]);
document.getElementById('year').textContent = new Date().getFullYear();
