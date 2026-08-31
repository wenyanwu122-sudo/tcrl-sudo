(function () {
  function langInfo() {
    var path = window.location.pathname;
    if (path.indexOf('/en/main/') !== -1) {
      return { lang: 'en', base: path.split('/en/main/')[0] + '/en/main/' };
    }
    if (path.indexOf('/zh/main/') !== -1) {
      return { lang: 'zh', base: path.split('/zh/main/')[0] + '/zh/main/' };
    }
    return { lang: 'zh', base: '/zh/main/' };
  }

  function navItems(lang) {
    if (lang === 'en') {
      return [
        { text: 'Overview', href: 'index.html' },
        { text: 'Tinker SDK', href: 'imported/tinker.html' },
        { text: 'Quick Start', href: 'imported/tinker__quickstart.html' },
        { text: 'Models', href: 'imported/tinker__models.html' },
        { text: 'Loss Functions', href: 'imported/tinker__losses.html' },
        { text: 'CLI', href: 'imported/tinker__cli.html' },
        { text: 'API Reference', href: 'imported/tinker__api-reference.html' },
        { text: 'Cookbook', href: 'imported/cookbook.html' }
      ];
    }
    return [
      { text: '概览', href: 'index.html' },
      { text: 'Tinker SDK', href: 'imported/tinker.html' },
      { text: '快速开始', href: 'imported/tinker__quickstart.html' },
      { text: '模型', href: 'imported/tinker__models.html' },
      { text: 'Loss Functions', href: 'imported/tinker__losses.html' },
      { text: 'CLI 参考', href: 'imported/tinker__cli.html' },
      { text: 'API 参考', href: 'imported/tinker__api-reference.html' },
      { text: 'Cookbook', href: 'imported/cookbook.html' }
    ];
  }

  function normalize(path) {
    return path.replace(/\/index\.html$/, '/').replace(/\.html$/, '').replace(/\/$/, '');
  }

  function mountLeftNav() {
    if (document.querySelector('.tcrl-leftnav')) return;
    var info = langInfo();
    var nav = document.createElement('aside');
    nav.className = 'tcrl-leftnav';
    nav.setAttribute('aria-label', info.lang === 'en' ? 'Primary navigation' : '一级导航');

    var title = document.createElement('div');
    title.className = 'tcrl-leftnav-title';
    title.textContent = info.lang === 'en' ? 'Navigation' : '章节导航';
    nav.appendChild(title);

    var list = document.createElement('ul');
    list.className = 'tcrl-leftnav-list';
    var current = normalize(window.location.pathname);
    navItems(info.lang).forEach(function (item) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      var absolutePath = info.base + item.href;
      a.href = absolutePath;
      a.textContent = item.text;
      if (current === normalize(absolutePath) || current.indexOf(normalize(absolutePath) + '/') === 0) {
        a.className = 'active';
      }
      li.appendChild(a);
      list.appendChild(li);
    });
    nav.appendChild(list);
    document.body.appendChild(nav);
    document.body.classList.add('tcrl-has-leftnav');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', mountLeftNav);
  } else {
    mountLeftNav();
  }
})();
