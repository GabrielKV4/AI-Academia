function generateSummary() {

    const mockMarkdown = `
## Key Concepts

- Cognitive Load Theory  
- Executive Function  

---

> **Key Definition**
>
> Executive function is the ability to regulate behavior.

---

> **Important Formula**
>
> \`\`\`
> F = ma
> \`\`\`

---

> **Exam Tip**
>
> Focus on intrinsic vs extrinsic load.  
`;

    document.getElementById("outputArea").innerHTML = marked.parse(mockMarkdown);
}



const toggleBtn = document.getElementById("themeToggle");

toggleBtn.addEventListener("click", function () {
    const htmlElement = document.documentElement;

    if (htmlElement.getAttribute("data-bs-theme") === "dark") {
        htmlElement.setAttribute("data-bs-theme", "light");
    } else {
        htmlElement.setAttribute("data-bs-theme", "dark");
    }
});



var upload = document.getElementById('upload');

function onFile() {
    var me = this,
        file = upload.files[0],
        name = file.name.replace(/.[^/.]+$/, '');
    // console.log('upload code goes here', file, name);
    if (file.type === 'application/vnd.ms-powerpoint' ||
    file.type === 'application/vnd.openxmlformats-officedocument.presentationml.presentation') {
        if (file.size < (1024 * 1024 * 1024)) {
            upload.parentNode.className = 'area mb-3 uploading';
            // console log the file name and size in MB
            console.log('File name: ' + file.name);
            console.log('File size: ' + (file.size / (1024 * 1024)).toFixed(2) + ' MB');
        } else {
            window.alert('File size is too large, please ensure you are uploading a file of less than 1GB');
        }
    } else {
        window.alert('File type ' + file.type + ' not supported');
    }
}

upload.addEventListener('dragenter', function (e) {
    upload.parentNode.className = 'area mb-3 dragging';
}, false);

upload.addEventListener('dragleave', function (e) {
    upload.parentNode.className = 'area mb-3';
}, false);

upload.addEventListener('dragdrop', function (e) {
    onFile();
}, false);

upload.addEventListener('change', function (e) {
    onFile();
}, false);
