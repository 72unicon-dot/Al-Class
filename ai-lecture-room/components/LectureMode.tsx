import React, { useState } from 'react';
import { COURSES, Course, Lecture } from '../data/courses';

interface LectureModeProps {
    onBack: () => void;
}

const LectureMode: React.FC<LectureModeProps> = ({ onBack }) => {
    const [activeCourseId, setActiveCourseId] = useState<string | null>(null);
    const [selectedLecture, setSelectedLecture] = useState<{ coursePath: string; file: string; title: string } | null>(null);

    const toggleCourse = (courseId: string) => {
        setActiveCourseId(prev => prev === courseId ? null : courseId);
    };

    const handleLectureClick = (course: Course, lecture: Lecture) => {
        setSelectedLecture({
            coursePath: course.path,
            file: lecture.file,
            title: lecture.title
        });
    };

    // Calculate the source URL for the iframe
    // Assuming the app is served from ai-lecture-room/dist/, we need to go up two levels to access course folders.
    // URL: ../../c01_basics/filename.html
    const iframeSrc = selectedLecture
        ? `../../${selectedLecture.coursePath}/${selectedLecture.file}`
        : '';

    return (
        <div className="flex h-full w-full bg-gray-900 text-white overflow-hidden animate-in fade-in zoom-in-95 duration-500">
            {/* Sidebar - Course List */}
            <div className="w-80 flex-shrink-0 bg-gray-950 border-r border-gray-800 flex flex-col">
                <div className="p-4 border-b border-gray-800 flex justify-between items-center">
                    <h2 className="text-lg font-bold text-white"><i className="fas fa-book-reader mr-2 text-blue-500"></i>전체 강의</h2>
                    <button onClick={onBack} className="text-gray-500 hover:text-white transition-colors text-xs uppercase font-bold tracking-wider">
                        <i className="fas fa-times mr-1"></i> 닫기
                    </button>
                </div>

                <div className="flex-1 overflow-y-auto p-4 space-y-2 custom-scrollbar">
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
            </div>

            {/* Main Content - Lecture Viewer */}
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
