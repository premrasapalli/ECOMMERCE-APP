const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());

app.get("/api/health", (req,res) => res.json({status:"ok"}));

app.listen(4000, () => console.log("Backend running on 4000"));
