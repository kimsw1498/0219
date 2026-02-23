function switchTab(e, tabId) {
    document.querySelectorAll('.content-view').forEach(v => v.classList.remove('active'));
    document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
    
    const target = document.getElementById(tabId);
    if(target) target.classList.add('active');
    
    e.currentTarget.classList.add('active');
    document.getElementById('main-scroll').scrollTop = 0;
}