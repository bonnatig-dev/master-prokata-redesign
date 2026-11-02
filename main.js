document.documentElement.classList.add('js');
const h=document.querySelector('.hdr');const b=document.querySelector('.burger');
b&&b.addEventListener('click',()=>{const o=h.classList.toggle('open');b.setAttribute('aria-expanded',o)});
const solid=()=>h.classList.toggle('solid',scrollY>40||h.classList.contains('open'));addEventListener('scroll',solid,{passive:true});solid();
// blur-in: 50ms inside group, 100ms between blocks
document.querySelectorAll('[data-g]').forEach(g=>{g.querySelectorAll('[data-r]').forEach((el,i)=>el.style.setProperty('--d',i*50+'ms'))});
document.querySelectorAll('[data-b]').forEach(sec=>{[...sec.children].forEach((blk,j)=>blk.querySelectorAll?.('[data-r]').forEach(el=>{const d=parseInt(el.style.getPropertyValue('--d')||0);el.style.setProperty('--d',(d+j*100)+'ms')}))});
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{rootMargin:'0px 0px -8% 0px'});
document.querySelectorAll('[data-r]').forEach(el=>io.observe(el));
