# Faculty Publications Summary Generator

## Overview

The **Faculty Publications Summary Generator** is a web-based AI solution designed to automate the creation of publication summaries for faculty members. This tool streamlines the process of gathering, summarizing, and exporting academic publication data, particularly useful for Higher Education Institutions (HEIs) when submitting faculty profiles to accrediting bodies. The solution integrates multiple academic databases like **Google Scholar**, **DBLP**, and **CrossRef**, and utilizes **DOIs** to fetch accurate metadata, enabling users to generate customized publication records for a specific time period.

## Problem Statement

Faculty members are required to showcase their research publications for various purposes, including profile building, accreditation, and institutional reporting. Gathering this information manually from different sources and formatting it for submission is time-consuming and prone to errors. This project addresses the need for a solution that can automate the retrieval of publication data and generate customized reports.

## Features

- **DOI Implementation**:
  - Fetches metadata such as titles, abstracts, and author details using **DOIs** from the **CrossRef API**.
- **Publication Summaries**:
  - Summarizes publication abstracts using **BART** to create concise and meaningful overviews of research work.
- **Academic Database Integration**:
  - Crawls **Google Scholar** and **DBLP** for publication records, with the ability to filter based on time period and faculty name.
- **Custom Queries**:
  - Users can search and filter publications by specific time periods (e.g., year-wise or within a certain date range).
- **Multiple Export Options**:
  - Generates **Word** and **Excel** files for journal and conference publications, providing a user-friendly exportable format for submission.

## DOI Implementation

The solution utilizes **DOIs** to enhance the accuracy of the publication metadata retrieval process. When a user inputs DOIs, the system fetches essential information such as:

- Title of the research paper
- Full author names
- Publication venue (journal/conference)
- Abstract

Steps:

1. The user inputs a **DOI**.
2. The system queries the **CrossRef API** to retrieve metadata.
3. The fetched metadata, including the **abstract**, is summarized using **BART**.
4. Results are displayed and can be exported.

## Roadmap

### Phase 1: Core Features

- Implement **DOI-based retrieval** using CrossRef API.
- Parse **BibTeX** and **Excel** files for author and publication data.
- Summarize publication abstracts using **BART**.

### Phase 2: Database Integration

- Crawl **Google Scholar** and **DBLP** for additional data.
- Implement advanced filtering (e.g., publication type, time period).

### Phase 3: Export and UI Improvements

- Add **Word** and **Excel** export features.
- Enhance the **Streamlit** UI for better user experience.

## Tech Stack

- **Python**: Backend language for logic and API integration.
- **Streamlit**: For building the web interface.
- **CrossRef API**: For retrieving DOI metadata.
- **Google Scholar/DBLP**: For crawling academic databases.
- **BART (Hugging Face)**: For summarizing abstracts.

## Conclusion

The **Faculty Publications Summary Generator** provides an efficient solution to automate the collection, summarization, and export of academic publications. By using a combination of **DOI-based retrieval**, **academic database crawling**, and **NLP-powered summarization**, this tool simplifies the workflow for institutions and faculty members alike, ensuring seamless integration with accreditation processes.
