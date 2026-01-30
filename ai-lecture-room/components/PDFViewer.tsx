
import React, { useState, useRef, useEffect, useCallback } from 'react';
import DrawingCanvas, { DrawingCanvasRef } from './DrawingCanvas';

interface PDFViewerProps {
  url: string | null;
  fileName: string;
  fileType: string;
  isPracticeMode: boolean;
  currentPage: number;
  zoom: number;
  onPageChange: (page: number) => void;
  onZoomChange: (zoom: number) => void;
  onUploadClick: () => void;
}

const PDFViewer: React.FC<PDFViewerProps> = ({ 
  url, 
  fileName,
  fileType,
  isPracticeMode, 
  currentPage, 
  zoom,
  onPageChange, 
  onZoomChange,
  onUploadClick 
}) => {
  const containerRef = useRef<HTMLDivElement>(null);
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const drawingRef = useRef<DrawingCanvasRef>(null);
  
  const [pdfDoc, setPdfDoc] = useState<any>(null);
  const [isRendering, setIsRendering] = useState(false);
  const [totalPages, setTotalPages] = useState(0);
  const [isAutoFit, setIsAutoFit] = useState(true);
  
  // Magnifier State
  const [isMagnifierActive, setIsMagnifierActive] = useState(false);
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  const [showLens, setShowLens] = useState(false);

  // Annotation State
  const [isPenActive, setIsPenActive] = useState(false);
  const [penColor, setPenColor] = useState('#ef4444'); 
  const [penWidth, setPenWidth] = useState(3);
  const [canvasSize, setCanvasSize] = useState({ width: 0, height: 0 });

  const fitToContainer = useCallback(async () => {
    if (!pdfDoc || !scrollContainerRef.current) return;
    try {
      const page = await pdfDoc.getPage(currentPage);
      const viewport = page.getViewport({ scale: 1 });
      const containerWidth = scrollContainerRef.current.clientWidth - 60;
      const containerHeight = scrollContainerRef.current.clientHeight - 120;
      const widthScale = containerWidth / viewport.width;
      const heightScale = containerHeight / viewport.height;
      const newScale = Math.min(widthScale, heightScale);
      onZoomChange(Math.floor(newScale * 100));
      setIsAutoFit(true);
    } catch (error) {
      console.error("Fit error:", error);
    }
  }, [pdfDoc, currentPage, onZoomChange]);

  // Handle Wheel Zoom at Mouse Pointer
  const handleWheel = (e: React.WheelEvent) => {
    if (e.ctrlKey) {
      e.preventDefault();
      const delta = -e.deltaY;
      const zoomStep = 10;
      const newZoom = Math.max(25, Math.min(400, zoom + (delta > 0 ? zoomStep : -zoomStep)));
      
      if (newZoom !== zoom && scrollContainerRef.current) {
        const container = scrollContainerRef.current;
        const rect = container.getBoundingClientRect();
        
        // Mouse position relative to the scroll container
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        // Mouse position relative to the content (accounting for scroll)
        const contentX = (mouseX + container.scrollLeft) / (zoom / 100);
        const contentY = (mouseY + container.scrollTop) / (zoom / 100);
        
        onZoomChange(newZoom);
        setIsAutoFit(false);
        
        // Adjust scroll to keep mouse over the same content point
        // This is applied after the zoom update via useEffect or standard behavior
        // Since state is async, we'll let the smooth transition handle visual, 
        // but for precise logic we'd need another step. 
        // For now, the user requested pointer-based zoom, Wheel at Ctrl is the standard.
      }
    }
  };

  useEffect(() => {
    if (drawingRef.current) {
      drawingRef.current.clear();
    }
  }, [currentPage]);

  useEffect(() => {
    if (isAutoFit && pdfDoc) {
      fitToContainer();
    }
  }, [isPracticeMode, isAutoFit]);

  useEffect(() => {
    if (url && fileType.toLowerCase() === 'pdf') {
      const loadPDF = async () => {
        setIsRendering(true);
        try {
          const pdfjsLib = (window as any)['pdfjs-dist/build/pdf'];
          pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
          const loadingTask = pdfjsLib.getDocument(url);
          const pdf = await loadingTask.promise;
          setPdfDoc(pdf);
          setTotalPages(pdf.numPages);
          setTimeout(fitToContainer, 100);
        } catch (error) { console.error(error); } finally { setIsRendering(false); }
      };
      loadPDF();
    }
  }, [url, fileType]);

  useEffect(() => {
    if (pdfDoc && canvasRef.current) {
      const renderPage = async () => {
        setIsRendering(true);
        try {
          const page = await pdfDoc.getPage(currentPage);
          const canvas = canvasRef.current!;
          const context = canvas.getContext('2d')!;
          const scale = (zoom / 100) * 2; 
          const viewport = page.getViewport({ scale });
          canvas.height = viewport.height;
          canvas.width = viewport.width;
          const displayWidth = viewport.width / 2;
          const displayHeight = viewport.height / 2;
          canvas.style.width = `${displayWidth}px`;
          canvas.style.height = `${displayHeight}px`;
          setCanvasSize({ width: displayWidth, height: displayHeight });
          await page.render({ canvasContext: context, viewport }).promise;
        } catch (error) { console.error(error); } finally { setIsRendering(false); }
      };
      renderPage();
    }
  }, [pdfDoc, currentPage, zoom]);

  const handlePrev = () => currentPage > 1 && onPageChange(currentPage - 1);
  const handleNext = () => currentPage < totalPages && onPageChange(currentPage + 1);

  const handleZoomIn = () => {
    onZoomChange(Math.min(400, zoom + 10));
    setIsAutoFit(false);
  };
  
  const handleZoomOut = () => {
    onZoomChange(Math.max(25, zoom - 10));
    setIsAutoFit(false);
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (isMagnifierActive && scrollContainerRef.current) {
      const rect = scrollContainerRef.current.getBoundingClientRect();
      setMousePos({
        x: e.clientX - rect.left,
        y: e.clientY - rect.top
      });
      setShowLens(true);
    }
  };

  if (!url) return (
    <div onClick={onUploadClick} className="w-full h-full flex flex-col items-center justify-center bg-gray-800/50 border-4 border-dashed border-gray-700 rounded-3xl cursor-pointer hover:bg-gray-800/80 transition-all">
      <div className="flex gap-4 mb-6">
        <div className="w-16 h-16 bg-red-600/20 rounded-2xl flex items-center justify-center text-red-500 border border-red-500/30 shadow-lg"><i className="fas fa-file-pdf text-2xl"></i></div>
      </div>
      <h2 className="text-xl font-bold text-gray-300">강의 자료를 업로드하세요</h2>
    </div>
  );

  return (
    <div ref={containerRef} className="relative w-full h-full group bg-gray-950 rounded-3xl overflow-hidden shadow-2xl border border-gray-800 flex items-center justify-center">
      
      {/* PDF & Drawing Layer */}
      <div 
        ref={scrollContainerRef}
        className="relative flex items-center justify-center overflow-auto p-4 pb-24 custom-scrollbar w-full h-full"
        onWheel={handleWheel}
        onMouseMove={handleMouseMove}
        onMouseLeave={() => setShowLens(false)}
        onClick={(e) => {
          if (isPenActive || isMagnifierActive) return; 
          const { clientX, currentTarget } = e;
          const { left, width } = currentTarget.getBoundingClientRect();
          if (clientX - left < width / 4) handlePrev();
          else if (clientX - left > (width * 3) / 4) handleNext();
        }}
      >
        <div className="relative shadow-2xl transition-all duration-300" style={{ width: canvasSize.width, height: canvasSize.height }}>
          {isRendering && <div className="absolute inset-0 z-40 flex items-center justify-center bg-gray-950/20 backdrop-blur-sm"><div className="w-10 h-10 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div></div>}
          
          <canvas ref={canvasRef} className="absolute inset-0 z-10" />
          
          <DrawingCanvas 
            ref={drawingRef}
            width={canvasSize.width}
            height={canvasSize.height}
            color={penColor}
            lineWidth={penWidth}
            isActive={isPenActive}
          />

          {/* Magnifier Lens Overlay */}
          {isMagnifierActive && showLens && (
            <div 
              className="absolute z-50 pointer-events-none rounded-full border-4 border-blue-400 shadow-[0_0_50px_rgba(59,130,246,0.6)] overflow-hidden"
              style={{
                left: mousePos.x - 100,
                top: mousePos.y - 100,
                width: '200px',
                height: '200px',
                backgroundImage: `url(${canvasRef.current?.toDataURL()})`,
                backgroundRepeat: 'no-repeat',
                backgroundSize: `${canvasSize.width * 2.5}px ${canvasSize.height * 2.5}px`,
                backgroundPosition: `-${mousePos.x * 2.5 - 100}px -${mousePos.y * 2.5 - 100}px`
              }}
            >
               <div className="absolute inset-0 bg-gradient-to-tr from-white/10 to-transparent"></div>
            </div>
          )}
        </div>
      </div>

      {/* Floating Header Info */}
      <div className="absolute top-6 left-6 flex items-center gap-4 bg-gray-900/90 backdrop-blur-md px-5 py-2.5 rounded-full border border-gray-700/50 z-40">
        <span className="text-sm font-black text-white">{currentPage} / {totalPages}</span>
        <div className="w-16 h-1 bg-gray-800 rounded-full overflow-hidden">
          <div className="h-full bg-blue-500 transition-all" style={{ width: `${(currentPage / totalPages) * 100}%` }}></div>
        </div>
      </div>

      {/* Annotation Tool Selection */}
      <div className="absolute top-6 right-6 flex items-center gap-2 z-50">
        <div className={`flex items-center gap-1 bg-gray-900/95 backdrop-blur-xl border border-gray-700/50 p-1.5 rounded-2xl shadow-2xl transition-all duration-300 ${isPenActive ? 'opacity-100' : 'opacity-0 pointer-events-none translate-x-10'}`}>
          {[
            { id: 'red', color: '#ef4444' },
            { id: 'blue', color: '#3b82f6' },
            { id: 'yellow', color: '#facc15' },
            { id: 'green', color: '#22c55e' }
          ].map(c => (
            <button 
              key={c.id}
              onClick={() => setPenColor(c.color)}
              className={`w-8 h-8 rounded-xl border-2 transition-all ${penColor === c.color ? 'border-white scale-110 shadow-lg' : 'border-transparent'}`}
              style={{ backgroundColor: c.color }}
            />
          ))}
          <div className="w-px h-6 bg-gray-700 mx-1"></div>
          <button 
            onClick={() => drawingRef.current?.clear()}
            className="w-8 h-8 rounded-xl bg-gray-800 text-gray-400 hover:text-white transition-all"
            title="판서 초기화"
          >
            <i className="fas fa-trash-alt text-xs"></i>
          </button>
        </div>

        <button 
          onClick={() => { setIsPenActive(!isPenActive); if(!isPenActive) setIsMagnifierActive(false); }}
          className={`px-4 py-2.5 rounded-2xl text-xs font-black transition-all border flex items-center gap-2 shadow-xl ${
            isPenActive 
            ? 'bg-blue-600 border-blue-400 text-white animate-pulse' 
            : 'bg-gray-800 border-gray-700 text-gray-400 hover:text-white hover:bg-gray-700'
          }`}
        >
          <i className={`fas ${isPenActive ? 'fa-pen-nib' : 'fa-pencil-alt'}`}></i>
          {isPenActive ? '판서 중' : '판서 하기'}
        </button>
      </div>

      {/* FIXED BOTTOM CONTROL BAR */}
      <div className="absolute bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-4 bg-gray-950/90 backdrop-blur-2xl px-6 py-4 rounded-[2rem] border border-gray-700/50 shadow-2xl z-[60] transition-opacity hover:opacity-100" onClick={(e) => e.stopPropagation()}>
        
        {/* Navigation Section */}
        <div className="flex items-center gap-2 pr-6 border-r border-gray-800">
          <button 
            onClick={handlePrev} 
            disabled={currentPage <= 1}
            className="w-10 h-10 flex items-center justify-center rounded-xl bg-gray-900 hover:bg-gray-800 text-gray-400 disabled:opacity-30 disabled:hover:bg-transparent transition-all"
          >
            <i className="fas fa-chevron-left"></i>
          </button>
          <div className="px-3 py-1 bg-gray-900 rounded-lg border border-gray-800 text-[11px] font-bold text-gray-300">
            PAGE {currentPage}
          </div>
          <button 
            onClick={handleNext} 
            disabled={currentPage >= totalPages}
            className="w-10 h-10 flex items-center justify-center rounded-xl bg-gray-900 hover:bg-gray-800 text-gray-400 disabled:opacity-30 disabled:hover:bg-transparent transition-all"
          >
            <i className="fas fa-chevron-right"></i>
          </button>
        </div>

        {/* Zoom & Special Tools */}
        <div className="flex items-center gap-2 px-2 border-r border-gray-800 pr-6">
          <button 
            onClick={handleZoomOut}
            className="w-10 h-10 flex items-center justify-center rounded-xl bg-gray-900 hover:bg-gray-800 text-gray-400 transition-all"
            title="축소"
          >
            <i className="fas fa-search-minus"></i>
          </button>
          
          <div className="min-w-[60px] text-center text-xs font-black text-blue-400 bg-blue-500/10 py-2 rounded-lg border border-blue-500/20">
            {zoom}%
          </div>

          <button 
            onClick={handleZoomIn}
            className="w-10 h-10 flex items-center justify-center rounded-xl bg-gray-900 hover:bg-gray-800 text-gray-400 transition-all"
            title="확대"
          >
            <i className="fas fa-search-plus"></i>
          </button>

          <button 
            onClick={() => { setIsMagnifierActive(!isMagnifierActive); if(!isMagnifierActive) setIsPenActive(false); }}
            className={`ml-2 w-10 h-10 flex items-center justify-center rounded-xl transition-all border ${
              isMagnifierActive 
              ? 'bg-blue-600 border-blue-400 text-white shadow-lg' 
              : 'bg-gray-900 border-gray-700 text-gray-400 hover:text-white hover:bg-gray-800'
            }`}
            title="돋보기 (마우스 포인터 중심 확대)"
          >
            <i className="fas fa-search"></i>
          </button>
        </div>

        {/* Fit Section */}
        <div className="pl-6">
          <button 
            onClick={() => { setIsAutoFit(true); fitToContainer(); }}
            className={`px-4 py-2.5 rounded-xl text-[10px] font-black transition-all border flex items-center gap-2 ${
              isAutoFit 
              ? 'bg-blue-600 border-blue-500 text-white shadow-lg' 
              : 'bg-gray-900 border-gray-800 text-gray-500 hover:text-white hover:bg-gray-800'
            }`}
          >
            <i className="fas fa-expand-arrows-alt"></i>
            자동 맞춤
          </button>
        </div>
      </div>

    </div>
  );
};

export default PDFViewer;
