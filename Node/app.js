const express = require('express');
const app = express();
const cors = require('cors');

const port = 3001;
app.use(cors());

// Sample data for the API
const apiData = { message: 'Hello from Node.js API!' };

app.get('/api/data', (req, res) => {
    res.json(apiData);
});

app.listen(port, () => {
    console.log(`Node.js server is running on port ${port}`);
});
