# Customer Support Response Time Violinplot

This project generates a Seaborn violinplot visualizing the distribution
and density of customer support first-response times across multiple
channels for a major retail client of Predovic Luettgen.

The visualization is designed for executive presentations, board reports,
and strategic planning documents.

## Files

- `chart.py`  
  - Generates realistic synthetic response time data for:
    - Email
    - Live Chat
    - Phone
    - Social Media
  - Creates a Seaborn violinplot using `sns.violinplot()`
  - Applies professional styling (Seaborn theme, labels, title, color palette)
  - Saves the final chart as `chart.png` with exactly 512x512 pixels
    (8x8 inches at 64 dpi)

- `chart.png`  
  - The generated Seaborn violinplot image.

## How to Run

1. Install dependencies:

   ```bash
   pip install seaborn matplotlib pandas numpy
   ```
2. Run the script from inside this folder:

    ```bash
    python chart.py
    ```
3. This will create `chart.png` in the same directory.

## Contact

Email for this submission: 22f3001170@ds.study.iitm.ac.in