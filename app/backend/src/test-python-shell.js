const { PythonShell } = require('python-shell');
const path = require('path');

const options = {
  scriptPath: path.resolve(__dirname, '../dist/python'), // Python 스크립트 경로
  pythonPath: 'python',
  mode: 'text',
  pythonOptions: ['-u'],
};

PythonShell.run('coin.py', options, (err, output, stderr) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  if (stderr) {
    console.error('Stderr:', stderr);
    return;
  }
  console.log('Output:', output);
});
