
import React, { useState, useEffect, useRef } from 'react';

interface LiveSubtitlesProps {
  isActive: boolean;
  onSentenceComplete: (sentence: string) => void;
}

const LiveSubtitles: React.FC<LiveSubtitlesProps> = ({ isActive, onSentenceComplete }) => {
  const [transcript, setTranscript] = useState('');
  const [interimTranscript, setInterimTranscript] = useState('');
  const recognitionRef = useRef<any>(null);
  const isActiveRef = useRef(isActive);
  const isManuallyStoppingRef = useRef(false);

  // Sync ref with prop to avoid stale closures in callbacks
  useEffect(() => {
    isActiveRef.current = isActive;
  }, [isActive]);

  useEffect(() => {
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    
    if (SpeechRecognition && isActive) {
      isManuallyStoppingRef.current = false;
      const recognition = new SpeechRecognition();
      recognition.continuous = true;
      recognition.interimResults = true;
      // 언어 설정을 다시 한국어로 변경
      recognition.lang = 'ko-KR';

      recognition.onresult = (event: any) => {
        let interimStr = '';

        for (let i = event.resultIndex; i < event.results.length; ++i) {
          if (event.results[i].isFinal) {
            onSentenceComplete(event.results[i][0].transcript);
          } else {
            interimStr += event.results[i][0].transcript;
          }
        }
        setInterimTranscript(interimStr);
      };

      recognition.onerror = (event: any) => {
        if (event.error === 'aborted') {
          console.debug('Speech recognition aborted (expected during stop or system interrupt)');
          return;
        }

        console.error('Speech recognition error:', event.error);
        if (event.error === 'no-speech' && isActiveRef.current) {
          try { recognition.start(); } catch(e) {}
        }
      };

      recognition.onend = () => {
        if (isActiveRef.current && !isManuallyStoppingRef.current) {
          setTimeout(() => {
            if (isActiveRef.current && !isManuallyStoppingRef.current) {
              try { 
                recognition.start(); 
              } catch(e) {
                console.debug('Failed to restart recognition:', e);
              }
            }
          }, 300);
        }
      };

      recognitionRef.current = recognition;
      try {
        recognition.start();
      } catch (e) {
        console.error('Start error:', e);
      }
    }

    return () => {
      if (recognitionRef.current) {
        isManuallyStoppingRef.current = true;
        recognitionRef.current.stop();
        recognitionRef.current = null;
      }
    };
  }, [isActive, onSentenceComplete]);

  if (!isActive || (!interimTranscript && !transcript)) return null;

  return (
    <div className="absolute bottom-32 left-1/2 -translate-x-1/2 w-[80%] max-w-4xl z-[100] pointer-events-none animate-in fade-in slide-in-from-bottom-4">
      <div className="bg-black/60 backdrop-blur-xl border border-white/10 rounded-2xl px-8 py-4 shadow-[0_10px_40px_rgba(0,0,0,0.5)] flex items-center gap-4">
        <div className="flex-shrink-0 w-10 h-10 bg-red-600 rounded-full flex items-center justify-center animate-pulse shadow-[0_0_15px_rgba(239,68,68,0.5)]">
          <i className="fas fa-microphone text-white text-xs"></i>
        </div>
        <div className="flex-1 overflow-hidden">
          <p className="text-xl font-bold text-white leading-relaxed drop-shadow-lg truncate">
            {interimTranscript || "말씀하시는 내용을 분석 중입니다..."}
          </p>
          <div className="flex gap-1 mt-1">
             <div className="h-1 bg-red-500 rounded-full animate-pulse" style={{ width: '40%' }}></div>
             <div className="h-1 bg-white/10 rounded-full flex-1"></div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LiveSubtitles;
