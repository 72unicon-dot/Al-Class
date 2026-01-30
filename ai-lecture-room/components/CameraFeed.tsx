
import React, { useEffect, useRef, useState, useCallback } from 'react';

interface CameraFeedProps {
  isActive: boolean;
}

type BgEffect = 'none' | 'blur' | 'virtual';

const CameraFeed: React.FC<CameraFeedProps> = ({ isActive }) => {
  const videoRef = useRef<HTMLVideoElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const [stream, setStream] = useState<MediaStream | null>(null);
  const [error, setError] = useState<string | null>(null);
  
  // 상태 관리: 위치, 크기 및 배경 효과
  const [position, setPosition] = useState({ x: window.innerWidth - 320, y: window.innerHeight - 320 });
  const [size, setSize] = useState(280);
  const [bgEffect, setBgEffect] = useState<BgEffect>('none');
  const [showEffectMenu, setShowEffectMenu] = useState(false);
  
  const [isDragging, setIsDragging] = useState(false);
  const [isResizing, setIsResizing] = useState(false);
  
  const dragStartPos = useRef({ x: 0, y: 0 });
  const resizeStartSize = useRef(0);
  const resizeStartMousePos = useRef({ x: 0, y: 0 });

  const startCamera = useCallback(async () => {
    try {
      // 먼저 미디어 장치 지원 여부 확인
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        setError("이 브라우저는 카메라를 지원하지 않습니다. Chrome 또는 Edge를 사용해주세요.");
        return;
      }

      // 사용 가능한 장치 목록 확인
      const devices = await navigator.mediaDevices.enumerateDevices();
      const videoDevices = devices.filter(device => device.kind === 'videoinput');
      
      if (videoDevices.length === 0) {
        setError("연결된 카메라가 없습니다. 웹캠을 연결해주세요.");
        return;
      }

      const currentStream = await navigator.mediaDevices.getUserMedia({ 
        video: { 
          width: { ideal: 640 }, 
          height: { ideal: 640 }, 
          facingMode: "user" 
        }, 
        audio: false 
      });
      setStream(currentStream);
      if (videoRef.current) {
        videoRef.current.srcObject = currentStream;
      }
      setError(null);
    } catch (err: any) {
      console.error("Error accessing camera:", err);
      if (err.name === 'NotAllowedError' || err.name === 'PermissionDeniedError') {
        setError("카메라 권한이 거부되었습니다. 브라우저 주소창 왼쪽 🔒 아이콘을 클릭하여 카메라를 허용해주세요.");
      } else if (err.name === 'NotFoundError' || err.name === 'DevicesNotFoundError') {
        setError("카메라를 찾을 수 없습니다. 웹캠이 연결되어 있는지 확인해주세요.");
      } else if (err.name === 'NotReadableError' || err.name === 'TrackStartError') {
        setError("카메라가 다른 프로그램에서 사용 중입니다. 다른 앱(Zoom, Teams 등)을 종료해주세요.");
      } else if (err.name === 'OverconstrainedError') {
        setError("카메라 설정이 지원되지 않습니다. 다른 카메라를 시도해주세요.");
      } else if (err.name === 'SecurityError') {
        setError("보안 오류: HTTPS 또는 localhost에서만 카메라를 사용할 수 있습니다.");
      } else {
        setError(`카메라 오류: ${err.name || '알 수 없는 오류'} - ${err.message || ''}`);
      }
    }
  }, []);

  useEffect(() => {
    if (isActive) {
      startCamera();
    } else {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
        setStream(null);
      }
    }

    return () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
    };
  }, [isActive, startCamera]);

  const handleMouseDown = (e: React.MouseEvent) => {
    const target = e.target as HTMLElement;
    if (target.closest('.resize-handle')) {
      setIsResizing(true);
      resizeStartSize.current = size;
      resizeStartMousePos.current = { x: e.clientX, y: e.clientY };
    } else if (!target.closest('.effect-control') && !target.closest('.error-retry')) {
      setIsDragging(true);
      dragStartPos.current = {
        x: e.clientX - position.x,
        y: e.clientY - position.y
      };
    }
  };

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (isResizing) {
        const deltaX = e.clientX - resizeStartMousePos.current.x;
        const deltaY = e.clientY - resizeStartMousePos.current.y;
        const delta = Math.max(deltaX, deltaY);
        const newSize = Math.max(160, Math.min(600, resizeStartSize.current + delta));
        setSize(newSize);
        return;
      }

      if (isDragging) {
        const newX = e.clientX - dragStartPos.current.x;
        const newY = e.clientY - dragStartPos.current.y;
        const boundedX = Math.max(20, Math.min(newX, window.innerWidth - size - 20));
        const boundedY = Math.max(20, Math.min(newY, window.innerHeight - size - 20));
        setPosition({ x: boundedX, y: boundedY });
      }
    };

    const handleMouseUp = () => {
      setIsDragging(false);
      setIsResizing(false);
    };

    if (isDragging || isResizing) {
      window.addEventListener('mousemove', handleMouseMove);
      window.addEventListener('mouseup', handleMouseUp);
    }

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mouseup', handleMouseUp);
    };
  }, [isDragging, isResizing, size]);

  if (!isActive) return null;

  const getBackgroundStyles = () => {
    switch (bgEffect) {
      case 'blur': return 'blur-2xl scale-125 opacity-40 grayscale-[0.3]';
      case 'virtual': return 'opacity-0';
      default: return 'blur-0 scale-100 opacity-100';
    }
  };

  const getBorderColor = () => {
    if (error) return 'border-red-500 shadow-[0_0_30px_rgba(239,68,68,0.3)]';
    switch (bgEffect) {
      case 'blur': return 'border-purple-500 shadow-[0_0_50px_rgba(168,85,247,0.4)]';
      case 'virtual': return 'border-cyan-400 shadow-[0_0_50px_rgba(34,211,238,0.5)]';
      default: return 'border-blue-500 shadow-[0_0_50px_rgba(59,130,246,0.5)]';
    }
  };

  return (
    <div 
      ref={containerRef}
      className={`fixed z-50 group select-none ${isDragging ? 'cursor-grabbing' : isResizing ? 'cursor-nwse-resize' : 'cursor-grab'}`}
      style={{ 
        left: `${position.x}px`, 
        top: `${position.y}px`,
        width: `${size}px`,
        height: `${size}px`,
        transition: (isDragging || isResizing) ? 'none' : 'transform 0.1s ease-out'
      }}
      onMouseDown={handleMouseDown}
    >
      <div className={`effect-control absolute -left-16 top-1/2 -translate-y-1/2 flex flex-col gap-3 transition-all duration-500 ${showEffectMenu && !error ? 'opacity-100 translate-x-0' : 'opacity-0 translate-x-10 pointer-events-none'}`}>
        {[
          { id: 'none', icon: 'fa-video', label: 'ORIGINAL', color: 'bg-blue-600' },
          { id: 'blur', icon: 'fa-wind', label: 'BLUR', color: 'bg-purple-600' },
          { id: 'virtual', icon: 'fa-magic', label: 'STUDIO', color: 'bg-cyan-500' }
        ].map(eff => (
          <button
            key={eff.id}
            onClick={() => { setBgEffect(eff.id as BgEffect); setShowEffectMenu(false); }}
            className={`w-14 h-14 rounded-2xl flex flex-col items-center justify-center gap-1 border transition-all shadow-2xl relative overflow-hidden group/btn ${
              bgEffect === eff.id 
              ? `${eff.color} border-white/50 text-white scale-110 z-10` 
              : 'bg-gray-900/90 border-gray-800 text-gray-500 hover:text-white hover:bg-gray-800 backdrop-blur-xl'
            }`}
          >
            <i className={`fas ${eff.icon} text-xs ${bgEffect === eff.id ? 'animate-bounce' : ''}`}></i>
            <span className="text-[7px] font-black tracking-tighter">{eff.label}</span>
            {bgEffect === eff.id && <div className="absolute inset-0 bg-white/20 animate-pulse"></div>}
          </button>
        ))}
      </div>

      <div className={`relative w-full h-full rounded-full overflow-hidden border-[6px] transition-all duration-700 bg-gray-950 ${getBorderColor()} group-hover:scale-[1.02]`}>
        
        {error ? (
          <div className="flex flex-col items-center justify-center h-full text-center p-6 bg-gray-900/80 backdrop-blur-md">
            <i className="fas fa-video-slash text-2xl text-red-500 mb-3 animate-pulse"></i>
            <p className="text-[9px] text-gray-300 font-black uppercase tracking-widest leading-relaxed mb-3">
              {error}
            </p>
            <button 
              onClick={(e) => { e.stopPropagation(); startCamera(); }}
              className="error-retry px-3 py-1.5 bg-red-600 hover:bg-red-500 text-white text-[8px] font-black rounded-lg transition-all active:scale-95 shadow-lg"
            >
              다시 시도
            </button>
          </div>
        ) : (
          <>
            {bgEffect === 'virtual' && (
              <div className="absolute inset-0 bg-gradient-to-br from-blue-900 via-gray-950 to-purple-900 animate-gradient-xy">
                <div className="absolute inset-0 opacity-20 bg-[url('https://www.transparenttextures.com/patterns/carbon-fibre.png')]"></div>
                <div className="absolute -top-1/4 -left-1/4 w-full h-full bg-blue-500/20 blur-[100px] rounded-full animate-pulse"></div>
                <div className="absolute -bottom-1/4 -right-1/4 w-full h-full bg-purple-500/20 blur-[100px] rounded-full animate-pulse" style={{ animationDelay: '1s' }}></div>
              </div>
            )}
            
            <video
              ref={videoRef}
              autoPlay
              playsInline
              muted
              className={`w-full h-full object-cover scale-x-[-1] pointer-events-none transition-all duration-1000 ${getBackgroundStyles()}`}
            />
            
            {(bgEffect !== 'none' && stream) && (
              <video
                autoPlay
                playsInline
                muted
                style={{ clipPath: 'circle(44% at center)' }}
                className="absolute inset-0 w-full h-full object-cover scale-x-[-1] pointer-events-none z-10 brightness-[1.05] contrast-[1.05]"
                onLoadedMetadata={(e) => {
                   (e.target as HTMLVideoElement).srcObject = stream;
                }}
              />
            )}

            <div className="absolute inset-0 bg-radial-vignette pointer-events-none z-20 opacity-60"></div>
            
            <button 
              onClick={() => setShowEffectMenu(!showEffectMenu)}
              className="effect-control absolute top-6 right-6 w-10 h-10 rounded-xl bg-black/40 backdrop-blur-xl border border-white/10 text-white/50 hover:text-white hover:bg-blue-600 transition-all z-30 flex items-center justify-center opacity-0 group-hover:opacity-100 shadow-2xl active:scale-90"
              title="Camera Effects"
            >
              <i className={`fas fa-wand-magic-sparkles text-sm ${showEffectMenu ? 'text-white' : ''}`}></i>
            </button>

            <div className="absolute inset-0 flex items-center justify-center pointer-events-none opacity-0 group-hover:opacity-10 transition-opacity">
              <i className="fas fa-arrows-alt text-5xl text-white"></i>
            </div>
          </>
        )}
      </div>

      <div className="resize-handle absolute bottom-3 right-3 w-10 h-10 bg-blue-600 rounded-full border-[3px] border-gray-950 flex items-center justify-center shadow-2xl cursor-nwse-resize opacity-0 group-hover:opacity-100 transition-all hover:scale-110 z-40 active:scale-95">
        <i className="fas fa-expand-alt text-white text-[10px] rotate-90"></i>
      </div>
      
      {!error && (
        <div className="absolute bottom-8 left-3 w-8 h-8 bg-green-500 rounded-full border-[3px] border-gray-950 flex items-center justify-center shadow-2xl pointer-events-none z-40">
          <div className="w-2.5 h-2.5 bg-white rounded-full animate-pulse shadow-[0_0_10px_#fff]"></div>
        </div>
      )}
      
      <div className="absolute -bottom-5 left-1/2 -translate-x-1/2 bg-gray-950/90 backdrop-blur-xl text-white text-[10px] font-black px-6 py-2 rounded-2xl shadow-2xl opacity-0 group-hover:opacity-100 transition-all whitespace-nowrap pointer-events-none uppercase tracking-[0.1em] border border-gray-800 z-40 flex items-center gap-2">
        <span className="w-1 h-1 bg-blue-500 rounded-full"></span>
        Instructor Kim Sun-jung
      </div>
    </div>
  );
};

export default CameraFeed;
