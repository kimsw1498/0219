function switchTab(e, tabId) {
    document.querySelectorAll('.content-view').forEach(v => v.classList.remove('active'));
    document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
    
    document.getElementById(tabId).classList.add('active');
    e.currentTarget.classList.add('active');
    
    document.getElementById('main-scroll').scrollTop = 0;
}