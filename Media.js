const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(express.json());

const upload = multer({ dest: 'uploads/' });

// Upload media (photo)
app.post('/media/upload', upload.single('photo'), (req, res) => {
    const file = req.file;
    if (!file) {
        return res.status(400).json({ error: 'Please upload a file' });
    }

    res.status(200).json({
        message: 'File uploaded successfully',
        filePath: file.path
    });
});

// Get media file
app.get('/media/:filename', (req, res) => {
    const filename = req.params.filename;
    const filePath = path.join(__dirname, 'uploads', filename);

    fs.exists(filePath, exists => {
        if (!exists) {
            return res.status(404).json({ error: 'File not found' });
        }
        res.sendFile(filePath);
    });
});

app.listen(3002, () => {
    console.log('Media Service running on port 3002');
});
