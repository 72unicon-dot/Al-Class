
import React, { useEffect, useRef, useState, useCallback } from 'react';
import DrawingCanvas, { DrawingCanvasRef } from './DrawingCanvas';

interface ScreenShareProps {
  isActive: boolean;
}

const ScreenShare: React.FC<ScreenShareProps> = ({ isActive }) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const drawingRef = useRef<DrawingCanvasRef>(null);
  
  const [stream, setStream] = useState<MediaStream | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isFitMode, setIsFitMode] = useState(true); // true: contain, false: cover
  
  // Annotation State
  const [isPenActive, setIsPenActive] = useState(false);
  const [penColor, setPenColor] = useState('#3b82f6');
  const [penWidth, setPenWidth] = useState(3);
  const [canvasSize, setCanvasSize] = useState({ width: 0, height: 0 });

  const startSharing = async () => {
    try {
      setError(null);
      const mediaStream = await navigator.mediaDevices.getDisplayMedia({
        video: { 
          cursor: "always",
          displaySurface: "monitor"
        } as any,
        audio: false,
      });
      setStream(mediaStream);
      if (videoRef.current) {
        videoRef.current.srcObject = mediaStream;
      }
      
      mediaStream.getVideoTracks()[0].onended = () => {
        stopSharing();
      };
    } catch (err: any) {
      console.error("Error sharing screen:", err);
      if (err.name === 'NotAllowedError' || err.name === 'PermissionDeniedError') {
        setError("화면 공유 권한이 거부되었거나 사용자가 취소했습니다. 실습을 위해 화면 공유를 허용해주세요.");
      } else {
        setError("화면 공유를 시작할 수 없습니다. 시스템 설정을 확인해주세요.");
      }
    }
  };

  const stopSharing = () => {
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
      setStream(null);
    }
    if (videoRef.current) {
      videoRef.current.srcObject = null;
    }
    drawingRef.current?.clear();
    setIsPenActive(false);
  };

  const updateCanvasSize = useCallback(() => {
    if (containerRef.current) {
      setCanvasSize({
        width: containerRef.current.clientWidth,
        height: containerRef.current.clientHeight
      });
    }
  }, []);

  useEffect(() => {
    if (isActive) {
      if (!stream) startSharing();
      updateCanvasSize();
      window.addEventListener('resize', updateCanvasSize);
    } else {
      stopSharing();
    }
    return () => {
      stopSharing();
      window.removeEventListener('resize', updateCanvasSize);
    };
  }, [isActive]);

  const toggleFitMode = (e: React.MouseEvent) => {
    e.stopPropagation();
    setIsFitMode(!isFitMode);
  };

  return (
    <div ref={containerRef} className="relative group w-full h-full bg-black rounded-3xl overflow-hidden shadow-2xl border border-gray-800 transition-all duration-500">
      {isActive ? (
        <>
          <video
            ref={videoRef}
            autoPlay
            playsInline
            muted
            className={`w-full h-full transition-all duration-500 ${isFitMode ? 'object-contain' : 'object-cover'}`}
          />
          
          <DrawingCanvas 
            ref={drawingRef}
            width={canvasSize.width}
            height={canvasSize.height}
            color={penColor}
            lineWidth={penWidth}
            isActive={isPenActive}
          />
          
          {!stream && !error && (
            <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-900/80 backdrop-blur-sm z-10">
              <div className="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mb-6"></div>
              <p className="text-gray-300 font-bold">화면 공유를 준비 중입니다...</p>
            </div>
          )}

          {error && (
            <div className="absolute inset-0 flex flex-col items-center justify-center bg-gray-900/90 backdrop-blur-md p-10 text-center z-10">
              <div className="w-16 h-16 bg-red-600/20 rounded-2xl flex items-center justify-center text-red-500 mb-6 border border-red-500/30">
                <i className="fas fa-exclamation-triangle text-2xl"></i>
              </div>
              <p className="text-red-400 font-black mb-2 uppercase tracking-tighter text-lg">Permission Denied</p>
              <p className="text-gray-400 font-medium mb-6 max-w-xs mx-auto leading-relaxed">{error}</p>
              <button 
                onClick={startSharing}
                className="px-8 py-3 bg-red-600 hover:bg-red-500 text-white rounded-2xl text-xs font-black transition-all shadow-xl active:scale-95"
              >
                화면 공유 다시 시도
              </button>
            </div>
          )}

          {/* Top Status & Annotation Toolbar */}
          <div className="absolute top-6 left-6 right-6 flex items-center justify-between z-40 pointer-events-none">
            <div className="flex items-center gap-3">
              <div className="flex items-center gap-2 bg-red-600 px-3 py-1.5 rounded-full shadow-lg">
                <div className="w-2 h-2 bg-white rounded-full animate-pulse"></div>
                <span className="text-[10px] font-black text-white uppercase tracking-wider">LIVE STREAMING</span>
              </div>
            </div>

            {stream && (
              <div className="flex items-center gap-2 pointer-events-auto">
                <div className={`flex items-center gap-1 bg-gray-900/95 backdrop-blur-xl border border-gray-700/50 p-1.5 rounded-2xl shadow-2xl transition-all duration-300 ${isPenActive ? 'opacity-100' : 'opacity-0 pointer-events-none translate-x-10'}`}>
                  {[
                    { id: 'blue', color: '#3b82f6' },
                    { id: 'red', color: '#ef4444' },
                    { id: 'green', color: '#22c55e' },
                    { id: 'yellow', color: '#facc15' }
                  ].map(c => (
                    <button 
                      key={c.id}
                      onClick={() => setPenColor(c.color)}
                      className={`w-7 h-7 rounded-lg border-2 transition-all ${penColor === c.color ? 'border-white scale-110 shadow-lg' : 'border-transparent'}`}
                      style={{ backgroundColor: c.color }}
                    />
                  ))}
                </div>

                <div className="flex items-center gap-2">
                  <button 
                    onClick={() => drawingRef.current?.clear()}
                    className={`px-3 py-2.5 rounded-2xl text-[11px] font-black transition-all border flex items-center gap-2 shadow-xl bg-gray-900/80 border-gray-700 text-gray-400 hover:text-red-400 hover:bg-red-950/20 backdrop-blur-md ${isPenActive ? 'opacity-100' : 'opacity-0 pointer-events-none scale-90'}`}
                  >
                    <i className="fas fa-trash-alt"></i>
                    지우기
                  </button>

                  <button 
                    onClick={() => setIsPenActive(!isPenActive)}
                    className={`px-4 py-2.5 rounded-2xl text-[11px] font-black transition-all border flex items-center gap-2 shadow-xl ${
                      isPenActive 
                      ? 'bg-blue-600 border-blue-400 text-white' 
                      : 'bg-gray-900/80 border-gray-700 text-gray-400 hover:text-white hover:bg-gray-800 backdrop-blur-md'
                    }`}
                  >
                    <i className={`fas ${isPenActive ? 'fa-pen-nib' : 'fa-pencil-alt'}`}></i>
                    {isPenActive ? '실습 판서 중' : '화면 판서'}
                  </button>
                </div>
              </div>
            )}
          </div>

          {/* Bottom Controls */}
          {stream && (
            <div className="absolute bottom-8 right-8 flex items-center gap-3 opacity-0 group-hover:opacity-100 transition-all duration-500 translate-y-4 group-hover:translate-y-0 z-40">
              <button 
                onClick={toggleFitMode}
                className={`flex items-center gap-2 px-5 py-2.5 rounded-2xl text-[11px] font-black transition-all border shadow-2xl ${
                  isFitMode 
                  ? 'bg-blue-600 border-blue-500 text-white' 
                  : 'bg-gray-900/90 border-gray-700 text-gray-300 hover:text-white hover:bg-gray-800'
                }`}
              >
                <i className={`fas ${isFitMode ? 'fa-expand' : 'fa-compress'}`}></i>
                {isFitMode ? '화면 채우기' : '화면 맞춤'}
              </button>
              
              <button 
                onClick={(e) => { e.stopPropagation(); stopSharing(); startSharing(); }}
                className="w-10 h-10 flex items-center justify-center bg-gray-900/90 border border-gray-700 rounded-2xl text-gray-400 hover:text-white hover:bg-gray-800 transition-all shadow-2xl"
                title="화면 소스 다시 선택"
              >
                <i className="fas fa-sync-alt"></i>
              </button>
            </div>
          )}
        </>
      ) : (
        <div className="w-full h-full flex flex-col items-center justify-center text-gray-600 bg-gray-900/50 p-10 text-center">
          <div className="w-20 h-20 bg-gray-800 rounded-3xl flex items-center justify-center mb-6 border border-gray-700/50">
            <i className="fas fa-laptop-code text-3xl"></i>
          </div>
          <p className="text-sm font-bold max-w-[200px] leading-relaxed">
            실습 모드에서 PC 화면이 표시됩니다.
          </p>
        </div>
      )}
    </div>
  );
};

export default ScreenShare;
