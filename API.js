const express = require('express');
const axios = require('axios');
const app = express();

app.use(express.json());

// Forward requests to User Service
app.use('/users', async (req, res) => {
    const url = `http://localhost:3001${req.originalUrl}`;
    try {
        const response = await axios({
            method: req.method,
            url,
            data: req.body
        });
        res.status(response.status).json(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).json({ error: error.message });
    }
});

// Forward requests to Media Service
app.use('/media', async (req, res) => {
    const url = `http://localhost:3002${req.originalUrl}`;
    try {
        const response = await axios({
            method: req.method,
            url,
            data: req.body
        });
        res.status(response.status).json(response.data);
    } catch (error) {
        res.status(error.response?.status || 500).json({ error: error.message });
    }
});

app.listen(3000, () => {
    console.log('API Gateway running on port 3000');
});
