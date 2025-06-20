const { spawn } = require('child_process');
const path = require('path');

// 실행할 Python 스크립트 경로
const scriptPath = path.join(__dirname, 'convert_hwp_to_pdf.py');

// spawn은 명령어와 인자들을 나눠서 작성
const pyProcess = spawn('python', [scriptPath]);

// stdout: 실시간으로 출력
pyProcess.stdout.on('data', (data) => {
  console.log(`[stdout] ${data.toString()}`);
});

// stderr: 에러 출력
pyProcess.stderr.on('data', (data) => {
  console.error(`[stderr] ${data.toString()}`);
});

// 프로세스 종료 후 결과 코드 확인
pyProcess.on('close', (code) => {
  if (code === 0) {
    console.log('변환 성공적으로 완료되었습니다.');
  } else {
    console.error(`프로세스가 오류 코드 ${code}로 종료되었습니다.`);
  }
});

