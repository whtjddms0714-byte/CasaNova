
window.CasaNova = window.CasaNova || {};
CasaNova.formatKRW = function(num){
  if(num==null||isNaN(num)) return '-';
  return '₩'+Number(num).toLocaleString('ko-KR');
};
CasaNova.createChart = function(ctxType, type, data, options){
  const ctx = (typeof ctxType === 'string') ? document.getElementById(ctxType).getContext('2d') : ctxType.getContext('2d');
  return new Chart(ctx, Object.assign({type, data}, options||{}));
};
CasaNova.renderPagination = function(containerEl, totalItems, perPage, curPage, onPage){
  const totalPages = Math.max(1, Math.ceil(totalItems/perPage));
  containerEl.innerHTML = '';
  for(let i=1;i<=totalPages;i++){
    const btn = document.createElement('button');
    btn.textContent = i;
    btn.className = (i===curPage)?'active':'';
    btn.onclick = ()=> onPage(i);
    containerEl.appendChild(btn);
  }
};
