
import React from 'react';

interface LandingPageProps {
  onEnter: () => void;
}

const LandingPage: React.FC<LandingPageProps> = ({ onEnter }) => {
  return (
    <div className="fixed inset-0 z-[1000] bg-gray-900 overflow-y-auto custom-scrollbar flex flex-col items-center justify-center p-6 sm:p-12">
      {/* Background Decor */}
      <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none opacity-30">
        <div className="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-blue-600/20 blur-[120px] rounded-full animate-pulse"></div>
        <div className="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-purple-600/20 blur-[120px] rounded-full animate-pulse" style={{ animationDelay: '1s' }}></div>
      </div>

      <div className="max-w-5xl w-full flex flex-col items-center relative z-10">
        {/* Logo Section */}
        <div className="flex flex-col items-center mb-12 animate-in fade-in slide-in-from-top-4 duration-1000">
          <div className="w-20 h-20 bg-blue-600 rounded-[2rem] flex items-center justify-center shadow-2xl shadow-blue-900/40 mb-6 group transition-transform hover:rotate-12">
            <i className="fas fa-layer-group text-3xl text-white"></i>
          </div>
          <h1 className="text-4xl sm:text-6xl font-black text-white tracking-tighter text-center leading-tight">
            <span className="text-blue-500">KIM SABU</span><br />
            SMART LECTURE HALL
          </h1>
          <p className="mt-6 text-gray-400 font-bold uppercase tracking-[0.3em] text-[10px] sm:text-xs">Smart Interactive Education System v3.5</p>
        </div>

        {/* Entrance Button */}
        <button 
          onClick={onEnter}
          className="group relative px-12 py-5 bg-blue-600 hover:bg-blue-500 text-white rounded-[2rem] font-black text-lg tracking-widest shadow-2xl shadow-blue-900/50 transition-all active:scale-95 mb-16 animate-in zoom-in-95 duration-700"
        >
          <span className="relative z-10 flex items-center gap-3">
            강의실 입장하기
            <i className="fas fa-arrow-right group-hover:translate-x-1 transition-transform"></i>
          </span>
          <div className="absolute inset-0 bg-white/20 rounded-[2rem] opacity-0 group-hover:opacity-100 transition-opacity"></div>
        </button>

        {/* Info Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 w-full animate-in fade-in slide-in-from-bottom-10 duration-1000 delay-300">
          {[
            { 
              icon: 'fa-microphone', 
              title: 'AI LIVE SUBTITLES', 
              desc: '강의 내용이 실시간으로 텍스트화되어 기록되며, 종료 시 자동으로 메모장 파일이 생성됩니다.',
              color: 'text-red-500',
              bg: 'bg-red-500/10'
            },
            { 
              icon: 'fa-desktop', 
              title: 'INTERACTIVE PRACTICE', 
              desc: '강의 슬라이드와 실시간 PC 화면 공유를 동시에 보며 막힘없는 실습 환경을 제공합니다.',
              color: 'text-blue-400',
              bg: 'bg-blue-400/10'
            },
            { 
              icon: 'fa-robot', 
              title: 'GEMINI AI ASSISTANT', 
              desc: '강의 중 궁금한 사항은 김사부 AI에게 언제든 질문하여 전문적인 답변을 받을 수 있습니다.',
              color: 'text-cyan-400',
              bg: 'bg-cyan-400/10'
            }
          ].map((item, idx) => (
            <div key={idx} className="bg-gray-800/40 backdrop-blur-xl border border-gray-700/50 rounded-[2.5rem] p-8 hover:bg-gray-800/60 transition-all hover:translate-y-[-5px] group">
              <div className={`w-14 h-14 ${item.bg} rounded-2xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform`}>
                <i className={`fas ${item.icon} ${item.color} text-xl`}></i>
              </div>
              <h4 className="text-white font-black text-sm mb-3 tracking-wider">{item.title}</h4>
              <p className="text-gray-500 text-xs font-bold leading-relaxed">{item.desc}</p>
            </div>
          ))}
        </div>

        {/* Instructor Footer */}
        <div className="mt-20 flex flex-col items-center gap-2 opacity-50 grayscale hover:grayscale-0 hover:opacity-100 transition-all duration-700">
          <div className="h-px w-20 bg-gray-700 mb-4"></div>
          <p className="text-[10px] font-black tracking-[0.5em] text-gray-500 uppercase">Instructor</p>
          <span className="text-lg font-black text-white tracking-tighter">김 선 중 (김사부)</span>
        </div>
      </div>

      <div className="fixed bottom-10 left-10 flex flex-col gap-1">
        <div className="flex items-center gap-2">
           <div className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></div>
           <span className="text-[10px] font-black text-gray-500">SERVER ONLINE</span>
        </div>
        <p className="text-[8px] text-gray-700 font-bold uppercase tracking-widest">Optimized for Chrome v120+</p>
      </div>
    </div>
  );
};

export default LandingPage;
