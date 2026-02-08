import React, { useState, useMemo } from 'react';
import { COURSES, Course, Lecture } from '../data/courses';
import { SEARCH_INDEX, SearchItem } from '../data/searchIndex';

interface LectureModeProps {
    onBack: () => void;
}

const LectureMode: React.FC<LectureModeProps> = ({ onBack }) => {
    const [activeCourseId, setActiveCourseId] = useState<string | null>(null);
    const [selectedLecture, setSelectedLecture] = useState<Lecture & { coursePath: string } | null>(null);

    // Search State
    const [searchQuery, setSearchQuery] = useState('');
    const [isSearchFocused, setIsSearchFocused] = useState(false);

    const toggleCourse = (id: string) => {
        setActiveCourseId(activeCourseId === id ? null : id);
    };

    const handleLectureClick = (course: Course, lecture: Lecture) => {
        setSelectedLecture({ ...lecture, coursePath: course.path });
    };

    // Search Logic
    const searchResults = useMemo(() => {
        if (!searchQuery.trim()) return [];

        const lowerQuery = searchQuery.toLowerCase();
        return SEARCH_INDEX.filter(item =>
            item.lectureTitle.toLowerCase().includes(lowerQuery) ||
            item.content.toLowerCase().includes(lowerQuery)
        ).slice(0, 50); // Limit results
    }, [searchQuery]);

    const handleSearchResultClick = (item: SearchItem) => {
        const course = COURSES.find(c => c.id === item.courseId);
        if (course) {
            const lecture = course.lectures.find(l => l.file === item.file);
            if (lecture) {
                setActiveCourseId(course.id);
                handleLectureClick(course, lecture);
                setSearchQuery(''); // Close search results
                setIsSearchFocused(false);
            }
        }
    };

    const iframeSrc = selectedLecture
        ? `../../${selectedLecture.coursePath}/${selectedLecture.file}`
        : '';

    return (
        <div className="flex w-full h-full bg-gray-900 border-t border-gray-800">
            {/* Sidebar - Course List */}
            <div className="w-80 border-r border-gray-800 bg-gray-950 flex flex-col">
                <div className="p-4 border-b border-gray-800 flex items-center justify-between bg-gray-900">
                    <h2 className="font-bold text-gray-100 flex items-center gap-2">
                        <i className="fas fa-layer-group text-blue-500"></i>
                        전체 강의
                    </h2>
                    <button onClick={onBack} className="text-gray-500 hover:text-white text-xs">
                        <i className="fas fa-times"></i> 닫기
                    </button>
                </div>

                <div className="flex-1 overflow-y-auto p-2 space-y-2 custom-scrollbar relative">
                    {COURSES.map(course => (
                        <div key={course.id} className="rounded-xl overflow-hidden border border-gray-800 bg-gray-900/50">
                            <button
                                onClick={() => toggleCourse(course.id)}
                                className={`w-full px-4 py-3 flex justify-between items-center transition-colors ${activeCourseId === course.id ? 'bg-gray-800 text-white' : 'text-gray-400 hover:bg-gray-800/50 hover:text-gray-200'}`}
                            >
                                <span className="font-bold text-sm truncate pr-2">{course.title}</span>
                                <i className={`fas fa-chevron-down text-xs transform transition-transform ${activeCourseId === course.id ? 'rotate-180 text-blue-500' : ''}`}></i>
                            </button>

                            {activeCourseId === course.id && (
                                <div className="bg-black/20 py-1 border-t border-gray-800">
                                    {course.lectures.map((lecture, idx) => (
                                        <button
                                            key={idx}
                                            onClick={() => handleLectureClick(course, lecture)}
                                            className={`w-full text-left px-5 py-2 text-xs flex items-center gap-2 transition-all border-l-2 ${selectedLecture?.file === lecture.file
                                                    ? 'text-blue-400 bg-blue-500/10 border-blue-500'
                                                    : 'text-gray-500 hover:text-gray-300 hover:bg-white/5 border-transparent'
                                                }`}
                                        >
                                            <i className={`fas ${selectedLecture?.file === lecture.file ? 'fa-play-circle' : 'fa-file-alt'} w-4`}></i>
                                            <span className="truncate">{lecture.title}</span>
                                        </button>
                                    ))}
                                </div>
                            )}
                        </div>
                    ))}
                </div>

                {/* Search Input Area */}
                <div className="p-4 border-t border-gray-800 bg-gray-900 relative">
                    <div className="relative">
                        <i className="fas fa-search absolute left-3 top-1/2 -translate-y-1/2 text-gray-500 text-xs"></i>
                        <input
                            type="text"
                            placeholder="강의 내용 검색..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            onFocus={() => setIsSearchFocused(true)}
                            className="w-full bg-gray-950 border border-gray-700 text-gray-200 text-xs rounded-lg pl-9 pr-8 py-2.5 focus:outline-none focus:border-blue-500 transition-colors"
                        />
                        {searchQuery && (
                            <button
                                onClick={() => setSearchQuery('')}
                                className="absolute right-3 top-1/2 -translate-y-1/2 text-gray-500 hover:text-white"
                            >
                                <i className="fas fa-times-circle"></i>
                            </button>
                        )}
                    </div>

                    {/* Search Results Popover */}
                    {(isSearchFocused || searchQuery) && searchResults.length > 0 && (
                        <div className="absolute bottom-full left-0 w-full bg-gray-900 border border-gray-700 rounded-t-xl shadow-2xl max-h-96 overflow-y-auto custom-scrollbar z-50">
                            <div className="p-2 sticky top-0 bg-gray-900 border-b border-gray-800 flex justify-between items-center">
                                <span className="text-xs font-bold text-blue-400">{searchResults.length}건 발견</span>
                                <button onClick={() => setIsSearchFocused(false)} className="text-gray-500 hover:text-white"><i className="fas fa-chevron-down"></i></button>
                            </div>
                            {searchResults.map((item, idx) => (
                                <button
                                    key={idx}
                                    onClick={() => handleSearchResultClick(item)}
                                    className="w-full text-left p-3 border-b border-gray-800 last:border-0 hover:bg-gray-800 transition-colors group"
                                >
                                    <div className="text-xs font-bold text-gray-300 group-hover:text-blue-400 mb-1">{item.lectureTitle}</div>
                                    <div className="text-[10px] text-gray-500 mb-1">{item.courseTitle}</div>
                                    <div className="text-[10px] text-gray-600 line-clamp-2">{item.content.substring(0, 150)}...</div>
                                </button>
                            ))}
                        </div>
                    )}

                    {(isSearchFocused || searchQuery) && searchQuery && searchResults.length === 0 && (
                        <div className="absolute bottom-full left-0 w-full bg-gray-900 border border-gray-700 p-4 text-center text-xs text-gray-500 rounded-t-xl">
                            검색 결과가 없습니다.
                        </div>
                    )}
                </div>
            </div>

            {/* Main Content Viewer */}
            <div className="flex-1 bg-white relative flex flex-col">
                {selectedLecture ? (
                    <>
                        <div className="h-10 bg-gray-100 border-b border-gray-200 flex items-center px-4 justify-between">
                            <span className="text-xs font-bold text-gray-600 truncate">
                                <i className="fas fa-chalkboard-teacher mr-2 text-blue-600"></i>
                                {selectedLecture.title}
                            </span>
                            <a href={iframeSrc} target="_blank" rel="noopener noreferrer" className="text-xs text-blue-500 hover:text-blue-700 font-bold">
                                <i className="fas fa-external-link-alt mr-1"></i> 새 창으로 열기
                            </a>
                        </div>
                        <iframe
                            src={iframeSrc}
                            className="w-full h-full border-none"
                            title="Lecture Viewer"
                        />
                    </>
                ) : (
                    <div className="w-full h-full flex flex-col items-center justify-center text-gray-400 bg-gray-900">
                        <i className="fas fa-book-open text-6xl mb-4 opacity-20"></i>
                        <p className="text-lg font-medium opacity-50">좌측 목록에서 강의를 선택하세요</p>
                    </div>
                )}
            </div>
        </div>
    );
};

export default LectureMode;
