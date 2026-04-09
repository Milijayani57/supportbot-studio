-- Table 1: tracks uploaded documents
CREATE TABLE documents (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  filename TEXT NOT NULL,
  upload_time TIMESTAMP DEFAULT NOW(),
  status TEXT DEFAULT 'pending'
);

-- Table 2: stores chat history
CREATE TABLE chat_history (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  session_id TEXT NOT NULL,
  question TEXT NOT NULL,
  answer TEXT NOT NULL,
  timestamp TIMESTAMP DEFAULT NOW()
);