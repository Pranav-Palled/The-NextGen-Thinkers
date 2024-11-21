const fileInput = document.getElementById('fileInput');
const questionInput = document.getElementById('questionInput');
const submitBtn = document.getElementById('submitBtn');
const answerDiv = document.getElementById('answer');

submitBtn.addEventListener('click', async () => {
  const file = fileInput.files[0];
  const question = questionInput.value;

  // Send file and question to backend for processing
  const response = await fetch('/process', {
    method: 'POST',
    body: new FormData().append('file', file).append('question', question)
  });

  const data = await response.json();
  answerDiv.textContent = data.answer;
});