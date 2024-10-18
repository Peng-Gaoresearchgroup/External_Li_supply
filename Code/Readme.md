# AI Summarization for Organic Electroactive Molecules

### Description
The "AI_summarization_for_organic_electroactive_molecules.py" script is the main program used to summarize molecular and electrochemical reaction information from the references. The pdf files under py2 floder are input files for presentation.The ''Output.txt'' file is output file.

### Operating System
- Windows, Mac , Linux

### Necessary Python Modules
- DrissionPage (most version should be fine)
- loguru (most version should be fine)
- requests (most version should be fine)

### Demo
- The inputs are pdf files of literature or patents related to electrochemical organic synthesis, ''1.pdf'' is an example, and the input files should be placed under the py2 folder.
- After running ''AI_summarization_for_organic_electroactive_molecules.py'', the output file (''Output.txt'') is expected to collect relevant reaction information, including reactants and products in a format of [compound A][CAS number], and the reaction conditions including temperature, potential, solvent, electrode, etc.

### Instructions for Use
- Put the input pdf files in py2 folder，named in only numbers, ''1.pdf'' for example.
- Run ''AI_summarization_for_organic_electroactive_molecules.py''.
- To reproduce the paper, all pdf files of the references and patents mentioned in the ''References_and_patents.md'' under Data folder should be put in the py2 floder. Run ''AI_summarization_for_organic_electroactive_molecules.py''. The summarized content will be saved to ''Output.txt''. Runtime expected to be 20 days (Depends on the frequency of web page visits). After the necessary organization, the 20 redox-active centers' summarization files were obtained in the Data folder.

### Disclaimer
- This code is intended for educational and research purposes only. Please ensure that you comply with relevant laws and regulations as well as the terms of service of the target website when using this code. The author is not responsible for any legal liabilities or other issues arising from the use of this code.