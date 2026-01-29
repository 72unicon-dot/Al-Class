
import React, { useState, useEffect } from 'react';

interface LectureNotesProps {
  notes: string;
  setNotes: (notes: string) => void;
  onClose: () => void;
}

const LectureNotes: React.FC<LectureNotesProps> = ({ notes, setNotes, onClose }) => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const handleSave = () => {
    if (!notes.trim()) {
      alert("기록된 내용이 없습니다.");
      return;
    }
    const blob = new Blob([notes], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    const now = new Date();
    const timestamp = `${now.getFullYear()}${now.getMonth()+1}${now.getDate()}_${now.getHours()}${now.getMinutes()}`;
    
    link.href = url;
    link.download = `김사부_강의노트_${timestamp}.txt`;
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className={`absolute bottom-6 left-6 right-6 z-[70] transition-all duration-500 transform ${isVisible ? 'translate-y-0 opacity-100' : 'translate-y-10 opacity-0'}`}>
      <div className="bg-gray-900/80 backdrop-blur-2xl border border-blue-500/30 rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.5)] overflow-hidden">
        {/* Header */}
        <div className="px-6 py-3 border-b border-gray-800 flex items-center justify-between bg-gray-950/40">
          <div className="flex items-center gap-3">
            <div className="w-8 h-8 bg-blue-600/20 rounded-xl flex items-center justify-center border border-blue-500/20">
              <i className="fas fa-edit text-blue-500 text-xs"></i>
            </div>
            <div>
              <h4 className="text-[10px] font-black text-white uppercase tracking-widest">Live Lecture Notes</h4>
              <p className="text-[8px] text-gray-500 font-bold uppercase tracking-tighter">Real-time Content Archiving</p>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button 
              onClick={handleSave}
              className="flex items-center gap-2 px-4 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-full text-[10px] font-black transition-all shadow-lg active:scale-95"
            >
              <i className="fas fa-save"></i>
              메모장 저장 (.txt)
            </button>
            <button 
              onClick={onClose}
              className="w-8 h-8 flex items-center justify-center rounded-full text-gray-500 hover:bg-red-500/20 hover:text-red-500 transition-all"
            >
              <i className="fas fa-times text-xs"></i>
            </button>
          </div>
        </div>
        
        {/* Input Area */}
        <div className="p-4 relative">
          <textarea
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
            placeholder="강의 내용을 여기에 기록하세요... (내용은 자동으로 유지됩니다)"
            className="w-full h-32 bg-transparent text-gray-200 text-sm font-medium leading-relaxed resize-none focus:outline-none placeholder:text-gray-700 custom-scrollbar"
          />
          <div className="absolute bottom-4 right-6 pointer-events-none opacity-20">
             <i className="fas fa-quote-right text-4xl text-blue-500"></i>
          </div>
        </div>

        {/* Status Footer */}
        <div className="px-6 py-2 bg-blue-600/5 flex items-center justify-between text-[8px] text-blue-500/60 font-black uppercase tracking-widest">
           <span>Words: {notes.trim() ? notes.trim().split(/\s+/).length : 0}</span>
           <span>Characters: {notes.length}</span>
        </div>
      </div>
    </div>
  );
};

export default LectureNotes;
