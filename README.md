# PDF Type Classification Model

## Overview
This project aims to automate the classification of PDF documents (e.g., fund statements, invoices, resumes) into predefined types such as **Type A** and **Type B**.  
Currently, PDFs are manually categorized into folders, but with the recent shift to S3-based uploads, an automated model is required to classify them directly.

The **data extraction logic** (text extraction from PDFs) has already been handled in Shivam's main project.  
Our task focuses on:
- Understanding the text differences between each type,
- Creating embeddings or ML-based features,
- And training a lightweight, open-source **LLM or ML model** to classify the PDFs.

## Project Flow

PDF in S3 → Extract Text
→ Preprocess & Clean Text  
→ Generate Features / Embeddings  
→ Train & Evaluate Model (Type A / Type B)  
→ Predict Type for New PDFs