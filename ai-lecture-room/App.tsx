
import React, { useState, useRef, useEffect, useCallback } from 'react';
import { ViewMode, Resource } from './types';
import PDFViewer from './components/PDFViewer';
import ScreenShare from './components/ScreenShare';
import AIAssistant from './components/AIAssistant';
import CameraFeed from './components/CameraFeed';
import LectureRecorder from './components/LectureRecorder';
import LectureResources from './components/LectureResources';
import LectureNotes from './components/LectureNotes';
import LiveSubtitles from './components/LiveSubtitles';
import LandingPage from './components/LandingPage';

import LectureMode from './components/LectureMode';

const App: React.FC = () => {
  const [isEntered, setIsEntered] = useState(false); // 강의실 입장 상태 관리
  const [viewMode, setViewMode] = useState<ViewMode>(ViewMode.SLIDE);
  const [fileData, setFileData] = useState<{ url: string, name: string, type: string } | null>(null);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [zoom, setZoom] = useState<number>(100);
  const [showAI, setShowAI] = useState(false);
  const [showResources, setShowResources] = useState(false);
  const [showCamera, setShowCamera] = useState(true);
  const [showNotepad, setShowNotepad] = useState(false);
  const [showSubtitles, setShowSubtitles] = useState(false);
  const [lectureNotes, setLectureNotes] = useState("");
  const [isFullscreen, setIsFullscreen] = useState(false);

  const [activeResource, setActiveResource] = useState<Resource | null>(null);
  const [splitRatio, setSplitRatio] = useState(50);
  const [isResizing, setIsResizing] = useState(false);

  const fileInputRef = useRef<HTMLInputElement>(null);
  const videoInputRef = useRef<HTMLInputElement>(null);
  const imageInputRef = useRef<HTMLInputElement>(null);
  const mainContainerRef = useRef<HTMLDivElement>(null);
  const prevShowSubtitles = useRef(false);

  useEffect(() => {
    const handleFullscreenChange = () => setIsFullscreen(!!document.fullscreenElement);
    document.addEventListener('fullscreenchange', handleFullscreenChange);
    return () => document.removeEventListener('fullscreenchange', handleFullscreenChange);
  }, []);

  // AI 자막 상태 변화 감지 로직
  useEffect(() => {
    if (!isEntered) return;

    // 1. 자막이 켜질 때 (마이크 ON)
    if (prevShowSubtitles.current === false && showSubtitles === true) {
      setLectureNotes("");
      setShowNotepad(true);
    }

    // 2. 자막이 꺼질 때 (마이크 OFF)
    if (prevShowSubtitles.current === true && showSubtitles === false) {
      if (lectureNotes.trim().length > 0) {
        setShowNotepad(true);
        setTimeout(() => {
          if (window.confirm("AI 자막 강의 기록이 완료되었습니다. 메모장으로 저장하시겠습니까?\n저장 후에는 내용이 자동으로 삭제됩니다.")) {
            triggerSaveNotes();
          }
        }, 500);
      }
    }
    prevShowSubtitles.current = showSubtitles;
  }, [showSubtitles, lectureNotes, isEntered]);

  const triggerSaveNotes = () => {
    if (!lectureNotes.trim()) return;
    const blob = new Blob([lectureNotes], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    const now = new Date();
    const timestamp = `${now.getFullYear()}${now.getMonth() + 1}${now.getDate()}_${now.getHours()}${now.getMinutes()}`;
    link.href = url;
    link.download = `김사부_강의노트_${timestamp}.txt`;
    link.click();
    URL.revokeObjectURL(url);

    setLectureNotes("");
    alert("강의 노트 저장 완료! 다음 강의를 위해 메모장이 초기화되었습니다.");
  };

  const toggleFullscreen = () => {
    if (!document.fullscreenElement) {
      document.documentElement.requestFullscreen().catch(err => console.error(err));
    } else {
      document.exitFullscreen();
    }
  };

  const handleSubtitleComplete = useCallback((sentence: string) => {
    setLectureNotes(prev => prev + (prev ? "\n" : "") + sentence.trim());
  }, []);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isEntered) return;
      if (document.activeElement?.tagName === 'TEXTAREA' || document.activeElement?.tagName === 'INPUT') return;

      if (fileData?.type === 'pdf' && !activeResource) {
        if (e.key === 'ArrowRight' || e.key === 'Space') setCurrentPage(prev => prev + 1);
        else if (e.key === 'ArrowLeft') setCurrentPage(prev => Math.max(1, prev - 1));
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.addEventListener('keydown', handleKeyDown);
  }, [fileData, activeResource, isEntered]);

  const startResizing = useCallback((e: React.MouseEvent) => {
    e.preventDefault();
    setIsResizing(true);
  }, []);

  const stopResizing = useCallback(() => setIsResizing(false), []);

  const resize = useCallback((e: MouseEvent) => {
    if (!isResizing || !mainContainerRef.current) return;
    const containerRect = mainContainerRef.current.getBoundingClientRect();
    const newRatio = ((e.clientX - containerRect.left) / containerRect.width) * 100;
    if (newRatio >= 20 && newRatio <= 80) setSplitRatio(newRatio);
  }, [isResizing]);

  useEffect(() => {
    if (isResizing) {
      window.addEventListener('mousemove', resize);
      window.addEventListener('mouseup', stopResizing);
    }
    return () => {
      window.removeEventListener('mousemove', resize);
      window.removeEventListener('mouseup', stopResizing);
    };
  }, [isResizing, resize, stopResizing]);

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>, fileCategory: 'doc' | 'video' | 'image' = 'doc') => {
    const file = event.target.files?.[0];
    if (file) {
      const url = URL.createObjectURL(file);
      const extension = file.name.split('.').pop()?.toLowerCase() || '';

      if (fileCategory === 'video') {
        setActiveResource({ id: 'l-v-' + Date.now(), type: 'video', title: file.name, description: '로컬 영상', link: url, isLocal: true });
      } else if (fileCategory === 'image') {
        setActiveResource({ id: 'l-i-' + Date.now(), type: 'image', title: file.name, description: '로컬 이미지', link: url, isLocal: true });
      } else {
        setFileData({ url, name: file.name, type: extension });
        setCurrentPage(1);
        setActiveResource(null);
      }
      if (event.target) event.target.value = '';
    }
  };

  const getYoutubeEmbedUrl = (url: string) => {
    const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    const match = url.match(regExp);
    return match && match[2].length === 11 ? `https://www.youtube-nocookie.com/embed/${match[match.length - 1]}?autoplay=1` : url;
  };

  // 강의실 입장 애니메이션을 위해 입장 상태가 바뀔 때 전체 화면 여부 확인 가능
  const enterLectureHall = () => {
    setIsEntered(true);
  };

  if (!isEntered) {
    return <LandingPage onEnter={enterLectureHall} />;
  }

  if (viewMode === ViewMode.LECTURE) {
    return (
      <div className="flex h-screen w-screen bg-gray-900 text-white font-sans overflow-hidden">
        {/* Sidebar for Lecture Mode */}
        <div className="w-20 bg-gray-950 border-r border-gray-800 flex flex-col items-center py-8 gap-6 z-[100]">
          <div className="w-12 h-12 bg-blue-600 rounded-2xl flex items-center justify-center shadow-xl shadow-blue-900/30 mb-4 cursor-pointer" onClick={() => setIsEntered(false)}>
            <i className="fas fa-layer-group text-xl"></i>
          </div>
          <nav className="flex flex-col gap-4">
            <button onClick={() => setViewMode(ViewMode.LECTURE)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.LECTURE ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="강의 모드"><i className="fas fa-book text-xl"></i></button>
            <button onClick={() => setViewMode(ViewMode.SLIDE)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.SLIDE ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="슬라이드 모드"><i className="fas fa-desktop text-xl"></i></button>
            <button onClick={() => setViewMode(ViewMode.SPLIT)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.SPLIT ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="분할 화면 모드"><i className="fas fa-columns text-xl"></i></button>
            <button onClick={() => setViewMode(ViewMode.PRACTICE)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.PRACTICE ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="실습 전용 모드"><i className="fas fa-laptop-code text-xl"></i></button>
          </nav>
        </div>

        <div className="flex-1 flex flex-col overflow-hidden relative">
          <LectureMode onBack={() => setViewMode(ViewMode.SLIDE)} />
        </div>
      </div>
    );
  }

  return (
    <div className={`flex h-screen w-screen bg-gray-900 text-white font-sans overflow-hidden animate-in fade-in duration-1000 ${isResizing ? 'cursor-col-resize select-none' : ''}`}>
      <input type="file" ref={fileInputRef} accept=".pdf,.ppt,.pptx" className="hidden" onChange={(e) => handleFileUpload(e, 'doc')} />
      <input type="file" ref={videoInputRef} accept="video/*" className="hidden" onChange={(e) => handleFileUpload(e, 'video')} />
      <input type="file" ref={imageInputRef} accept="image/*" className="hidden" onChange={(e) => handleFileUpload(e, 'image')} />

      {/* Sidebar */}
      <div className="w-20 bg-gray-950 border-r border-gray-800 flex flex-col items-center py-8 gap-6 z-[100]">
        <div className="w-12 h-12 bg-blue-600 rounded-2xl flex items-center justify-center shadow-xl shadow-blue-900/30 mb-4 cursor-pointer" onClick={() => setIsEntered(false)}>
          <i className="fas fa-layer-group text-xl"></i>
        </div>
        <nav className="flex flex-col gap-4">
          <button onClick={() => setViewMode(ViewMode.LECTURE)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.LECTURE ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="강의 모드"><i className="fas fa-book text-xl"></i></button>
          <button onClick={() => setViewMode(ViewMode.SLIDE)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.SLIDE ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="슬라이드 모드"><i className="fas fa-desktop text-xl"></i></button>
          <button onClick={() => setViewMode(ViewMode.SPLIT)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.SPLIT ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="분할 화면 모드"><i className="fas fa-columns text-xl"></i></button>
          <button onClick={() => setViewMode(ViewMode.PRACTICE)} className={`p-4 rounded-2xl transition-all ${viewMode === ViewMode.PRACTICE ? 'bg-gray-800 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="실습 전용 모드"><i className="fas fa-laptop-code text-xl"></i></button>
          <div className="h-px w-8 bg-gray-800 my-2"></div>
          <button onClick={() => setShowNotepad(!showNotepad)} className={`p-4 rounded-2xl transition-all ${showNotepad ? 'bg-blue-600/20 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="강의 노트"><i className="fas fa-sticky-note text-xl"></i></button>
          <button onClick={() => setShowSubtitles(!showSubtitles)} className={`p-4 rounded-2xl transition-all ${showSubtitles ? 'bg-red-600/20 text-red-500' : 'text-gray-500 hover:text-gray-300'}`} title="AI 라이브 자막"><i className={`fas ${showSubtitles ? 'fa-microphone' : 'fa-microphone-slash'} text-xl`}></i></button>
          <button onClick={() => setShowCamera(!showCamera)} className={`p-4 rounded-2xl transition-all ${showCamera ? 'bg-blue-600/20 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="카메라 토글"><i className={`fas ${showCamera ? 'fa-video' : 'fa-video-slash'} text-xl`}></i></button>
          <button onClick={() => { setShowResources(!showResources); }} className={`p-4 rounded-2xl transition-all ${showResources ? 'bg-purple-600/20 text-purple-400' : 'text-gray-500 hover:text-gray-300'}`} title="자료실"><i className="fas fa-folder-open text-xl"></i></button>
          <button onClick={() => { setShowAI(!showAI); }} className={`p-4 rounded-2xl transition-all ${showAI ? 'bg-blue-600/20 text-blue-400' : 'text-gray-500 hover:text-gray-300'}`} title="AI 비서"><i className="fas fa-robot text-xl"></i></button>
        </nav>
        <div className="mt-auto">
          <button onClick={() => fileInputRef.current?.click()} className="p-4 rounded-2xl text-gray-500 hover:text-blue-400 transition-all"><i className="fas fa-file-upload text-xl"></i></button>
        </div>
      </div>

      <div className="flex-1 flex flex-col overflow-hidden relative">
        <header className="h-20 bg-gray-900/40 backdrop-blur-xl border-b border-gray-800 flex items-center justify-between px-10 z-[100]">
          <div className="flex flex-col">
            <h1 className="text-xl font-black tracking-tighter"><span className="text-blue-500">김사부</span> 강의실</h1>
            <span className="text-[10px] text-gray-500 font-bold uppercase tracking-[0.2em]">Smart Interactive System</span>
          </div>
          <div className="flex items-center gap-4">
            <LectureRecorder />
            <button onClick={toggleFullscreen} className="w-10 h-10 flex items-center justify-center rounded-xl bg-gray-800 text-gray-400 hover:text-white transition-all"><i className={`fas ${isFullscreen ? 'fa-compress' : 'fa-expand'}`}></i></button>

            <div className="flex items-center gap-2 bg-gray-950 p-1.5 rounded-2xl border border-gray-800 shadow-inner">
              <button
                onClick={() => setShowSubtitles(!showSubtitles)}
                className={`flex items-center gap-2 px-4 py-1.5 rounded-xl text-[10px] font-black transition-all ${showSubtitles ? 'bg-red-600 text-white animate-pulse' : 'bg-transparent text-gray-500 hover:text-gray-300'}`}
              >
                <i className={`fas ${showSubtitles ? 'fa-microphone' : 'fa-microphone-alt-slash'}`}></i>
                AI 자막 {showSubtitles ? 'ON' : 'OFF'}
              </button>
              <button onClick={() => setViewMode(viewMode === ViewMode.SLIDE ? ViewMode.SPLIT : ViewMode.SLIDE)} className={`px-6 py-1.5 rounded-xl text-[10px] font-black transition-all border ${viewMode !== ViewMode.SLIDE ? 'bg-red-500/10 border-red-500 text-red-500' : 'bg-blue-600 border-blue-500 text-white'}`}>
                <i className={`fas ${viewMode !== ViewMode.SLIDE ? 'fa-stop' : 'fa-laptop-code'} mr-2`}></i>
                {viewMode !== ViewMode.SLIDE ? '강의 모드' : '실습 시작'}
              </button>
            </div>
          </div>
        </header>

        <main ref={mainContainerRef} className="flex-1 p-8 overflow-hidden bg-gray-900 relative">
          <div className="h-full w-full flex relative">
            {(viewMode === ViewMode.SLIDE || viewMode === ViewMode.SPLIT) && (
              <div style={{ width: viewMode === ViewMode.SPLIT ? `${splitRatio}%` : '100%', transition: isResizing ? 'none' : 'width 0.5s cubic-bezier(0.4, 0, 0.2, 1)' }} className="h-full relative overflow-hidden">
                {activeResource ? (
                  <div className="w-full h-full bg-gray-950 rounded-3xl overflow-hidden relative shadow-2xl border border-gray-800 group/res">
                    {activeResource.type === 'video' ? (
                      activeResource.isLocal ? <video key={activeResource.id} src={activeResource.link} controls autoPlay className="w-full h-full object-contain" /> : <iframe key={activeResource.id} src={getYoutubeEmbedUrl(activeResource.link)} className="w-full h-full border-none" allow="autoplay; encrypted-media" allowFullScreen />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center p-4 bg-gray-900"><img key={activeResource.id} src={activeResource.link} className="max-w-full max-h-full object-contain rounded-xl shadow-2xl" /></div>
                    )}
                    <button onClick={() => setActiveResource(null)} className="absolute top-4 right-4 px-4 py-2 bg-gray-900/90 backdrop-blur-md border border-gray-700 text-white rounded-xl text-xs font-black opacity-0 group-hover/res:opacity-100 transition-all hover:bg-red-600">슬라이드로 복귀</button>
                  </div>
                ) : (
                  <PDFViewer url={fileData?.url || null} fileName={fileData?.name || ''} fileType={fileData?.type || ''} isPracticeMode={viewMode === ViewMode.SPLIT} currentPage={currentPage} zoom={zoom} onPageChange={setCurrentPage} onZoomChange={setZoom} onUploadClick={() => fileInputRef.current?.click()} />
                )}
                {showNotepad && (
                  <LectureNotes
                    notes={lectureNotes}
                    setNotes={setLectureNotes}
                    onClose={() => setShowNotepad(false)}
                    onSave={triggerSaveNotes}
                  />
                )}
              </div>
            )}

            {viewMode === ViewMode.SPLIT && (
              <div onMouseDown={startResizing} className="w-2 group cursor-col-resize relative z-10 flex items-center justify-center -mx-1">
                <div className={`w-1 h-[20%] rounded-full bg-blue-500/30 group-hover:bg-blue-500/80 ${isResizing ? 'bg-blue-500 scale-y-150 h-full' : ''}`}></div>
              </div>
            )}

            {(viewMode === ViewMode.SPLIT || viewMode === ViewMode.PRACTICE) && (
              <div style={{ width: viewMode === ViewMode.SPLIT ? `${100 - splitRatio}%` : '100%', transition: isResizing ? 'none' : 'width 0.5s cubic-bezier(0.4, 0, 0.2, 1)' }} className="h-full relative overflow-hidden animate-in fade-in zoom-in-95">
                <ScreenShare isActive={viewMode === ViewMode.SPLIT || viewMode === ViewMode.PRACTICE} />
              </div>
            )}
          </div>

          <LiveSubtitles isActive={showSubtitles} onSentenceComplete={handleSubtitleComplete} />
          <CameraFeed isActive={showCamera} />
        </main>

        <footer className="h-10 bg-gray-950 border-t border-gray-800 flex items-center px-10 justify-between text-[9px] text-gray-500 font-bold uppercase tracking-widest">
          <div className="flex items-center gap-4">
            <div>SERVER: OPTIMIZED</div>
            <div className="flex items-center gap-2">
              <div className={`w-1.5 h-1.5 rounded-full ${showSubtitles ? 'bg-red-500 animate-pulse' : 'bg-gray-700'}`}></div>
              <span className={showSubtitles ? 'text-red-500' : 'text-gray-600'}>{showSubtitles ? 'AI LIVE TRANSCRIBING...' : 'STT READY'}</span>
            </div>
          </div>
          <div>Smart Lecture v3.5.0 // Session Auto-Refresh Enabled</div>
        </footer>
      </div>

      {showAI && <AIAssistant onClose={() => setShowAI(false)} />}
      {showResources && (
        <LectureResources
          onClose={() => setShowResources(false)}
          onSelectResource={(res) => { setActiveResource(res); setShowResources(false); }}
          onStartPractice={() => {
            setShowResources(false);
            if (viewMode === ViewMode.SLIDE) setViewMode(ViewMode.SPLIT);
          }}
          onTriggerVideoUpload={() => videoInputRef.current?.click()}
          onTriggerImageUpload={() => imageInputRef.current?.click()}
        />
      )}
    </div>
  );
};

export default App;
