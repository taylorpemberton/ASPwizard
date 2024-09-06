const express = require('express');
const path = require('path');
const app = express();
const port = process.env.PORT || 3001; // Change 3000 to 3001 or another available port

// Serve static files from the current directory
app.use(express.static(__dirname));

// Route for the home page
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
  console.log(`To access the server from other devices on your network, use your computer's IP address instead of localhost`);
});
