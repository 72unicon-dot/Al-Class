
import React, { useState, useRef, useEffect } from 'react';
import { Resource } from '../types';

interface LectureResourcesProps {
  onClose: () => void;
  onSelectResource: (res: Resource) => void;
  onStartPractice: () => void;
  onTriggerVideoUpload?: () => void;
  onTriggerImageUpload?: () => void;
}

type TabType = 'practice' | 'reference';

const LectureResources: React.FC<LectureResourcesProps> = ({ 
  onClose, 
  onSelectResource, 
  onStartPractice,
  onTriggerVideoUpload,
  onTriggerImageUpload
}) => {
  const [isPinned, setIsPinned] = useState(false);
  const [activeTab, setActiveTab] = useState<TabType>('practice');
  const containerRef = useRef<HTMLDivElement>(null);

  const practiceTools = [
    { id: 'p1', title: '구글 AI 스튜디오', description: '제미나이 API 개발 환경', link: 'https://aistudio.google.com/', icon: 'fa-brain' },
    { id: 'p2', title: '제미나이 (Gemini)', description: '멀티모달 대화형 AI', link: 'https://gemini.google.com/', icon: 'fa-wand-magic-sparkles' },
    { id: 'p3', title: '노트북 LM', description: 'AI 기반 문서 분석 노트', link: 'https://notebooklm.google.com/', icon: 'fa-book-open-reader' },
    { id: 'p4', title: '구글 Stitch', description: 'AI 에이전트 제작 도구', link: 'https://stitch.withgoogle.com/', icon: 'fa-vial' },
    { id: 'p5', title: '티처블 머신', description: '웹 기반 머신러닝 학습', link: 'https://teachablemachine.withgoogle.com/', icon: 'fa-microchip' },
    { id: 'p6', title: 'Suno AI', description: 'AI 음악 생성 서비스', link: 'https://suno.com/', icon: 'fa-music' }
  ];

  const resources: Resource[] = [
    { id: '1', type: 'video', title: '파이썬 기초 문법 가이드', description: '핵심 요약 강의 (YouTube)', link: 'https://www.youtube.com/watch?v=yytWGELNeOI' },
    { id: '4', type: 'image', title: '데이터 사이언스 로드맵', description: '인포그래픽 자료', link: 'https://images.unsplash.com/photo-1551288049-bbda4865cda1?auto=format&fit=crop&q=80&w=1000' }
  ];

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (!isPinned && containerRef.current && !containerRef.current.contains(event.target as Node)) onClose();
    };
    if (!isPinned) document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [isPinned, onClose]);

  const getIcon = (type: string, customIcon?: string) => {
    if (customIcon) return <i className={`fas ${customIcon} text-blue-400`}></i>;
    switch (type) {
      case 'pdf': return <i className="fas fa-file-pdf text-red-500"></i>;
      case 'video': return <i className="fas fa-play-circle text-blue-500"></i>;
      case 'image': return <i className="fas fa-file-image text-green-400"></i>;
      case 'url': return <i className="fas fa-external-link-alt text-blue-400"></i>;
      default: return <i className="fas fa-file"></i>;
    }
  };

  const handlePracticeClick = (url: string) => {
    const windowFeatures = "width=1280,height=850,menubar=no,toolbar=no,location=yes,status=no,resizable=yes,scrollbars=yes";
    window.open(url, '_blank', windowFeatures);
    onStartPractice();
  };

  return (
    <div ref={containerRef} className="flex flex-col h-full bg-gray-950/95 backdrop-blur-2xl border-l border-gray-800 w-85 shadow-2xl relative z-30 animate-in fade-in slide-in-from-right-10 duration-300">
      {/* Header */}
      <div className="p-4 border-b border-gray-800 flex items-center justify-between bg-gray-900/50">
        <div className="flex items-center gap-3">
          <div className="w-8 h-8 bg-purple-600/20 rounded-xl flex items-center justify-center">
            <i className="fas fa-folder-open text-purple-500"></i>
          </div>
          <h3 className="font-black text-sm text-white">강의 자료실</h3>
        </div>
        <div className="flex items-center gap-1">
          <button 
            onClick={() => setIsPinned(!isPinned)} 
            className={`w-8 h-8 rounded-lg flex items-center justify-center transition-all ${isPinned ? 'bg-purple-600/20 text-purple-500 border border-purple-500/30' : 'text-gray-500 hover:text-gray-300'}`}
          >
            <i className={`fas fa-thumbtack text-xs ${isPinned ? 'rotate-0' : '-rotate-45'}`}></i>
          </button>
          <button 
            onClick={onClose} 
            className="w-8 h-8 rounded-lg flex items-center justify-center text-gray-500 hover:text-red-500 transition-all"
          >
            <i className="fas fa-times text-xs"></i>
          </button>
        </div>
      </div>

      {/* Tabs Navigation */}
      <div className="flex border-b border-gray-800 bg-gray-900/30">
        <button 
          onClick={() => setActiveTab('practice')}
          className={`flex-1 py-3 text-[11px] font-black uppercase tracking-wider transition-all relative ${activeTab === 'practice' ? 'text-blue-400' : 'text-gray-500 hover:text-gray-400'}`}
        >
          실습 도구
          {activeTab === 'practice' && <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-blue-500 shadow-[0_0_10px_rgba(59,130,246,0.5)]"></div>}
        </button>
        <button 
          onClick={() => setActiveTab('reference')}
          className={`flex-1 py-3 text-[11px] font-black uppercase tracking-wider transition-all relative ${activeTab === 'reference' ? 'text-purple-400' : 'text-gray-500 hover:text-gray-400'}`}
        >
          참고 자료
          {activeTab === 'reference' && <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-purple-500 shadow-[0_0_10px_rgba(168,85,247,0.5)]"></div>}
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
        {activeTab === 'practice' ? (
          <div className="space-y-4 animate-in fade-in slide-in-from-top-2 duration-300">
            <div className="flex flex-col gap-1 px-1">
              <h5 className="text-[10px] font-black text-blue-400 uppercase tracking-widest flex items-center gap-2">
                <i className="fas fa-tools"></i> Practice Workspace
              </h5>
              <p className="text-[9px] text-gray-500 font-bold">* 클릭 시 별도의 새 창으로 실습 환경이 열립니다.</p>
            </div>
            
            <div className="space-y-2">
              {practiceTools.map((tool) => (
                <button 
                  key={tool.id} 
                  onClick={() => handlePracticeClick(tool.link)}
                  className="w-full text-left block group bg-blue-600/5 border border-blue-600/10 hover:border-blue-500/50 rounded-2xl p-3.5 transition-all hover:bg-blue-600/10 active:scale-[0.98]"
                >
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-xl bg-gray-950 flex items-center justify-center border border-gray-800 group-hover:border-blue-500/30 transition-all">
                      {getIcon('url', tool.icon)}
                    </div>
                    <div className="flex-1 min-w-0">
                      <h4 className="text-xs font-black text-gray-200 group-hover:text-blue-400 transition-colors truncate">{tool.title}</h4>
                      <p className="text-[9px] text-gray-500 mt-0.5 line-clamp-1">{tool.description}</p>
                    </div>
                    <i className="fas fa-window-restore text-[10px] text-gray-700 group-hover:text-blue-500 group-hover:translate-x-1 transition-all"></i>
                  </div>
                </button>
              ))}
            </div>
          </div>
        ) : (
          <div className="space-y-6 animate-in fade-in slide-in-from-top-2 duration-300">
            {/* Quick Upload Actions */}
            <div className="grid grid-cols-2 gap-2">
              <button 
                onClick={onTriggerVideoUpload} 
                className="flex flex-col items-center gap-2 p-4 rounded-2xl bg-blue-600/5 border border-blue-500/20 hover:bg-blue-600/10 hover:border-blue-500/40 transition-all text-center group active:scale-[0.98]"
              >
                <i className="fas fa-video text-blue-400 text-xl group-hover:scale-110 transition-transform"></i>
                <span className="text-[10px] font-black text-blue-400 uppercase">영상 업로드</span>
              </button>
              <button 
                onClick={onTriggerImageUpload} 
                className="flex flex-col items-center gap-2 p-4 rounded-2xl bg-green-600/5 border border-green-500/20 hover:bg-green-600/10 hover:border-green-500/40 transition-all text-center group active:scale-[0.98]"
              >
                <i className="fas fa-image text-green-400 text-xl group-hover:scale-110 transition-transform"></i>
                <span className="text-[10px] font-black text-green-400 uppercase">이미지 업로드</span>
              </button>
            </div>

            <div className="space-y-3">
              <h5 className="text-[10px] font-black text-purple-400 uppercase tracking-widest px-1 flex items-center gap-2">
                <i className="fas fa-layer-group"></i> Lecture Materials
              </h5>
              <div className="space-y-2">
                {resources.map((res) => (
                  <button 
                    key={res.id} 
                    onClick={() => onSelectResource(res)} 
                    className="w-full text-left block group bg-gray-900/40 border border-gray-800/50 hover:border-purple-500/50 rounded-2xl p-3.5 transition-all hover:bg-gray-800/50 active:scale-[0.98]"
                  >
                    <div className="flex items-start gap-3">
                      <div className="w-10 h-10 rounded-xl bg-gray-950 flex items-center justify-center border border-gray-800 group-hover:border-purple-500/30 transition-all">
                        {getIcon(res.type)}
                      </div>
                      <div className="flex-1 min-w-0">
                        <h4 className="text-xs font-black text-gray-200 group-hover:text-purple-400 transition-colors truncate">{res.title}</h4>
                        <p className="text-[10px] text-gray-500 mt-1 line-clamp-2 leading-relaxed font-medium">{res.description}</p>
                      </div>
                    </div>
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
      
      {/* Footer Info Box */}
      <div className="p-4 border-t border-gray-800 bg-gray-900/30">
        <div className="bg-gray-950/50 rounded-xl p-3 border border-gray-800/50 flex items-center gap-3">
          <div className="w-6 h-6 rounded-full bg-blue-500/10 flex items-center justify-center border border-blue-500/20 shrink-0">
            <i className="fas fa-info text-[8px] text-blue-500"></i>
          </div>
          <p className="text-[9px] text-gray-500 font-bold leading-tight italic">
            {activeTab === 'practice' 
              ? "사이트가 새 창으로 열리면 해당 창을 화면 공유 영역으로 이동해 주세요."
              : "참고 자료를 선택하면 슬라이드 영역에서 즉시 확인할 수 있습니다."}
          </p>
        </div>
      </div>
    </div>
  );
};

export default LectureResources;
