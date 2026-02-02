/**
 * 검색 UI 컴포넌트
 */

import { performSearch, getSuggestions, getPopularSearches } from './search.js';
import { debounce } from './utils.js';

/**
 * 검색 바 초기화
 * @param {string} containerId - 컨테이너 요소 ID
 */
export function initSearchBar(containerId = 'searchContainer') {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = `
        <div class="search-bar">
            <div class="search-input-wrapper">
                <i class="fas fa-search search-icon"></i>
                <input 
                    type="text" 
                    id="searchInput" 
                    class="search-input"
                    placeholder="강의 또는 실습 검색... (예: AI, 프롬프트, Canva)"
                    autocomplete="off"
                />
                <button id="clearSearch" class="clear-search-btn" style="display: none;">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            
            <div class="search-filters">
                <select id="dayFilter" class="filter-select">
                    <option value="">모든 Day</option>
                    <option value="day01">Day 01</option>
                    <option value="day02">Day 02</option>
                    <option value="day03">Day 03</option>
                    <option value="day04">Day 04</option>
                    <option value="day05">Day 05</option>
                    <option value="day06">Day 06</option>
                    <option value="day07">Day 07</option>
                    <option value="day08">Day 08</option>
                </select>
                
                <select id="typeFilter" class="filter-select">
                    <option value="">전체</option>
                    <option value="lecture">강의</option>
                    <option value="practice">실습</option>
                </select>
            </div>
            
            <div id="suggestions" class="suggestions-dropdown" style="display: none;"></div>
        </div>
        
        <div id="popularSearches" class="popular-searches"></div>
        <div id="searchResults" class="search-results"></div>
    `;

    setupSearchListeners();
    displayPopularSearches();
}

/**
 * 검색 이벤트 리스너 설정
 */
function setupSearchListeners() {
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearch');
    const dayFilter = document.getElementById('dayFilter');
    const typeFilter = document.getElementById('typeFilter');

    // 실시간 검색 (디바운스)
    const debouncedSearch = debounce(() => {
        executeSearch();
    }, 300);

    const debouncedSuggestions = debounce(() => {
        showSuggestions();
    }, 200);

    searchInput.addEventListener('input', (e) => {
        const value = e.target.value;
        clearBtn.style.display = value ? 'block' : 'none';

        if (value.length >= 2) {
            debouncedSearch();
            debouncedSuggestions();
        } else {
            clearResults();
            hideSuggestions();
        }
    });

    searchInput.addEventListener('focus', () => {
        if (searchInput.value.length >= 2) {
            showSuggestions();
        }
    });

    searchInput.addEventListener('blur', () => {
        // 약간의 지연을 두어 클릭 이벤트가 먼저 처리되도록
        setTimeout(hideSuggestions, 200);
    });

    clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        clearBtn.style.display = 'none';
        clearResults();
        hideSuggestions();
        displayPopularSearches();
        searchInput.focus();
    });

    dayFilter.addEventListener('change', executeSearch);
    typeFilter.addEventListener('change', executeSearch);
}

/**
 * 검색 실행
 */
function executeSearch() {
    const query = document.getElementById('searchInput').value;
    const dayFilter = document.getElementById('dayFilter').value;
    const typeFilter = document.getElementById('typeFilter').value;

    if (!query || query.trim().length < 2) {
        clearResults();
        return;
    }

    const results = performSearch(query, {
        day: dayFilter,
        type: typeFilter
    });

    displayResults(results, query);
    hidePopularSearches();
}

/**
 * 검색 결과 표시
 * @param {Array} results - 검색 결과
 * @param {string} query - 검색어
 */
function displayResults(results, query) {
    const container = document.getElementById('searchResults');

    if (results.length === 0) {
        container.innerHTML = `
            <div class="no-results">
                <i class="fas fa-search text-gray-400 text-5xl mb-4"></i>
                <h3 class="text-xl font-bold text-gray-700 mb-2">검색 결과가 없습니다</h3>
                <p class="text-gray-500">다른 검색어로 시도해보세요</p>
            </div>
        `;
        return;
    }

    container.innerHTML = `
        <div class="results-header">
            <p class="results-count">
                <strong>${results.length}개</strong>의 결과를 찾았습니다
            </p>
        </div>
        <div class="results-grid">
            ${results.map(item => createResultCard(item)).join('')}
        </div>
    `;
}

/**
 * 검색 결과 카드 생성
 * @param {Object} item - 검색 결과 항목
 * @returns {string} HTML 문자열
 */
function createResultCard(item) {
    const typeIcon = item.type === 'lecture' ? 'fa-book' : 'fa-code';
    const typeText = item.type === 'lecture' ? '강의' : '실습';
    const typeColor = item.type === 'lecture' ? 'blue' : 'purple';

    return `
        <a href="${item.url}" class="result-card">
            <div class="result-header">
                <span class="result-badge ${typeColor}">
                    <i class="fas ${typeIcon}"></i>
                    ${typeText}
                </span>
                <span class="result-day">${item.dayName}</span>
            </div>
            <h3 class="result-title">${item.highlightedTitle}</h3>
            <p class="result-description">${item.description}</p>
            <div class="result-footer">
                <span class="result-link">
                    자세히 보기 <i class="fas fa-arrow-right"></i>
                </span>
            </div>
        </a>
    `;
}

/**
 * 자동완성 제안 표시
 */
function showSuggestions() {
    const query = document.getElementById('searchInput').value;
    if (!query || query.length < 2) {
        hideSuggestions();
        return;
    }

    const suggestions = getSuggestions(query, 5);
    const container = document.getElementById('suggestions');

    if (suggestions.length === 0) {
        hideSuggestions();
        return;
    }

    container.innerHTML = suggestions.map(suggestion => `
        <div class="suggestion-item" data-suggestion="${suggestion}">
            <i class="fas fa-search text-gray-400"></i>
            <span>${suggestion}</span>
        </div>
    `).join('');

    // 제안 클릭 이벤트
    container.querySelectorAll('.suggestion-item').forEach(item => {
        item.addEventListener('click', () => {
            const suggestion = item.dataset.suggestion;
            document.getElementById('searchInput').value = suggestion;
            executeSearch();
            hideSuggestions();
        });
    });

    container.style.display = 'block';
}

/**
 * 자동완성 숨기기
 */
function hideSuggestions() {
    const container = document.getElementById('suggestions');
    if (container) {
        container.style.display = 'none';
    }
}

/**
 * 인기 검색어 표시
 */
function displayPopularSearches() {
    const container = document.getElementById('popularSearches');
    const popularSearches = getPopularSearches();

    container.innerHTML = `
        <div class="popular-searches-section">
            <h3 class="popular-title">
                <i class="fas fa-fire text-orange-500"></i>
                인기 검색어
            </h3>
            <div class="popular-tags">
                ${popularSearches.map((term, index) => `
                    <button class="popular-tag" data-term="${term}">
                        <span class="tag-number">${index + 1}</span>
                        ${term}
                    </button>
                `).join('')}
            </div>
        </div>
    `;

    // 인기 검색어 클릭 이벤트
    container.querySelectorAll('.popular-tag').forEach(tag => {
        tag.addEventListener('click', () => {
            const term = tag.dataset.term;
            document.getElementById('searchInput').value = term;
            executeSearch();
        });
    });

    container.style.display = 'block';
}

/**
 * 인기 검색어 숨기기
 */
function hidePopularSearches() {
    const container = document.getElementById('popularSearches');
    if (container) {
        container.style.display = 'none';
    }
}

/**
 * 검색 결과 초기화
 */
function clearResults() {
    const container = document.getElementById('searchResults');
    if (container) {
        container.innerHTML = '';
    }
}
