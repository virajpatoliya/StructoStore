// Document Scanning
function scanDocument() {
  const panNumber = document.getElementById('pan-number').value;
  const fileInput = document.getElementById('document-file');
  const file = fileInput.files[0];
  
  if (panNumber && file) {
    const reader = new FileReader();
    reader.onload = function(event) {
      const base64File = event.target.result.split(',')[1];
      fetch('/document-scan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ pan_number: panNumber, document_file: base64File })
      })
      .then(response => response.json())
      .then(data => alert(data.response))
      .catch(error => alert(`Error: ${error}`));
    };
    reader.readAsDataURL(file);
  } else {
    alert('Please fill in all fields and select a file.');
  }
}

// Call Log Backup
function uploadCallLog() {
  const fileInput = document.getElementBy
}