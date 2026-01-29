
import React, { useState, useRef, useEffect } from 'react';

type Resolution = '720p' | '1080p' | 'original';
type FrameRate = 30 | 60;
type Bitrate = 2500000 | 5000000 | 8000000;

const LectureRecorder: React.FC = () => {
  const [isRecording, setIsRecording] = useState(false);
  const [recordingTime, setRecordingTime] = useState(0);
  const [showSettings, setShowSettings] = useState(false);
  
  const [resolution, setResolution] = useState<Resolution>('1080p');
  const [fps, setFps] = useState<FrameRate>(30);
  const [bitrate, setBitrate] = useState<Bitrate>(5000000);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);
  const timerRef = useRef<number | null>(null);
  const settingsRef = useRef<HTMLDivElement>(null);
  const audioContextRef = useRef<AudioContext | null>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (settingsRef.current && !settingsRef.current.contains(event.target as Node)) {
        setShowSettings(false);
      }
    };
    if (showSettings) {
      document.addEventListener('mousedown', handleClickOutside);
    }
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, [showSettings]);

  const startRecording = async () => {
    try {
      // 1. 화면 공유 스트림 획득 (시스템 오디오 포함 시도)
      const videoConstraints: any = { frameRate: fps };
      if (resolution === '720p') {
        videoConstraints.width = { ideal: 1280 };
        videoConstraints.height = { ideal: 720 };
      } else if (resolution === '1080p') {
        videoConstraints.width = { ideal: 1920 };
        videoConstraints.height = { ideal: 1080 };
      }

      const displayStream = await navigator.mediaDevices.getDisplayMedia({
        video: videoConstraints,
        audio: true // 시스템 오디오 공유 허용 여부
      });

      // 2. 마이크 스트림 획득 (강사 목소리)
      let micStream: MediaStream | null = null;
      try {
        micStream = await navigator.mediaDevices.getUserMedia({ audio: true });
      } catch (micErr) {
        console.warn("마이크를 찾을 수 없거나 권한이 거부되었습니다. 마이크 없이 녹화를 진행합니다.");
      }

      // 3. 오디오 믹싱 (AudioContext 사용)
      const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
      audioContextRef.current = audioContext;
      const destination = audioContext.createMediaStreamDestination();

      // 시스템 오디오 소스 추가 (화면 공유에 오디오가 포함된 경우)
      if (displayStream.getAudioTracks().length > 0) {
        const displayAudioSource = audioContext.createMediaStreamSource(new MediaStream([displayStream.getAudioTracks()[0]]));
        displayAudioSource.connect(destination);
      }

      // 마이크 오디오 소스 추가
      if (micStream && micStream.getAudioTracks().length > 0) {
        const micAudioSource = audioContext.createMediaStreamSource(micStream);
        micAudioSource.connect(destination);
      }

      // 4. 비디오 트랙과 믹싱된 오디오 트랙 결합
      const combinedStream = new MediaStream([
        ...displayStream.getVideoTracks(),
        ...destination.stream.getAudioTracks()
      ]);

      const recorder = new MediaRecorder(combinedStream, {
        mimeType: 'video/webm;codecs=vp9,opus',
        videoBitsPerSecond: bitrate
      });

      recorder.ondataavailable = (e) => {
        if (e.data.size > 0) {
          chunksRef.current.push(e.data);
        }
      };

      recorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: 'video/webm' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        const now = new Date();
        const timestamp = `${now.getFullYear()}${now.getMonth()+1}${now.getDate()}_${now.getHours()}${now.getMinutes()}`;
        
        a.href = url;
        a.download = `김사부강의실_녹화_${resolution}_${timestamp}.webm`;
        a.click();
        
        chunksRef.current = [];
        URL.revokeObjectURL(url);
        
        // 모든 트랙 중지
        combinedStream.getTracks().forEach(track => track.stop());
        displayStream.getTracks().forEach(track => track.stop());
        if (micStream) micStream.getTracks().forEach(track => track.stop());
        if (audioContextRef.current) audioContextRef.current.close();
        
        stopTimer();
      };

      mediaRecorderRef.current = recorder;
      recorder.start();
      setIsRecording(true);
      setShowSettings(false);
      startTimer();
      
      displayStream.getVideoTracks()[0].onended = () => {
        if (isRecording) stopRecording();
      };

    } catch (err) {
      console.error("Recording error:", err);
      alert("녹화 시작에 실패했습니다. 화면 공유 창에서 '오디오 공유'를 체크했는지, 마이크 권한이 있는지 확인해주세요.");
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && isRecording) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  const startTimer = () => {
    setRecordingTime(0);
    timerRef.current = window.setInterval(() => {
      setRecordingTime(prev => prev + 1);
    }, 1000);
  };

  const stopTimer = () => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
    setRecordingTime(0);
  };

  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  return (
    <div className="flex items-center gap-3 relative">
      {isRecording && (
        <div className="flex items-center gap-2 px-3 py-1.5 bg-gray-800 rounded-lg border border-red-500/30 animate-pulse">
          <div className="w-2 h-2 bg-red-500 rounded-full"></div>
          <span className="text-[11px] font-black text-red-500 font-mono">
            {formatTime(recordingTime)}
          </span>
        </div>
      )}
      
      <div className="flex items-center bg-gray-800 rounded-xl border border-gray-700 overflow-hidden shadow-lg group">
        <button 
          onClick={isRecording ? stopRecording : startRecording}
          className={`px-5 py-2.5 text-xs font-black transition-all flex items-center gap-2 ${
            isRecording 
            ? 'bg-red-600 text-white hover:bg-red-500' 
            : 'text-gray-400 hover:text-white hover:bg-gray-700'
          }`}
        >
          <i className={`fas ${isRecording ? 'fa-stop-circle' : 'fa-circle'} ${isRecording ? '' : 'text-red-500'}`}></i>
          {isRecording ? '녹화 중지' : '강의 녹화'}
        </button>

        {!isRecording && (
          <button 
            onClick={() => setShowSettings(!showSettings)}
            className={`w-10 h-10 border-l border-gray-700 flex items-center justify-center transition-all ${
              showSettings ? 'bg-blue-600 text-white' : 'text-gray-500 hover:text-white hover:bg-gray-700'
            }`}
            title="녹화 품질 설정"
          >
            <i className={`fas fa-cog ${showSettings ? 'animate-spin-slow' : ''}`}></i>
          </button>
        )}
      </div>

      {showSettings && !isRecording && (
        <div 
          ref={settingsRef}
          className="absolute top-full mt-3 right-0 w-64 bg-gray-900 border border-gray-700 rounded-2xl p-5 shadow-2xl z-[70] animate-in fade-in slide-in-from-top-2"
        >
          <h4 className="text-[10px] font-black text-gray-500 uppercase tracking-widest mb-4">REC Quality Settings</h4>
          
          <div className="space-y-4">
            <div>
              <label className="text-[11px] font-bold text-gray-400 mb-2 block">해상도</label>
              <div className="grid grid-cols-3 gap-1.5">
                {(['720p', '1080p', 'original'] as Resolution[]).map((r) => (
                  <button
                    key={r}
                    onClick={() => setResolution(r)}
                    className={`py-1.5 rounded-lg text-[10px] font-bold border transition-all ${
                      resolution === r 
                      ? 'bg-blue-600 border-blue-500 text-white' 
                      : 'bg-gray-800 border-gray-700 text-gray-500 hover:border-gray-500'
                    }`}
                  >
                    {r.toUpperCase()}
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="text-[11px] font-bold text-gray-400 mb-2 block">프레임 레이트</label>
              <div className="grid grid-cols-2 gap-1.5">
                {([30, 60] as FrameRate[]).map((f) => (
                  <button
                    key={f}
                    onClick={() => setFps(f)}
                    className={`py-1.5 rounded-lg text-[10px] font-bold border transition-all ${
                      fps === f 
                      ? 'bg-blue-600 border-blue-500 text-white' 
                      : 'bg-gray-800 border-gray-700 text-gray-500 hover:border-gray-500'
                    }`}
                  >
                    {f} FPS
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="text-[11px] font-bold text-gray-400 mb-2 block">비트레이트</label>
              <div className="grid grid-cols-3 gap-1.5">
                {[
                  { label: 'Low', val: 2500000 },
                  { label: 'Mid', val: 5000000 },
                  { label: 'High', val: 8000000 }
                ].map((b) => (
                  <button
                    key={b.val}
                    onClick={() => setBitrate(b.val as Bitrate)}
                    className={`py-1.5 rounded-lg text-[10px] font-bold border transition-all ${
                      bitrate === b.val 
                      ? 'bg-blue-600 border-blue-500 text-white' 
                      : 'bg-gray-800 border-gray-700 text-gray-500 hover:border-gray-500'
                    }`}
                  >
                    {b.label}
                  </button>
                ))}
              </div>
            </div>
          </div>

          <div className="mt-5 pt-4 border-t border-gray-800 flex items-center justify-between">
             <div className="text-[9px] text-gray-500 font-mono italic">
               Est. Size: {Math.round(bitrate / 8 / 1024 / 1024 * 60)}MB/min
             </div>
             <div className="text-[9px] text-blue-500 font-bold">
               {resolution.toUpperCase()} @ {fps}FPS
             </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default LectureRecorder;
