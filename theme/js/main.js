// 返回顶端按钮功能
(function() {
    'use strict';

    // 创建返回顶端按钮
    function createBackToTopButton() {
        const backToTop = document.createElement('a');
        backToTop.href = '#';
        backToTop.className = 'back-to-top hidden';
        backToTop.innerHTML = '↑';
        backToTop.setAttribute('aria-label', '返回顶部');

        document.body.appendChild(backToTop);

        // 滚动事件监听
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTop.classList.remove('hidden');
            } else {
                backToTop.classList.add('hidden');
            }
        });

        // 点击事件
        backToTop.addEventListener('click', function(e) {
            e.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // 页面加载完成后初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', createBackToTopButton);
    } else {
        createBackToTopButton();
    }
})();