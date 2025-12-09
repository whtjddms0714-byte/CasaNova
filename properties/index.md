---
layout: page
title: "Properties"
---
<section>
<h2>Property Recommendations</h2>
<p class="lead">당신의 예산과 선호를 반영한 추천 매물 목록입니다.</p>

<div class="card">
  <div id="summaryBar" class="card" style="background:var(--casa-nova-secondary); padding:12px;">
    <div><strong>총 구매 가능 금액:</strong> <span id="totalBudget">₩500,000,000</span></div>
    <div><strong>선택 지역:</strong> <span id="chosenRegion">강남구</span></div>
    <div><strong>최우선:</strong> <span id="topPref">교통</span></div>
  </div>

  <div id="propList" style="margin-top:12px;"></div>
</div>

</section>

<script>
(function(){
  const listings = Array.from({length:30}, (_,i)=>({
    id:'P'+i,
    price: Math.floor(300 + Math.random()*300)*1000000,
    addr:'강남구 예시동 '+(i+1),
    score: +(Math.random()*100).toFixed(1),
    distances:{subway:Math.ceil(Math.random()*15), park:Math.ceil(Math.random()*20)}
  }));
  const propList = document.getElementById('propList');
  propList.innerHTML = listings.map(l=>(
    '<div class="link-card" style="margin-bottom:8px; display:flex; justify-content:space-between; align-items:center;">'
    + '<div><strong>'+l.addr+'</strong><div class="muted">'+l.score+' pts</div></div>'
    + '<div style="text-align:right">'
    + '<div style="color:var(--casa-nova-primary); font-weight:800">'+(CasaNova.formatKRW(l.price))+'</div>'
    + '<div class="small">지하철 '+l.distances.subway+'분</div>'
    + '<div style="margin-top:6px"><button class="btn btn-outline" onclick="alert(\'지도 보기: '+l.addr+'\')">지도에서 보기</button></div>'
    + '</div></div>'
  )).join('');
})();
</script>
const form = document.getElementById("user-form");
  const errorBox = document.getElementById("error-message");
  const priorityList = document.getElementById("priority-list");
  const skipLoanButton = document.getElementById("skip-loan");

  // ----------------------------------------------------
  // 드래그 앤 드롭 로직 (간단 구현)
  // ----------------------------------------------------
  let draggingItem = null;

  priorityList.addEventListener("dragstart", (e) => {
    if (e.target.classList.contains('priority-item')) {
      draggingItem = e.target;
      setTimeout(() => e.target.classList.add('dragging'), 0);
    }
  });

  priorityList.addEventListener("dragend", (e) => {
    e.target.classList.remove('dragging');
    draggingItem = null;
    // 드래그가 끝났을 때 순위 번호 업데이트
    updatePriorityRanks();
  });

  priorityList.addEventListener("dragover", (e) => {
    e.preventDefault();
    if (draggingItem) {
      const afterElement = getDragAfterElement(priorityList, e.clientY);
      const currentItem = draggingItem;
      if (afterElement == null) {
        priorityList.appendChild(currentItem);
      } else {
        priorityList.insertBefore(currentItem, afterElement);
      }
    }
  }, false); // useCapture를 false로 설정하여 정상적인 이벤트 흐름 보장

  function getDragAfterElement(container, y) {
    const draggableElements = [...container.querySelectorAll('.priority-item:not(.dragging)')];

    return draggableElements.reduce((closest, child) => {
      const box = child.getBoundingClientRect();
      const offset = y - box.top - box.height / 2;
      if (offset < 0 && offset > closest.offset) {
        return { offset: offset, element: child };
      } else {
        return closest;
      }
    }, { offset: Number.NEGATIVE_INFINITY }).element;
  }
  
  // 순위 번호를 업데이트하는 함수
  function updatePriorityRanks() {
      const items = priorityList.querySelectorAll('.priority-item');
      items.forEach((item, index) => {
          item.querySelector('.priority-rank').textContent = `[${index + 1}]`;
      });
  }


  // ----------------------------------------------------
  // 가중치 계산 로직
  // ----------------------------------------------------
  function getPriorityWeights() {
    const listItems = document.querySelectorAll("#priority-list .priority-item");
    
    // 백엔드에서 요구하는 순서: w_park, w_school, w_mart, w_transport
    const weightsMap = {
        "w_park": 0,
        "w_school": 1,
        "w_mart": 2,
        "w_transport": 3
    };
    
    // [w_park, w_school, w_mart, w_transport] 순서로 저장될 배열 (초기값 0)
    const orderedWeights = [0, 0, 0, 0]; 
    
    // 순위대로 4, 3, 2, 1 가중치 부여
    listItems.forEach((item, index) => {
        const weightValue = 4 - index; // 1위: 4, 4위: 1
        const key = item.getAttribute('data-key'); // data-key (w_park, w_school 등) 읽기
        
        // 올바른 순서대로 가중치를 배열에 삽입
        if (weightsMap.hasOwnProperty(key)) {
             orderedWeights[weightsMap[key]] = weightValue;
        }
    });
    
    return orderedWeights; 
  }

  // ----------------------------------------------------
  // 폼 제출 이벤트 (대출 추천 받고 진행하기)
  // ----------------------------------------------------
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    errorBox.textContent = "";

    const income_monthly = Number(
      document.getElementById("income_monthly").value || 0
    );
    const credit_score = Number(
      document.getElementById("credit_score").value || 0
    );
    const dsr_ratio = Number(document.getElementById("dsr_ratio").value || 0.4);
    const existing_debt = Number(
      document.getElementById("existing_debt").value || 0
    );
    const existing_debt_monthly_payment = Number(
      document.getElementById("existing_debt_monthly_payment").value || 0
    );
    const married = document.getElementById("married").checked;
    const first_job = document.getElementById("first_job").checked;

    const asset = Number(document.getElementById("asset").value || 0);
    const budget_limit_raw = document.getElementById("budget_limit").value;
    const budget_limit = budget_limit_raw ? Number(budget_limit_raw) : null;
    const target_gu = document.getElementById("target_gu").value || "";

    // ⭐️ 드래그 순서에 따른 가중치 계산
    const weights = getPriorityWeights();

    if (!income_monthly || !credit_score) {
      errorBox.textContent = "월 소득과 신용점수는 필수입니다.";
      return;
    }

    const userInfo = {
      income_monthly,
      credit_score,
      dsr_ratio,
      existing_debt,
      existing_debt_monthly_payment,
      married,
      first_job,
      asset,
      budget_limit,
      target_gu,
      // ⭐️ weights 배열 사용
      weights: weights, 
    };

    // localStorage에 저장
    localStorage.setItem("casanova_user_info", JSON.stringify(userInfo));

    // 대출 여부에 따라 분기
    const loanChoice = document.querySelector(
      'input[name="loan_choice"]:checked'
    ).value;

    if (loanChoice === "yes") {
      // 대출 추천 페이지로 이동
      window.location.href = "/loans.html";
    } else {
      // 대출 없이 부동산 추천 → selected_loan_amount = 0으로 설정 후 바로 마지막 페이지로
      localStorage.setItem("casanova_selected_loan_amount", JSON.stringify(0));
      window.location.href = "/properties.html";
    }
  });


  // ----------------------------------------------------
  // 대출 없이 바로 매물 찾기 버튼 로직
  // ----------------------------------------------------
  skipLoanButton.addEventListener("click", () => {
    // 1. 대출 선택을 "no"로 강제 설정
    document.querySelector('input[name="loan_choice"][value="no"]').checked = true;

    // 2. 폼 제출 이벤트 실행 (데이터 저장 및 페이지 이동 로직 실행)
    const submitEvent = new Event('submit', { cancelable: true });
    form.dispatchEvent(submitEvent);
  });