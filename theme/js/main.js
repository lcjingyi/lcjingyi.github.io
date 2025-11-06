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

// 代码块折叠功能
(function() {
    'use strict';

    function enhanceCodeBlocks() {
        const codeBlocks = document.querySelectorAll('.highlight');

        codeBlocks.forEach((codeBlock, index) => {
            // 获取代码语言
            let language = '代码';
            const preElement = codeBlock.querySelector('pre');
            if (preElement) {
                const classNames = preElement.className.split(' ');
                const languageClass = classNames.find(cls => cls.startsWith('language-'));
                if (languageClass) {
                    language = languageClass.replace('language-', '').toUpperCase();
                }
            }

            // 创建折叠头部
            const header = document.createElement('div');
            header.className = 'code-header';
            header.innerHTML = `
                <span class="code-language">${language}</span>
                <button class="code-toggle" aria-label="折叠代码块">
                    <span class="toggle-icon">−</span>
                </button>
            `;

            // 插入头部
            codeBlock.insertBefore(header, codeBlock.firstChild);

            // 添加折叠功能
            const toggleButton = header.querySelector('.code-toggle');
            const preElement = codeBlock.querySelector('pre');

            toggleButton.addEventListener('click', function() {
                const isCollapsed = preElement.classList.contains('collapsed');

                if (isCollapsed) {
                    // 展开
                    preElement.classList.remove('collapsed');
                    toggleButton.querySelector('.toggle-icon').textContent = '−';
                    toggleButton.setAttribute('aria-label', '折叠代码块');
                } else {
                    // 折叠
                    preElement.classList.add('collapsed');
                    toggleButton.querySelector('.toggle-icon').textContent = '+';
                    toggleButton.setAttribute('aria-label', '展开代码块');
                }
            });
        });
    }

    // 页面加载完成后初始化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', enhanceCodeBlocks);
    } else {
        enhanceCodeBlocks();
    }
})();