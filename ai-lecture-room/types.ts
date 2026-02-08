
export interface SlideState {
  file: File | null;
  previewUrl: string | null;
  currentPage: number;
}

export enum ViewMode {
  SLIDE = 'SLIDE',
  SPLIT = 'SPLIT',
  PRACTICE = 'PRACTICE',
  LECTURE = 'LECTURE'
}

export interface ChatMessage {
  role: 'user' | 'model';
  text: string;
}

export interface Resource {
  id: string;
  type: 'pdf' | 'url' | 'video' | 'image'; // image 추가
  title: string;
  description: string;
  link: string;
  isLocal?: boolean;
}
