---
layout: page
title: "Loan Comparison"
---
<section>
<h2>Loan Comparison</h2>
<p class="lead">대출 상품을 비교하고 20개씩 페이지로 탐색하세요.</p>

<div class="card">
  <div class="input-row">
    <label>금리 범위</label>
    <input id="rateMin" class="input" placeholder="최소(%)" type="number" />
    <input id="rateMax" class="input" placeholder="최대(%)" type="number" />
    <select id="loanType" class="input"><option value=''>전체</option><option value='credit'>신용</option><option value='mortgage'>담보</option></select>
    <button class="btn btn-primary" id="applyFilters">필터 적용</button>
  </div>

  <div id="loanList"></div>
  <div id="pagination" class="pagination"></div>
</div>

<div class="card" style="margin-top:12px;">
  <h3>금리 분포</h3>
  <canvas id="rateHistogram" style="height:220px;"></canvas>
</div>

</section>

<script>
(function(){
  // demo loans
  let loans = [];
  for(let i=0;i<150;i++){
    loans.push({id:'L'+i, name:'은행 '+(i%10+1)+' 상품 '+(i+1), rate: +(Math.random()*5+1).toFixed(2), type: i%2? 'credit':'mortgage', score: +(Math.random()*100).toFixed(1)});
  }
  const perPage=20; let curPage=1; let filtered = loans.slice();
  const loanList = document.getElementById('loanList');
  const pagination = document.getElementById('pagination');

  function render(){
    const start=(curPage-1)*perPage;
    const subset = filtered.slice(start, start+perPage);
    loanList.innerHTML = subset.map(l=>`<div class="link-card"><div style="display:flex;justify-content:space-between;"><div><strong>${l.name}</strong><div class="muted">유형: ${l.type}</div></div><div style="text-align:right"><div style="color:var(--casa-nova-primary);font-weight:800">${l.rate}%</div><div class="muted">${l.score} pts</div><div style="margin-top:6px"><button class="btn btn-outline" onclick="alert('선택: ${l.name}')">선택</button></div></div></div></div>`).join('');
    CasaNova.renderPagination(pagination, filtered.length, perPage, curPage, (p)=>{ curPage=p; render(); });
    renderHistogram();
  }
  function applyFilters(){
    const min = parseFloat(document.getElementById('rateMin').value) || 0;
    const max = parseFloat(document.getElementById('rateMax').value) || 100;
    const type = document.getElementById('loanType').value;
    filtered = loans.filter(l=> l.rate>=min && l.rate<=max && (type? l.type===type:true));
    curPage=1; render();
  }
  document.getElementById('applyFilters').onclick = applyFilters;

  function renderHistogram(){
    const ctx = document.getElementById('rateHistogram');
    const data = filtered.map(f=>f.rate);
    if(window._rateChart) window._rateChart.destroy();
    window._rateChart = CasaNova.createChart(ctx, 'bar', {
      labels: data.map((_,i)=>i+1),
      datasets:[{label:'금리', data, backgroundColor:'rgba(0,102,204,0.6)'}]
    });
  }

  render();
})();
</script>
