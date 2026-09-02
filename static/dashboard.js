document.addEventListener('DOMContentLoaded', function(){
  const toggle = document.getElementById('toggle-cards');
  const stats = document.getElementById('stats');
  const newProduct = document.getElementById('new-product');

  if(toggle && stats){
    toggle.addEventListener('click', ()=>{
      stats.classList.toggle('collapsed');
      if(stats.classList.contains('collapsed')){
        toggle.textContent = 'Show Metrics'
      } else {
        toggle.textContent = 'Hide Metrics'
      }
    })
  }

  if(newProduct){
    newProduct.addEventListener('click', ()=>{
      alert('Open add product form (wireframe).');
    })
  }
});
