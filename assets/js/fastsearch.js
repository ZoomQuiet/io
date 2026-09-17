import * as params from '@params';

const INDEX_URL = '/index.json';
const resList = document.getElementById('searchResults');
const sInput = document.getElementById('searchInput');
const searchBox = document.getElementById('searchbox');
const searchStatus = document.getElementById('searchStatus');

let fuse;
let currentElement = null;
let firstResult = null;
let lastResult = null;

const defaultFuseOptions = {
    distance: 100,
    threshold: 0.4,
    ignoreLocation: true,
    keys: ['title', 'permalink', 'summary', 'content']
};

const buildFuseOptions = () => {
    if (!params.fuseOpts) {
        return defaultFuseOptions;
    }

    const minMatchCharLength = params.fuseOpts.minmatchcharlength;
    return {
        isCaseSensitive: params.fuseOpts.iscasesensitive ?? false,
        includeScore: params.fuseOpts.includescore ?? false,
        includeMatches: params.fuseOpts.includematches ?? false,
        minMatchCharLength: minMatchCharLength == null || minMatchCharLength < 1 ? 1 : minMatchCharLength,
        shouldSort: params.fuseOpts.shouldsort ?? true,
        findAllMatches: params.fuseOpts.findallmatches ?? false,
        keys: params.fuseOpts.keys ?? defaultFuseOptions.keys,
        location: params.fuseOpts.location ?? 0,
        threshold: params.fuseOpts.threshold ?? defaultFuseOptions.threshold,
        distance: params.fuseOpts.distance ?? defaultFuseOptions.distance,
        ignoreLocation: params.fuseOpts.ignorelocation ?? defaultFuseOptions.ignoreLocation
    };
};

const debounce = (fn, delay) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = window.setTimeout(() => fn(...args), delay);
    };
};

const setSearchStatus = (message, visible = true) => {
    if (!searchStatus) {
        return;
    }
    searchStatus.textContent = message;
    searchStatus.hidden = !visible;
};

const reset = () => {
    currentElement = null;
    firstResult = null;
    lastResult = null;

    resList.innerHTML = '';
    sInput.value = '';
    sInput.focus();
};

const setActiveResult = (element) => {
    document.querySelectorAll('.focus').forEach((item) => item.classList.remove('focus'));
    if (!element) {
        return;
    }

    element.focus();
    element.parentElement?.classList.add('focus');
    currentElement = element;
};

const renderResults = (results) => {
    if (!Array.isArray(results) || results.length === 0) {
        resList.innerHTML = '';
        firstResult = null;
        lastResult = null;
        currentElement = null;
        return;
    }

    const fragment = document.createDocumentFragment();
    for (const result of results) {
        const li = document.createElement('li');
        const title = document.createTextNode(result.item.title);
        const icon = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        icon.setAttribute('width', '24');
        icon.setAttribute('height', '24');
        icon.setAttribute('viewBox', '0 0 24 24');
        icon.setAttribute('fill', 'none');
        icon.setAttribute('stroke', 'currentColor');
        icon.setAttribute('stroke-width', '2');
        icon.setAttribute('stroke-linecap', 'round');
        icon.setAttribute('stroke-linejoin', 'round');
        icon.classList.add('feather', 'feather-chevrons-right');
        icon.innerHTML = '<polyline points="13 17 18 12 13 7"></polyline><polyline points="6 17 11 12 6 7"></polyline>';

        const link = document.createElement('a');
        link.className = 'entry-link';
        link.href = result.item.permalink;
        link.setAttribute('aria-label', result.item.title);

        li.appendChild(title);
        li.appendChild(icon);
        li.appendChild(link);
        fragment.appendChild(li);
    }

    resList.innerHTML = '';
    resList.appendChild(fragment);
    firstResult = resList.firstElementChild;
    lastResult = resList.lastElementChild;
};

const performSearch = () => {
    if (!fuse) {
        return;
    }

    const query = sInput.value.trim();
    if (!query) {
        renderResults([]);
        return;
    }

    const searchOptions = params.fuseOpts?.limit ? { limit: params.fuseOpts.limit } : undefined;
    const results = searchOptions ? fuse.search(query, searchOptions) : fuse.search(query);
    renderResults(results);
};

const initSearch = async () => {
    if (!sInput || !resList) {
        return;
    }

    setSearchStatus('正在加载搜索索引…');

    try {
        const response = await fetch(INDEX_URL);
        if (!response.ok) {
            throw new Error(`Search index load failed: ${response.status}`);
        }

        const data = await response.json();
        if (!Array.isArray(data) || data.length === 0) {
            throw new Error('Search index is empty');
        }

        fuse = new Fuse(data, buildFuseOptions());
        setSearchStatus('', false);

        if (sInput.value.trim()) {
            performSearch();
        }
    } catch (error) {
        console.error(error);
        setSearchStatus('搜索索引加载失败，请刷新页面后重试。');
    } finally {
        sInput.disabled = false;
        sInput.focus();
    }
};

window.addEventListener('DOMContentLoaded', initSearch);

sInput?.addEventListener('input', debounce(performSearch, 150));

sInput?.addEventListener('search', () => {
    if (!sInput.value) {
        reset();
    }
});

document.addEventListener('keydown', (event) => {
    const { key } = event;
    const activeElement = document.activeElement;
    const isInsideSearchBox = searchBox?.contains(activeElement);

    if (key === 'Escape') {
        reset();
        return;
    }

    if (!firstResult || !isInsideSearchBox) {
        return;
    }

    if (key === 'ArrowDown') {
        event.preventDefault();
        if (activeElement === sInput) {
            setActiveResult(firstResult.querySelector('.entry-link'));
        } else if (activeElement?.parentElement !== lastResult) {
            setActiveResult(activeElement?.parentElement?.nextElementSibling?.querySelector('.entry-link'));
        }
    } else if (key === 'ArrowUp') {
        event.preventDefault();
        if (activeElement?.parentElement === firstResult) {
            setActiveResult(sInput);
        } else if (activeElement !== sInput) {
            setActiveResult(activeElement?.parentElement?.previousElementSibling?.querySelector('.entry-link'));
        }
    } else if (key === 'ArrowRight' && activeElement?.matches?.('.entry-link')) {
        activeElement.click();
    }
});
