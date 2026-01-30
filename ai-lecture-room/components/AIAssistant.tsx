
import React, { useState, useRef, useEffect } from 'react';
import { getAIResponse } from '../services/gemini';
import { ChatMessage } from '../types';

interface AIAssistantProps {
  onClose?: () => void;
}

const AIAssistant: React.FC<AIAssistantProps> = ({ onClose }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isListening, setIsListening] = useState(false);
  const scrollRef = useRef<HTMLDivElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const recognitionRef = useRef<any>(null);
  const isStoppingRef = useRef(false);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages]);

  // 음성 인식 초기화
  useEffect(() => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    if (SpeechRecognition) {
      const recognition = new SpeechRecognition();
      recognition.continuous = false;
      recognition.interimResults = false;
      recognition.lang = 'ko-KR';

      recognition.onresult = (event: any) => {
        const transcript = event.results[0][0].transcript;
        setInput(transcript);
        setIsListening(false);
      };

      recognition.onerror = (event: any) => {
        if (event.error === 'aborted') return;
        console.error('Speech recognition error:', event.error);
        setIsListening(false);
      };

      recognition.onend = () => {
        setIsListening(false);
        isStoppingRef.current = false;
      };

      recognitionRef.current = recognition;
    }

    return () => {
      if (recognitionRef.current) {
        isStoppingRef.current = true;
        recognitionRef.current.abort();
      }
    };
  }, []);

  const toggleListening = () => {
    if (isListening) {
      isStoppingRef.current = true;
      recognitionRef.current?.stop();
      setIsListening(false);
    } else {
      if (!recognitionRef.current) {
        alert('이 브라우저는 음성 인식을 지원하지 않습니다.');
        return;
      }
      try {
        isStoppingRef.current = false;
        recognitionRef.current.start();
        setIsListening(true);
      } catch (e) {
        console.error('Recognition start error:', e);
      }
    }
  };

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMsg: ChatMessage = { role: 'user', text: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    const history = messages.map(m => ({
      role: m.role,
      parts: [{ text: m.text }]
    }));

    const aiResponse = await getAIResponse(input, history);
    setMessages(prev => [...prev, { role: 'model', text: aiResponse || 'No response' }]);
    setIsLoading(false);
  };

  return (
    <div 
      ref={containerRef}
      className="fixed bottom-24 right-8 w-96 h-[600px] flex flex-col bg-gray-900/90 backdrop-blur-3xl border border-gray-700/50 rounded-[2.5rem] shadow-[0_20px_60px_rgba(0,0,0,0.6)] z-[200] overflow-hidden animate-in fade-in zoom-in-95 slide-in-from-bottom-10 duration-500 cubic-bezier(0.34, 1.56, 0.64, 1)"
    >
      <div className="p-5 border-b border-gray-800/50 flex items-center justify-between bg-gray-950/40">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 bg-blue-600/20 rounded-2xl flex items-center justify-center border border-blue-500/30">
            <i className="fas fa-robot text-blue-500"></i>
          </div>
          <div>
            <h3 className="font-black text-sm text-white tracking-tight">AI 강의 조수</h3>
            <div className="flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></span>
              <span className="text-[9px] text-gray-500 font-bold uppercase tracking-widest">Always Ready</span>
            </div>
          </div>
        </div>
        
        <button 
          onClick={onClose}
          className="w-10 h-10 rounded-2xl flex items-center justify-center text-gray-500 hover:bg-red-500/20 hover:text-red-500 transition-all active:scale-90"
          title="닫기"
        >
          <i className="fas fa-times text-sm"></i>
        </button>
      </div>

      <div ref={scrollRef} className="flex-1 overflow-y-auto p-5 space-y-4 custom-scrollbar">
        {messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center px-8">
            <div className="w-16 h-16 bg-blue-600/10 rounded-3xl flex items-center justify-center mb-6 border border-blue-500/20">
              <i className="fas fa-magic text-2xl text-blue-500/50"></i>
            </div>
            <p className="text-xs font-bold text-gray-400 leading-relaxed uppercase tracking-widest opacity-60">
              "실습 중 궁금한 점을<br/>김사부 AI에게 물어보세요"
            </p>
          </div>
        )}
        {messages.map((msg, idx) => (
          <div key={idx} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-in slide-in-from-bottom-2 duration-300`}>
            <div className={`max-w-[85%] p-4 rounded-[1.5rem] text-[13px] leading-relaxed shadow-lg ${
              msg.role === 'user' 
              ? 'bg-blue-600 text-white font-medium rounded-tr-none' 
              : 'bg-gray-800/80 text-gray-200 border border-gray-700/50 rounded-tl-none backdrop-blur-md'
            }`}>
              {msg.text}
            </div>
          </div>
        ))}
        {isLoading && (
          <div className="flex justify-start">
            <div className="bg-gray-800/50 border border-gray-700/50 p-4 rounded-[1.5rem] rounded-tl-none flex gap-1.5 items-center">
              <span className="w-1.5 h-1.5 bg-blue-500 rounded-full animate-bounce [animation-delay:-0.3s]"></span>
              <span className="w-1.5 h-1.5 bg-blue-500 rounded-full animate-bounce [animation-delay:-0.15s]"></span>
              <span className="w-1.5 h-1.5 bg-blue-500 rounded-full animate-bounce"></span>
            </div>
          </div>
        )}
      </div>

      <div className="p-5 pt-2 bg-gray-950/60 border-t border-gray-800/50">
        <div className="relative flex items-center gap-2">
          <div className="relative flex-1">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSend()}
              placeholder={isListening ? "듣고 있습니다..." : "메시지를 입력하세요..."}
              className={`w-full bg-gray-900 border ${isListening ? 'border-red-500 ring-2 ring-red-500/20' : 'border-gray-800'} rounded-2xl py-4 pl-5 pr-14 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500/20 text-sm transition-all placeholder:text-gray-600 shadow-inner`}
            />
            <button
              onClick={toggleListening}
              className={`absolute right-2 top-2 w-10 h-10 flex items-center justify-center rounded-xl transition-all shadow-lg ${
                isListening 
                ? 'bg-red-600 text-white animate-pulse' 
                : 'bg-gray-800 text-gray-500 hover:text-white hover:bg-gray-700'
              }`}
              title="음성 인식 시작"
            >
              <i className={`fas ${isListening ? 'fa-microphone' : 'fa-microphone-alt'} text-sm`}></i>
            </button>
          </div>

          <button
            onClick={handleSend}
            disabled={isLoading || !input.trim()}
            className="w-12 h-12 flex items-center justify-center rounded-2xl bg-blue-600 text-white hover:bg-blue-500 disabled:bg-gray-800 disabled:text-gray-700 transition-all shadow-xl shadow-blue-900/20 shrink-0 active:scale-95"
          >
            <i className="fas fa-paper-plane text-sm"></i>
          </button>
        </div>
        
        {isListening && (
          <div className="mt-3 flex items-center justify-center gap-2">
            <div className="flex gap-1">
              {[1,2,3,4,5].map(i => (
                <div key={i} className="w-1 h-3 bg-red-500 rounded-full animate-pulse" style={{ animationDelay: `${i * 0.1}s` }}></div>
              ))}
            </div>
            <span className="text-[10px] text-red-500 font-black uppercase tracking-[0.2em] ml-2">Voice Recording</span>
          </div>
        )}

        <p className="text-[9px] text-gray-600 mt-4 text-center font-bold uppercase tracking-widest opacity-40">
          Powered by Gemini AI Engine
        </p>
      </div>

      <div className="absolute -bottom-10 left-1/2 -translate-x-1/2 w-32 h-20 bg-blue-500/20 blur-[60px] pointer-events-none rounded-full"></div>
    </div>
  );
};

export default AIAssistant;
