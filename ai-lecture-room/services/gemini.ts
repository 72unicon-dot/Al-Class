
import { GoogleGenAI } from "@google/genai";

// Initialize the Google GenAI SDK using the API key strictly from the environment variable.
const ai = new GoogleGenAI({ apiKey: process.env.API_KEY });

export const getAIResponse = async (prompt: string, history: {role: string, parts: {text: string}[]}[]) => {
  try {
    const response = await ai.models.generateContent({
      model: "gemini-3-flash-preview",
      contents: [
        ...history,
        { role: 'user', parts: [{ text: prompt }] }
      ],
      config: {
        systemInstruction: "당신은 김사부 강사의 강의를 돕는 AI 어시스턴트입니다. 학생들의 실습 질문에 친절하고 전문적으로 답변하세요. 답변은 한국어로 제공합니다.",
        temperature: 0.7,
      },
    });
    // Access the .text property directly as it is a getter, not a function.
    return response.text;
  } catch (error) {
    console.error("Gemini API Error:", error);
    return "죄송합니다. AI 응답을 가져오는 중 오류가 발생했습니다.";
  }
};
