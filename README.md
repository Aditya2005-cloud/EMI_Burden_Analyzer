# EMI Burden Analyzer

A practical Streamlit app to check whether a user is overburdened with EMIs.

## Project Path

`D:\PYprojects\EMI_Burden_Analyzer`

## Inputs

- Monthly salary
- Current monthly EMIs
- Remaining loan tenure

## Outputs

- EMI-to-income ratio
- Financial stress level
- Income left after EMIs
- Projected remaining EMI outflow

## Simple Setup

Virtual env:
`D:\PYprojects\EMI_Burden_Analyzer\Scripts\Activate.ps1`

Requirements file:
`D:\PYprojects\EMI_Burden_Analyzer\requirements.txt`

Project code:
`D:\PYprojects\EMI_Burden_Analyzer\code\app.py`

## Run App

From project folder:

```powershell
.\Scripts\python.exe -m streamlit run code/app.py
```

If you are inside `code` folder:

```powershell
..\Scripts\python.exe -m streamlit run .\app.py
```
