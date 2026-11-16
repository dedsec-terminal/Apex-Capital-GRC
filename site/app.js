fetch('../data/register.json').then(response=>{
  if(!response.ok) throw new Error('Register unavailable');
  return response.json();
}).then(data=>{
  const riskGrid=document.querySelector('#risk-grid');
  data.risks.forEach(risk=>{
    const card=document.createElement('article'); card.className='risk-card';
    const top=document.createElement('div'); top.className='risk-top';
    const id=document.createElement('span'); id.className='risk-id'; id.textContent=risk.id;
    const badge=document.createElement('span'); badge.className=`badge ${risk.rating.toLowerCase()}`; badge.textContent=risk.rating;
    const title=document.createElement('h3'); title.textContent=risk.title;
    const meta=document.createElement('div'); meta.className='risk-meta'; meta.append('Scenario score ');
    const score=document.createElement('b'); score.textContent=risk.inherentScore; meta.append(score,' / 25 · Inherent');
    top.append(id,badge); card.append(top,title,meta); riskGrid.append(card);
  });
  const testList=document.querySelector('#test-list');
  data.tests.forEach(test=>{
    const row=document.createElement('div'); row.className='test-row';
    const id=document.createElement('span'); id.className='test-number'; id.textContent=test.id;
    const title=document.createElement('span'); title.textContent=test.title;
    const status=document.createElement('span'); status.className='test-state'; status.textContent='PLANNED';
    row.append(id,title,status); testList.append(row);
  });
}).catch(()=>{
  document.querySelector('#risk-grid').textContent='Risk register data could not be loaded.';
  document.querySelector('#test-list').textContent='Test register data could not be loaded.';
});
